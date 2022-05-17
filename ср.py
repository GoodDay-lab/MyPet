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


def F(n):
    if n > 2:
       return F(n-1)+ F(n-2)
    else: return 1
print(F(5))