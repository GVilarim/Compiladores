# Letra D - Forma Normal de Greibach

# Definição das produções iniciais
producoes = {
    "S": ['AB', 'CSB'],
    "A": ['aB', 'C'],
    "B": ['bbB', 'b']
}

# Cria as renomeações
def create_renames(producoes):
    renames = {}
    count = 1
    for p in producoes.keys():
        renames[p] = f'A{count}'
        count += 1
    return renames


# Função para imprimir as produções
def print_out(producoes):
    for key in producoes.keys():
        print(f'{key} -> ', end='')
        for item in producoes[key]:
            if producoes[key].index(item) == len(producoes[key]) - 1:
                print(f' {item} ', end='')
            else:
                print(f' {item} ', end='|')
        print()

# Imprime as produções originais
print_out(producoes)
print()

# Dicionário para armazenar as renomeações
renames = create_renames(producoes)

# Aplica as renomeações nas produções
for p in producoes.keys():
    for pos, item in enumerate(producoes[p]):
        for i in item:
            # Verifica se é uma variavel e não está presente nas produções
            if i.isupper() and i not in producoes.keys():
                # Remove a produção caso alguma variável se não esteja presente nas produções
                producoes[p].remove(item)
                break
            if i.isupper():
                # Realiza a renomeação
                word = producoes[p][pos].replace(i, renames[i])
                producoes[p][pos] = word
    producoes[renames[p]] = producoes.pop(p, "")

# Realiza a expansão das produções
for p in producoes.keys():
    for item in producoes[p]:
        if item.isupper() and item[:2] in producoes.keys():
            for c in producoes[item[:2]]:
                # Cria uma nova produção combinando substituindo pela regra variavel -> terminal+variavel
                producao = f'{c}{item[2:]}'
                # Remove a produção original e adiciona a nova produção
                producoes[p].remove(item)
                producoes[p].append(producao)

# Imprime as produções após as transformações
print_out(producoes)
