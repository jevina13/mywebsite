from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages          # for flash messages
from django.conf import settings             # holds EMAIL_* settings


# Create your views here.
def home(request):
    return render(request, 'base/home.html')


def submit(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        if not (name and email and subject and message):
            messages.error(request, "All fields are required.")
            return redirect("home")

        full_message = f"Name: {name}\nEmail: {email}\n\n{message}"

        send_mail(
            subject=f"New message from portfolio: {subject}",
            message=full_message,
            from_email=email,                       # from user
            recipient_list=['jevina.web@gmail.com'],  # your inbox
            fail_silently=False,
        )

        messages.success(request, "Thanks! Your message was sent.")
        return redirect("home")

    return render("home")
