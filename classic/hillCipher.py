def matrix_modulo(A,m):
    """
    Apply modulo m operation to each element in the matrix A.

    Args:
    - A (list of lists): Input matrix.
    - m (int): Modulo value.

    Returns:
    - list of lists: Modified matrix with each element modulo m.
    """
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] = A[i][j] %m
    return A

def extendedEuclid(a, m):
    """
    Perform the Extended Euclidean Algorithm to find the modular inverse of a modulo m.

    Args:
    - a (int): Number to find the inverse of.
    - m (int): Modulo value.

    Returns:
    - int or None: Modular inverse of a modulo m or None if not found.
    """
    A2 = 0
    A3 = m
    B2 = 1
    B3 = a
    while B3 != 1 and B3 != 0:
        Q = A3 // B3
        (A2, A3, B2, B3) = (B2, B3, A2 - Q * B2, A3 - Q * B3)  
    if B3 == 1:
        return B2%m
    else:
        return None

def letter_to_number(s):
    """
    Convert a letter to its corresponding number representation.

    Args:
    - s (str): Input letter.

    Returns:
    - int: Corresponding numerical value.
    """
    if 'a' <= s <= "z":
        return ord(s) - ord('a') + 26
    else:
        return ord(s) - ord('A')
    
def number_to_letter(x):
    """
    Convert a numerical value to its corresponding letter representation.

    Args:
    - x (int): Input numerical value.

    Returns:
    - str: Corresponding letter.
    """
    if x < 26:
        return chr(x + ord('A'))
    else:
        return chr(x - 26 + ord('a'))

def matrix_multiply(A, B):
    """
    Perform matrix multiplication between matrices A and B.

    Args:
    - A (list of lists): First matrix.
    - B (list of lists): Second matrix.

    Returns:
    - list of lists: Resultant matrix after multiplication.
    """
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                result[i][j] += A[i][k] * B[k][j]

    return result

def inverseMatrix2(matrix):
    """
    Calculate the inverse of a 2x2 matrix modulo 26.

    Args:
    - matrix (list of lists): Input 2x2 matrix.

    Returns:
    - list of lists or None: Inverse of the input matrix or None if the matrix is not invertible.
    """
    a, b = matrix[0][0], matrix[0][1]
    c, d = matrix[1][0], matrix[1][1]
    
    determinant = a * d - b * c
    if determinant == 0:
        return None
    inv_det = extendedEuclid(int(determinant%26), 26)

    if inv_det == None:
        return None
    inverse = [[inv_det*d, inv_det*-b],[inv_det*-c, inv_det*a]]
    
    return inverse

def inverseMatrix3(matrix):
    """
    Calculate the inverse of a 3x3 matrix modulo 26.

    Args:
    - matrix (list of lists): Input 3x3 matrix.

    Returns:
    - list of lists or None: Inverse of the input matrix or None if the matrix is not invertible.
    """
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]

    determinant = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    if determinant == 0:
        return None
    inv_det = extendedEuclid(int(determinant%26), 26)

    if inv_det ==None:
        return None
    
    adjugate = [
        [(e * i - f * h), -(b * i - c * h), (b * f - c * e)],
        [-(d * i - f * g), (a * i - c * g), -(a * f - c * d)],
        [(d * h - e * g), -(a * h - b * g), (a * e - b * d)]
    ]

    inverse = [[adjugate[r][c]*inv_det for c in range(3)] for r in range(3)]

    return inverse

def hill_Encrypt(p,K,n):
    """
    Encrypt plaintext using the Hill cipher algorithm.

    Args:
    - p (str): Input plaintext.
    - K (list of lists): Encryption key matrix.
    - n (int): Size of the key matrix.

    Returns:
    - str: Encrypted ciphertext.
    """
    # remove all spaces, commas, unknown characters...
    t = ''
    for i in range(len(p)):
        if 97<=ord(p[i])<=122 or 65 <=ord(p[i])<=90:
            t = t+p[i]

    if len(t)%int(n) != 0:
        t = t + (int(n)-(len(t)%int(n)))*"Z" 
        
    
    # compute results
    c = ""
    i = 0
    while i < len(t):  
        P = [[letter_to_number(t[_])] for _ in range(i, i+len(K))]
        C = matrix_multiply(K, P)
        C = matrix_modulo(C, 26)
        for j in range(len(C)):
                c+= number_to_letter(C[j][0])
        i+= len(K)
    
    # re-add unknown characters...
    for i in range(len(p)):
        if 97<=ord(p[i])<=122 or 65 <=ord(p[i])<=90:
            if p[i].islower():
                c = c[:i] + c[i].lower() + c[i+1:]
        else:
            c = c[:i] + p[i] + c[i:]
    
    return c

def hill_Decrypt(c,k,n):
    """
    Decrypt ciphertext using the Hill cipher algorithm.

    Args:
    - c (str): Input ciphertext.
    - k (list of lists): Decryption key matrix.
    - n (int): Size of the key matrix.

    Returns:
    - str: Decrypted plaintext or a message indicating the matrix is not invertible.
    """
    if int(n) == 2:
        inv_key = inverseMatrix2(k)
    else:
        inv_key = inverseMatrix3(k)
    if inv_key == None:
        return "Matrix is not invertible!"
    
    return hill_Encrypt(c,inv_key,n)

def hill(t,k,n,mode):
    """
    Encrypts or decrypts text using the Hill cipher algorithm based on the mode specified.

    Args:
    - t (str): Input text (plaintext or ciphertext).
    - k (list of lists): Encryption or decryption key matrix.
    - n (int): Size of the key matrix.
    - mode (str): Specifies whether to 'encrypt' or 'decrypt'.

    Returns:
    - str or tuple: Encrypted ciphertext or decrypted plaintext. If encryption was performed, it also returns the inverse matrix.
    """
    if mode.lower() =="encrypt":
        if n == 2:
            return hill_Encrypt(t,k,n),inverseMatrix2(k)
        else:
            return hill_Encrypt(t,k,n),inverseMatrix3(k)
    elif mode.lower() =="decrypt":
        if n == 2:
            return hill_Decrypt(t,k,n),inverseMatrix2(k)
        else:
            return hill_Decrypt(t,k,n),inverseMatrix3(k)