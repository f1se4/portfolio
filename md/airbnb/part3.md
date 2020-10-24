# Barcelona Airbnb DS analysis (3rd part)
```
\
|--Airbnb_Barcelona.ipynb
|--data
|   |-output.csv
|--model
    |-randforestKK_NNNN.joblib
```
Here we are going to model our data to perform the best result we could and then save the model to use in a production system as a reference and consumable service

## Importing Libraries


```python
#Data
import pandas as pd 
import numpy as np

#Graphics libraries
from plotnine import *
import seaborn as sns
import matplotlib.pyplot as plt

#Librearies for ML model
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from sklearn.feature_selection import SelectKBest, f_regression
#Accuracy
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
```

## Reading the data
At the end of *part1* we finished with cleaned data set **output.csv**, we will continue using this data set, which is the same that we have analyzed in *part2*. 

Correlations found in *part2* will be dropped.

Categorical data that we use as is in *part2*, here we will transform in columns and Boolean data type, without losing the information, it will be ready for model.


```python
airbnb_data = pd.read_csv("./data/output.csv")
airbnb_data.drop(['Unnamed: 0',
                  'id',
                  'latitude',
                  'longitude',
                  'bedroom comforts', #bathroom essentials related
                  'host_total_listings_count', #related to host_listings_count
                  'Unnamed: 225',
                  'room_type',
                  'bathrooms'],axis=1,inplace=True)

# One-hot encode using pandas get_dummies
airbnb_data = pd.get_dummies(airbnb_data)
```


```python
(
    ggplot(airbnb_data,aes(sample='price')) +
    geom_qq(color=orange) + 
    stat_qq_line(color=light_orange) +
    labs(title='Fig 1 - QQPlot for Price Distribution') 
)
```

    
![png](/static/notebooks/airbnb/part3/output_6_0.png)



## Independent variable vs dependent variables
We are going to separate our dependent variable (the one we want to predict) from the independent values.


```python
X = airbnb_data.drop(['price'],axis=1).astype('float').values
y = airbnb_data['price'].astype('float')
```

## Random Forest Model
We are going to do regression model based on Random Forest algorithm. We are going to use this model based on:

- We have several columns/characteristics to be evaluated and this model it's good one to lots of columns regression (independent variables).

### Filter Selection

As we have more or less 200 variables to be analyzed, we could try to fit all them or try to find the most relevant ones. To do that we could select the best features based on univariate statistical tests, removing all but the $k$ highest scoring features.

Also, we could check how this $k$ feature impacts in our model score, so we would try to find the best combination of relevant features, which could let us to explain the model (in random forest is always difficult) and also make our model more efficient as it will do less calculation to good result.


```python
results = []
print('|----|---------------------|')
print('| k  |    SQRT(MSQE)       |')
for i in range (1,45):
    Xraw = airbnb_data.drop(['price'],axis=1).astype('float')
    X = Xraw.values
    y = airbnb_data['price'].astype('float')      
    X = SelectKBest(f_regression,k=i).fit_transform(X,y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    random_forest_regression = RandomForestRegressor()
    random_forest_regression.fit(X_train,y_train)
    y_test_pred = random_forest_regression.predict(X_test)
    results.append((mean_squared_error(y_test,y_test_pred))**(1/2))
    print('|----|---------------------|')
    print('|',i,' | ',(mean_squared_error(y_test,y_test_pred))**(1/2),'|')
print('|----|---------------------|')
```

    |----|---------------------|
    | k  |    SQRT(MSQE)       |
    |----|---------------------|
    | 1  |  29.816610467450396 |
    |----|---------------------|
    | 2  |  29.4726279422337   |
    |----|---------------------|
    | .. |     ......          |
    |----|---------------------|
    | 44 |  23.962164201192262 |
    |----|---------------------|
    

We have check model score for 1-45 $k$ possibilities, in fact it has been checked some more, but this is possible final result, as it seems that some *limit* value has been find.


```python
x_elbow = np.arange(1,len(results)+1,1)
y_elbow = results
elbow = pd.DataFrame({'x':x_elbow,'y':y_elbow})
(
    ggplot(elbow,aes(x='x',y='y'))+
    geom_line(color=orange) +
    scale_x_continuous( limits=(1,50), breaks=range(1,50,1))+
    geom_vline(xintercept=34,color=yellow_orange) +
    labs(x='k Number',y='SQRT(MSQE)',title='Fig 2 - Error vs "k" variable (LR)') +
)
```

    
![png](/static/notebooks/airbnb/part3/output_13_0.png)


When we arrive to 27 features the model scores values near 23, and around 34 we find minimum in all the tests that have been done, so we will take $k=34$.

### Model pre-filtered and score


```python
n=34
N_ESTIM = 1000
Xraw = airbnb_data.drop(['price'],axis=1).astype('float')
X = Xraw.values
y = airbnb_data['price'].astype('float')      
selection = SelectKBest(f_regression,k=n)
train_data = selection.fit(X,y)
cols = selection.get_support(indices=True)
X = Xraw.iloc[:,cols].reset_index(drop=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
random_forest_regression = RandomForestRegressor(n_jobs=2,n_estimators=N_ESTIM, oob_score=True)
random_forest_regression.fit(X_train,y_train)
y_test_predict = random_forest_regression.predict(X_test)
y_train_predict = random_forest_regression.predict(X_train)
print('K filter value: ',n)
print('Number Random Forests: ',N_ESTIM)
rf_results=pd.DataFrame({'algorithm':['Random Forest'],
                         'Training error': [mean_absolute_error(y_train,y_train_predict)],
                         'Test error':[mean_absolute_error(y_test,y_test_predict)],
                         'Train_r2_score':[r2_score(y_train,y_train_predict)],
                         'Test_r2_Score':[r2_score(y_test,y_test_predict)]})
print(rf_results) 
```

    K filter value:  34
    Number Random Forests:  1000
           algorithm  Training error  Test error  Train_r2_score  Test_r2_Score
    0  Random Forest        6.395379   17.598877        0.933483       0.515582
    


```python
feat_imp=pd.DataFrame(random_forest_regression.feature_importances_,index=Xraw.iloc[:,cols].columns,columns=['Importance'])
feat_imp['feature'] = feat_imp.index
feat_imp_top10 = feat_imp.loc[feat_imp['Importance'].nlargest(10).index]
ax = sns.barplot(x="Importance", y="feature", data=feat_imp_top10,palette="Oranges")
# Title 
plt.suptitle("Fig 3 - Random Forest Top10 Features",y=0.93, size = 24);
```


    
![png](/static/notebooks/airbnb/part3/output_16_0.png)
    


Also we will try to have graphical view of how is distributed our predicted data from testing data.


```python
result_df = pd.DataFrame({'Test Data':y_test,'Predicted Data':y_test_pred})
result_df.reset_index(drop=True,inplace=True)
result_df['id'] = result_df.index
result_df = pd.melt(result_df,id_vars='id', value_vars=['Test Data','Predicted Data'])

(
    ggplot(result_df,aes(x='id',y='value',color='variable')) +  
    geom_point() +
    scale_color_manual(values = ['#10D0EE',orange]) +
    labs(title='Fig 4 - Predicted Data vs Test Data (RF)',x='',y='Price $',color='Data Type') +
)
```
    
![png](/static/notebooks/airbnb/part3/output_19_0.png)


Well $R^2=0,52$ It's not a good result, but it's not the worst. Comparing predicted and testing data it seems that it has good behavior around the mean price of the dataset and it's not so good with the prices that are down in the table and up in the table.


## Decision Tree


```python
# Decision Tree
X = Xraw.iloc[:,cols].reset_index(drop=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
dt=DecisionTreeRegressor().fit(X_train,y_train)
train_predict=dt.predict(X_train)
test_predict=dt.predict(X_test)
dt_results=pd.DataFrame({'algorithm':['Decision Tree'],
                         'Training error': [mean_absolute_error(y_train,train_predict)],
                         'Test error':[mean_absolute_error(y_test,test_predict)],
                         'Train_r2_score':[r2_score(y_train,train_predict)],
                         'Test_r2_Score':[r2_score(y_test,test_predict)]})
print(dt_results)    
```

           algorithm  Training error  Test error  Train_r2_score  Test_r2_Score
    0  Decision Tree        0.006893   23.471691        0.999932       0.042407
    


```python
result_df = pd.DataFrame({'Test Data':y_test,'Predicted Data':test_predict})
result_df.reset_index(drop=True,inplace=True)
result_df['id'] = result_df.index
result_df = pd.melt(result_df,id_vars='id', value_vars=['Test Data','Predicted Data'])
(
    ggplot(result_df,aes(x='id',y='value',color='variable')) +  
    geom_point() +
    scale_color_manual(values = ['#10D0EE',orange]) +
    labs(title='Fig 5 - Predicted Data vs Test Data (DT)',x='',y='Price $',color='Data Type') +
)
```
    
![png](/static/notebooks/airbnb/part3/output_23_0.png)


It's clearly overfitted.


```python
feat_imp=pd.DataFrame(dt.feature_importances_,index=Xraw.iloc[:,cols].columns,columns=['Importance'])
feat_imp['feature'] = feat_imp.index
feat_imp_top10 = feat_imp.loc[feat_imp['Importance'].nlargest(10).index]
ax = sns.barplot(x="Importance", y="feature", data=feat_imp_top10,palette="Oranges")
# Title 
plt.suptitle("Fig 6 - Decision Tree Top10 Features",y=0.93, size = 24);
```

![png](/static/notebooks/airbnb/part3/output_25_0.png)
  
## XGboost


```python
# XGB Regressor
xg=XGBRegressor().fit(X_train,y_train)
train_predict=xg.predict(X_train)
test_predict=xg.predict(X_test)
xg_results=pd.DataFrame({'algorithm':['XGBoost'],
                         'Training error': [mean_absolute_error(y_train,train_predict)],
                         'Test error':[mean_absolute_error(y_test,test_predict)],
                         'Train_r2_score':[r2_score(y_train,train_predict)],
                         'Test_r2_Score':[r2_score(y_test,test_predict)]})
print(xg_results) 
```

      algorithm  Training error  Test error  Train_r2_score  Test_r2_Score
    0   XGBoost       13.575936    18.06282         0.69686       0.490257
    


```python
result_df = pd.DataFrame({'Test Data':y_test,'Predicted Data':test_predict})
result_df.reset_index(drop=True,inplace=True)
result_df['id'] = result_df.index
result_df = pd.melt(result_df,id_vars='id', value_vars=['Test Data','Predicted Data'])
(
    ggplot(result_df,aes(x='id',y='value',color='variable')) +  
    geom_point() +
    scale_color_manual(values = ['#10D0EE',orange]) +
    labs(title='Fig 7 - Predicted Data vs Test Data (XGB)',x='',y='Price $',color='Data Type') +
)
```
    
![png](/static/notebooks/airbnb/part3/output_28_0.png)

```python
feat_imp=pd.DataFrame(xg.feature_importances_,index=Xraw.iloc[:,cols].columns,columns=['Importance'])
feat_imp['feature'] = feat_imp.index
feat_imp_top10 = feat_imp.loc[feat_imp['Importance'].nlargest(10).index]
plt.figure(figsize=(20,15))
sns.set(rc={
    'axes.facecolor':'#303030', 
    'figure.facecolor':'#303030',
    'text.color':light_white,
    'axes.labelcolor':light_white,
    'xtick.color':light_white,
    'ytick.color':light_white,
})
ax = sns.barplot(x="Importance", y="feature", data=feat_imp_top10,palette="Oranges")
# Title 
plt.suptitle("Fig 8 - XGBoost Top10 Features",y=0.93, size = 24);
```
 
![png](/static/notebooks/airbnb/part3/output_29_0.png)
    
## Model Comparision

```python
pd.concat([rf_results,dt_results,xg_results],axis=0,ignore_index=True)
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>algorithm</th>
      <th>Training error</th>
      <th>Test error</th>
      <th>Train_r2_score</th>
      <th>Test_r2_Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Random Forest</td>
      <td>6.395379</td>
      <td>17.598877</td>
      <td>0.933483</td>
      <td>0.515582</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Decision Tree</td>
      <td>0.006893</td>
      <td>23.471691</td>
      <td>0.999932</td>
      <td>0.042407</td>
    </tr>
    <tr>
      <th>2</th>
      <td>XGBoost</td>
      <td>13.575936</td>
      <td>18.062820</td>
      <td>0.696860</td>
      <td>0.490257</td>
    </tr>
  </tbody>
</table>
</div>

## Conclusions

## Save the best model


```python
from joblib import dump, load
dump(random_forest_regression, './models/randforest35_1000.joblilb')
```
    ['./models/randforest35_1000.joblilb']


