palavra_exemplo = "lgica"


def insere_letras(fatias):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
    for E, D in fatias:
        for letra in letras:
            novas_palavras.append(E + letra + D)
        return novas_palavras


def gerador_palavras(palavra):
    fatias = []
    for i in range(len(palavra)+1):
        fatias.append((palavra[:i], palavra[i:]))
    palavras_geradas = insere_letras(fatias)
    return palavras_geradas


palavras_geradas = gerador_palavras(palavra_exemplo)
print(palavras_geradas)


def corretor(palavra):
    palavras_geradas = gerador_palavras(palavra)
    palavra_correta = max(palavras_geradas, key=probabilidade)
    return palavra_correta

def gen_test(archive):
 lista_palavras_teste = []
 f = open(archive, "r")
 for linha in f:
    correta, errada = linha.split()
    lista_palavras_teste.append((correta, errada))
 f.close()
 return lista_palavras_teste

def avaliador(testes, vocabulario):
    numero_palavras = len(testes)
    acertou = 0
    desconhecida = 0
    for correta, errada in testes:
        palavra_corrigida = corretor(errada)
        if palavra_corrigida == correta:
            acertou += 1
        else:
            desconhecida += (correta not in vocabulario)
    taxa_acerto = round(acertou*100/numero_palavras, 2)
    taxa_desconhecida = round(desconhecida*100/numero_palavras, 2)
    print(f"{taxa_acerto}% de {numero_palavras} palavras, desconhecidas é {taxa_desconhecida}%")

def deletando_caracteres(fatias):
    novas_palavras = []
    for E, D in fatias:
        novas_palavras.append(E + D[1:])
    return novas_palavras

def insere_letras(fatias):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
    for E, D in fatias:
        for letra in letras:
            novas_palavras.append(E + letra + D)
    return novas_palavras

def deletando_caracteres(fatias):
    novas_palavras = []
    for E, D in fatias:
        novas_palavras.append(E + D[1:])
    return novas_palavras

def troca_letra(fatias):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzáàãâéèêíìóòõôúùûç'
    for E, D in fatias:
        for letra in letras:
            novas_palavras.append(E + letra + D[1:])
    return novas_palavras

def gerador_palavras(palavra):
    fatias = []
    for i in range(len(palavra)+1):
        fatias.append((palavra[:i],palavra[i:]))
    palavras_geradas = insere_letras(fatias)
    palavras_geradas += deletando_caracteres(fatias)
    palavras_geradas += troca_letra(fatias)
    return palavras_geradas

def insere_letras(fatias):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
    for E, D in fatias:
        for letra in letras:
            novas_palavras.append(E + letra + D)
    return novas_palavras

def deletando_caracteres(fatias):
    novas_palavras = []
    for E, D in fatias:
        novas_palavras.append(E + D[1:])
    return novas_palavras

def troca_letra(fatias):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzáàãâéèêíìóòõôúùûç'
    for E, D in fatias:
        for letra in letras:
            novas_palavras.append(E + letra + D[1:])
    return novas_palavras

def inverte_letra(fatias):
    novas_palavras = []
    for E, D in fatias:
        novas_palavras.append(E + D[1] + D[0] + D[2:])
    return novas_palavras

def gerador_palavras(palavra):
    fatias = []
    for i in range(len(palavra)+1):
        fatias.append((palavra[:i],palavra[i:]))
    palavras_geradas = insere_letras(fatias)
    palavras_geradas += deletando_caracteres(fatias)
    palavras_geradas += troca_letra(fatias)
    return palavras_geradas




def novo_corretor(palavra):
    palavras_geradas = gerador_palavras(palavra)
    palavra_correta = max(palavras_geradas, key=probabilidade)
    return palavra_correta
