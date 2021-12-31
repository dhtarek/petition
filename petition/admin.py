from django.contrib import admin

# Register your models here.
from .models import petitions
from .models import domaine
from .models import direction
from .models import citoyen
from .models import commune
admin.site.register(petitions)
admin.site.register(domaine)
admin.site.register(direction)
admin.site.register(citoyen)
admin.site.register(commune)