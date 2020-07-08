from django.contrib import admin

from .models import Registro
# Register your models here.


class AdminRegistro(admin.ModelAdmin):
	list_display = ["__unicode__", "asunto", "correo"]
	class Meta:
		model = Registro
			

admin.site.register(Registro, AdminRegistro)