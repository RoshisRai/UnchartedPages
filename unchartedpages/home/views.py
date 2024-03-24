from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Blog, NewsletterSubscriber, ContactUs, BookOrder
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sites.shortcuts import get_current_site
from django.db.models import Q


def validate_email_address(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def blogs(request):
    try:
        left_blog = Blog.objects.all().order_by('-id')[:1][0]
        right_blogs = Blog.objects.all().order_by('-id')[1:3]
        blogs = Blog.objects.all().order_by('-id')
        top_three_slugs = [left_blog.slug]
        for i in right_blogs:
            top_three_slugs.append(i.slug)
        main_blogs = []
        for i in blogs:
            if i.slug not in top_three_slugs:
                main_blogs.append(i)
        random_blogs = Blog.objects.all().order_by('?')
        other_blogs = []
        for i in random_blogs:
            if i.slug not in top_three_slugs:
                other_blogs.append(i)
        context = {
            'left_blog': left_blog,
            'right_blogs': right_blogs,
            'main_blogs': main_blogs,
            'other_blogs': other_blogs[:4]
        }
    except Exception as e:
        context = {
            'left_blog': None,
            'right_blogs': [],
            'main_blogs': [],
            'other_blogs': []
        }
    return render(request, 'home/blogs.html', context)

def blog_search(request):
    query = request.GET.get('blog-search')
    context = {
        'query': query,
    }
    if(len(query) <= 3):
        messages.error(request, 'Cound not find any matches. The number of search words is too small.')
    elif(len(query)>= 120):
        messages.error(request, 'The query length is above 120. Please! make it shorter.')
    else:
        blog1 = Blog.objects.filter(title__icontains=query)
        blog2 = Blog.objects.filter(sub_title__icontains=query)
        blog3 = Blog.objects.filter(categories__icontains=query)
        blog4 = Blog.objects.filter(author__icontains=query)
        blog5 = Blog.objects.filter(content__icontains=query)
        blogst = blog1.union(blog2)
        blognd = blogst.union(blog3)
        blogrd = blognd.union(blog4)
        blogs = blogrd.union(blog5)
        context['blogs'] = blogs
    return render(request, 'home/blogsearch.html', context)

def blog_post(request, slug):
    blog = Blog.objects.get(slug=slug)
    prev_blog_slug = next_blog_slug = None
    if Blog.objects.filter(id=blog.id-1).exists():
        prev_blog_slug = Blog.objects.get(id=blog.id-1).slug
    if Blog.objects.filter(id=blog.id+1).exists():
        next_blog_slug = Blog.objects.get(id=blog.id+1).slug

    blog_category_list = blog.categories
    print(blog_category_list)
    related_blogs = []
    for i in blog_category_list:
        blog_filter = Blog.objects.filter(categories__icontains=i).order_by('-id')
        for j in blog_filter:
            if j not in related_blogs:
                if j.slug != blog.slug:
                    related_blogs.append(j)
    other_blogs = Blog.objects.all().order_by('-id')[:4]
    context = {
        'blog' : blog,
        'related_blogs': related_blogs[:3],
        'other_blogs': other_blogs,
        'prev_blog_slug': prev_blog_slug,
        'next_blog_slug': next_blog_slug,
    }
    return render(request, 'home/blogpost.html', context)

def buy_book(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if validate_email_address(email):
            phone = request.POST.get('phone')
            if len(phone) == 10:
                name = request.POST.get('name')
                email = request.POST.get('email')
                phone = request.POST.get('phone')
                payment_receipt = request.FILES.get('payment_receipt')
                additional_notes_or_comments = request.POST.get('additional_notes_or_comments')
                book_order = BookOrder(name=name, email=email, phone=phone, payment_receipt=payment_receipt, additional_notes_or_comments=additional_notes_or_comments)
                book_order.save()
                messages.success(request, 'Book purchased sucessfully! Your book will be delivered within 24 hours of your purchase!!')
            else:
                messages.error(request, 'Please enter a valid phone number. Thank you!')
        return redirect('home')
    else:
        return render(request, 'home/buybook.html')

def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if validate_email_address(email):
            phone = request.POST.get('phone')
            if len(phone) == 10:
                name = request.POST.get('name')
                subject = request.POST.get('subject')
                message = request.POST.get('message')
                contact = ContactUs(name=name, email=email, phone=phone, subject=subject, message=message)
                contact.save()
                messages.success(request, 'Your message has been sent successfully!!')
            else:
                messages.error(request, 'Please enter a valid phone number. Thank you!')
            return HttpResponseRedirect(request. META['HTTP_REFERER'])
        else:
            messages.error(request, 'Please enter a valid email address. Thank you!')
        return HttpResponseRedirect(request. META['HTTP_REFERER'])
    elif request.method == 'GET':
        return render(request, 'home/contact.html')

def faq(request):
    return render(request, 'home/faq.html')

def newsletter_subscriber(request):
    if request.method == 'POST':
        email = request.POST.get('subscribe-email')
        if validate_email_address(email):
            subscriber = NewsletterSubscriber(email=email)
            subscriber.save()
            messages.success(request, 'Thank you for subscribing Uncharted Pages')
        else:
            messages.error(request, 'Please enter a valid email address. Thank you!')
        return HttpResponseRedirect(request. META['HTTP_REFERER'])
