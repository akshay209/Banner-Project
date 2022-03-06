from django.urls import path
from . import views


urlpatterns = [
    path('',views.loginpage,name='loginpage'),
    
    path('upload',views.upload,name='upload'),
    path('logoff',views.logoff,name='logoff'),
    path('ban_main',views.ban_main,name='ban_main'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('activate/<int:id>/',views.activate,name='activate'),
    path('deactivate/<int:id>/',views.deactivate,name='deactivate'),
    path('delete/<int:id>/',views.delete,name='delete'),
]