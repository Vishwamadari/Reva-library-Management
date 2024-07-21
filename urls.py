from django.urls import path
from .views import helloView, addBookView, editBookView, deleteBookView, bookDetailView

urlpatterns = [
    path('', helloView, name='home'),
    path('book/add/', addBookView, name='add-book'),
    path('book/edit/<int:book_id>/', editBookView, name='edit-book'),
    path('book/delete/<int:book_id>/', deleteBookView, name='delete-book'),
    path('book/<int:book_id>/', bookDetailView, name='book-detail'),
]
