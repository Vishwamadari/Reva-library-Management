from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Book, Borrow
from .forms import BookForm, BorrowForm

def helloView(request):
    books = Book.objects.all()
    return render(request, 'viewbook.html', {'books': books})

def addBookView(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def editBookView(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-detail', book_id=book_id)
    else:
        form = BookForm(instance=book)
    
    return render(request, 'book_detail.html', {
        'book': book,
        'form': form,
        'is_admin': request.user.is_superuser,
    })

def deleteBookView(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('/')
    return render(request, 'delete_book.html', {'book': book})

def bookDetailView(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    borrowed_records = Borrow.objects.filter(book=book).select_related('user')
    is_admin = request.user.is_superuser
    
    context = {
        'book': book,
        'borrowed_records': borrowed_records,
        'is_admin': is_admin,
    }
    
    return render(request, 'book_detail.html', context)

def borrowBookView(request):
    if request.method == 'POST':
        form = BorrowForm(request.POST)
        if form.is_valid():
            book_id = form.cleaned_data['book_id']
            student_name = form.cleaned_data['student_name']
            student_id = form.cleaned_data['student_id']
            branch = form.cleaned_data['branch']
            
            # Handle book borrowing logic
            book = get_object_or_404(Book, id=book_id)
            # Save the borrowing record
            Borrow.objects.create(
                book=book,
                student_name=student_name,
                student_id=student_id,
                branch=branch,
                issue_date=timezone.now()
            )
            
            return redirect('book-detail', book_id=book_id)
    else:
        form = BorrowForm()
    
    return render(request, 'borrow_book.html', {'form': form})
