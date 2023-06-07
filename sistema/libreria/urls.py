from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('us', views.us, name='us'),
    path('books', views.books, name="books"),
    path('books/add', views.addBooks, name="addBooks"),
    path('books/edit', views.editBooks, name="editBooks")
]
