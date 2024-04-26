from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FileUploadParser


from news.models import Yangilik, Comment, Text, Photo, Author, Book, CarAuthor, Car, Mavzu, Masala, User, Taklif, Talab
from news.serializer import (NewsSerializer, CommentPostSer, CommentGetSer, TextSerializer, PhotoSerializer,
								AuthorSer, BookSer, BookGetSer, CarAuthorSer, CarGetSer, CarSer, U_Ser, MavzuSer,MasalaSer, MasalaGetSer,
								USer, Talab_Ser, Talab_GetSer, Taklif_Ser, Taklif_GetSer
								)


class UserView(APIView):
	def get(self, request):
		u = User.objects.all()
		b = U_Ser(u, many= True)
		return Response (b.data)
	def post(self, request):
		b = U_Ser(data = request.data)
		if b.is_valid():
			b.save()
			return Response(b.data)
		return Response(b.errors)
		

class MavzuView(APIView):
	def get(self, request):
		m = Mavzu.objects.all()
		c = MavzuSer(m, many= True)
		return Response (c.data)
	def post(self, request):
		c = MavzuSer(data = request.data)
		if c.is_valid():
			c.save()
			return Response(c.data)
		return Response(c.errors)

class MasalaView(APIView):
	def get(self, request):
		m = Masala.objects.all()
		s = MasalaGetSer(m, many= True)
		return Response (s.data)
	def post(self, request):
		s = MasalaSer(data = request.data)
		if s.is_valid():
			s.save()
			return Response(s.data)
		return Response(s.errors)
		
# --------------------------------------------------------------------------------------------

class CarAuthorView(APIView):
	def get(self, request):
		a = CarAuthor.objects.all()
		c = CarAuthorSer(a, many= True)
		return Response(c.data)
	def post(self,request):
		c = CarAuthorSer(data = request.data)
		if c.is_valid():
			c.save()
			return Response(c.data)
		return Response(c.errors)

class CarView(APIView):
	def get(self, request):
		a = Car.objects.all()
		c = CarGetSer(a, many= True)
		return Response(c.data)
	def post(self,request):
		c = CarSer(data = request.data)
		if c.is_valid():
			c.save()
			return Response(c.data)
		return Response(c.errors)


# --------------------------------------------------------------------------------------------


class AuthorView(APIView):
	def get(self, request):
		a = Author.objects.all()
		s = AuthorSer(a, many= True)
		return Response(s.data)
	def post(self,request):
		s = AuthorSer(data = request.data)
		if s.is_valid():
			s.save()
			return Response(s.data)
		return Response(s.errors)

class BookView(APIView):
	def get(self, request):
		a = Book.objects.all()
		s = BookGetSer(a, many= True)
		return Response(s.data)
	def post(self,request):
		s = BookSer(data = request.data)
		if s.is_valid():
			s.save()
			return Response(s.data)
		return Response(s.errors)

# --------------------------------------------------------------------------------------------

class CommentView(APIView):
	def get(self, request):
		comments = Comment.objects.all()
		s = CommentGetSer(comments, many = True)
		return Response(s.data)

	def post(self, request):
		s = CommentPostSer(data=request.data)
		if s.is_valid():
			s.save()
			return Response(s.data)
		return Response (s.errors)

# --------------------------------------------------------------------------------------------

class TextApiList(APIView):
	perser_classes = [MultiPartParser]

	def get(self, request):
		t = Text.objects.all()
		dict_data = TextSerializer(t, many= True)
		return Response(dict_data.data)

	def post(self, request):
		
		serializer = TextSerializer (data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors)			

# --------------------------------------------------------------------------------------------

class NewsApiList(APIView):
	perser_classes = [MultiPartParser]

	def get(self, request):
		a = Yangilik.objects.all()
		dict_data = NewsSerializer(a, many= True)

		return Response(dict_data.data)

	def post(self, request):
		print(request.data)
		text_list = request.data.getlist('text',[])
		rasm_list = request.data.getlist('rasm',[])
		print(rasm_list)

		serializer = NewsSerializer(data = request.data)
		if serializer.is_valid():
			news = serializer.save()
			for x in text_list:
				t = Text.objects.create(text=x)
				news.text.add(t)
			for x in rasm_list:
				p = Photo.objects.create(photo=x)
				news.photo.add(p)
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors)

# --------------------------------------------------------------------------------------------

class NewsDetailAPIView(APIView):
	def get(self, request, id):
		a = Yangilik.objects.get(id=id)
		ser = NewsSerializer(a)
		return Response(ser.data)

	def put(self, request, id):
		a = Yangilik.objects.get(id=id)
		serializer = NewsSerializer(data = request.data, instance=a)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors)


	def patch(self, request, id):
		a = Yangilik.objects.get(id=id)
		# rasm_list = request.data.getlist('rasm',[])
		# for x in rasm_list:
		# 		p = Photo.objects.create(photo=x)
		# 		news.photo.add(a)

		serializer = NewsSerializer (data = request.data, instance=a, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors)

	def delete(self, request, id):
		a = Yangilik.objects.get(id=id)
		a.delete()
		message = {"delete" : "successfull"}
		return Response(message)

# --------------------------------------------------------------------------------------------

class USerView(APIView):
	def get(self, request):
		u = User.objects.all()
		b = USer(u, many= True)
		return Response (b.data)
	def post(self, request):
		b = USer(data = request.data)
		if b.is_valid():
			b.save()
			return Response(b.data)
		return Response(b.errors)


class TaklifView(APIView):
	def get(self, request):
		m = Taklif.objects.all()
		s = Taklif_GetSer(m, many= True)
		return Response (s.data)
	def post(self, request):
		s = Taflif_Ser(data = request.data)
		if s.is_valid():
			s.save()
			return Response (s.data)
		return Response (s.errors)

class TalabView(APIView):
	def get(self, request):
		m = Talab.objects.all()
		s = Talab_GetSer(m, many= True)
		return Response (s.data)
	def post(self, request):
		s = Talab_Ser(data = request.data)
		if s.is_valid():
			s.save()
			return Response (s.data)
		return Response (s.errors)

# --------------------------------------------------------------------------------------------

def news(request):
	all_news = Yangilik.object.all()
	return render(request, "link.html", {"yangiliklar": all_news})


def home(request):
	return render(request, "home.html")

def menu(request):
	return render(request, "menu.html")