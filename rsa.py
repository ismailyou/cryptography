def pgcd(a, b):
    if a < b:
        t = a
        a, b = b, t

    while b != 0:
        a, b = b, a % b
    return a


def look_for_e(phi):
    l = []
    for i in range(2, phi - 1):
        a = pgcd(i, phi)
        if a == 1:
            l.append(i)
    return l


def look_for_d(e, phi):
    l = []
    for i in range(2, phi):
        a = pgcd(e * i, phi)
        if a == 1:
            l.append(i)
    return l


def E(message, public_key, n):
    return pow(int(message), int(public_key)) % int(n)


def D(message, private_key, n):
    return pow(int(message), int(private_key)) % int(n)


def calcule_modulo(n, ex, mod):
    return pow(n, ex) % mod


def euclide_etendu(r, m):
    a, b, c, d = m, r, 1, 0
    while b != 1:
        temp_a, temp_b, temp_c, temp_d = a, b, c, d

        a = b
        b = temp_a % b
        c = (temp_d - temp_c * (temp_a // temp_b)) % m
        d = temp_c

    return abs(c)


def is_prime_number(a):
    if a == 2:
        return True
    elif a < 2 or a % 2 == 0:
        return False
    for x in range(2, a):
        if a % x == 0:
            return False
    return True


def get_prime_number(start, end):
    prime_list = []
    for n in range(start, end):
        is_prime = is_prime_number(n)
        if is_prime:
            prime_list.append(n)

    return prime_list


def searching_q_and_p(n):
    primes = get_prime_number(1, n)
    for i, x in enumerate(primes):
        for j, y in enumerate(primes):
            if i != j:
                if x * y == n:
                    return x, y


def calculate_phi(p, q):
    return (p - 1) * (q - 1)


def search_for_private_key(e, n):
    p, q = searching_q_and_p(n)
    phi = calculate_phi(p, q)
    print("p et q :", p, q)
    print("phi :", phi)
    print("e :", e)
    d = euclide_etendu(e, phi)
    print("d ", d)


if __name__ == '__main__':
    # phi = 24
    # e = look_for_e(phi)
    #
    # for x in e[0:1]:
    #     d = look_for_d(x, phi)
    #
    # print("e : ", e)
    # print("d : ", d)
    #
    # print("-------------")
    #
    # e = e[0]
    # d = d[0]
    # m = 5
    # n = 35
    #
    # e = 79
    # d = 1019
    # m = 688
    # n = 3337
    # C = E(m, e, n)
    #
    # print("encrypt ", m, " = ", C)
    #
    # M = D(C, d, n)
    # print("decrypt ", C, " = ", M)
    #
    #print(calcule_modulo(32, 13,  257))
    # print(calcule_modulo(5, 11, 14))
    # print(calcule_modulo(17, 154, 100))
    #print(pgcd(12345, 17))
    # print(pgcd(105, 45))
    #
    #
    # print(euclide_etendu(5, 13))
    # print(euclide_etendu(7, 22))

    #search_for_private_key(11, 319)

    # search_for_private_key(3, 55)
    #print(E(3, 37, 731))
    #
    # print(D(12, 7, 33))
    #
    #print(E(33, 7, 55))
    #print(D(22, 7, 55))
    # print(E(23, 27, 55))
    #
    #search_for_private_key(3, 55)

    #print(E(40, 3, 55))

    #print(D(35, 27, 55))

    print(pgcd(105, 45))
