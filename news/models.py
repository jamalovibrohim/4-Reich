from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from Mistake.models import *


class User(AbstractUser):
    JINS = [
            ('male', 'Male'),
            ('female', 'Female'),
        ]
    gender = models.CharField(max_length=6, choices = JINS)
    phone = models.CharField(max_length=13)
    image = models.ImageField(upload_to = 'user_photos')
    def __str__(self):
        return self.username

class Ish_turi(models.Model):
    ish_name = models.CharField(max_length=100)
    ish_id = models.CharField(unique=True)
    def __str__(self):
        return self.ish_name

class Xodim(models.Model):
    JINS = [
            ('male', 'Male'),
            ('female', 'Female'),
        ]
    gender = models.CharField(max_length=6, choices = JINS, null = True)
    name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    image = models.ImageField(upload_to = 'xodim_photos')
    phone = models.CharField(max_length=13)
    ish_turi = models.ForeignKey(Ish_turi, on_delete = models.CASCADE, related_name = 'ish_turi')
    xodim_id = models.CharField(unique=True)
    bolimi = models.ForeignKey(Bolim, on_delete = models.CASCADE, related_name = 'bolim')
    def __str__(self):
        return self.name

# --------------------------------------------------------------------------------------------

class Mavzu(models.Model):
	theme = models.CharField(max_length = 100)


class Masala(models.Model):
	sharti = models.TextField()
	user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user_masala')
	mavzu = models.ForeignKey(Mavzu, on_delete = models.CASCADE, related_name = 'mavzu_masala')




# --------------------------------------------------------------------------------------------

class CarAuthor(models.Model):
	car_a = models.CharField(max_length = 20)
 
	def __str__(self):
		return self.name


class Car(models.Model):
	rusumi = models.CharField(max_length = 20)
	yili = models.CharField(max_length = 10)
	ca = models.ForeignKey(CarAuthor, on_delete = models.CASCADE, related_name = 'auto')

# --------------------------------------------------------------------------------------------

class Author(models.Model):
	first_name = models.CharField(max_length = 50)

	def __str__(self):
		return self.name

class Book(models.Model):
	name = models.CharField(max_length = 50)
	author = models.ForeignKey(Author, on_delete = models.CASCADE, related_name = 'book')

# --------------------------------------------------------------------------------------------

class Photo(models.Model):
	photo = models.ImageField(upload_to = 'news/')

# --------------------------------------------------------------------------------------------

class Text(models.Model):
	text = models.TextField()

# yangilik yaratish

class Yangilik(models.Model):

	sarlavha = models.CharField(max_length = 200)
	matn = models.TextField()
	photo = models.ManyToManyField(Photo)
	text = models.ManyToManyField(Text)

	class Meta:
		verbose_name_plural = "Yangiliklar"


#  Create your models here.

class Comment(models.Model):
	comment = models.TextField()
	news = models.ForeignKey(Yangilik, on_delete = models.CASCADE, related_name = "news_comments")
	created_at = models.DateField(auto_now_add = True)

# --------------------------------------------------------------------------------------------

class User(AbstractUser):

	status = (
	('admin', 'Admin'),
	('user', 'User'),
	)

	jins = (
	('erkak', 'Erkak'),
	('ayol', 'Ayol'),


	)

	number = models.IntegerField()
	# photo = models.ImageField(upload_to = 'user_photos/', null = True, blank = True)
	status = models.CharField(choices = status, default = 'user')
	jinsi = models.CharField(choices = jins),
	full_name = models.CharField(max_length = 200)

	def __str__(self):
		return self.username



class Talab(models.Model):
	Kompaniya  = models.CharField(max_length = 20)
	Modeli = models.CharField(max_length = 20)
	Rangi = models.CharField(max_length = 10)
	Bosh_narxi = models.IntegerField()IntegerField()
	Oxirgi_narxi = models.IntegerField()
	Xolati = models.TextField()
	# Phone_number = models.IntegerField()
	Qushimcha = models.TextField()
	Talabgor = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'talabgorlar')

# class Rasm(models.Model):
	# Rasmi = models.ImageField(upload_to = 'taklif/', null = True, blank = True)

class Taklif(models.Model):
	Kompaniya  = models.CharField(max_length = 20)
	Modeli = models.CharField(max_length = 20)
	Rangi = models.CharField(max_length = 10)
	Narxi = models.IntegerField()
	Xolati = models.TextField()
	# Phone_number = models.IntegerField()
	Manzil = models.CharField(max_length = 200)
	Qushimcha = models.TextField()
	Taklifchi = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'taklifchi')
