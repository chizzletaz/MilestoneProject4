from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=25, required=True)
    email = forms.EmailField(max_length=25, required=True)
    message_subject = forms.CharField(max_length=100, required=True)
    message_body = forms.CharField(max_length=1500, widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email',
            'message_subject': 'Subject',
            'message_body': 'Message',
        }
        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = f'{placeholders[field]} *'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'space-form rounded-0'
            self.fields[field].label = False