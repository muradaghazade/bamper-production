from django import forms
from core.models import Order, Contact

class OrderForm(forms.ModelForm):
    title = forms.CharField(required = True, widget=forms.TextInput(attrs={'id': 'question', 'placeholder': 'Ehtiyat hissəsinin adını daxil edin', 'class': 'part-input'})) 
    phone = forms.CharField(required = True, widget=forms.TextInput(attrs={'id': 'question', 'placeholder': 'Əlaqə nömrənizi daxil edin', 'class': 'part-input'})) 
    class Meta:
        model = Order
        fields = ['title', 'image', 'phone']

class ManualForm(forms.ModelForm):
    make = forms.CharField(required = True, widget=forms.TextInput(attrs={'id': 'question', 'placeholder': 'Avtomobilinizin markasını daxil edin', 'class': 'part-input'}))
    model = forms.CharField(required = True, widget=forms.TextInput(attrs={'id': 'question', 'placeholder': 'Avtomobilinizin modelini daxil edin', 'class': 'part-input'}))
    year = forms.CharField(required = True, widget=forms.TextInput(attrs={'id': 'question', 'placeholder': 'Avtomobilinizin ilin daxil edin', 'class': 'part-input'})) 
    title = forms.CharField(required = True, widget=forms.TextInput(attrs={'id': 'question', 'placeholder': 'Ehtiyat hissəsinin adını daxil edin', 'class': 'part-input'})) 
    phone = forms.CharField(required = True, widget=forms.TextInput(attrs={'id': 'question', 'placeholder': 'Əlaqə nömrənizi daxil edin', 'class': 'part-input'})) 
    class Meta:
        model = Order
        fields = ['make', 'model', 'year' ,'title', 'image', 'phone']

class ContactForm(forms.ModelForm):
    name = forms.CharField(required = True, widget=forms.TextInput(attrs={'id': 'question', 'placeholder': 'Ad və soyad'}))
    phone = forms.CharField(required = True, widget=forms.TextInput(attrs={'id': 'question', 'placeholder': 'Nömrə'}))
    email = forms.CharField(required = True, widget=forms.EmailInput(attrs={'id': 'question', 'placeholder': 'Email'}))
    message = forms.CharField(required = True, widget=forms.Textarea(attrs={'id': 'question', 'placeholder': 'Mesaj', 'class': 'message_inp', 'style': 'padding-top: 15px;'}))
    class Meta:
        model = Contact
        fields = '__all__'

class IndexContactForm(forms.ModelForm):
    name = forms.CharField(required = True, widget=forms.TextInput(attrs={'id': 'question', 'placeholder': 'Adınızı daxil edin', "class": "contact-name-input mt-4"}))
    phone = forms.CharField(required = True, widget=forms.TextInput(attrs={'id': 'question', 'placeholder': 'Nömrənizi daxil edin', "class": "contact-name-input mt-3"}))
    email = forms.CharField(required = True, widget=forms.EmailInput(attrs={'id': 'question', 'placeholder': 'E-poçt ünvanınızı daxil edin', 'class': 'contact-name-input mt-3'}))
    message = forms.CharField(required = True, widget=forms.Textarea(attrs={'id': 'question', 'placeholder': 'Mesajınızı daxil edin', 'class': 'contact-name-textarea mt-3', 'style': 'padding-top: 15px;', "style": "resize: none;"}))
    class Meta:
        model = Contact
        fields = '__all__'
