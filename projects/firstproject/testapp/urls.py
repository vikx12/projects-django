from testapp import views
from django.conf.urls import url
urlpatterns=[
url('info',views.employees_info_view),
url('^$',views.greeting),
url('about',views.about),
url('contact',views.showcontact),
]
