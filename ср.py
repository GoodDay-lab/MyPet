# def F(n):
#     if n > 2:
#         return F(n-1) + G(n-2)
#     else:
#         return 1
#
#
# def G(n):
#     if n > 2:
#         return G(n-1) + F(n-2)
#     else:
#         return 1
# print(F(7))





# def F(n):
#     if n > 2:
#         return F(n-1) + G(n-2)
#     else:
#         return 1
#
#
# def G(n):
#     if n > 2:
#         return G(n-1) + F(n-2)
#     else:
#         return 1
# print(F(8))





# def F(n):
#     if n > 2:
#         return F(n-1) + G(n-2)
#     else:
#         return 1
#
#
# def G(n):
#     if n > 2:
#         return G(n-1) + F(n-2)
#     else:
#         return 1
# print(F(6))


# def F(n):
#      if n > 0:
#          G(n - 1)
#
#
# def G(n):
#     print("*")
#     if n > 1:
#         F(n - 2)
# print(F(11))

# def F(n):
#     if n > 0:
#           G(n - 1)
#
#
# def G(n):
#     print("*")
#     if n > 1:
#         F(n - 3)
# print(F(11))
#
#
# def F(n):
#     if n > 2:
#        return F(n-1)+ F(n-2)
#     else: return 1
# print(F(5))

# n = 3
# s = 0
# while n <= 26:
#     s += 6
#     n += 1
# print(s)

# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (x or not y) and not(w == z) and w == 1:
#                     print(x, y, z, w)


def f(n):
    string = ''
    while n > 0:
        string += str(n % 6)
        n //= 6
    return string


print(f(36 ** 8 + 6 ** 20 - 12).count('0'))

# lst = []
# for i in range(-10000, 10000):
#     s = i
#     s = (s - 21) // 10
#     n = 1
#     while s > 0:
#         n = n * 2
#         s = s - n
#     if n == 32:
#         lst.append(i)
# print(min(lst))


# def f(n):
#     if n == 1:
#         return 1
#     if n % 2 == 0:
#         return n + f(n - 1)
#     else:
#         return 2 * f(n - 2)
# print(f(24))

