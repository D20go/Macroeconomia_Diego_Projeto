def comparacao ( minha_idade, idade_STEM, nome_1, nome_2):
    if (minha_idade) < (idade_STEM):
        print(f" Olá {nome_1}, você é mais novo do que a {nome_2}")
    elif(minha_idade) == (idade_STEM):
        print(f"Olá{nome_1}, vocês possuem a mesma idade")
    else:
        print(f" Você {nome_1}, és mais velho do que a {nome_2}")

comparacao(28, 104, "Diego", "Maria Laura Mouzinho")

print(" " * 30)
def localidade (pais_1, pais_2):
    if (pais_1) != (pais_2):
        print(f" Vocês nasceram em países diferentes")
    else:
        print(f" Uaaaaaaaaaaaaaaal!! Vocês são brasileiros! ")

localidade ("Brasil", "Brasil")
print("" * 30)

def cidade_natal (cidade_1, cidade_2, nome_1, nome_2):
    if ( cidade_1 ) != ( cidade_2 ):
        print(f" Olá {nome_1}, você é paulista e a {nome_2} é pernambucana!")
    else:
        print(f" Poxa, que legal! Vocês nasceram na mesma cidade!!")

cidade_natal("São Paulo", "Pernambuco", "Diego", " Maria Laura Moutinho")