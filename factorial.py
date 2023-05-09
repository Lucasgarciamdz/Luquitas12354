# define a factorial fuction
def factorial_pro(m):
    if m == 0:
        return 1
    else:
        return m * factorial_pro(m-1)
