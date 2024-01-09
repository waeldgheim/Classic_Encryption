def playfair_cipher(plaintext, key, mode):  
    
    # Define the alphabet, excluding 'j'  
    alphabet = 'abcdefghiklmnopqrstuvwxyz' 

    d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
 
    
    # Remove whitespace and 'j' from the key and convert to lowercase  
    key = key.lower().replace(' ', '').replace('j', 'i')  
    
    # Construct the key square  
    key_square = ''  
    for letter in key + alphabet:  
        if letter not in key_square:  
            key_square += letter  
            
    # Split the plaintext into digraphs, padding with 'x' or 'z' if necessary
    k = ""
    for i in range(len(plaintext)):
        if plaintext[i].lower() in d:
            k = k+plaintext[i]
    k = k.replace(' ', '').replace('j', 'i')
    
    for i in range(0,len(k),2):
        p = k[i:i+2]
        if len(p) == 2:
            if p[0] == p[1] and p[0] != 'x':
                k = k[:i+1]+'x'+k[i+1:]
                
            elif p[0] == p[1] and p[0] != 'z':
                k = k[:i+1]+'z'+k[i+1:]
                
    if len(k) % 2 == 1:
        k += 'x'  
    digraphs = [k[i:i+2] for i in range(0, len(k), 2)]
    
    # Define the encryption/decryption functions  
    def encrypt(digraphs): 
        result = ''
        for digraph in digraphs:
            a, b = digraph  
            row_a, col_a = divmod(key_square.index(a.lower()), 5)   #gives quotient, remainder which are the row, column of the entry
            row_b, col_b = divmod(key_square.index(b.lower()), 5)  
            if row_a == row_b:  
                col_a = (col_a + 1) % 5            #if letters are on the same row, move each column to the right
                col_b = (col_b + 1) % 5  
            elif col_a == col_b:  
                row_a = (row_a + 1) % 5             #if letters are on the same column, move each row downwards
                row_b = (row_b + 1) % 5  
            else:  
                col_a, col_b = col_b, col_a         # else swap the columns (anti-clockwise substitutions)

            if a.isupper():                                     #to preserve capital letters
                r = key_square[row_a*5+col_a].upper()
            else:
                r = key_square[row_a*5+col_a]

            if b.isupper():
                l = key_square[row_b*5+col_b].upper()
            else:
                l = key_square[row_b*5+col_b]

            result += r+ l
        return result,key_square
    
    def decrypt(digraphs):  
        result = ''
        for digraph in digraphs:
            a, b = digraph  
            row_a, col_a = divmod(key_square.index(a.lower()), 5)  
            row_b, col_b = divmod(key_square.index(b.lower()), 5)  
            if row_a == row_b:  
                col_a = (col_a - 1) % 5             #if letters are on the same row, move each column to the left
                col_b = (col_b - 1) % 5  
            elif col_a == col_b:  
                row_a = (row_a - 1) % 5             #if letters are on the same column, move each row upwards
                row_b = (row_b - 1) % 5  
            else:  
                col_a, col_b = col_b, col_a          # else swap the columns (anti-clockwise substitutions)

            if a.isupper():
                r = key_square[row_a*5+col_a].upper()
            else:
                r = key_square[row_a*5+col_a]

            if b.isupper():
                l = key_square[row_b*5+col_b].upper()
            else:
                l = key_square[row_b*5+col_b]
            result += r+ l
        return result,key_square
    
# Encrypt or decrypt the plaintext  
    if mode.lower() == 'encrypt':
        r,k = encrypt(digraphs) 
        return r,k
    elif mode.lower() == 'decrypt': 
        r,k = decrypt(digraphs)
        return r,k