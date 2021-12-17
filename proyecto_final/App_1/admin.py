from django.contrib import admin
from .models import Internos, jefes_de_trabajo, maestros, preceptores

# Register your models here.
admin.site.register(Internos)
admin.site.register(jefes_de_trabajo)
admin.site.register(maestros)
admin.site.register(preceptores)