# %%

A = 1
B = 2

print(A)
print(B)
# %%
# Unpacking variables

C = A 
A = B
B = C
print(A)
print(B)
# %%

A, B = B, A  # Unpacking variables
print(A)
print(B)

# %%
a,b, *resto = [1, 2, 3, 4, 5, 6]
print(a, b, resto)

# %%

def soma (a, *args):
    total = a + sum(args)
    return total

soma (1, 10, 30)

# %%
def soma2(a, b, c, d):
    return a+b+c+d

values = [3, 4, 5, 6]
soma2(*values) # Unpacking a list into function arguments

# %%
dados = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

for i, j in dados.items():
    print(i, j)
