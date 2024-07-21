from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year', 'genre', 'isbn', 'description', 'price']



class BorrowForm(forms.Form):
    book_id = forms.IntegerField(label='Book ID')
    student_name = forms.CharField(max_length=100, label='Student Name')
    student_id = forms.CharField(max_length=100, label='Student ID')
    branch = forms.CharField(max_length=100, label='Branch')
