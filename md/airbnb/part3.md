### Barcelona Airbnb DS analysis (3rd part)
```
\
|--Airbnb_Barcelona.ipynb
|--data
|   |-output.csv
|--model
    |-randforestKK_NNNN.joblib
```
Here we are going to model our data to perform the best result we could and then save the model to use in a production system as a reference and consumable service.

## Importing Libraries


```python
#Data
import pandas as pd 
import numpy as np

#Graphics libraries
from plotnine import *

#Librearies for ML model
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_selection import SelectKBest, f_regression
#Accuracy
from sklearn.metrics import r2_score, mean_squared_error
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
                  'Unnamed: 225',
                  'room_type',
                  'bathrooms'],axis=1,inplace=True)

# One-hot encode using pandas get_dummies
airbnb_data = pd.get_dummies(airbnb_data)
```

## Random Forest Model
We are going to do regression model based on Random Forest algorithm. We are going to use this model based on:

- We have several columns/characteristics to be evaluated and this model it's good one to lots of columns regression (independent variables).

### Independent variable vs dependent variables
We are going to separate our dependent variable (the one we want to predict) from the independent values.

```python
X = airbnb_data.drop(['price'],axis=1).astype('float').values
y = airbnb_data['price'].astype('float')
```

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
    | 1  |  29.817989519612908 |
    |----|---------------------|
    | 2  |  29.472481835763922 |
    |----|---------------------|
    | .. |  ....               |
    |----|---------------------|
    | 44 |  23.94505585617044  |
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
    labs(x='k Number',y='SQRT(MSQE)',title='Fig 1 - Error vs "k" variable (LR)')
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
y_test_pred = random_forest_regression.predict(X_test)
print('K filter value: ',n)
print('Number Random Forests: ',N_ESTIM)
print('K best features: ',Xraw.columns[cols])
print((mean_squared_error(y_test,y_test_pred))**(1/2))
print(r2_score(y_test,y_test_pred))
```

    K filter value:  34
    Number Random Forests:  1000
    K best features:  Index(['host_is_superhost', 'host_identity_verified', 'instant_bookable',
           'bedrooms', 'beds', 'number_of_reviews', 'host_listings_count',
           'host_total_listings_count', 'minimum_nights', 'location1d',
           'host greets you', 'hot water', 'pack \u2019n play/travel crib',
           'paid parking off premises', 'paid parking on premises.1',
           'property_type_Boat', 'property_type_Entire apartment',
           'property_type_Entire condominium', 'property_type_Entire house',
           'property_type_Entire loft', 'property_type_Entire serviced apartment',
           'property_type_Entire villa', 'property_type_Private room in apartment',
           'property_type_Private room in condominium',
           'property_type_Private room in guest suite',
           'property_type_Private room in hostel',
           'property_type_Private room in house',
           'property_type_Private room in serviced apartment',
           'property_type_Room in aparthotel',
           'property_type_Room in boutique hotel', 'property_type_Room in hotel',
           'property_type_Room in serviced apartment',
           'property_type_Shared room in apartment',
           'property_type_Shared room in hostel'],
          dtype='object')
    23.658059115421015
    0.5147660400294438
    

Also, we will try to have graphical view of how is distributed our predicted data from testing data.


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
    labs(title='Fig 2 - Predicted Data vs Test Data',x='',y='Price $',color='Data Type') 
)
```
    
![png](/static/notebooks/airbnb/part3/output_18_0.png)
    

Well $R^2=0,52$ It's not a good result, but it's not the worst. Comparing predicted and testing data it seems that it has good behavior around the mean price of the dataset and it's not so good with the prices that are down in the table and up in the table.

## Conclusions

We have found when using filter options, that there are some features that impacts over the price:

*Validation and Comparison*
```
'host_is_superhost'(1)
'host_identity_verified'
'number_of_reviews'
'host_listings_count'
```
*Basic Requirements*
```
'instant_bookable',
'bedrooms' 
'beds'
'minimum_nights'
'hot water'
```
*Baby Requirements*
'high chair'
'pack play/travel crib'
*Others*
```
'host greets you'
```
The other are related to property 'type' but they are not top 10 relevant as we suppose initially. In fact the price is much sensible to the reputation and requirements than which type of property is the publication. So, laws of supply and demand seems to be the 'clue' for price determination.


*$(1)$ The "superhost" designation on Airbnb is a sign that an Airbnb host has gotten consistently good reviews over at least a year of hosting. Airbnb checks the status of hosts four times a year to ensure that a superhost badge is still relevant for each host.*

## Save the model


```python
from joblib import dump, load
dump(random_forest_regression, './models/randforest35_1000.joblilb')
```

    ['./models/randforest35_1000.joblilb']


