from django.contrib import admin
from .models import Categorias, Post

# Register your models here.
class CategoriasAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Categorias,CategoriasAdmin)
admin.site.register(Post, PostAdmin)