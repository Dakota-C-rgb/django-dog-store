from django.contrib import admin
from app.models import DogTag, DogProduct

# Register your models here.
@admin.register(DogTag)
class DogTagAdmin(admin.ModelAdmin):
    pass


@admin.register(DogProduct)
class DogProductAdmin(admin.ModelAdmin):
    pass
