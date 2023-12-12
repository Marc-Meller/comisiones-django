from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def contacto(request):
    if request.method == "POST":
        subject = request.POST.get("asunto")
        message = request.POST.get("mensaje") + "\n\nEnviado por: " + request.POST.get("email") + (" from Django.")
        email_from = request.POST.get("email")
        recipient_list = ["endermenforce10@gmail.com", "mpmc2000@hotmail.com"]
        
        send_mail(subject, message, email_from, recipient_list, fail_silently=False)
        
        return render(request, "gracias.html", {"email_remitente": email_from, "email_destinatario": recipient_list[1]})
    
    return render(request, "contacto.html")