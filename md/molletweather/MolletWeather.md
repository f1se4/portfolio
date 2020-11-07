# Rain prediction in my town based on past variables (not physic model)

## Libraries

```python
# Data library
import pandas as pd

# Graphic libraries
import seaborn as sns
import matplotlib.pyplot as plt
from plotnine import *

# Date Libraries
from datetime import datetime

# Machine Learning Libraries
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import xgboost as xg #Algorithm, we will take classifier.
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn import metrics
```
## Reading Data
We are going to read 3 different Data from [Meteocat Opendata](https://www.meteo.cat/wpweb/serveis/cataleg-de-serveis/serveis-oberts/dades-obertes/):

- **Stations information:** id and name of all Catalonian weather stations, it will let us to filter by the nearest station to my town, in this case 'Parets del Vallès'.
- **Raw data by time:** Each day in different time there lots of measurment, this table have all the data saved in *'VALOR_LECTURA'* and which is the units of this measurement comes from *'CODI_VARIABLE'*. This file has been filtered from origin, because when saving all station data the file was coming to big... and if fact I only want 1 station.
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

'DATA_LECUTRA' is a date which will help us to simplify the model by days, and help us to eliminate some hours non-mesured data, but in the future we will try to do hourly as for raining reasons microstate of the weather could be really important.

### Joining measure information detail with measurement value

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

Then we will get the other features and create new dataframe, resampled to Day/Mean value and with non NaN values with 4320 samples.


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

We will also for fit our classification model going to transform our precipitation feature from measure to yes|not has rained feature, 1 to has rained and 0 to not.


```python
rained = lambda x: 1 if x>0 else 0
df_result['Precipitació'] = df_result['Precipitació'].apply(rained)
```

### Balancing data

In my region Mediterranian climate we have some raining days, but the usual is that we have sunny days. So we will check if we have balanced data as initial hypothesis is that not.


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
sns.heatmap(df_result.corr()>0.7,cmap='magma')
plt.title("Fig 1 - Correlation Matrix")
```
    
![png](/static/notebooks/molletweather/output_27_1.png)
    
After visual check we will drop:

```python
df_result.drop(['Temperatura mínima',
                'Temperatura màxima',
                'Pressió atmosfèrica mínima',
                'Humitat relativa mínima',
                'Pressió atmosfèrica màxima'],axis=1,inplace=True)
```

### Dealing with *NaN* values
In this case we will apply mean value from column to the correspondence *Nan* value.

```python
df_result = df_result.apply(lambda x: x.fillna(x.mean()),axis=0)
```

### Validating data Distribution and outliers

```python
n=2
for col in df_result.drop(['Precipitació'],axis=1).columns:
    sns.boxplot(data=df_result[col])
    plt.title('Fig '+str(n)+' - '+str(col))
    plt.show()
    n+=1
```


    
![png](/static/notebooks/molletweather/output_30_0.png)
    



    
![png](/static/notebooks/molletweather/output_30_1.png)
    



    
![png](/static/notebooks/molletweather/output_30_2.png)
    



    
![png](/static/notebooks/molletweather/output_30_3.png)
    



    
![png](/static/notebooks/molletweather/output_30_4.png)
    



    
![png](/static/notebooks/molletweather/output_30_5.png)
    

We have not find any important outlier or non-sense value so we are ready to start our modeling

```python
df_raw_data = df_result.copy() #we will save our cleaned data
```

## Quick view of raining days characteristics

We are going to plot 2 different graphics, summary relation plot of all features with our predicted value (rain yes/rain no) to see if we will find some relevant classification issue, or something to deal before modeling.

```python
sns.pairplot(df_result,hue='Precipitació')
plt.suptitle("Fig 8 - Relation Plot between all features",  y=1.02, size = 28);
```


    
![png](/static/notebooks/molletweather/output_33_0.png)
    


Well, it seems that when raining there are always some frontier that would be classify raining days vs not.

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


    
![png](/static/notebooks/molletweather/output_35_0.png)
    


## Modeling our classification Algorithm

### XGBoost

#### Split into train and testing data


```python
df_result = df_raw_data.copy() #to ensure that we use raw cleaned data
scaler = StandardScaler()
X = scaler.fit_transform(df_result.drop('Precipitació',axis=1))
y = df_result['Precipitació']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
```

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


    
![png](/static/notebooks/molletweather/output_42_0.png)
    


                  precision    recall  f1-score   support
    
               0       0.76      0.82      0.79       420
               1       0.77      0.71      0.74       364
    
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


    
![png](/static/notebooks/molletweather/output_44_0.png)
    


### Logistic Regression

#### Split into train and testing data and scaling data


```python
df_result = df_raw_data.copy()
scaler = StandardScaler()
X = scaler.fit_transform(df_result.drop('Precipitació',axis=1))
y = df_result['Precipitació']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
```

#### Creating and fitting our model


```python
model_lr = LogisticRegression()
model_lr.fit(X_train,y_train)
```

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

    
![png](/static/notebooks/molletweather/output_52_0.png)
    


                  precision    recall  f1-score   support
    
               0       0.76      0.86      0.81       420
               1       0.81      0.68      0.74       364
    
        accuracy                           0.78       784
       macro avg       0.78      0.77      0.77       784
    weighted avg       0.78      0.78      0.78       784
    
    

### Random Forest
#### Split into train and testing data and scaling data


```python
X = df_result.drop('Precipitació',axis=1)
y = df_result['Precipitació']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
```

#### Creating and fitting our model


```python
model_rf = RandomForestClassifier()
model_rf.fit(X_train,y_train)
```

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

    
![png](/static/notebooks/molletweather/output_59_0.png)
    


                  precision    recall  f1-score   support
    
               0       0.76      0.85      0.80       420
               1       0.80      0.68      0.74       364
    
        accuracy                           0.77       784
       macro avg       0.78      0.77      0.77       784
    weighted avg       0.78      0.77      0.77       784
    
    

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


    
![png](/static/notebooks/molletweather/output_61_0.png)
    


### Support Vector Machine (SVM)

We will use 'rbf' kernel **Radial Basis Function (RBF)**, It seems the best to use from standard sklearn models.

We have different parameters for *rbf* kernel, depends on our distribution. It's going to be used gamma=1 and C=1, as we have clear differentiation and not big distribution for our features, as we have seen in *Fig 9*.

![image.png](/static/notebooks/molletweather/image.png)

#### Split into train and testing data


```python
df_result = df_raw_data.copy()
scaler = StandardScaler() #Logistic regression variable weigh is relevant so we will scale it
X = scaler.fit_transform(df_result.drop('Precipitació',axis=1))
y = df_result['Precipitació']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
```

#### Creating and fitting our model


```python
model_svm = svm.SVC(kernel='rbf',gamma=1,C=1)
model_svm.fit(X,y)
```
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
    
![png](/static/notebooks/molletweather/output_70_0.png)
    


                  precision    recall  f1-score   support
    
               0       0.84      0.91      0.87       420
               1       0.89      0.79      0.84       364
    
        accuracy                           0.86       784
       macro avg       0.86      0.85      0.86       784
    weighted avg       0.86      0.86      0.86       784
    