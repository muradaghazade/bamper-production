from django import forms
from core.models import Order, Contact

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['title', 'image', 'phone']

        widgets = {
            'title': forms.TextInput(attrs={'id': 'question', 'placeholder': 'Ehtiyat hissəsinin adını daxil edin', 'class': 'part-input'}),
            'phone': forms.TextInput(attrs={'id': 'question', 'placeholder': 'Əlaqə nömrənizi daxil edin', 'class': 'part-input'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'id': 'question', 'placeholder': 'Ad və soyad'}),
            'phone': forms.TextInput(attrs={'id': 'question', 'placeholder': 'Nömrə'}),
            'email': forms.EmailInput(attrs={'id': 'question', 'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'id': 'question', 'placeholder': 'Mesaj', 'class': 'message_inp', 'style': 'padding-top: 15px;'}),
        }

class IndexContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'id': 'question', 'placeholder': 'Adınızı daxil edin', "class": "contact-name-input mt-4"}),
            'phone': forms.TextInput(attrs={'id': 'question', 'placeholder': 'Nömrənizi daxil edin', "class": "contact-name-input mt-3"}),
            'email': forms.EmailInput(attrs={'id': 'question', 'placeholder': 'E-poçt ünvanınızı daxil edin', 'class': 'contact-name-input mt-3'}),
            'message': forms.Textarea(attrs={'id': 'question', 'placeholder': 'Mesajınızı daxil edin', 'class': 'contact-name-textarea mt-3', 'style': 'padding-top: 15px;', "style": "resize: none;"}),
        }