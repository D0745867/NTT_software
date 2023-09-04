import math


class Root:
    # def __init__(self, a, m):
    #   self.a = a
    #   self.m = m

    @staticmethod
    # N是幾個項次，P是模數
    # Wn = g ^ (p-1)/n modp
    def t_factor(root, N, P):
        factors = []
        wn = root ** ((P - 1) / N)
        for i in range(int(N/2)):
            pi = i * 2
            if pi == 0:
                w = 1
            else:
                w = (wn**pi) % P
                print(root, P-1, pi, w)
            factors.append(w)
        return factors

    @staticmethod
    def check_coprime(self, a, m):
        if math.gcd(a, m) == 1:
            return True
        else:
            return False

    def order(self, a, m):
        return True

    # totient function
    def totient(self, m):
        counter = 0
        list = []
        for i in range(m - 1):
            if math.gcd(i + 1, m) == 1:
                counter += 1
                list.append(i + 1)
        return counter, list

    def find_root(self, totient, m):
        roots = []
        for item in totient:
            toggle = 0
            for i in range(2, len(totient)):
                # print(str(item) + "^" + str(i) + "%" + str(m) + "=" + str((item ** i) % m))
                if (item ** i) % m == 1:
                    toggle = 1
                    break
            if not toggle:
                roots.append(item)
        print("Roots:" + str(roots))
        return roots, roots[0]


a = Root()

# is_coprime = a.check_coprime(2, 4)
# print(is_coprime) # False
_, totient = a.totient(7)
roots, st_root = a.find_root(totient, len(totient) + 1)
print(a.t_factor(3, 8, 17))
