from django.db import models
from django.db.models.base import Model
from froala_editor.fields import FroalaField
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10)
    description=models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=120)

    class Meta:
        verbose_name = ("Catégorie")
        verbose_name_plural = ("Catégories")

    def __str__(self):
        return self.name

"""class Profile(models.Model):
 #   user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='profile_photos',blank=True,null=True)
    desc = models.CharField(max_length=200)

    class Meta:
        verbose_name = ("Photo profil")
        verbose_name_plural = ("Photo profil")

    def __str__(self):
        return f' {self.profile_photo} Profile'"""

class About(models.Model):
    title = models.CharField(max_length=500)
    #about_body = RichTextField()
    about_body = FroalaField()
    sub_about_body= RichTextField()
    image1_about= models.ImageField(upload_to='image_about')
    image2_about= models.ImageField(upload_to='image_about')

    class Meta:
        verbose_name = ("A propo")

    def __str__(self):
        return self.title
class Blogs(models.Model):
    title=models.CharField(max_length=60)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    description=FroalaField()
    authname=models.CharField(max_length=15)
    img=models.ImageField(upload_to='blog',blank=True,null=True)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    actif = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Publication")
        verbose_name_plural = ("Publications")

    def __str__(self):
        return self.title

#Blogs.objects.all()
#Blogs.objects.count() affiche le nombre de publication

class Comment(models.Model):
    commentaire = models.ForeignKey(Blogs, related_name="comments", on_delete=models.CASCADE)
    commenter_name = models.CharField(max_length=200)
    comment_body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Commentaire")
        verbose_name_plural = ("Commentaires")

    def __str__(self):
        return '%s - %s' % (self.commentaire.authname, self.commenter_name)

class Video(models.Model):
    title=models.CharField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = FroalaField()
    name = models.CharField(max_length=30)
    video=models.FileField(upload_to="video/%y")
    heure = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name = ("Vidéo")
        verbose_name_plural = ("Vidéos")

    def __str__(self):
        return self.title

"""class Internship(models.Model):
    fullname=models.CharField(max_length=60)
    usn=models.CharField(max_length=60)
    email=models.CharField(max_length=60)
    college_name=models.CharField(max_length=100)
    offer_status=models.CharField(max_length=60)
    start_date=models.CharField(max_length=60)
    end_date=models.CharField(max_length=60)
    proj_report=models.CharField(max_length=60)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.usn"""
