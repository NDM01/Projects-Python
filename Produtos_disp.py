print()

lista = {
    'l1': {
        'tipo': 'Carne',
        'disponivel': {
            'a': 'Carne de Vaca',
            'b': 'Carne Picada',
            'c': 'Frango',
            'd': 'Bife',
        },
    },
    'l2': {
        'tipo': 'Peixe',
        'disponivel': {
            'a': 'Dourada',
            'b': 'Salmão',
            'c': 'Bacalhau',
            'd': 'Frango',
        },
    },
    'l3': {
        'tipo': 'Bolachas',
        'disponivel': {
           'a': 'Oreo',
           'b': 'Bolacha Maria',
           'c': 'Filipinos',
           'd': 'Bolacha de água e sal',
        },
    },
    'l4': {
        'tipo': 'Sumos',
        'disponivel': {
           'a': 'Água',
           'b': 'Sumol de laranja',
           'c': 'Coca-Cola',
           'd': 'Ice-Tea manga',
        },
    },
}

print()

for tipo, gen in lista.items():
    print(f'{gen["tipo"]}:') 

    for resposta, dados_resposta in gen['disponivel'].items():
        print(f'{dados_resposta}')

    print()

    