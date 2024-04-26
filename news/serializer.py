from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Yangilik, Comment, Photo, Text, Author, Book, CarAuthor, Car, Mavzu, Masala


class U_Ser(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'first_name', 'last_name','password', 'email', 'username']

class MavzuSer(serializers.ModelSerializer):
	class Meta:
		model = Mavzu
		fields = ['id', 'theme']


class MasalaSer(serializers.ModelSerializer):
	class Meta:
		model = Masala
		fields = ['id', 'sharti', 'user', 'mavzu']

class MasalaGetSer(serializers.ModelSerializer):
	user = U_Ser()
	mavzu = MavzuSer()
	class Meta:
		model = Masala
		fields = ['id', 'sharti', 'user', 'mavzu']

# --------------------------------------------------------------------------------------------

class CarAuthorSer(serializers.ModelSerializer):
	class Meta:
		model = CarAuthor
		fields = ['id', 'car_a']


class CarSer(serializers.ModelSerializer):
	class Meta:
		model = Car
		fields = ['id', 'rusumi', 'yili', 'ca']

class CarGetSer(serializers.ModelSerializer):
	ca = CarAuthorSer()
	class Meta:
		model = Car
		fields = ['id', 'rusumi', 'yili', 'ca']

# --------------------------------------------------------------------------------------------

class AuthorSer(serializers.ModelSerializer):
	class Meta:
		model = Author
		fields = ['id', 'first_name']


class BookSer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = ['id', 'name', 'author']

class BookGetSer(serializers.ModelSerializer):
	author = AuthorSer()
	class Meta:
		model = Book
		fields = ['id', 'name', 'author']

# --------------------------------------------------------------------------------------------

class PhotoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Photo
		field = ['id', 'photo']

# --------------------------------------------------------------------------------------------

class TextSerializer(serializers.ModelSerializer):

	class Meta:
		model = Text
		fields = ['id', 'text']

# --------------------------------------------------------------------------------------------

class NewsSerializer(serializers.ModelSerializer):

	class Meta:
		model = Yangilik
		fields = ['id', 'sarlavha', 'matn', 'text', 'photo']
		read_only_fields = ['text', 'photo']


	def create(self, validated_data):
		print(validated_data)

		matn = validated_data.get('matn', None)
		sarlavha = validated_data.get('sarlavha', None)
		n = Yangilik.objects.create(matn = matn, sarlavha = sarlavha)
		return n

	def update(self, instance, validated_data):
		print(instance)
		instance.matn = validated_data.get('matn', instance.matn)
		instance.sarlavha = validated_data.get('sarlavha', instance.sarlavha)
		instance.save()
		return instance

# --------------------------------------------------------------------------------------------

class CommentPostSer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ['id', 'comment', 'news', 'created_at']


class CommentGetSer(serializers.ModelSerializer):
	news = NewsSerializer()
	class Meta:
		model = Comment
		fields = ['id', 'comment', 'news', 'created_at']

# --------------------------------------------------------------------------------------------

class USer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'number', 'status', 'jins', 'full_name']

class Talab_Ser(serializers.ModelSerializer):
	class Meta:
		model = Talab
		fields = ['id', 'Kompaniya', 'Modeli', 'Rangi', 'Bosh_narxi', 'Oxirgi_narxi', 'Xolati', 'Talabgor', 'Qushimcha']

class Talab_GetSer(serializers.ModelSerializer):
	Talabgor = User()
	class Meta:
		model = Talab
		fields = ['id', 'Kompaniya', 'Modeli', 'Rangi', 'Bosh_narxi', 'Oxirgi_narxi', 'Xolati', 'Talabgor', 'Qushimcha']

class Taklif_Ser(serializers.ModelSerializer):
	class Meta:
		model = Talab
		fields = ['id', 'Kompaniya', 'Modeli', 'Rangi', 'Narxi', 'Xolati', 'Manzil','Taklifchi', 'Qushimcha']

class Taklif_GetSer(serializers.ModelSerializer):
	Taklifchi = User()
	class Meta:
		model = Talab
		fields = ['id', 'Kompaniya', 'Modeli', 'Rangi', 'Narxi', 'Xolati', 'Manzil','Taklifchi', 'Qushimcha']