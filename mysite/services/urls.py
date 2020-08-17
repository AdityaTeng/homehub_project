from django.urls import path, include
from .views import ListRequestView, get_request, index, new_request, home
from django.conf.urls import url

# app_name = 'mymodule' # So we can use it like: {% url 'mymodule:user_register' %} on our template.
# urlpatterns = [
#     url(r'^register/$', views.user_register, name='user_register')
# ]

urlpatterns = [
    path('list_request_view/', ListRequestView.as_view(), name="request-all"),
    path('', home, name="home"),
    path('request/', get_request, name="get_request"),
    path('new_request/', new_request, name="new_request"),
    path('index/', index, name="index"),
    
]