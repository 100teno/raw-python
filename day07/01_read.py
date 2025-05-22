# %%

nome_arquivo = "historia.txt"

with open(nome_arquivo) as open_file:
    conteudo = open_file.read()

print(conteudo)

# abre o arquivo para leitura
# open_file = open(nome_arquivo)

# # exibe o conteúdo do arquivo
# conteudo = open_file.read()
# print(conteudo)

# # fechando o arquivo
# open_file.close()