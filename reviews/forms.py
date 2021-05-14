from django import forms
from reviews.models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('product', 'comment', 'date_added',)

