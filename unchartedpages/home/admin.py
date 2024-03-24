from django.contrib import admin
from .models import Blog, ContactUs, NewsletterSubscriber, BookOrder

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created_at', 'updated_at']
    search_fields = ['title__contains', 'author__contains']

    class Media:
        js = ('js/tinyinject.js',)

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'phone', 'subject', 'created_at', 'updated_at']
    search_fields = ['email__contains', 'phone__contains', 'subject__contains']

@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'created_at', 'updated_at']
    search_fields = ['email__contains']

@admin.register(BookOrder)
class BookOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'created_at', 'updated_at']
    search_fields = ['email__contains']