from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, Review

class ChoiceField(serializers.ChoiceField):
    
    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        if data == '' and self.allow_blank:
            return ''
        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)
class BookSerializer(serializers.ModelSerializer):
    genre = ChoiceField(choices=Book.GENRE_CHOICES)
    class Meta:
        model = Book
        fields = ['title', 'cover', 'author', 'description', 'pub_year', 'genre']

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ['review_text', 'user', 'book', 'rating']