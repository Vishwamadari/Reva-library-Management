from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, default='Unknown Author')
    publication_year = models.IntegerField(default=2000)
    genre = models.CharField(max_length=100, default='Unknown Genre')
    isbn = models.CharField(max_length=13, default='0000000000000')
    description = models.TextField(default='No description available')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return self.title

class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=50)
    branch = models.CharField(max_length=100)
    issue_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.student_name} borrowed {self.book.title}"
