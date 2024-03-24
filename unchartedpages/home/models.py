from django.db import models
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_delete

# Create your models here.
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    sub_title = models.TextField()
    main_image = models.ImageField(upload_to='NewsAndArticles/', blank=True, null=True)
    categories = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    author = models.CharField(max_length=120)
    slug = models.CharField(unique=True, max_length=200, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Blog, self).save(*args, **kwargs)

@receiver(post_delete, sender=Blog)
def post_save_blog_image(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.main_image.delete(save=False)
    except:
        pass

@receiver(pre_save, sender=Blog)
def pre_save_blog_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_img = instance.__class__.objects.get(id=instance.id).main_image
        try:
            new_img = instance.main_image
        except:
            new_img = None
        if new_img != old_img:
            import os
            if os.path.exists(old_img.path):
                os.remove(old_img.path)
    except:
        pass

class ContactUs(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=200)
    phone = models.BigIntegerField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name + "--" + str(self.phone) + "--" + self.subject

class NewsletterSubscriber(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.email
    
class BookOrder(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=200)
    phone = models.BigIntegerField()
    payment_receipt = models.FileField(upload_to='Payment Receipts/')
    additional_notes_or_comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + '--' + self.name + '--' + str(self.phone) + '--' + self.email

@receiver(post_delete, sender=BookOrder)
def post_save_apply_now_resume(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.payment_receipt.delete(save=False)
    except:
        pass

@receiver(pre_save, sender=BookOrder)
def pre_save_apply_now_resume(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_img = instance.__class__.objects.get(id=instance.id).payment_receipt
        try:
            new_img = instance.payment_receipt
        except:
            new_img = None
        if new_img != old_img:
            import os
            if os.path.exists(old_img.path):
                os.remove(old_img.path)
    except:
        pass