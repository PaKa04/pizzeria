from django.forms import Form, IntegerField, ModelForm, EmailField, EmailInput, CharField, TextInput, Textarea

from .models import Contact


# <input type="text" class="form-control" placeholder="First Name">
# <input type="text" class="form-control" placeholder="Last Name"
# <textarea name="" id="" cols="30" rows="3" class="form-control" placeholder="Message"></textarea>
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
        widgets = {
            'name': TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'placeholder': "First Name"
                }
            ),
            'email': TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'placeholder': "Last Name"
                }
            ),
            'message': Textarea(
                attrs={
                    'name': '',
                    'id': '',
                    'clos': '30',
                    'row': '3',
                    'class': 'form-control',
                    'placeholder': "Message"
                }
            )
        }


