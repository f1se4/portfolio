### Barcelona Airbnb DS analysis (3rd part)
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
from xgboost import XGBRegressor, to_graphviz
from sklearn.feature_selection import SelectKBest, f_regression
#Accuracy
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.metrics import balanced_accuracy_score, roc_auc_score, make_scorer # for scoring during cross validation
from sklearn.model_selection import GridSearchCV # cross validation
```

## Reading the data
At the end of *part1* we finished with cleaned data set **output.csv**, we will continue using this data set, which is the same that we have analyzed in *part2*. 

Correlations found in *part2* will be droped.

Categorical data that we use as is in *part2*, here we will transform in columns and boolean data type, without loosing the information, it will be ready for model.


```python
airbnb_data = pd.read_csv("./data/output.csv")
airbnb_data.drop(airbnb_data.filter(like='Unnamed').columns,axis=1,inplace=True)
airbnb_data.drop([
                  'id', #This was usefull for graphics analysis for samples, but not for modeling
                  'latitude',
                  'longitude',
                  'bedroom comforts', #bedroom essentials related
                  'host_total_listings_count', #related to host_listings_count
                  'microwave', #related to refrigerator
                ],axis=1,inplace=True)

# One-hot encode using pandas get_dummies
airbnb_data = pd.get_dummies(airbnb_data)
```

## Independent variable vs dependent variables
We are going to separate our dependent variable (the one we want to predict) from the independent values.


```python
Xraw = airbnb_data.drop(['price'],axis=1).astype('float')
X = Xraw.copy()
y = airbnb_data['price'].astype('float')
```

----

## Random Forest Model
We are going to do regression model based on Random Forest algorithm. We are going to use this model based on:

- We have several columns/characteristics to be evaluated and this model it's good one to lots of columns regression (independent variables).

### Filter Selection

As we have more or less 200 variables to be analyzed, we could try to fit all them or try to find the most relevant ones. To do that we could select the best features based on univariate statistical tests, removing all but the $k$ highest scoring features.

Also, we could check how this $k$ feature impacts in our model score, so we would try to find the best combination of relevant features, which could let us to explain the model (in random forest is always difficult) and also make our model more efficient as it will do less calculation to good result.


```python
results = []
count = 0
minim_abs = 99999999999
nmax = 9

N = X.shape[1]
print('|----|---------------------|')
print('| k  |       RMSE          |')
for i in range (1,N):
    X = Xraw.copy()
    X = SelectKBest(f_regression,k=i).fit_transform(X,y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)
    random_forest_regression = RandomForestRegressor()
    random_forest_regression.fit(X_train,y_train)
    y_test_pred = random_forest_regression.predict(X_test)
    results.append((mean_squared_error(y_test,y_test_pred))**(1/2))
    print('|----|---------------------|')
    print('|',i,' | ',(mean_squared_error(y_test,y_test_pred))**(1/2),'|')
    #Exit at nmax items not decreasing
    if len(results) != 0:
        if (mean_squared_error(y_test,y_test_pred))**(1/2) > minim_abs:
            count += 1
        else:
            minim_abs = (mean_squared_error(y_test,y_test_pred))**(1/2)            
            count = 0
    else:
        count = 0
    if count > nmax:
        print('|----|---------------------|')
        print('| breaking after nmax items|')
        break    
print('|----|---------------------|')
```

    |----|---------------------|
    | k  |       RMSE          |
    |----|---------------------|
    | 1  |  28.93177920365006 |
    |----|---------------------|
    | 2  |  28.897571906376317 |
    |----|---------------------|
    | .. |        ..           |
    |----|---------------------|
    | 78  |  23.28982612403383 |
    |----|---------------------|
    | 79  |  23.189823897435403 |
    |----|---------------------|
    | 80  |  23.31864216244052 |
    |----|---------------------|
    | 81  |  23.298398543690762 |
    |----|---------------------|
    | 82  |  23.246322375416927 |
    |----|---------------------|
    | 83  |  23.23919914973194 |
    |----|---------------------|
    | 84  |  23.255104654137757 |
    |----|---------------------|
    | 85  |  23.311416436432804 |
    |----|---------------------|
    | 86  |  23.27902654988726 |
    |----|---------------------|
    | 87  |  23.368225650619195 |
    |----|---------------------|
    | 88  |  23.370200396371878 |
    |----|---------------------|
    | breaking after nmax items|
    |----|---------------------|
 
```python
k=results.index(min(results)) + 1
print('Minimum Element in the list is',k,' and is ',min(results))
```

    Minimum Element in the list is 79  and is  23.189823897435403
    

We have check model score for $k$ possibilities, in fact it has been checked some more, but this is possible final result, as it seems that some *limit* value has been find.


```python
N = k + 10
x_elbow = np.arange(1,len(results)+1,1)
y_elbow = results
elbow = pd.DataFrame({'x':x_elbow,'y':y_elbow})
(
    ggplot(elbow,aes(x='x',y='y'))+
    geom_line(color=orange) +
    scale_x_continuous( limits=(1,N), breaks=range(1,N,1))+
    geom_vline(xintercept=k,color=yellow_orange) +
    labs(x='k Number',y='RMSE',title='Fig 2 - Error vs "k" variable (LR)') +
```


    
![png](/static/notebooks/airbnb/part3/output_14_0.png)
    

We will take k= {{k}}  as the minimum.

### Model pre-filtered and score


```python
N_ESTIM = 1000
X = Xraw
selection = SelectKBest(f_regression,k=k)
X = selection.fit_transform(X,y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)
random_forest_regression = RandomForestRegressor(n_jobs=2,n_estimators=N_ESTIM, oob_score=True)
random_forest_regression.fit(X_train,y_train)
y_test_predict = random_forest_regression.predict(X_test)
y_train_predict = random_forest_regression.predict(X_train)
print('K filter value: ',k)
print('Number Random Forests: ',N_ESTIM)
rf_results=pd.DataFrame({'algorithm':['Random Forest'],
                         'Training error': [mean_absolute_error(y_train,y_train_predict)],
                         'Test error':[mean_absolute_error(y_test,y_test_predict)],
                         'Train_r2_score':[r2_score(y_train,y_train_predict)],
                         'Test_r2_Score':[r2_score(y_test,y_test_predict)]})
print(rf_results) 
```

    K filter value:  79
    Number Random Forests:  1000
           algorithm  Training error  Test error  Train_r2_score  Test_r2_Score
    0  Random Forest        6.323665   17.327035        0.934937       0.529434
    


```python
feat_imp=pd.DataFrame(random_forest_regression.feature_importances_,
                      index=Xraw.iloc[:,selection.get_support(indices=True)].columns,
                      columns=['Importance'])
feat_imp['feature'] = feat_imp.index
feat_imp_top10 = feat_imp.loc[feat_imp['Importance'].nlargest(10).index]
ax = sns.barplot(x="Importance", y="feature", data=feat_imp_top10,palette="Oranges")
# Title 
plt.suptitle("Fig 3 - Random Forest Top10 Features",y=0.93, size = 24);
```


    
![png](/static/notebooks/airbnb/part3/output_17_0.png)
    


Also we will try to have graphical view of how is distributed our predicted data from testing data.


```python
result_df = pd.DataFrame({'Test Data':y_test,'Predicted Data':y_test_pred})
result_df.reset_index(drop=True,inplace=True)
result_df['id'] = result_df.index
result_df = pd.melt(result_df,id_vars='id', value_vars=['Test Data','Predicted Data'])
```


```python
(
    ggplot(result_df,aes(x='id',y='value',color='variable')) +  
    geom_point() +
    scale_color_manual(values = ['#10D0EE',orange]) +
    labs(title='Fig 4 - Predicted Data vs Test Data (RF)',x='',y='Price $',color='Data Type') +
)
```


    
![png](/static/notebooks/airbnb/part3/output_20_0.png)
    

Well $R^2=0,52$ It's not a good result, but it's not the worst. Comparing predicted and testing data it seems that it has good behavior around the mean price of the dataset and it's not so good with the prices that are down in the table and up in the table.


## Decision Tree


```python
# Decision Tree
X = Xraw
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
regtree = DecisionTreeRegressor(min_samples_split=2, min_samples_leaf=4, max_depth=7, random_state=0)
dt = regtree.fit(X_train,y_train)
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
    0  Decision Tree       18.362137     19.4424        0.477765       0.430368
    


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


    
![png](/static/notebooks/airbnb/part3/output_24_0.png)
    

It has aggregated some diferent prices classified by internal logic.


```python
feat_imp=pd.DataFrame(dt.feature_importances_,
                      index=Xraw.columns,
                      columns=['Importance'])
feat_imp['feature'] = feat_imp.index
feat_imp_top10 = feat_imp.loc[feat_imp['Importance'].nlargest(10).index]
ax = sns.barplot(x="Importance", y="feature", data=feat_imp_top10,palette="Oranges")
# Title 
plt.suptitle("Fig 6 - Decision Tree Top10 Features",y=0.93, size = 24);
```


    
![png](/static/notebooks/airbnb/part3/output_26_0.png)
    


## XGboost


```python
xgb_round1 = XGBRegressor()
```


```python
#ROUND1
param_grid = {
          'learn_rate':[0.1,0.05,0.01],
          'min_child_weight':[3,4,5], 
          'gamma':[i/10.0 for i in range(3,6)],  
          'subsample':[i/10.0 for i in range(6,11)],
          'colsample_bytree':[i/10.0 for i in range(6,11)], 
          'max_depth': [9,10,11],
          'n_estimators':[300,500,1000]
}
```


```python
optimal_params = GridSearchCV(
             estimator = xgb_round1,
             param_grid=param_grid,
             verbose=2, # NOTE: If you want to see what Grid Search is doing, set verbose=2
             n_jobs = 2,
             cv = 3 
            )

optimal_params.fit(X_train, 
                    y_train, 
                    early_stopping_rounds=10,                
                    eval_set=[(X_test, y_test)],
                    verbose=True)

print(optimal_params.best_score_)
print(optimal_params.best_params_)
```

    Fitting 3 folds for each of 6075 candidates, totalling 18225 fits
    

    [Parallel(n_jobs=2)]: Using backend LokyBackend with 2 concurrent workers.
    [Parallel(n_jobs=2)]: Done  37 tasks      | elapsed:   36.8s
    [Parallel(n_jobs=2)]: Done 158 tasks      | elapsed:  2.5min
    [Parallel(n_jobs=2)]: Done 361 tasks      | elapsed:  6.1min
    [Parallel(n_jobs=2)]: Done 644 tasks      | elapsed: 10.8min
    [Parallel(n_jobs=2)]: Done 1009 tasks      | elapsed: 16.9min
    [Parallel(n_jobs=2)]: Done 1454 tasks      | elapsed: 24.6min
    [Parallel(n_jobs=2)]: Done 1981 tasks      | elapsed: 33.5min
    [Parallel(n_jobs=2)]: Done 2588 tasks      | elapsed: 43.3min
    [Parallel(n_jobs=2)]: Done 3277 tasks      | elapsed: 56.9min
    [Parallel(n_jobs=2)]: Done 4046 tasks      | elapsed: 70.5min
    [Parallel(n_jobs=2)]: Done 4897 tasks      | elapsed: 84.9min
    [Parallel(n_jobs=2)]: Done 5828 tasks      | elapsed: 100.7min
    [Parallel(n_jobs=2)]: Done 6841 tasks      | elapsed: 117.8min
    [Parallel(n_jobs=2)]: Done 7934 tasks      | elapsed: 137.0min
    [Parallel(n_jobs=2)]: Done 9109 tasks      | elapsed: 159.0min
    [Parallel(n_jobs=2)]: Done 10364 tasks      | elapsed: 183.0min
    [Parallel(n_jobs=2)]: Done 11701 tasks      | elapsed: 212.9min
    [Parallel(n_jobs=2)]: Done 13118 tasks      | elapsed: 242.8min
    [Parallel(n_jobs=2)]: Done 14617 tasks      | elapsed: 274.6min
    [Parallel(n_jobs=2)]: Done 16196 tasks      | elapsed: 318.1min
    [Parallel(n_jobs=2)]: Done 17857 tasks      | elapsed: 355.4min
    [Parallel(n_jobs=2)]: Done 18225 out of 18225 | elapsed: 363.5min finished
    

    [21:43:44] WARNING: C:\Users\Administrator\workspace\xgboost-win64_release_1.2.0\src\learner.cc:516: 
    
    [0]	validation_0-rmse:51.91973
    Will train until validation_0-rmse hasn't improved in 10 rounds.
    [1]	validation_0-rmse:40.86495
    Stopping. Best iteration:
    [26]	validation_0-rmse:23.95060
    
    0.4834807959323069
    {'colsample_bytree': 0.6, 'gamma': 0.3, 'learn_rate': 0.1, 'max_depth': 10, 'min_child_weight': 4, 'n_estimators': 300, 'subsample': 1.0}
    

#### Final XGBoost model after parameters


```python
# Final model after adjusting parameters.
xg = XGBRegressor(seed=42,
                    objective='reg:squarederror',
                    gamma=0.3,
                    #learn_rate=0.05,
                    max_depth=10,
                    min_child_weight=4,
                    subsample=1,
                    colsample_bytree=0.6,
                    n_estimators=300)
xg.fit(X_train, 
            y_train, 
            verbose=False, 
            early_stopping_rounds=10,
            eval_set=[(X_test, y_test)])
```

    XGBRegressor(base_score=0.5, booster='gbtree', colsample_bylevel=1,
                 colsample_bynode=1, colsample_bytree=0.6, gamma=0.3, gpu_id=-1,
                 importance_type='gain', interaction_constraints='',
                 learning_rate=0.300000012, max_delta_step=0, max_depth=10,
                 min_child_weight=4, missing=nan, monotone_constraints='()',
                 n_estimators=300, n_jobs=0, num_parallel_tree=1, random_state=42,
                 reg_alpha=0, reg_lambda=1, scale_pos_weight=1, seed=42,
                 subsample=1, tree_method='exact', validate_parameters=1,
                 verbosity=None)

```python
# XGB Regressor
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
    0   XGBoost       12.439472   18.104947        0.749157       0.494361
    


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


    
![png](/static/notebooks/airbnb/part3/output_34_0.png)
    
```python
feat_imp=pd.DataFrame(xg.feature_importances_,
                      index=Xraw.columns,
                      columns=['Importance'])
feat_imp['feature'] = feat_imp.index
feat_imp_top10 = feat_imp.loc[feat_imp['Importance'].nlargest(10).index]
ax = sns.barplot(x="Importance", y="feature", data=feat_imp_top10,palette="Oranges")
# Title 
plt.suptitle("Fig 8 - XGBoost Top10 Features",y=0.93, size = 24);
```


    
![png](/static/notebooks/airbnb/part3/output_35_0.png)
    

```python
import os
import graphviz

file_path = r'C:/Users/f1se4/Google Drive/DataScience/PyProjects/Librerias/Graphviz/bin'
os.environ["PATH"] += os.pathsep + file_path
bst = xg.get_booster()

node_params = {'shape': 'box', ## make the nodes fancy
               'style': 'filled, rounded',
               'fillcolor': '#FFE6C4:#FF9822'} 
leaf_params = {'shape': 'box',
               'style': 'filled',
               'fillcolor': '#ef8354:#FFB650'}

graph_data = to_graphviz(booster=xg, 
                 num_trees=0, 
                 condition_node_params=node_params,
                 leaf_node_params=leaf_params)
source_graph = graph_data.source
str(source_graph)
texto = '''
    graph [ rankdir=TB ]
    bgcolor="#303030"
    filesize="10,10"
'''
source_graph = source_graph.replace('graph [ rankdir=TB ]',texto)
source_graph = source_graph.replace('#0000FF','#10D0EE" fontcolor="#FFFEF1')
source_graph = source_graph.replace('#FF0000','#FF0000" fontcolor="#FFFEF1')
graph_data.source = source_graph
graph_obj = graphviz.Source(graph_data.source)
graph_obj.render(filename='airbnbBCN')
graph_obj.view()
```

![image.png](/static/notebooks/airbnb/part3/tree.png)

<h5>link to full tree *pdf* Link to the <a href="/static/notebooks/airbnb/part3/airbnbBCN.pdf" target="_blank">Tree PDF</a></h5>

## Model Comparison


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
      <td>6.323665</td>
      <td>17.327035</td>
      <td>0.934937</td>
      <td>0.529434</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Decision Tree</td>
      <td>18.362137</td>
      <td>19.442400</td>
      <td>0.477765</td>
      <td>0.430368</td>
    </tr>
    <tr>
      <th>2</th>
      <td>XGBoost</td>
      <td>12.439472</td>
      <td>18.104947</td>
      <td>0.749157</td>
      <td>0.494361</td>
    </tr>
  </tbody>
</table>
</div>



The best model that it has been found using different technics is Random Forest. We will proceed to save it and we will be ready for consume it as a service. In terms of explaining the model, could be better to try to extract which is the information from xgboost, as it would easier to do some interpretation from this model than from Random Forest.

----

## Save the best model


```python
from joblib import dump, load
dump(random_forest_regression, './models/randforest35_1000.joblilb')
```

    ['./models/randforest35_1000.joblilb']


