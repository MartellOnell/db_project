from django.urls import path

from api.deals import views


urlpatterns = [
    path('rooms/', views.RoomView.as_view(), name='rooms'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('booking/', views.BookingView.as_view(), name='booking'),
    path('order_menu/', views.OrderMenuView.as_view(), name='order_menu'),
    path('my_orders/', views.MyOrdersView.as_view(), name='my_orders'),
]