from rest_framework import serializers
from .models import Book, Review

class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ['author', 'title', 'cover', 'pub_year', 'genre', 'description', 'slug']