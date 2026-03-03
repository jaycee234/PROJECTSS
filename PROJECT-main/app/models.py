from django.db import models

# Create your models here.

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.author_name
    
class Members(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50) # Changed to EmailField for better validation
    phone_number = models.CharField(max_length=15) # Changed to CharField; Integers strip leading zeros

    def __str__(self):
        return self.name
    
class Books(models.Model):
    id =models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class BorrowRecords(models.Model):
    id = models.AutoField(primary_key=True)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    member = models.ForeignKey(Members, on_delete=models.CASCADE) # Changed field name from 'name' to 'member' for clarity
    book = models.ForeignKey(Books, on_delete=models.CASCADE)    # Changed field name from 'title' to 'book' for clarity

    def __str__(self):
        return f"{self.member.name} borrowed {self.book.title}"

