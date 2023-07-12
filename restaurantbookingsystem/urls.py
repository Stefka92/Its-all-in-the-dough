from django.urls import path
from .views import TableListView, BookingListView, BookingCreateView, BookingQueryView
from .views import TableListView



app_name = 'restaurantbookingsystem'

urlpatterns = [
    path('tables/', TableListView.as_view(), name='table_list'),
    path('bookings/', BookingListView.as_view(), name='booking_list'),
    path('bookings/create/', BookingCreateView.as_view(), name='booking_create'),
    path('bookings/query/', BookingQueryView.as_view(), name='booking_query'),
     path('', TableListView.as_view(), name='base.html'),
]





