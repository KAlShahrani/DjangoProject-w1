from django.urls import path
from . import views
urlpatterns = [
    path('', views.main, name='main'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/blogdetails/<int:pid>', views.pdetails, name='pdetails'),
    path('users/', views.users, name="users"),
    path('users/udetails/<int:uid>', views.udetails, name='udetails'),
    # path('comments/', views.comments, name='comments'),
    # path('categories/', views.categories, name='categories'),
]
