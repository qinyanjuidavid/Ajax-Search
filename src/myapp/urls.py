from django.urls import path
from myapp import views
from django.views.decorators.csrf import csrf_exempt
app_name="myapp"


urlpatterns=[
path('ajax/search/',csrf_exempt(views.AjaxIndexView),name="ajax_index"),
path('',views.IndexView,name="index")
]
