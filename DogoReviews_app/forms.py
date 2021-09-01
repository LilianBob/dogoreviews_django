from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Book, Review

class SearchForm(forms.Form):
    CATEGORY_CHOICES = [
        ('F', 'Forklore'),
        ('N', 'Nonfiction'),
        ('FA', 'Fantasy'),
        ('S', 'Biography'),
        ('P', 'Poetry')
    ]
    name = forms.CharField(label='book title', max_length=255, required=True)
    category = forms.ChoiceField(
        label='Choose a Category:', 
        widget=forms.RadioSelect, choices=CATEGORY_CHOICES,
        required=False
    )
    
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text', 'book', 'rating', 'user', 'created_at']
        widgets = {'book': forms.RadioSelect()}
        labels = {'user': u'Please enter a valid username', 'rating': u'Rating: 1 for least and 5 for most'}

