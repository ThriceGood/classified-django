from django.contrib import admin
from .models import Category, Advert, Comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'id')


class AdvertAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'title', 'pub_date')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'advert')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Advert, AdvertAdmin)
admin.site.register(Comment, CommentAdmin)
