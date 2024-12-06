from django.shortcuts import render, redirect
from apple.models import Contact
from apple.models import Booking
from .forms import RegistrationForm, LoginForm
from .models import CustomUser
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success')
            return redirect()

def index(request):
    return render(request, 'index.html')

def insert_data(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        return redirect('/#contact')
    
    return render(request, index.html)

def view(request):
    contact = Contact.objects.all()
    return render(request, 'view.html', {'contact': contact})

def booking_data(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        date = request.POST.get('date')
        time = request.POST.get('time')
        people = request.POST.get('people')
        message = request.POST.get('message')
        tablenumber = request.POST.get('tablenumber')

        # Check if table is already booked for the same date
        existing_booking = Booking.objects.filter(tablenumber=tablenumber, date=date).first()
        if existing_booking:
            messages.error(request, f'Table {tablenumber} is already booked for {date}')
            return redirect('/#book-a-table')
        
        booking = Booking(name=name, email=email, date=date, time=time, people=people, message=message, tablenumber=tablenumber)
        booking.save()
        messages.success(request, 'Booking successful!')
        return redirect('/#book-a-table')

def book(request):
    booking = Booking.objects.all()
    return render(request, 'book.html', {'booking': booking}) 

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/staffpanel/')  # Redirect to a success page
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def staffpanel(request):
    return render(request, 'staffpanel.html', {'user': request.user})
    


