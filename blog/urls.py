from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    #Slug , anybody enters an interger after blog, I want to represent that int as blog_id then pass it to detail
    path('<int:blog_id>/', views.detail, name='detail'),


]