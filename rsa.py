def pgcd(a: int, b: int):
    if a < b:
        t = a
        a, b = b, t

    while b != 0:
        a, b = b, a % b
    return a


def look_for_e(phi: int):
    l = []
    for i in range(2, phi - 1):
        a = pgcd(i, phi)
        if a == 1:
            l.append(i)
    return l


def look_for_d(e: int, phi: int):
    l = []
    for i in range(2, phi):
        a = pgcd(e * i, phi)
        if a == 1:
            l.append(i)
    return l


def encrypt(message: int, public_key: int, n: int):
    return pow(int(message), int(public_key)) % int(n)


def decrypt(message: int, private_key: int, n: int):
    return pow(int(message), int(private_key)) % int(n)


def calcule_modulo(n: int, ex: int, mod: int):
    return pow(n, ex) % mod


def euclide_etendu(r: int, m: int):
    a, b, c, d = m, r, 1, 0
    while b != 1:
        temp_a, temp_b, temp_c, temp_d = a, b, c, d

        a = b
        b = temp_a % b
        c = (temp_d - temp_c * (temp_a // temp_b)) % m
        d = temp_c

    return abs(c)


def is_prime_number(a: int):
    if a == 2:
        return True
    elif a < 2 or a % 2 == 0:
        return False
    for x in range(2, a):
        if a % x == 0:
            return False
    return True

def searching_q_and_p(n: int):
    primes = get_prime_number(1, n)
    for i, x in enumerate(primes):
        for j, y in enumerate(primes):
            if i != j:
                if x * y == n:
                    return x, y


def calculate_phi(p: int, q: int):
    return (p - 1) * (q - 1)


def search_for_private_key(e: int, n: int):
    p, q = searching_q_and_p(n)
    phi = calculate_phi(p, q)
    print("p et q :", p, q)
    print("phi :", phi)
    print("e :", e)
    d = euclide_etendu(e, phi)
    print("d ", d)
    return d

def get_prime_number(start: int, end: int):
    prime_list = []
    for n in range(start, end):
        is_prime = is_prime_number(n)
        if is_prime:
            prime_list.append(n)

    return prime_list

if __name__ == '__main__':

    e = 79
    d = 1019
    m = 688
    n = 3337

    # Chiffrement
    C = encrypt(m, e, n)
    print("m : ", m)
    print("C = ", C)
    
    # Chiffrement
    M = decrypt(C, d, n)
    print("m : ", M)

    #Calculate modulo:
    # n ^ ex mod(mod)
    mod = calcule_modulo(n=32, ex=13, mod=257)
    print("modulo : ", mod)

    # Calculate pgcd:
    print("pgcd ", pgcd(12345, 17))

    # Calculate modulo:
    #   r ^ -1 mod(m)
    print("inverse modulo : ",euclide_etendu(r= 5, m= 13))
    print("inverse modulo : ",euclide_etendu(r= 7, m= 22))

    # search for private from e and n
    d = search_for_private_key(e = 11, n = 319)

    # search for private from e and n
    d = search_for_private_key(3, 55)
