from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Member(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)
    membership_id = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="loans")
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="loans")
    loan_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.book.title} borrowed by {self.member.name}"
