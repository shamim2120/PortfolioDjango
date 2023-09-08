from django.shortcuts import render,redirect
from myapp.models import Contact

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact') 
        message = request.POST.get('message')
        query = Contact(name=name, email=email, contact=contact, message=message)
        query.save()

        return redirect('/contact') 
    return render(request, 'contact.html')