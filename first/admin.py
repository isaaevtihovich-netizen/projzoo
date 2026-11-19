from django.contrib import admin
from .models import *
@admin.register(Vid)
class VidAdmin(admin.ModelAdmin):
    pass
@admin.register(Tip)
class TipAdmin(admin.ModelAdmin):
    pass
@admin.register(Klimzona)
class KlimzonaAdmin(admin.ModelAdmin):
    pass
@admin.register(Animals)
class AnimalsAdmin(admin.ModelAdmin):
    pass
@admin.register(Dolznost)
class DolznostAdmin(admin.ModelAdmin):
    pass
@admin.register(Pol)
class PolAdmin(admin.ModelAdmin):
    pass
@admin.register(CategSotr)
class CategSotrAdmin(admin.ModelAdmin):
    pass
@admin.register(Sotr)
class SotrAdmin(admin.ModelAdmin):
    pass
