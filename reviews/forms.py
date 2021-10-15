from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """ Create a form fro users to add a review """
    class Meta:
        model = Review
        fields = ('title', 'comment', 'rating')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'comment': 'Review',
            'rating': 'Rating',
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'rating':
                placeholder = f'{placeholders[field]} *'
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'space-form rounded-0'


class EditReviewForm(forms.ModelForm):
    """ Create a form fro users to add a review """
    class Meta:
        model = Review
        fields = ('title', 'comment', 'rating')
        widgets = {
            'title': forms.TextInput(attrs={'id': 'edit_title'}),
            'comment': forms.Textarea(attrs={'id': 'edit_comment'}),
            'rating': forms.Select(attrs={'id': 'edit_rating'}),
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'space-form rounded-0'
        