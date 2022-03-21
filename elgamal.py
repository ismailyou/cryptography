def is_generator(g, p):
    l = []
    for i in range(1, p):
        l.append(pow(g, i) % p)
    l.sort()
    return l

def get_private_key(p, g, a):
    return p, g, get_A(a, g, p)

def get_A(a, g, p):
    return pow(g, a) % p


def encrypt(message,p, g, A, k):
    c1 = pow(g, k) % p
    c2 = message * pow(A,k) % p
    return c1, c2

def decrypt(c1, c2, a, p):

    d = calcule_modulo(c1, a, p)
    iverce_d = get_inv_modulo(d, p)

    return (c2 *  iverce_d) % p

def calcule_modulo(n, ex, mod):
    return pow(n, ex) % mod

def get_inv_modulo(p, mod):
    a, b, c, d = mod, p, 1, 0
    while b != 1:
        temp_a, temp_b, temp_c, temp_d = a, b, c, d

        a = b
        b = temp_a % b
        c = (temp_d - temp_c * (temp_a // temp_b)) % mod
        d = temp_c

    return abs(c)


if __name__ == '__main__':

    # is g a generator ?
    print(is_generator(2, 13))

    #Crypte
    g = 2
    p = 13
    m = 7
    k = 5
    a = 3

    cle_pub = a
    cle_priv = get_private_key(p= p, g= g, a= a)

    print("clé public : ", cle_pub)
    print("clé privé : ", cle_priv)

    #Cryptage :

    A = get_A(a=a, g=g, p=p)
    c = encrypt(message=m, p=p, g=g, A=A, k=k)

    print("c : ", c)

    #Decryptage:
    c1, c2 = c
    m = decrypt(c1, c2, a, p)
    print("message : ", m)

    print("--------------------------------------")
    a = 12
    g = 2
    p = 41
    m = 32
    k = 18

    cle_pub = a
    cle_priv = get_private_key(p= p, g= 2, a= a)

    print("clé public : ", cle_pub)
    print("clé privé : ", cle_priv)

    # Cryptage :
    print("message clair: ", m)
    A = get_A(a= 12, g= 2, p= 41)

    c = encrypt(message= m, p= p, g= g, A= A, k= k)
    print("message Chiffrée : ", c)

    # Decryptage :
    c1, c2 = c
    m = decrypt(c1= c1, c2= c2, a= a, p= p)
    print("message clair: ", m)