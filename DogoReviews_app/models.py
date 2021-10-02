from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.safestring import mark_safe

# Create your models here.
F='Forklore'
N='Nonfiction'
FA='Fantasy'
B='Biography'
P='Poetry'
class Book(models.Model):
    GENRE_CHOICES = [
        (F, 'Forklore'),
        (N, 'Nonfiction'),
        (FA, 'Fantasy'),
        (B, 'Biography'),
        (P, 'Poetry')
    ]
    bookId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    cover = models.ImageField(upload_to="covers")
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=10, choices=GENRE_CHOICES)
    pub_year = models.PositiveSmallIntegerField("Publication Year", null=True)
    
    class Meta:
        ordering = ["-author"]
    def __str__(self):
        return self.title

class ReviewManager(models.Manager):
    def review_validator(self, postData):
            errors = {}
            if (len(postData['review']) < 1):
                errors["blank"] = "Review should not be empty!"
            return errors
class Review(models.Model):
    review_text= models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(
        Book, related_name="reviews", on_delete=models.CASCADE
    )
    rating = models.IntegerField(
        default=1, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True) 

    objects=ReviewManager()
    
    def __str__(self):
        return '{} {} {}'.format(self.book, self.user, self.rating)
