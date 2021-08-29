from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify

# Create your models here.
class Book(models.Model):
    CATEGORY_CHOICES = [
        ('F', 'Forklore'),
        ('N', 'Nonfiction'),
        ('FA', 'Fantasy'),
        ('S', 'Biography'),
        ('P', 'Poetry')
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    cover = models.ImageField(upload_to="covers")
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    pub_year = models.PositiveSmallIntegerField("Publication Year", null=True)
    slug = models.SlugField(max_length=200)

    class Meta:
        ordering = ["-author"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(
        Book, related_name="reviews", on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text= models.TextField()
    rating = models.IntegerField(
        default=1, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True) 

    def __str__(self):
        return self.review_text
