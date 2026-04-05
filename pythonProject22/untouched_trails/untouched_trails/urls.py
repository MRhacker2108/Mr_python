from django.urls import path  # 👈 Ye line miss ho gayi hai, ise add karein
from travelapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('destinations/', views.destinations_view, name='destinations'),
    path('book/<int:place_id>/', views.book_destination, name='book_destination'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('about/', views.about_view, name='about'),
]