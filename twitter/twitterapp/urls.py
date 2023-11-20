from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile_list/', views.profile_list, name='profile_list'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('update_user/', views.update_user, name='update_user'),
    path('tweet_like/<int:pk>', views.tweet_like, name="tweet_like"),
    path('tweet_info/<int:pk>', views.tweet_info, name="tweet_info"),
    path('tweet_delete/<int:pk>', views.tweet_delete, name="tweet_delete"),
    path('comment_like/<int:pk>', views.comment_like, name="comment_like"),
    path('comment_delete/<int:pk>', views.comment_delete, name="comment_delete"),
]