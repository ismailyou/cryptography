class Knapsack:
    """is a list LSC"""

    def is_lsc(self, lsc: list):
        s = lsc[0]
        for i in range(1, len(lsc)):
            if s > lsc[i]:
                return False
            s += lsc[i]
        return True

    def get_message(self, A: list, c: int):
        m = []
        for ai in reversed(A):
            if c >= ai:
                m.insert(0, 1)
                c = c - ai
            else:
                m.insert(0, 0)

        return m

    def get_b(self, A: list, p: int, u: int):
        b = []
        for ai in A:
            b.append((p * ai) % u)

        return b

    def get_c_prim(self, c: int, p: int, u: int):
        p_moin = self.get_inverse_p(p, u)
        return (c * p_moin) % u

    def get_a_from_b(self, B: list, p: int, u: int):
        A = []
        p_moin = self.get_inverse_p(p, u)
        for bi in B:
            A.append((p_moin * bi) % u)
        return A

    def get_phi(self, x: int, p: int, u: int):
        return (x * p) % u

    def get_phi_moin(self, x: int, p: int, u: int):
        p_moin = self.get_inverse_p(p, u)
        return (x * p_moin) % u

    def get_c(self, m: list, lc: list, u: int):
        c = 0
        for i, x in enumerate(m):
            c += x * lc[i]
        return c % u

    def get_inverse_p(self, p: int, mod: int):
        a, b, c, d = mod, p, 1, 0
        while b != 1:
            temp_a, temp_b, temp_c, temp_d = a, b, c, d

            a = b
            b = temp_a % b
            c = (temp_d - temp_c * (temp_a // temp_b)) % mod
            d = temp_c

        return abs(c)


if __name__ == '__main__':
    k = Knapsack()

    print("--------------Example 1-----------------")

    c = 149
    p = 16
    u = 201
    A = [7, 11, 22, 47, 91]

    print("A = ", A)

    # 1 calcule c'
    c_prim = k.get_c_prim(c, p, u)

    print("c' = ", c_prim)

    # 2 decrypt
    m = k.get_message(A, c_prim)

    print("message = ", m)

    # 3 verification

    B = k.get_b(A, p, u)

    print("B : ", B)
    print("C : ", k.get_c(m, B, u))

    print("------------Example 2-------------------")
    c = 161
    p = 16
    u = 201
    A = [7, 11, 22, 47, 91]
    print("A = ", A)

    # 1 calcule c'
    c_prim = k.get_c_prim(c, p, u)

    print("c' = ", c_prim)

    # 2 decrypt

    m = k.get_message(A, c_prim)
    print("message = ", m)

    # 3 verification

    B = k.get_b(A, p, u)

    print("B : ", B)
    print("C : ", k.get_c(m, B, u))

    print("------------Example 3-------------------")

    c = 69
    p = 31
    u = 105
    B = [62, 93, 81, 88, 102, 37]
    print("inv(p) : ", k.get_inverse_p(p, u))

    # 1 Trouver M apartir de C
    A = k.get_a_from_b(B, p, u)
    print("A = ", A)

    c_prim = k.get_c_prim(c, p, u)
    m = k.get_message(A, c_prim)
    print("M : ", m)

    # 2 Verification
    c = k.get_c(m, B, u)
    print("C: ", c)
