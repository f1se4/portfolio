# Barcelona Airbnb DS analysis (4th part)
```
\
|--Airbnb_Barcelona.ipynb
|
|--model
    |-randforestKK_NNNN.joblib
```

## Deployment
We could select some different ways to deploy (if required) our machine model. In *part 3* we have saved **joblib** ML file and we can load our model from this file, and have 'just fitted' model to do our predictions.

You can do different ways, create service with *json* interface to retrieve any calculation/classification etc... for this study I have tried to do it through *streamlit*, I have worked with plotly dash and some other ways of web deployment as *flask* or *django* and other dynamic presentation libraries as *Bokeh* and want to check how *streamlit* is to work with (I have liked ^^).

So the code presented here is small streamlit dashboard. I have reduced the scope a lot to don't have 70 fields to fill etc... So I was only closing this project different way, learning a bit more. 

I have re-executed random forest regression with KBaseFilter of 7. Some of these fields could be grouped from a 'selection' point of view and the model has reduced its accuracy to 0.39, but I believe that for this case it's not important.

Of course, if this web application is interesting for someone, we could improve a lot it, using full model, and adding some other features (neighbor comparison, error of the price predicted, etc...)

## DashBoard Code

### Import Libraries

```python
import streamlit as st
import numpy as np

import joblib

from pathlib import Path
path_directory = str(Path().absolute())
```

### Define Title and constants
Here we will start main() function. I use streamlit title widget and then I define my 'selection' values.
I have taken them from unique values from original dataset. (```df.column.unique```).

```python
def main():

    st.title('Airbnb Barcelona Advanced Analytics')

    beds_num = (0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10., 11., 12.,
       13., 14., 15., 16., 17., 18., 19., 20., 23., 24., 25., 28., 30.,
       np.nan)

    bedrooms_num = ( 1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10., 11., 12., 15.,
       np.nan)

    Property_type  = st.sidebar.selectbox("Room Type", ("Private Room",
                                                        "Entire home/apt",
                                                        "Entire Apartment",
                                                        "Private Room in apartment",
                                                        "Another"))
    host_listing_mean = 18.108853910477126
```

Then the logic of the widgets of selection and fill the array to use with the model.

```python
    if Property_type == 'Private Room':
        room_type_Private_room = 1
        bedrooms_num = ( 1., np.nan)        
    elif Property_type == 'Entire home/apt':
        room_type_Entire = 1
    elif Property_type == 'Entire Apartment':
        property_type_Entire_apartment = 1
    elif Property_type == 'Private Room in apartment':
        property_type_Private_room_in_apartment = 1
        bedrooms_num = ( 1., np.nan)

    beds = st.sidebar.selectbox("Beds", beds_num)
    bedrooms = st.sidebar.selectbox("Bedrooms", bedrooms_num)
    host_listing_mean = 18.108853910477126

    room_type_Entire                        = 0
    room_type_Private_room                  = 0
    property_type_Entire_apartment          = 0
    property_type_Private_room_in_apartment = 0


    if Property_type == 'Private Room':
        room_type_Private_room = 1
    elif Property_type == 'Entire home/apt':
        room_type_Entire = 1
    elif Property_type == 'Entire Apartment':
        property_type_Entire_apartment = 1
    elif Property_type == 'Private Room in apartment':
        property_type_Private_room_in_apartment = 1

    # Price calculation
    ## Get the model
    file_path = path_directory + r"\models\randforest7_1000.joblilb"
    rf_model = joblib.load(file_path)
    X = [[bedrooms, 
        beds, 
        host_listing_mean, 
        room_type_Entire, 
        room_type_Private_room, 
        property_type_Entire_apartment, 
        property_type_Private_room_in_apartment]]

    y_predict = rf_model.predict(X)
```

Last aspects, some disclaimers and presentation.

```python
    st.sidebar.markdown("""
        #### Notes
        For this explotation sample, random forest model has been reduced to 7 most important features.
        Some of them are different property types, Beds, Bedrooms and host_listing_counts, this one 
        as it's something that is unknown for new properties has been reduced to the mean of the dataset.
    """)

    #Image
    st.image("wordcloud.png",use_column_width=True)

    # validation
    result = "{:.2f}".format(y_predict[0])
    st.success(f"Predicted Price= {result} $")
```

And usual execution function to package managing, etc...

```python
if __name__ == "__main__":
    main()
```
## Some Screenshots

![screenshot](/static/notebooks/airbnb/part4/dashboard.png)
