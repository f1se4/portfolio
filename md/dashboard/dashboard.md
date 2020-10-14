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
