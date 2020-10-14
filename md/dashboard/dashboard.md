# Dashboard

## Introduction

For this project I'm going to do short/quick reference as it was hard work to do and there are lots of code lines implemented.

Also as it was a theorical practice but using real data, I have 'blur' all references or any possible sensible data, to focus only in the context and backend technology used.

In fact, the 'concept' of the Dashboard it's easy:

1. Using Django Framework with created app to manage authorizations, and sqlite3 DB connections.
2. Plotly Dash, there is library that let to implement plotly dash over django template.
3. Responsive web by using in all templates bootstrap css classes.
4. It has some limitations, as the dash filters works only for the 'technology' that dash page is related to.
5. There are lot, lot of work to adapt all raw information from ticketing tools, etc... I have developed some type of ETL to get all data and transform to sqlite table with calculations etc... that it's refreshed each hour with delta data, etc... and let that on-line tool get any desired data in real-quick-time.    

## Django

I have used [Django](https://www.djangoproject.com/) as web framework, because it's solid, escalable python well known tool, with lots of doucmentation and big community.

Django works using layers for different functionalities, the basic ones are views and model layers. The views render pages and model is the connection to data base core. You can create basic django web only with views, and then you can add 'apps' and each 'app' has its own model layer, security layer is related to django app, and 'wraps' django views to connect them.

### Views, Url and html template

#### views.py

Views are the first objects to be called. Here sample of the first page, and quick look to security wrapper, and also server error handlers where you could personalize them at your own.

Login class and view are pre-defined, and you only need a bit of html/css to re-use and adapt to your web theme.

```python
def initial_page(request):
    context = {}
    return render(request,'index.html',context)

@login_required(login_url="/login/")
def xxx_page(request):
    context = {}
    return render(request,'xxx.html',context)

def handler404(request, exception):
    data = {}
    return render(request,'Error.html',data)

def handler500(request):
    data = {}
    return render(request,'Error.html',data)
```

#### urls.py

The views need an additional objects that belongs to views layers which are the 'url' defintion. Here you define url path and which function view is called, here you import also dash-plotly-django references, you will also to modify some lines in setting file, and you can find all these in the documentation ([django-plotly-dash](https://github.com/GibbsConsulting/django-plotly-dash)), here you will find also django wiki add-on implemented as FAQ tool for users.

```python
from django.contrib import admin
from django.urls import path, include
from django_plotly_dash.views import add_to_session
from DashBoard import views
from django.contrib.auth.views import LogoutView
from DashBoard.Dash_Apps import xxx
from DashBoard import updates_log


handler404 = 'DashBoard.views.handler404'
handler500 = 'DashBoard.views.handler500'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.initial_page, name='initial_page'),
    path('xxx/', views.xxx, name='xxx'),
# Add Django site authentication urls (for login, logout, password management)
    path('login/', views.login_view, name="login"),
    path("logout/", LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('notifications/', include('django_nyt.urls')),
    path('wiki/', include('wiki.urls')),
    # Add-on For dash to Django always last one
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
]
```
#### templates

I have 1 base template that defines nav bar, footer and calls all css/js scripts/etc.. that are common for all web pages.

Quick summary to have an idea of base.

Here it's important to take a look to security class "user" that is the logged session, and also mandatory {} for plotly dash to connect the page to any dash application page defined.

```html
{% load static %}
<html>
  <head>
    {% load plotly_dash %}
    {% plotly_header %}
    ...
  </head>
  <body>
    <div class='wrapper'>
      <div ='twelve columns'>
        <div class="banner">
          <h2>DashBoard Title</h2>
        </div>
      </div>
        <nav class="navbar navbar-dark bg-dark">
          <a class="navbar-brand" href={% url 'initial_page' %}>Home</a>
          {% if user.is_authenticated %}
          <a class="navbar-brand" href={% url 'xxx' %}>xxx</a>
          {% endif %}
        </nav>
        <div class="container">

          {% block content %}{% endblock content %}

        </div>
        <div class="piepagina">
            ...
      </div>
  </body>
{% plotly_footer %}
</html>
```
Then I have defined each page rendered by the views layer like this:

```html
{% extends "base.html" %}
{% load plotly_dash %}
{% plotly_header %}
<!-- Static assets -->
{% load static %}
{% block content %}
{% if user.is_authenticated %}
<!-- Contenido de la página -->
{% plotly_direct name="xxx" %}
{% endif %}
{% endblock content %}
{% plotly_footer %}
```
[Jinja2](https://palletsprojects.com/p/jinja/) library is used as backend (same as Flask Web Framework) and use the same therminology and 'transformations'.

### Model Layer

I have used Django app to add model layer to web page, for me model layer a part that from security management of the web, has another interesting behaivour, and it's that it makes really really easy to manage the database related to the web its migration, administration, etc...  By default it uses sqlite data base and I have not changed this because in a 'training' project as it is this one it's easier to work with one-file db as sqlite does.

Here there is not much to add, as I am not going to publish the database model, but basically if you have worked with relational DB, key values, data tables, etc... you will have no issue in this part.

## Plotly-Dash

[Plotly Dash OpenSource](https://plotly.com/dash/) it's really good presentation solution and easy way to have dynamic on-line graphics and other web data science tools framework, multiplatform, etc...

All web functionallities that are not implemented in this solution are really covered by Django, so the dual use of both of them, makes deployment of statistical, ML, Data analysis Dashboard, clear, solid and scalable.

From here, we start with different paradigm. We could forget for now Django framework and start thinking in Plotly Dash language.

The clue are this brackets in our templates.

```html
{% plotly_header %}.
...
{% plotly_direct name="xxx" %}
...
{% plotly_footer %}
```
**plotly_direct_name** will call and embed our plotly-dash by calling *xxx.py* which has to have dash app defined inside.

### Plotly-Dash Apps

As all the pages are the same, except first page, all them are calling 'template' that uses *xxx* name as parameter to trigger all the filters related to each technology.

```python
from DashBoard.Dash_Apps.Dash_Tech_Base import dash_template_tech

app = dash_template_tech('xxx')
```
And then all my dashboard logic is implemented in *dash_template_tech()* function, which in fact is returning DjangoDash application. I'm not going to do plotly-dash course ^^ and paste 1000 code lines its principal file and lots more in customized modules with data filtering/transformation/etc... :S, so I will explain what have this plotly dash application.

1. Connects to sqlite database
2. Apply initial filters depending on *xxx*
3. Dash Layout, plotly dash has its own functions to call html elements, that are customizable through wrappers that will let using dynamic filters in the app.
   1. You can call 'styles classes' so it's possible to use bootstrap also in dash html elements, and continue with responsive web.
4. Callback functions (the plotly-dash wrappers), it defines an input and output, input are filters to be used and outputs are layout elements.
5. Each callback function is related to one metric from the dashboard and has different functions to re-filter, re-calculate data, etc... also, callback functions are called initially.
6. Different filters to calculate and work with data, here pandas and sql are on fire.

Shortened code with one sample of callback and layout:

```python
def dash_template_tech(tech):
    connection.commit()

    now = datetime.date.today()
    yesterday = now - datetime.timedelta(days=1)

   get_data(connection,sql_list,tech,now)

    app = DjangoDash(nombre_app)

    # Bootstrap CSS.
    app.css.append_css({'external_url': 'https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css'})

    app.layout = html.Div([
        ...
        ...
             html.Div([
                html.P('',className='col-12'),
                html.P('',className='col-12'),
                html.H6("Details for selected Aging tickets",className='col-12'),
                html.Div([
                    dcc.Dropdown(id = 'aging-drop',
                              options=aging_def,
                              value=['G. >60','F. >30','E. >15','D. >7'],
                              placeholder="Aging Category",
                              clearable=False,
                              multi=True),
                    html.Table(id='agingdetails',className='table table-sm table-striped table-dark')
                    ],className='col-12')
                ],className='row'),
            ],className='d-print-none'),   
        ...
        ...    
    ])

# Callbacks

    @app.callback(
    Output('agingdetails', 'children'),
    [Input('my-date-picker-single', 'date'),
    Input('country-drop', 'value'),
    Input('aging-drop', 'value'),
        ])
    def update_output_ag_dt_all(date,countries,aging):
        if countries is not None:
            if date is not None:
                if aging is not None:
                    date = datetime.datetime.strptime(re.split('T| ', date)[0], '%Y-%m-%d')
                    now = date
                    df_ag_dt_all= get_data_open_ag_dt_all(connection,tech,now,countries,aging)
                    return func_df.me_table_link(df_ag_dt_all)
```

"And that's all", the rest are more callbacks functions, pandas working... I have also added some matplotlib and seaborn graphics for testing and to check if it's possible to add some graphic don't affordable by plotly.

## Some views

Presentation page, it's done in markdown and latex for dash, It has coloured map plot with 'beauty' view of country ticket origin.

![firstpage](/static/notebooks/dashboard/images/firstpage.png)

To be able to see data, you need to be logged in, as said before, authorization managing, session, etc... is wrapped by django app authorization module.

![security](/static/notebooks/dashboard/images/djangosecurity.png)

After logging, you have visibility about different service technologies managed in the tool.

![selected](/static/notebooks/dashboard/images/selectedareas.png)

As said before, we have some different global filters for each technology relevants from business point of view.

![dinamic](/static/notebooks/dashboard/images/dinamicfilters.png)

Each technology has the same 'Dash' template, then it has different backend filters when starting loading the page, and some frontend filters managed by the user, which updates all the dashboard graphics.

Here you have global view of what could see for each technology. Additionally you could print the dashboard as report.

![full](/static/notebooks/dashboard/images/fulldashboard.png)
