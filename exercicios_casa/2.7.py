#Solicite ao usuário o nome de uma fruta e exiba o preço correspondente
# %%
import unicodedata

def remove_acento(texto):
    # Remove acentos de letras
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

# Dicionario original com acentos
frutas = {
    "Maçã"      :  "R$1.50",
    "Banana"    :  "R$2.75",
    "Uva"       :  "R$1.90",
    "Pera"      :  "R$1.25",
    "Laranja"   :  "R$0.65",
    "Limão"     :  "R$1.25",
    "Goiaba"    :  "R$2.15",
    "Abacaxi"   :  "R$3.20",
    "Melancia"  :  "R$5.80"
}

# Criar um dicionário auxiliar que mapeia as frutas sem acento (minúsculas)
# para a chave original
lookup = { remove_acento(chave).lower(): chave for chave in frutas.keys() }

# Exibe a lista de frutas para o usuário
for chave, valor in frutas.items():
    print(f"{chave} -> {valor}")
# Solicita ao usuário o nome da fruta
entrada = input("Digite o nome da fruta: ")
# Remove acentos e converte para minúsculas
entrada_normalizada = remove_acento(entrada).lower()
# Busca a fruta no dicionário
if entrada_normalizada in lookup:
    # Se encontrado, obtém o nome original da fruta
    fruta_original = lookup[entrada_normalizada]
    print(f"O preço da {fruta_original} é {frutas[fruta_original]}")
else:
    print("Fruta não encontrada na lista.")
# %%