from django.urls import path
from .views import home, about, blogs, blog_post, buy_book, contact, faq, newsletter_subscriber, blog_search

urlpatterns = [
    path('', home, name='home'),
    path('about-us/', about, name='about'),
    path('blogs/', blogs, name='blogs'),
    path('blog-search/', blog_search, name='blog-search'),
    path('blog-post/<slug:slug>/', blog_post, name='blog-post'),
    path('buy-book/', buy_book, name='buy-book'),
    path('contact-us/', contact, name='contact'),
    path('frequently-asked-questions/', faq, name='faq'),
    path('newsletter-subscriber/', newsletter_subscriber, name='newsletter-subscriber'),
]
