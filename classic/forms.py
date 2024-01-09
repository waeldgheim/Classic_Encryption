from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_alphabetic_key(value):
    if not value.isalpha():
        raise ValidationError("Key must contain only alphabetic characters.")
    return value

def validate_ascii(value):
    if not value.isascii():
        raise ValidationError(
            _('The input contains non-ASCII characters. Only ASCII characters are allowed.'),
            params={'value': value},
        )

def validate_all_alphabet_characters(value):
    if len(set(value.lower())) != 26:
        raise ValidationError("Key must contain all 26 letters of the alphabet.")
    return value

def validate_numeric(value):
    if not value.replace(" ", "").isnumeric():
        raise ValidationError("Only numeric characters (and spaces) are allowed.")
    return value

def validate_alphabet_space(value):
    if not value.replace(" ", "").isalpha():
        raise ValidationError("Only alphabetic characters (and spaces) are allowed.")
    return value

class Affine(forms.Form):
    plaintext = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Ex: The Affine Cipher is s1mple and e4sy!','rows': 4, 'cols': 50}),
        label="",
        validators=[validate_ascii]
    )
    a = forms.IntegerField(
        label="a (Multiplicative Key)",
        widget=forms.NumberInput(attrs={'placeholder': 'Ex: 35 = 35 mod 26 = 9', 'style': 'width: 164px;'}),  # Adjust the width as needed
    )
    b = forms.IntegerField(
        label="b (Additive Key)",
        widget=forms.NumberInput(attrs={'placeholder': 'Ex: 45 = 45 mod 26 = 19', 'style': 'width: 164px;'}),  # Adjust the width as needed
    )
    mode = forms.ChoiceField(choices=((("Encrypt","Encrypt"),("Decrypt","Decrypt"))))
    
class CrackedAffineForm(forms.Form):
    ciphertext = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Try encrypting "Sweetest Delight" and then inputting the ciphertext here with E and T as most frequent letters ','rows': 4, 'cols': 50}),
        label="",
        validators=[validate_ascii]
    )
    firstletter = forms.CharField(
        max_length=1,
        widget=forms.TextInput(attrs={'placeholder': 'Default: E', 'value': 'e'}),
        required=False,
        label="First Most Frequent Letter",
        validators=[validate_alphabetic_key]
    )
    secondletter = forms.CharField(
        max_length=1,
        widget=forms.TextInput(attrs={'placeholder': 'Default: T', 'value': 't'}),
        required=False,
        label="Second Most Frequent Letter",
        validators=[validate_alphabetic_key]
    )
class TopBruteForm(forms.Form):
    ciphertext = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Try encrypting "A sentence must have a complete idea that stands alone. This is also called an independent clause." and then inputting the ciphertext here','rows': 4, 'cols': 50}),
        label="",
        validators=[validate_ascii]
    )

class Vigenere(forms.Form):
    text = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Ex: The Vigenere Cipher is s1mple and e4sy!','rows': 4, 'cols': 50}),validators=[validate_ascii])
    key = forms.CharField(label='Enter the Vigenere key',validators=[validate_alphabetic_key], widget=forms.TextInput(attrs={'placeholder': 'Ex: Monarchy'}))
    mode = forms.ChoiceField(choices=((("Encrypt","Encrypt"),("Decrypt","Decrypt"))))

class Monoalphabetic(forms.Form):
    text = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Ex: The Monoalphabetic Cipher is s1mple and e4sy!','rows': 4, 'cols': 50}),validators=[validate_ascii])
    key = forms.CharField(label='Key', max_length=26,validators=[validate_alphabetic_key,validate_all_alphabet_characters], widget=forms.TextInput(attrs={'placeholder': 'Ex: ZYXWVUTSRQPONMLKJIHGFEDCBA','size': 35}))
    mode = forms.ChoiceField(choices=((("Encrypt","Encrypt"),("Decrypt","Decrypt"))))

class Playfair(forms.Form):
    plaintext = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Ex: The Playfair Cipher is s1mple and e4sy!','rows': 4, 'cols': 50}),
        label="",
        validators=[validate_ascii]
    )
    key = forms.CharField(label="Key",max_length=26,validators=[validate_alphabet_space], widget=forms.TextInput(attrs={'placeholder': 'Ex: Waterloo'}))
    mode = forms.ChoiceField(choices=((("Encrypt","Encrypt"),("Decrypt","Decrypt"))))

class HillCipher2x2Form(forms.Form):
    text_2x2 = forms.CharField(label='Enter Text:', widget=forms.Textarea(attrs={'placeholder': 'Ex: Hill Cipher is s1mple and e4sy!','rows': 4, 'cols': 50}),validators=[validate_ascii])
    key_00_2x2 = forms.IntegerField(label='')
    key_01_2x2 = forms.IntegerField(label='')
    key_10_2x2 = forms.IntegerField(label='')
    key_11_2x2 = forms.IntegerField(label='')
    operation_2x2 = forms.ChoiceField(label = 'Mode:', choices=((("Encrypt","Encrypt"),("Decrypt","Decrypt"))))

class HillCipher3x3Form(forms.Form):
    text_3x3 = forms.CharField(label='Enter Text:', widget=forms.Textarea(attrs={'placeholder': 'Ex: Hill Cipher is s1mple and e4sy!','rows': 4, 'cols': 50}),validators=[validate_ascii])
    key_00_3x3 = forms.IntegerField(label='')
    key_01_3x3 = forms.IntegerField(label='')
    key_02_3x3 = forms.IntegerField(label='')
    key_10_3x3 = forms.IntegerField(label='')
    key_11_3x3 = forms.IntegerField(label='')
    key_12_3x3 = forms.IntegerField(label='')
    key_20_3x3 = forms.IntegerField(label='')
    key_21_3x3 = forms.IntegerField(label='')
    key_22_3x3 = forms.IntegerField(label='')
    operation_3x3 = forms.ChoiceField(label = 'Mode:', choices=((("Encrypt","Encrypt"),("Decrypt","Decrypt"))))

class ExtendedEuclid(forms.Form):
    a = forms.IntegerField(
        label="a",
        widget=forms.NumberInput(attrs={'placeholder': 'Ex: 35 = 35 mod 26 = 9', 'style': 'width: 164px;'}),  # Adjust the width as needed
    )
    b = forms.IntegerField(
        label="b",
        widget=forms.NumberInput(attrs={'placeholder': 'Ex: 45 = 45 mod 26 = 19', 'style': 'width: 164px;'}),  # Adjust the width as needed
    )

