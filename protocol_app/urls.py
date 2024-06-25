from django.urls import path
from .views import *

app_name = 'protocol_app'


urlpatterns = [
    path('create_user/', create_user, name='create_user'),
    path('upload_pdf/', upload_pdf, name='upload_pdf'),
    path('login_user/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout'),
    path('', home, name='home'),
]
