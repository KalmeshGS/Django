from django.conf.urls import url
from . import views

urlpatterns = {
    url(r'^index', views.index, name="index"),
    url(r'^adminsigninform/$', views.adminsigninform, name="adminsigninform"),
    url(r'^admindata/$', views.admindata, name="admindata"),
    url(r'^adminloginform/$', views.adminloginform, name="adminloginform"),
    url(r'^admin/$', views.admin, name="admin"),
    url(r'^adminhome/$', views.adminhome, name="adminhome"),
    url(r'^updatebook/(?P<slug>[-\w\s]+)/$', views.updatebook, name="updatebook"),
    url(r'^ubook/$', views.ubook, name="updatebook"),
    url(r'^retrivevebook/$', views.viewbook, name="viewbook"),
    url(r'^addbook/$', views.addbook, name="updatebook"),
    url(r'^bookupdate/$', views.bookupdate, name="bookupdate"),
     url(r'^studentview/$', views.studentbookview, name="studentview"),
    url(r'^deletebook/(?P<slug>[-\w]+)/$', views.deletebook, name="updatebook"),
    url(r'^dbook/$', views.dbook, name="updatebook"),


}

