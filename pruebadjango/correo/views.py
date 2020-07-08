from django.shortcuts import render
from .forms import RegForm
from .models import Registro
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.
def inicio(request):
	form = RegForm(request.POST or None)
	context = {
		"form":form
	}

	if form.is_valid():
		form_data = form.cleaned_data
		abc = form_data.get("correo_form")
		obj = Registro.objects.create(correo=abc)

	return render(request, "inicio.html", context)


def contacto(request):

	if request.method=="POST":

		subject=request.POST["Asunto"]

		message=request.POST["mensaje"] + " " + request.POST["email"]

		email_from=request.POST["email"]

		recipient_list=[email_from]

		send_mail(subject, message, email_from, recipient_list)

		return render(request, "inicio.html")
		

	return render(request, "correo.html")