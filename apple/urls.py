from django.urls import path
from django.contrib.auth.views import LogoutView
from RedAppleHotel.urls import views
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('insert_data/', views.insert_data, name='insert_data'),
    path('booking_data/', views.booking_data, name='booking_data'),
    path('view/', views.view, name='view'),
    path('book/', views.book, name='book'),
    path('login/', views.login_view, name='login'),  # Updated to use login_view
    path('staffpanel/',views.staffpanel, name='staffpanel'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout')
]
