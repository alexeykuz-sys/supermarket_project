from django import forms
from reviews.models import Review


class ReviewForm(forms.ModelForm):
    """add review form"""
    
    class Meta:
        model = Review
        fields = ['user', 'date_added','title', 'comment' ]
