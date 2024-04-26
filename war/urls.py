"""
URL configuration for war project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .function import (home,menu,NewsApiList,NewsDetailAPIView,TextApiList,
                        AuthorView, BookView, CarAuthorView, CarView, UserView, MavzuView, MasalaView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', NewsApiList.as_view()),
    path('text/', TextApiList.as_view()),
    path('news/<int:id>/', NewsDetailAPIView.as_view()),
    # path('news/', news, name = "news"),
    path('api-auth/', include('rest_framework.urls')),
    # path('', home, name = 'home'),
    path('menu/', menu, name = 'menu'),
    path('author/', AuthorView.as_view()),
    path('book/', BookView.as_view()),
    path('car_a/', CarAuthorView.as_view()),
    path('car/', CarView.as_view()),
    path('user/', UserView.as_view()),
    path('mavzu/', MavzuView.as_view()),
    path('masala/', MasalaView.as_view())
]

