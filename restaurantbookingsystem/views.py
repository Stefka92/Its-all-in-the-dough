from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Table, Booking, BookingQuery

class TableListView(View):
    def get(self, request):
        tables = Table.objects.all()
        return render(request, 'restaurantbookingsystem/table_list.html', {'tables': tables})

class BookingListView(View):
    def get(self, request):
        bookings = Booking.objects.all()
        return render(request, 'restaurantbookingsystem/booking_list.html', {'bookings': bookings})

class BookingCreateView(View):
    def get(self, request):
        tables = Table.objects.filter(is_available=True)
        return render(request, 'restaurantbookingsystem/booking_create.html', {'tables': tables})

    def post(self, request):
        table_id = request.POST.get('table')
        table = get_object_or_404(Table, id=table_id)
        date = request.POST.get('date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        booking = Booking.objects.create(
            date=date,
            start_time=start_time,
            end_time=end_time,
            table=table,
            customer_name=customer_name,
            customer_email=customer_email,
            created_by=request.user
        )
        table.is_available = False
        table.save()
        return redirect('booking_list')

class BookingQueryView(View):
    def get(self, request):
        return render(request, 'restaurantbookingsystem/booking_query.html')

    def post(self, request):
        date = request.POST.get('date')
        booking_query = BookingQuery.objects.create(date=date)
        return redirect('booking_list')
