# Rain prediction in my town based on past variables (not physic model)

## Libraries


```python
# Data library
import pandas as pd
import numpy as np

# Graphic libraries
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from plotnine import *

# Date Libraries
from datetime import datetime

# Machine Learning Libraries
from sklearn.model_selection import train_test_split
from sklearn import model_selection
from sklearn.preprocessing import StandardScaler
import xgboost as xg #Algorithm, we will take classifier.
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn import metrics
from mlxtend.evaluate import mcnemar_table, mcnemar
```

## Reading Data
We are going to read 3 different Data from [Meteocat Opendata](https://www.meteo.cat/wpweb/serveis/cataleg-de-serveis/serveis-oberts/dades-obertes/):

- **Stations information:** id and name of all Catalonian weather stations, it will let us to filter by the nearest station to my town, in this case 'Parets del Vallès'.
- **Raw data by time:** Each day in different time there lots of measurement, this table have all the data saved in *'VALOR_LECTURA'* and which is the units of this measurement comes from *'CODI_VARIABLE'*. This file has been filtered from origin, because when saving all station data the file was coming to big... and if fact I only want 1 station.
- **Measurement data:** From *'CODI_VARIABLE'* you have which is the measurement, units, description, etc...

First one, is only for validate that our *'CODI_ESTACIO'* is the one that we have pre-filtered in the origin (with meteocat filter options).

Second one and Third one will require some 'work' because we don't have 'standard' columns=features and observations in 'row', as we have different features in rows for 1 observation...


```python
df_station = pd.read_csv("./data/Metadades_estacions_meteorol_giques_autom_tiques.csv",sep=',')
df_data = pd.read_csv("./data/Dades_meteorol_giques_de_la_XEMA.csv")
df_var = pd.read_csv("./data/Metadades_variables_meteorol_giques.csv")
df_station[df_station['CODI_ESTACIO']=='XG'].head()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>CODI_ESTACIO</th>
      <th>NOM_ESTACIO</th>
      <th>LATITUD</th>
      <th>LONGITUD</th>
      <th>EMPLACAMENT</th>
      <th>ALTITUD</th>
      <th>NOM_MUNICIPI</th>
      <th>NOM_COMARCA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>XG</td>
      <td>Parets del Vallès</td>
      <td>41.56734</td>
      <td>2.22619</td>
      <td>CEIP Pau Vila</td>
      <td>123.0</td>
      <td>Parets del Vallès</td>
      <td>Vallès Oriental</td>
    </tr>
  </tbody>
</table>
</div>


## Data cleaning and adjustments


```python
print('Raw data types: ',df_data.dtypes)
print('Variables identifier type: ',df_var.CODI_VARIABLE.dtype)
```

    Raw data types:  ID                object
    CODI_ESTACIO      object
    CODI_VARIABLE      int64
    DATA_LECTURA      object
    DATA_EXTREM       object
    VALOR_LECTURA    float64
    CODI_ESTAT        object
    CODI_BASE         object
    dtype: object
    Variables identifier type:  int64
    

Our value 'VALOR_LECTURA' it's in the correct type, we will have to check that it's the same in all the process, 'CODI_VARIABLE' will have to be the same type as 'CODI_VARIABLE' of *df_var*, as it is, so we could merge in the next steps.

'DATA_LECUTRA' is a date which will help us to simplify the model by days, and help us to eliminate some hours non-measured data.

### Joining mesure information detail with mesurement value

We are going to Merge both datasets using 'CODI_VARIABLE' as key element.


```python
df_res = pd.merge(df_data,df_var,on='CODI_VARIABLE')
df_res.drop(['ID',
             'CODI_BASE',
             'CODI_TIPUS_VAR',
             'DECIMALS',
             'CODI_ESTACIO',
             'DATA_EXTREM',
             'CODI_ESTAT'],axis=1,inplace=True)
```

### Date and indexing by date


```python
dateparse = lambda x: datetime.strptime(x, '%d/%m/%Y %H:%M:%S %p')
df_res['DATA_LECTURA'] = df_res['DATA_LECTURA'].apply(dateparse)
df_res.index = df_res['DATA_LECTURA']
```

Now we have dataframe indexed by datetime index. Any Series we get from this dataframe will be timeseries array.

### Transforming features rows in columns

We are going to check at first if when selecting features from rows we will have same series length, because we need to have same length to create columns in a dataframe, in this first version of this project we will avoid dealing with non-existing values by deleting all the feature, as the principal weather features, such temperature, pressure and humidity are fine.


```python
#I'm going to check all features resampling by day and see which have faulty days
for val in df_res['NOM_VARIABLE'].unique():
    ts = df_res['VALOR_LECTURA'][df_res['NOM_VARIABLE']==val]
    t_day = ts.resample('D').mean()
    numrows = t_day.count()
    print(val,': ',numrows,' tipo: ',t_day.dtype)
```

    Precipitació màxima en 1 minut :  4181  tipo:  float64
    Direcció de la ratxa màxima del vent a 10 m :  4320  tipo:  float64
    Ratxa màxima del vent a 10 m :  4320  tipo:  float64
    Humitat relativa mínima :  4320  tipo:  float64
    Temperatura mínima :  4320  tipo:  float64
    Temperatura màxima :  4320  tipo:  float64
    Irradiància solar global :  4320  tipo:  float64
    Precipitació :  4320  tipo:  float64
    Pressió atmosfèrica :  4320  tipo:  float64
    Humitat relativa :  4320  tipo:  float64
    Temperatura :  4320  tipo:  float64
    Direcció de vent 10 m (m. 1) :  4181  tipo:  float64
    Velocitat del vent a 10 m (esc.) :  4181  tipo:  float64
    Humitat relativa màxima :  4181  tipo:  float64
    Pressió atmosfèrica mínima :  4320  tipo:  float64
    Pressió atmosfèrica màxima :  4320  tipo:  float64
    

We will drop features <> 4320 observations.

Then we will get the other features and create new dataframe, resampled to Day/Mean value and with non NaN values with 4320 samples. So we could avoid NaN validation.


```python
df_result = pd.DataFrame()
for val in df_res['NOM_VARIABLE'].unique():
    if val not in ['Precipitació màxima en 1 minut',
                      'Velocitat del vent a 10 m (esc.)',
                      'Direcció de vent 10 m (m. 1)',
                      'Humitat relativa màxima']:
        ts = df_res['VALOR_LECTURA'][df_res['NOM_VARIABLE']==val]
        t_day = ts.resample('D').mean()
        numrows = t_day.count()
        print(val,': ',numrows,' tipo: ',t_day.dtype)
        df_result[val] = t_day.values
df_result.index = t_day.index
```

    Direcció de la ratxa màxima del vent a 10 m :  4320  tipo:  float64
    Ratxa màxima del vent a 10 m :  4320  tipo:  float64
    Humitat relativa mínima :  4320  tipo:  float64
    Temperatura mínima :  4320  tipo:  float64
    Temperatura màxima :  4320  tipo:  float64
    Irradiància solar global :  4320  tipo:  float64
    Precipitació :  4320  tipo:  float64
    Pressió atmosfèrica :  4320  tipo:  float64
    Humitat relativa :  4320  tipo:  float64
    Temperatura :  4320  tipo:  float64
    Pressió atmosfèrica mínima :  4320  tipo:  float64
    Pressió atmosfèrica màxima :  4320  tipo:  float64
    

### Boolean result feature

To fit our classification model we are going to transform our precipitation feature from measure to yes|not has rained to integer feature, 1 to has rained and 0 to not.


```python
rained = lambda x: 1 if x>0 else 0
df_result['Precipitació'] = df_result['Precipitació'].apply(rained)
```

### Balancing data

In my region Mediterranean climate we have some raining days, but the usual is that we have sunny days. So we will check if we have balanced data as initial hypothesis is that not.


```python
total = df_result.Precipitació.count()
rain_days = (df_result.Precipitació == 1).sum() / total * 100
normal_days = (df_result.Precipitació == 0).sum() / total * 100
print("Raining days proportion: %.2f %%"%rain_days)
print("Normal days proportion : %.2f %%"%normal_days)
```

    Raining days proportion: 24.83 %
    Normal days proportion : 75.17 %
    

There are different ways to balance data, in this case and for the moment we will proceed with the easiest one. We are going to get sub-sample from normal_days, and then concat to rain days.


```python
df_rain = df_result[df_result.Precipitació == 1]
df_normal = df_result[df_result.Precipitació == 0]
```


```python
N_normal = 0.4
df_normal_reduced = df_normal.sample(frac=N_normal)
df_result = pd.concat([df_rain,df_normal_reduced],join='inner')
total = df_result.Precipitació.count()
rain_days = (df_result.Precipitació == 1).sum() / total * 100
normal_days = (df_result.Precipitació == 0).sum() / total * 100
print("Raining days proportion: %.2f %%"%rain_days)
print("Normal days proportion : %.2f %%"%normal_days)
```

    Raining days proportion: 45.22 %
    Normal days proportion : 54.78 %
    

Before balancing the dataset, we have done some model without balancing data and we had bad recall for raining days, so we prefer to have model with some wrong positives and improve our accuracy to raining days.

### Dropping correlated variables


```python
plt.title("Fig 1 - Correlation Matrix")
sns.heatmap(df_result.corr()>0.7,cmap='magma');
```


    
![png](/static/notebooks/molletweather/output_27_0.png)
    


After visual check we will drop:


```python
df_result.drop(['Temperatura mínima',
                'Temperatura màxima',
                'Pressió atmosfèrica mínima',
                'Humitat relativa mínima',
                'Pressió atmosfèrica màxima'],axis=1,inplace=True)
```

### Validating data Distribution and outliers


```python
df_result = df_result.apply(lambda x: x.fillna(x.mean()),axis=0)
```


```python
n=2
for col in df_result.drop(['Precipitació'],axis=1).columns:
    plt.boxplot(df_result[col], widths = 0.6,
                patch_artist=True,
                boxprops=dict(facecolor=orange, color=yellow_orange),
                capprops=dict(color=orange),
                whiskerprops=dict(color=orange),
                flierprops=dict(color=orange, markeredgecolor=orange),
                medianprops=dict(color=yellow_orange))
    plt.title('Fig '+str(n)+' - '+str(col))
    plt.grid(color=light_white, linestyle='--', linewidth=0.5,alpha=0.1)
    plt.show()
    n+=1
```


    
![png](/static/notebooks/molletweather/output_33_0.png)
    



    
![png](/static/notebooks/molletweather/output_33_1.png)
    



    
![png](/static/notebooks/molletweather/output_33_2.png)
    



    
![png](/static/notebooks/molletweather/output_33_3.png)
    



    
![png](/static/notebooks/molletweather/output_33_4.png)
    



    
![png](/static/notebooks/molletweather/output_33_5.png)
    


We have not found any important outlier or non-sense value so we are ready to start our modeling

### Saving Data and shuffle
Date index has helped for resampling data (by day), but now it's not more necessary, we are going to drop this index to avoid any interference, and we will 


```python
df_result.reset_index(drop=True,inplace=True)
df_result.sample(frac=1)
df_raw_data = df_result.copy() #we will save our cleaned data
```

## Quick view of raining days characteristics
We are going to plot 2 different graphics, summary relation plot of all features with our predicted value (rain yes/rain no) to see if we will find some relevant classification issue, or something to deal before modeling. And one detailed case for completion.


```python
sns.pairplot(df_result,hue='Precipitació')
plt.suptitle("Fig 8 - Relation Plot between all features",  y=1.02, size = 28);
```


    
![png](/static/notebooks/molletweather/output_38_0.png)
    


Well, it seems that when raining there are always some frontier that would classify raining days vs not.

Some details about one relation to check this.


```python
df_graf = df_result.copy()
df_graf['Precipitació'] = df_graf['Precipitació'].apply(lambda x:str(x)) #to graf as boolean.
(
    ggplot(df_graf,aes(x='Pressió atmosfèrica',y='Humitat relativa',color='Precipitació'))+
    geom_point() +
    scale_color_manual(values = ['#10D0EE',orange]) +
    orange_dark_theme +
    labs(title='Fig 9 - Humitat relativa vs Pressió atmosfèrica')
).draw();
```


    
![png](/static/notebooks/molletweather/output_40_0.png)
    


## Modeling our classification Algorithm

### Split into train and testing data


```python
df_result = df_raw_data.copy() #to ensure that we use raw cleaned data
scaler = StandardScaler()
X = scaler.fit_transform(df_result.drop('Precipitació',axis=1))
y = df_result['Precipitació']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
```

### XGBoost

#### Creating and fitting our model


```python
model_xg = xg.XGBClassifier()
model_xg.fit(X_train,y_train)
```




    XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1,
                  colsample_bynode=1, colsample_bytree=1, gamma=0, gpu_id=-1,
                  importance_type='gain', interaction_constraints='',
                  learning_rate=0.300000012, max_delta_step=0, max_depth=6,
                  min_child_weight=1, missing=nan, monotone_constraints='()',
                  n_estimators=100, n_jobs=0, num_parallel_tree=1, random_state=0,
                  reg_alpha=0, reg_lambda=1, scale_pos_weight=1, subsample=1,
                  tree_method='exact', validate_parameters=1, verbosity=None)



#### Accuracy and Confusion Matrix


```python
y_pred = model_xg.predict(X_test)
```


```python
# Error and Variance scores
conf_matrix = metrics.confusion_matrix(y_test,y_pred)
sns.heatmap(conf_matrix,annot=True, cmap="Oranges" ,fmt='g')
plt.tight_layout()
plt.title('Fig 10 - Confusion matrix - XGBoost')
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()
print(metrics.classification_report(y_test,y_pred))
```


    
![png](/static/notebooks/molletweather/output_48_0.png)
    


                  precision    recall  f1-score   support
    
               0       0.78      0.81      0.79       420
               1       0.77      0.74      0.75       364
    
        accuracy                           0.77       784
       macro avg       0.77      0.77      0.77       784
    weighted avg       0.77      0.77      0.77       784
    
    

#### Feature Importance 


```python
feat_imp=pd.DataFrame(model_xg.feature_importances_,
                      index=df_result.drop('Precipitació',axis=1).columns,
                      columns=['Importance'])
feat_imp['feature'] = feat_imp.index
feat_imp_top10 = feat_imp.loc[feat_imp['Importance'].nlargest(10).index]
plt.title('Fig 11 - Features for XGBoost')
ax = sns.barplot(x="Importance", y="feature", data=feat_imp_top10,palette="Oranges");
```


    
![png](/static/notebooks/molletweather/output_50_0.png)
    


### Logistic Regression

#### Creating and fitting our model


```python
model_lr = LogisticRegression()
model_lr.fit(X_train,y_train)
params = model_lr.get_params()
print('Linear Regression: ',params)
```

    Linear Regression:  {'C': 1.0, 'class_weight': None, 'dual': False, 'fit_intercept': True, 
    'intercept_scaling': 1, 'l1_ratio': None, 'max_iter': 100, 'multi_class': 'auto', 'n_jobs': None, 
    'penalty': 'l2', 'random_state': None, 'solver': 'lbfgs', 'tol': 0.0001, 'verbose': 0, 'warm_start': False}
    

#### Accuracy and Confusion Matrix


```python
y_pred = model_lr.predict(X_test)
```


```python
# Error and Variance scores
conf_matrix = metrics.confusion_matrix(y_test,y_pred)
sns.heatmap(conf_matrix,annot=True, cmap="Oranges" ,fmt='g')
plt.tight_layout()
plt.title('Fig 12 - Confusion matrix Logistic Regression')
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()
print(metrics.classification_report(y_test,y_pred))
```


    
![png](/static/notebooks/molletweather/output_56_0.png)
    


                  precision    recall  f1-score   support
    
               0       0.75      0.81      0.78       420
               1       0.76      0.69      0.72       364
    
        accuracy                           0.75       784
       macro avg       0.75      0.75      0.75       784
    weighted avg       0.75      0.75      0.75       784
    
    

### Random Forest

#### Creating and fitting our model


```python
model_rf = RandomForestClassifier()
model_rf.fit(X_train,y_train)
params = model_rf.get_params()
print('Random Forest: ',params)
```

    Random Forest:  {'bootstrap': True, 'ccp_alpha': 0.0, 'class_weight': None, 'criterion': 'gini', 
    'max_depth': None, 'max_features': 'auto', 'max_leaf_nodes': None, 'max_samples': None, 
    'min_impurity_decrease': 0.0, 'min_impurity_split': None, 'min_samples_leaf': 1, 
    'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 100, 
    'n_jobs': None, 'oob_score': False, 'random_state': None, 'verbose': 0, 'warm_start': False}
    

#### Accuracy and Confusion Matrix


```python
y_pred = model_rf.predict(X_test)
```


```python
# Error and Variance scores
conf_matrix = metrics.confusion_matrix(y_test,y_pred)
sns.heatmap(conf_matrix,annot=True, cmap="Oranges" ,fmt='g')
plt.tight_layout()
plt.title('Fig 13 - Confusion matrix Random Forest')
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()
print(metrics.classification_report(y_test,y_pred))
```


    
![png](/static/notebooks/molletweather/output_62_0.png)
    


                  precision    recall  f1-score   support
    
               0       0.76      0.83      0.80       420
               1       0.78      0.70      0.74       364
    
        accuracy                           0.77       784
       macro avg       0.77      0.77      0.77       784
    weighted avg       0.77      0.77      0.77       784
    
    

#### Features 


```python
feat_imp=pd.DataFrame(model_rf.feature_importances_,
                      index=df_result.drop('Precipitació',axis=1).columns,
                      columns=['Importance'])
feat_imp['feature'] = feat_imp.index
feat_imp_top10 = feat_imp.loc[feat_imp['Importance'].nlargest(10).index]
plt.title('Fig 14 - Features for Random Forest')
ax = sns.barplot(x="Importance", y="feature", data=feat_imp_top10,palette="Oranges");
```


    
![png](/static/notebooks/molletweather/output_64_0.png)
    


### Support Vecotr Machine (SVM)

We will use 'rbf' kernel **Radial Basis Function (RBF)**, It seems the best to use from standard sklearn models.

We have different parameters for *rbf* kernel, depends on our distribution. We will use gamma=1 and C=1, as we have clear differentiation and not big distribution for our features, as we have seen in *Fig 9*.

![image.png](/static/notebooks/molletweather/image.png)

#### Creating and fitting our model


```python
model_svm = svm.SVC(kernel='rbf',gamma=1,C=1,probability=True)
model_svm.fit(X,y)
params = model_svm.get_params()
print('Support Vector Machine: ',params)
```

    Support Vector Machine:  {'C': 1, 'break_ties': False, 'cache_size': 200, 'class_weight': None, 
    'coef0': 0.0, 'decision_function_shape': 'ovr', 'degree': 3, 'gamma': 1, 
    'kernel': 'rbf', 'max_iter': -1, 'probability': True, 'random_state': None, 
    'shrinking': True, 'tol': 0.001, 'verbose': False}
    

#### Accuracy and Confusion Matrix


```python
y_pred = model_svm.predict(X_test)

# Error and Variance scores
conf_matrix = metrics.confusion_matrix(y_test,y_pred)
sns.heatmap(conf_matrix,annot=True, cmap="Oranges" ,fmt='g')
plt.tight_layout()
plt.title('Fig 15 - Confusion matrix Support Vector Machine')
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()
print(metrics.classification_report(y_test,y_pred))
```


    
![png](/static/notebooks/molletweather/output_71_0.png)
    


                  precision    recall  f1-score   support
    
               0       0.85      0.89      0.87       420
               1       0.87      0.82      0.84       364
    
        accuracy                           0.86       784
       macro avg       0.86      0.85      0.86       784
    weighted avg       0.86      0.86      0.86       784
    
    

## Comparing Models

### Adding our models to be compared


```python
# prepare models
models = []
models.append(('LR', model_lr))
models.append(('RF', model_rf))
models.append(('Xgb', model_xg))
models.append(('SVM', model_svm))
```

### Accuracy from K-Fold Cross Validation
We have studied different models individually, by checking that recall data is balanced, and we get good accuracy values, and also have checked different metaparameters for the different models. So we have defined different models with the best values by executing them one by one.

Now, we are going to compare all the models we have created, through K-Fold Cross validation to avoid overfitting as far as we could and most realistic accuracy for our models.

#### Evaluate each model by turn and get accuracy and $\sigma$


```python
# prepare configuration for cross validation test harness
seed = 666 #random number
k = 10 #K fold cross-validation number
# evaluate each model in turn
results = []
names = []
scoring = 'accuracy'
for name, model in models:
	kfold = model_selection.KFold(n_splits=k, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X, y, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)
```

    LR: 0.724545 (0.089277)
    RF: 0.727921 (0.088092)
    Xgb: 0.723678 (0.075765)
    SVM: 0.714410 (0.077524)
    

#### Visual Comparison


```python
# boxplot algorithm comparison
fig = plt.figure(figsize=(12,8))
fig.suptitle('Fig 16 - Algorithm Comparison',y=0.95,size=20)
ax = fig.add_subplot(111)
plt.boxplot(results, widths = 0.6,
            patch_artist=True,
            boxprops=dict(facecolor=orange, color=yellow_orange),
            capprops=dict(color=orange),
            whiskerprops=dict(color=orange),
            flierprops=dict(color=orange, markeredgecolor=orange),
            medianprops=dict(color=yellow_orange))
plt.grid(color=light_white, linestyle='--', linewidth=0.5,alpha=0.1)
ax.set_xticklabels(names)
plt.show();
```


    
![png](/static/notebooks/molletweather/output_79_0.png)
    


Another point of view of the same data


```python
# Density Plot and Histogram of all arrival delays
i = 0
plt.figure(figsize=(12,8))
for res in results:
    # Draw the density plot
    sns.set_palette("Oranges")
    sns.distplot(res, hist = False, kde = True,
                 kde_kws = {'linewidth': 2},
                 label = names[i])
    i+=1  
# Plot formatting
plt.legend(prop={'size': 12})
plt.grid(color=light_white, linestyle='--', linewidth=0.5,alpha=0.1)
plt.title('Fig 17 - Density Plot for accuracy Distribution',size=20)
plt.xlabel('Accuracy')
plt.ylabel('Density')
plt.show();
```


    
![png](/static/notebooks/molletweather/output_81_0.png)
    


### Roc Curves for different models


```python
i = 0
plt.figure(figsize=(12,8))
for name, model in models:
    probs = model.predict_proba(X_test)
    probs = probs[:, 1] #only positive class
    auc = metrics.roc_auc_score(y_test, probs)
    print(name,' AUC: %.2f' % auc)
    fpr, tpr, thresholds = metrics.roc_curve(y_test, probs)
    plt.plot(fpr, tpr, color=dark_theme_colors[i], label=name)
    i+=1
plt.title('Fig 18 - Receiver Operating Characteristic (ROC) Curve',size=20)
plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--',alpha=0.8)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend()
plt.show();
```

    LR  AUC: 0.84
    RF  AUC: 0.85
    Xgb  AUC: 0.85
    SVM  AUC: 0.93
    


    
![png](/static/notebooks/molletweather/output_83_1b.png)
    


### McNemar Comparision Between models
We are going to get 1 model, the one that has best results in different testing (however in k-fold validation it's bit lower) the Support Vector Machine. And we are going to apply McNemar comparision with the other models.

It uses null-hypothesis assuming that $P(1)$ and $P(2)$ are the same, so the alternative is that models are different, and we could evaluate *p-value* and compare.

To test the null hypothesis that the predictive performance of two models are equal (using a significance level of α=0.05)


```python
y_pred_svm = models[3][1].predict(X_test)
for name, model in models:
    if name != 'SVM':
        y_pred2 = model.predict(X_test)
        tb = mcnemar_table(y_target=y_test, 
                   y_model1=y_pred_svm, 
                   y_model2=y_pred2)
        chi2, p = mcnemar(ary=tb, corrected=True)
        print('************************** ',name,' ****************************')
        print('chi-squared:', chi2)
        print('p-value:', p)
        if p > 0.05:
            print("We can reject null-hypothesis, Models performs different")
        else:
            print("Null hypthoesis cannot be rejected, No significant difference")
```

    **************************  LR  ****************************
    chi-squared: 64.64646464646465
    p-value: 8.961694634394557e-16
    Null hypthoesis cannot be rejected, No significant difference
    **************************  RF  ****************************
    chi-squared: 47.86813186813187
    p-value: 4.558715474204364e-12
    Null hypthoesis cannot be rejected, No significant difference
    **************************  Xgb  ****************************
    chi-squared: 37.57798165137615
    p-value: 8.783035418793241e-10
    Null hypthoesis cannot be rejected, No significant difference
    

In fact, models are so near that this result could be something obvious, but now we can confirm in an objective way that there is no difference in terms of McNeman test using other models than SVM.

### Model visualization (using 2 principal features)
We are going to use 'Humitat relativa' and 'Pressió atmosfèrica' as they are 2 principal features in classification models, to take a look on how the classification models are working in the 'backend'.

For that I will use sklearn sample that I have found [here](https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html) that it's really interesant.


```python
# preprocess dataset, split into training and test part
h = .02  # step size in the mesh
df_result = df_raw_data.copy()
scaler = StandardScaler() #Logistic regression variable weigh is relevant so we will scale it
Xvalues = df_result.drop('Precipitació',axis=1)
Xvis = scaler.fit_transform(Xvalues[['Humitat relativa','Pressió atmosfèrica']])
Xvis_train, Xvis_test, yvis_train, yvis_test = train_test_split(Xvis, y, test_size=.4, random_state=42)
x_min, x_max = Xvis[:, 0].min() - .5, Xvis[:, 0].max() + .5
y_min, y_max = Xvis[:, 1].min() - .5, Xvis[:, 1].max() + .5
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# just plot the dataset first
plt.figure(figsize=(20,15))
plt.suptitle("Fig 19 - Classification Intiutive by Model",  y=1, size = 28)
cm = plt.cm.coolwarm
cm_bright = ListedColormap(['#10D0EE',orange])
ax = plt.subplot(1, len(models) + 1, 1)
ax.set_title("Input data")
# Plot the training points
ax.scatter(Xvis_train[:, 0], Xvis_train[:, 1], c=yvis_train, cmap=cm_bright,
           edgecolors=darked)
# Plot the testing points
ax.scatter(Xvis_test[:, 0], Xvis_test[:, 1], c=yvis_test, cmap=cm_bright, alpha=0.6,
           edgecolors=darked)
ax.set_xlim(xx.min(), xx.max())
ax.set_ylim(yy.min(), yy.max())
ax.set_xticks(())
ax.set_yticks(())
# iterate over classifiers
i = 2
for name, clf in models:
    ax = plt.subplot(1, len(models) + 1, i)
    clf.fit(Xvis_train, yvis_train)
    score = clf.score(Xvis_test, yvis_test)
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    if hasattr(clf, "decision_function"):
        Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
    else:
        Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    ax.contourf(xx, yy, Z, cmap=cm, alpha=.7)

    # Plot the training points
    ax.scatter(Xvis_train[:, 0], Xvis_train[:, 1], c=yvis_train, cmap=cm_bright,
               edgecolors=darked)
    # Plot the testing points
    ax.scatter(Xvis_test[:, 0], Xvis_test[:, 1], c=yvis_test, cmap=cm_bright,
               edgecolors=darked, alpha=0.6)

    ax.set_xlim(xx.min(), xx.max())
    ax.set_ylim(yy.min(), yy.max())
    ax.set_xticks(())
    ax.set_yticks(())
    ax.set_title(name)
    ax.text(xx.max() - .3, yy.min() + .3, ('Accuracy: %.2f' % score).lstrip('0'),
            size=15, horizontalalignment='right')
    i += 1
```


    
![png](/static/notebooks/molletweather/output_88_0.png)
    


### Automated tool - Tpot
We are going to use an automated tool to compare our score with automated score tool.
We are going to use [Tpot](http://epistasislab.github.io/tpot/) tool. In terms of score comparision we should know that by default k-fold cross validation for Tpot is *10* the same as we have used when comparing models.


```python
from tpot import TPOTClassifier
```


```python
tpot = TPOTClassifier(generations=5,population_size=50, verbosity=2, n_jobs=3)
tpot.fit(X_train, y_train)
```
```
HBox(children=(HTML(value='Optimization Progress'), FloatProgress(value=0.0, max=300.0), HTML(value='')))



Generation 1 - Current best internal CV score: 0.7954486836101027

Generation 2 - Current best internal CV score: 0.8055195127274171

Generation 3 - Current best internal CV score: 0.8055195127274171

Generation 4 - Current best internal CV score: 0.8055195127274171

Generation 5 - Current best internal CV score: 0.8055195127274171

Best pipeline: 
MLPClassifier(OneHotEncoder(input_matrix, minimum_fraction=0.25, sparse=False, threshold=10), 
alpha=0.1, learning_rate_init=0.001)

TPOTClassifier(generations=5, n_jobs=3, population_size=50, verbosity=2)
```

```python
print(tpot.score(X_test, y_test))
```

    0.764030612244898
    

Using this automated tool we have arrived to an accuracy of *0.76* and our best result by modeling one by one has been *0.73*, which is a really good result.

The algorithm that recommends Tpot is MLPClassifier it's Multi-layer Perceptron classifier. Neural network with *100* layers by default, and 'relu' activation function.

I think that an accuracy difference of *0.03* it's not so relevant for us than understanding or explaining the statistical model. Models done one by one could help much more how to explain or understand the dataset.

## Conclusions

If we should get only one model to our predictions we would get **Support Vector Machine**.

1- It has the best score in usual train/test validations, for *recall*, *f1 score* and *accuracy*

2- When doing K-Fold cross validation, all models have perform similar *accuracy*, standard deviation overlaps all the other model results.

3- It has far away the best *ROC Curve* and *AUC* value.

4- The way as describe different probabilities for raining days fits with the correlation.

5- Compared with other models there are no difference between confusion matrix results. (McNeman)

6- It's close also to *accuracy* from the model used by ML automation tool.
