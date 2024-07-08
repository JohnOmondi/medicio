
from django.contrib import admin
from django.urls import path
from runserver import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('inner/',views.inner,name='inner'),
    path('About/',views.About,name='About'),
    path('doctors/',views.doctors,name='doctors'),
    path('department/',views.department,name='department'),
    path('contact/',views.contact,name='contact'),


]
