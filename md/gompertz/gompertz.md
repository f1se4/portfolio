# IT Go-Live Study

**Gompertz Model for number of tickets from Go-Live to achieve some metrics, evaluate, compare with other projects and have some tools to create KPIs**

At first, and looking some go-live tickets (issues) generated during some different Go-Lives I thought that classic sigmoid function could fit my model.

However the real thing is that when you have release some new application in a production system, there is a gap between users starts to know/understand the functionallity of the new tool and detect issues or have questions about how it works, etc.. So at the start of the go-live (if there are not really big issues, what is expected after a good UAT) you don't expect to have several issues, so the growth at very initial point is slower than some days after, and of course, when the new application/tool/functionallity is coming more stable you should find that issues growth get slower another time.

This type of distribution is literally [Gompertz function](https://en.wikipedia.org/wiki/Gompertz_function), so my expectation is that I could fit this function to go-live ticketing and use its parameters as metrics and a quick knowledge of the Go-Live and Post-GoLive achievements.

```python
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import sqlite3

sns.set()

#Gombertz fit and error discovery libraries
import sklearn.metrics as sklm
from scipy.optimize import curve_fit
from scipy.optimize import fsolve
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
```python
# Usual aggrupations for temporal series discovery
df['Year'] = df.index.year
df['Month'] = df.index.month
df['Week'] = df.index.week
df['DayCount'] = np.arange(1,df['quantity'].shape[0]+1) #useful for functions
```