from django import forms
from reviews.models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['title', 'comment', 'date_added']

    