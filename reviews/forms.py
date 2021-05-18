from django import forms
from reviews.models import Review


class ReviewForm(forms.ModelForm):
    """add review form"""
    
    class Meta:
        model = Review
        fields = ('product','title', 'comment' )
