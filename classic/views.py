
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import *
from .affine import affine, crack_affine_cipher, top_brute_force
from .vigenere import vignere
from .mono import monoalphabetic
from .playfair import playfair_cipher
from .hillCipher import hill
from .extendedEuclid import extendedEuclid

#Home Page
def home(request):
    return render(request, "classic/home.html") 

#About Page
def about(request):
    return render(request, "classic/about.html") 

#Affine Implementation
def affine_algo(request):
    if request.method == 'POST':
        form = Affine(request.POST)
        if form.is_valid():
            plaintext = form.cleaned_data['plaintext']
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            mode = form.cleaned_data['mode']
            result = affine(plaintext, a, b,mode)
            context = {'form': form, 'result': result}
            return render(request, "classic/affine.html", context)
    else:
        form = Affine()
    
    return render(request, "classic/affine.html", {'form': form})

def top_brute_force_affine(request):
    if request.method == 'POST':
        form = TopBruteForm(request.POST)
        if form.is_valid():
            ciphertext = form.cleaned_data['ciphertext']
            results = top_brute_force(ciphertext)
            context = {'form': form, 'results': results}
            return render(request, "classic/topbruteforceaffine.html", context)
    else:
        form = TopBruteForm()

    return render(request, "classic/topbruteforceaffine.html", {'form': form})

def crack_affine(request):
    if request.method == 'POST':
        form = CrackedAffineForm(request.POST)
        if form.is_valid():
            ciphertext = form.cleaned_data['ciphertext']
            firstletter = form.cleaned_data.get('firstletter') or 'E'
            secondletter = form.cleaned_data.get('secondletter') or 'T'
            results = crack_affine_cipher(ciphertext,firstletter,secondletter)
            context = {'form': form, 'results': results}
            return render(request, "classic/crackaffine.html", context)
    else:
        form = CrackedAffineForm()

    return render(request, "classic/crackaffine.html", {'form': form})

#Vigenere Implementation
def vignere_cipher(request):
    if request.method == 'POST':
        form = Vigenere(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            key = form.cleaned_data['key']
            mode = form.cleaned_data['mode']
            result = vignere(text,key,mode)
            context = {'form': form, 'result': result}
            return render(request, "classic/vigenere.html", context)
    else:
        form = Vigenere()

    return render(request, "classic/vigenere.html", {'form': form})


#Monoalphabetic Implementation
def monoalphabetic_cipher(request):
    if request.method == 'POST':
        form = Monoalphabetic(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            key = form.cleaned_data['key']
            mode = form.cleaned_data['mode']
            result = monoalphabetic(text, key,mode)
            context = {'form': form, 'result': result}
            return render(request, "classic/monoalphabetic.html", context)
    else:
        form = Monoalphabetic()

    return render(request, "classic/monoalphabetic.html", {'form': form})

#Playfair Implementation
def playfair(request):
    if request.method == 'POST':
        form = Playfair(request.POST)
        if form.is_valid():
            plaintext = form.cleaned_data['plaintext']
            key = form.cleaned_data['key']
            mode = form.cleaned_data['mode']
            result,matrix = playfair_cipher(plaintext,key,mode)
            p=[]
            for i in matrix:
                p.append(i)
            context = {'form': form, 'result': result, "l":p}
            return render(request, "classic/playfair.html", context)
    else:
        form = Playfair()
    
    return render(request, "classic/playfair.html", {'form': form})

def hillcipher(request):
    result_2x2 = None
    result_3x3 = None

    if request.method == 'POST':
        form_2x2 = HillCipher2x2Form(request.POST)
        form_3x3 = HillCipher3x3Form(request.POST)

        if form_2x2.is_valid():
            text_2x2 = form_2x2.cleaned_data['text_2x2']
            key_matrix_2x2 = [
                [form_2x2.cleaned_data['key_00_2x2'], form_2x2.cleaned_data['key_01_2x2']],
                [form_2x2.cleaned_data['key_10_2x2'], form_2x2.cleaned_data['key_11_2x2']]
            ]
            mode_2x2 = form_2x2.cleaned_data['operation_2x2']
            result_2x2,k = hill(text_2x2, key_matrix_2x2, 2, mode_2x2)  # Call the hill function for 2x2
            key = []
            for i in key_matrix_2x2:
                for j in i:
                    key.append(j%26)
            inverse = []
            if k != None:
               for i in k:
                  for j in i:
                      inverse.append(j%26)
            return render(request, 'classic/hillcipher.html', {'form_2x2': form_2x2, 'form_3x3': form_3x3,'result_2x2': result_2x2,"key":key,"k":inverse})

        if form_3x3.is_valid():
            text_3x3 = form_3x3.cleaned_data['text_3x3']
            key_matrix_3x3 = [
                [form_3x3.cleaned_data['key_00_3x3'], form_3x3.cleaned_data['key_01_3x3'], form_3x3.cleaned_data['key_02_3x3']],
                [form_3x3.cleaned_data['key_10_3x3'], form_3x3.cleaned_data['key_11_3x3'], form_3x3.cleaned_data['key_12_3x3']],
                [form_3x3.cleaned_data['key_20_3x3'], form_3x3.cleaned_data['key_21_3x3'], form_3x3.cleaned_data['key_22_3x3']]
            ]
            mode_3x3 = form_3x3.cleaned_data['operation_3x3']
            result_3x3,k = hill(text_3x3, key_matrix_3x3, 3, mode_3x3)  # Call the hill function for 3x3
            key = []
            for i in key_matrix_3x3:
                for j in i:
                    key.append(j%26)
            inverse = []
            if k != None:
               for i in k:
                  for j in i:
                      inverse.append(j%26)
            return render(request, 'classic/hillcipher.html', {'form_3x3': form_3x3,'form_2x2': form_2x2,'result_3x3': result_3x3,"key":key,"k":inverse})
         

    else:
        form_2x2 = HillCipher2x2Form()
        form_3x3 = HillCipher3x3Form()

    return render(request, 'classic/hillcipher.html', {'form_2x2': form_2x2, 'form_3x3': form_3x3, 'result_2x2': result_2x2, 'result_3x3': result_3x3})


#Extended Euclid Implementation
def e_e(request):
    if request.method == 'POST':
        form = ExtendedEuclid(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            inverse = extendedEuclid(int(a), int(b))
            context = {'form': form, 'inverse': inverse}
            return render(request, "classic/extendedeuclid.html", context)
    else:
        form = ExtendedEuclid()

    return render(request, "classic/extendedeuclid.html", {'form': form})