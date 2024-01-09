import string
from collections import Counter
# Define the alphabet
alphabet = string.ascii_lowercase

def extended_gcd(a, b): #Extended Euclid
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)

def mod_inverse(a, m): #Find a inverse using extended euclid
    g, x, y = extended_gcd(a, m)
    if g != 1:
        return None
    else:
        return x % m
def find_a(c, b, m): #find a for letter frequency crack, try multiple a until it one returns desired c from b
    if c<0:
        c= c%26
    for a in range(m):
        if (a * b) % m == c:
            return a
    return None  # No solution found
def find_b(c, a, m): #find b for letter frequency crack, try multiple b until it one returns desired c from a
    for b in range(m):
        if (a + b) % m == c:
            return b
    return None  # No solution found

def affine(text,a,b,mode):

    def encrypt(plaintext, a, b):
        ciphertext = '' #initially empty string
        for char in plaintext:
            if char.isalpha():#check if it is a letter
                if char.isupper():#check if it is uppercase
                    char = char.lower()#make it lowercase
                    is_upper = True
                else:
                    is_upper = False
                char_index = alphabet.index(char)
                encrypted_index = (a * char_index + b) % 26
                encrypted_char = alphabet[encrypted_index]
                if is_upper:#if it was uppercase, return it to uppercase
                    encrypted_char = encrypted_char.upper()
                ciphertext += encrypted_char #add encrypted character to ciphertext
            else:
                ciphertext += char #if not a letter just add the character itself

        return ciphertext

    def decrypt(ciphertext, a, b):
        plaintext = ''
        a_inv = mod_inverse(a % 26, 26) #find a inverse
        if a_inv is None: #if no inverse exists just output a error
            return "No modular inverse of 'a' exists for decryption."
        for char in ciphertext:
            if char.isalpha():#check if it is a letter
                if char.isupper():#check if it is uppercase
                    char = char.lower()#make it lowercase
                    is_upper = True
                else:
                    is_upper = False
                char_index = alphabet.index(char)
                decrypted_index = (a_inv * (char_index - b)) % 26
                decrypted_char = alphabet[decrypted_index]
                if is_upper:#if it was uppercase, return it to uppercase
                    decrypted_char = decrypted_char.upper()
                plaintext += decrypted_char #add decrypted character to plaintext
            else:
                plaintext += char #if not a letter just add the character itself
        return plaintext
    

    if mode.lower() =="encrypt":# modes to help in implementing it in one page rather then multiple
        return encrypt(text,a,b)
    elif mode.lower() =="decrypt":
        return decrypt(text,a,b)

def crack_affine_cipher(ciphertext,firstletter='e',secondletter='t'): #default firstletter and secondletter to "e" and "t" respectively
        #Iterative search for most frequent letters
        letter_frequencies = {}
        for char in ciphertext:
            if char.isalpha():
                char = char.lower() #insist on char being lower case
                if char in letter_frequencies: #count frequency of letters
                    letter_frequencies[char] += 1 
                else:
                    letter_frequencies[char] = 1
        if len(firstletter)!= 1 or not firstletter.isalpha(): #insist on one letter and alphabetic character
            raise ValueError("Invalid input: The first letter must be a single character and alphabetic.")
        if len(secondletter)!= 1 or not secondletter.isalpha(): #insist on one letter and alphabetic character
            raise ValueError("Invalid input: The second letter must be a single character and alphabetic.")
      
        if firstletter.isupper():#check if it is uppercase
                    firstletter = firstletter.lower()#make it lowercase
        
        if secondletter.isupper():#check if it is uppercase
                    secondletter = secondletter.lower()#make it lowercase
                    
        #Find the two most frequent letters in the ciphertext
        most_frequent_letters = sorted(letter_frequencies, key=letter_frequencies.get, reverse=True)[:2] #sort it so that it is in descending order, cut array into first 2 only
        
        #use respective functions to find a and b, imitated methods learnt in homework to find a and b, make a equation like (by subtracting initial two equations from each other) (15*a) mod 26 = 13 and solve for a, then after that find b by replacing in any of the two equations ex: 10 = (13 + b) mod 26
        a = find_a((alphabet.index(most_frequent_letters[0]) - alphabet.index(most_frequent_letters[1])),  (alphabet.index(firstletter) - alphabet.index(secondletter)), 26)
        if a is None: #possible that a does not exist, output an error message to guess using other letters
            return "Failed to find a valid multiplicative constant. Please try different values for the most frequent letters."
        b = find_b(alphabet.index(most_frequent_letters[0]), (a*alphabet.index(firstletter)), 26)
        
        plaintext = affine(ciphertext, a, b,"decrypt") #after guessing a and b, try and decrypt the ciphertext using them
        
        return f"Decrypted Text: {plaintext}, Key Values: a={a}, b={b}, Guessed key using '{firstletter}' and '{secondletter} as most frequent letters'" #output guess atempt


def top_brute_force(ciphertext):
    #list of common words that will be iterated from when counting the score of each decrypted message
    common_words = set(["the", "and", "to", "in", "of", "a", "is", "that", "it", "with", "as", "was", "for", "on", "be", "this", "you", "I", "are", "have", "from", "or", "not", "your", "but", "at", "by", "we", "he", "she", "they", "there", "an", "if", "when", "where", "why", "how", "which", "what", "who", "while", "since", "until", "before", "after", "because", "under", "over", "between", "among", "through", "above", "below", "next", "last", "first", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "may", "can", "will", "should", "would", "could", "now", "then", "here", "there", "up", "down", "out", "into", "about", "around", "throughout"])


    def calculate_score(text):
        words = text.lower().split() #make all words lower case and split them into an array to search from
        common_word_count = sum(1 for word in words if word in common_words) #count words in sentence using common_words as reference
        return common_word_count

    top_decryptions = [] #array to store all decryptions

    for a in range(26):
        a_inv = mod_inverse(a, 26) #find a inverse for all possible a
        if a_inv is None: #if a_inv is doesnt exist, try another value of a
            continue
        for b in range(26):
            decrypted_text = affine(ciphertext, a, b,"decrypt") #for said value of a, decrypt it using all possible b
            score = calculate_score(decrypted_text) #calculate the score of that
            top_decryptions.append((decrypted_text, score)) #save it in array previously made

    top_decryptions.sort(key=lambda x: x[1], reverse=True) #sort, placing highest score first
    top_decryptions = top_decryptions[:3] #take only first 3

    top_decryptions_results = [] #array to store output of code
    for i, (decryption, score) in enumerate(top_decryptions): #list them in a nice way
        result = {
            "Rank": i + 1,
            "Decryption": decryption,
            "Score": score
        }
        top_decryptions_results.append(result) #append to new array previously made

    return top_decryptions_results #output results

