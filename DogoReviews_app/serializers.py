from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, Review

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['author', 'title', 'cover', 'pub_year', 'genre', 'description']

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ['review_text', 'user', 'book', 'rating']