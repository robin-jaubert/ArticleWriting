from django.urls import path
from app import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.FirstView.as_view(), name='first'),
    path('home/', views.BoardView.as_view(), name='index'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('edit/<int:pk>', views.postedit, name='edit'),
    path('create/', views.postcreate, name='create'),
    path('delete/<int:pk>/', views.postdelete, name='delete'),
    path('login/', views.LogView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register')
]
