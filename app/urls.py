from django.urls import path
from app import views

urlpatterns = [
    path('', views.BoardView.as_view(), name='index'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('edit/<int:pk>', views.postedit, name='edit'),
    path('create/', views.postcreate, name='create'),
    path('delete/<int:pk>/', views.postdelete, name='delete'),
]
