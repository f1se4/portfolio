# IT Go-Live Study

**Gompertz Model for number of tickets from Go-Live to achieve some metrics, evaluate, compare with other projects and have some tools to create KPIs**

At first, and looking some go-live tickets (issues) generated during some different Go-Lives I thought that classic sigmoid function could fit my model.

However the real thing is that when you have release some new application in a production system, there is a gap between users starts to know/understand the functionallity of the new tool and detect issues or have questions about how it works, etc.. So at the start of the go-live (if there are not really big issues, what is expected after a good UAT) you don't expect to have several issues, so the growth at very initial point is slower than some days after, and of course, when the new application/tool/functionallity is coming more stable you should find that issues growth get slower another time.

This type of distribution is literally [Gompertz function](https://en.wikipedia.org/wiki/Gompertz_function), so my expectation is that I could fit this function to go-live ticketing and use its parameters as metrics and a quick knowledge of the Go-Live and Post-GoLive achievements.

```python
import numpy as np
import pandas as pd
import datetime
import sqlite3

#Gombertz fit and error discovery libraries
import sklearn.metrics as sklm
from scipy.optimize import curve_fit
from scipy.optimize import fsolve

#Graphics libraries
import matplotlib.pyplot as plt
import seaborn as sns
from plotnine import *
```

## Read Data
Our data is stored in SQLITE table, it comes from ticket managing tool is taking all tickets related to incidences, queries and small requests solved during Go-Live and post Go-Live support from a IT project.

```python
con = sqlite3.connect("db.sqlite3")
cur = con.cursor()
sql = """SELECT count(requestid) as quantity,created_at as date
        FROM Tool
        WHERE groupme like '%Project Name%'
        Other relevant filters from the company
        GROUP BY created_at
        """
raw_data = pd.read_sql(sql,con)
df = raw_data.copy()

raw_data.head() #Take a look of raw_data
```
|index|quantity|date|
|--- |--- |--- |
|0|13|2020-01-27|
|1|4|2020-01-28|
|2|8|2020-01-29|
|3|7|2020-01-30|
|4|2|2020-01-31|

## Data analysis and exploration
### Basic data statistics

```python
# Change data type of 'date' column to pandas datatime index type.
df['date'] = df['date'].astype('datetime64[ns]')
df.index = df['date'] #Set date as index to create time indexed dataframe.
```
Ok, we have now time series of our go-live project. Let's take a look to the raw data as it comes from our tool

```python
all_tickets = (
    ggplot(df,aes(x='date',y='quantity')) +
    scale_x_date(date_breaks = "1 week",labels = date_format("%d-%b-%Y")) +  
    geom_line(color=orange, size=1.2) +
    personal_theme +
    labs(title='Tickets Opened during Go-Live Project',x='',y='')
)
all_tickets.draw();
```

![fullserie](/static/notebooks/gompertz/images/fullserie.png)

We are going to take a look hoow it's distributed our tickets.

```python
df['quantity'].describe()
```
```
count    88.000000
mean      4.772727
std       3.143054
min       1.000000
25%       2.000000
50%       4.000000
75%       7.000000
max      14.000000
```
Here, we have some different data that could help us to know or define additional metrics, but they are not really describing how the process of the go-live has worked, as it's not constant process and the behaivour is different along the time.

Here the principal interesting information is that we are working over 88 days of tickets, which is good dataset for timeseries.

We could see distribution by month of the dataset, only to be much more familiar with it:

```python
month_labels = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
month_distr = (
    ggplot(df,aes(x='Month',y='quantity',group='Month')) +
    scale_color_manual(values = personal_colors) +
    scale_x_continuous(breaks=(1,2,3,4,5,6,7,8,9,10,11,12),labels=month_labels) +
    geom_boxplot(color='red',fill=orange) +
    personal_theme +
    labs(title='Monthly Distribution',x='Month',y='Tickets Num.')
)
month_distr.draw()
```

![monthdistr](/static/notebooks/gompertz/images/month_distr.png)

Here we see that we have initial 2 month important volume of all generated tickets.

And finally, the most important one, as this is the one that let us to see the real behaivour of the go-live process in a general view, by analyzing its trend. I have applied 2 trend filters, rolling mean filter and [Hodrick-Prescott](https://en.wikipedia.org/wiki/Hodrick%E2%80%93Prescott_filter) for best smoothing reasons (because in this case it's not supposed to have seasonal component).

```python
#Trend from filter Hodrick-Prescot
from statsmodels.tsa.filters.hp_filter import hpfilter
hpcycle, df['TrendHP'] = hpfilter(df.quantity)

df['trend14'] = df['quantity'].rolling(14).mean()
df_trend = pd.melt(df, id_vars='date', value_vars=['quantity','trend14','TrendHP'])
df_trend['variable'] = df_trend['variable'].replace({'quantity':'Raw Data','trend14':'Rolling 14d Mean','TrendHP':'Hodrick-Prescot'})
```
And graph

```python
trend_graf = (
    ggplot(df_trend,aes(x='date',y='value',color='variable')) +
    scale_x_date(date_breaks = "1 week",labels = date_format("%d-%b-%Y")) +      
    scale_color_manual(values = personal_colors) +
    geom_line() +
    personal_theme +
    labs(title='Raw Data and Trend Visualization',x='Weeks',y='Tickets Num.')
)
trend_graf.draw()
```

![trend](/static/notebooks/gompertz/images/trend.png)

And let me take the Trend individually, because it will let me explain better initial hypothesis.

```python
trend_alone_graf = (
    ggplot(df,aes(x='date',y='TrendHP')) +
    scale_x_date(date_breaks = "1 week",labels = date_format("%d-%b-%Y")) +      
    scale_color_manual(values = personal_colors) +
    geom_line(color=orange) +
    personal_theme +
    labs(title='Tickets Trend Smoothed',x='Weeks',y='Tickets Num.')
)
trend_alone_graf.draw()
```

![trendalone](/static/notebooks/gompertz/images/trendalone.png)

Well, and my final 'discovery' analysis and the behaivour it's required to be modelized.

I need at first to have cumulative number of tickets:

```python
df['CumSum'] = df['quantity'].cumsum()
#Melting data for ggplot
df_hipo = pd.melt(df, id_vars='date', value_vars=['TrendHP','CumSum'])
df_hipo['variable'] = df_hipo['variable'].replace({'TrendHP':'Trend','CumSum':'Cumulative'})
```
And we will graph it at the same time we re-catch our trend graph.

```python
hipo_graf = (
    ggplot(df_hipo,aes(x='date',y='value',color='variable')) +
    scale_x_date(date_breaks = "1 week",labels = date_format("%d-%b-%Y")) +      
    scale_color_manual(values = personal_colors) +
    geom_line() +
    facet_wrap('variable',scales='free_y',nrow=2) +
    personal_theme +
    labs(title='Raw Data and Trend Visualization',x='Weeks',y='Tickets Num.')
)
hipo_graf.draw()
```

![trendalone](/static/notebooks/gompertz/images/hipotesis.png)
