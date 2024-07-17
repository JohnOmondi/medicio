
from django.contrib import admin
from django.urls import path
from runserver import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.index,name='index'),
    path('inner/',views.inner,name='inner'),
    path('About/',views.About,name='About'),
    path('doctors/',views.doctors,name='doctors'),
    path('department/',views.department,name='department'),
    path('contact/',views.contact,name='contact'),
    path('appointment/',views.Appointment,name='appointment'),
    path('show/',views.show,name='show'),
    path('delete/<int:id>',views.delete),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),

]
