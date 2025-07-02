from django import forms
from .models import *


class AddBook(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['name', 'description', 'isbn', 'price']
        # Forma tayyor
        # validation qushish
    def clean_description(self):
        description=self.cleaned_data['description']
        if not 10<len(description)<1000:
            raise forms.ValidationError("izoh 10ta harfdan kam va 1000 ta harfdan ko'p bo;lmasligi kerak")
        return description

    def clean_isbn(self):
        isbn=self.cleaned_data['isbn']
        if not isbn.isdigit() or len(isbn) != 13:
            raise forms.ValidationError('isbn xato yozilgan, qanday yozishni googledan toping')
        return isbn


