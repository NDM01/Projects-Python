print('Carros e motas disponíveis para venda')
print()



lista = {
    'l1': {
        'tipo': 'Carro',
        'disponivel': {
            'Fiat 500' : ' 12 000€',
            'Nissan gtr r34' : ' 74 000€',
            'Toyota Supra' : ' 50 000€',
            'Mercedes-Benz class S400': ' 100 000€',
            'Tesla model S P100D': ' 120 000€',
        },
    },
    'l2': {
        'tipo': 'Mota',
        'disponivel': {
            'Honda CB650R' : ' 9000€',
            'KTM SuperDuke R' : ' 14 000€',
            'Yamaha virago 250' : ' 2500€',
            'Yamaha R1000' : ' 10 000€',
            'Ducati Panigale V4S' : ' 20 000€',
            'Kawasaki Ninja H2R' : ' 90 000€',
        },
    },
    
}

for tipo, gen in lista.items():
    print(f'{gen["tipo"]}:') 

    for resposta, dados_resposta in gen['disponivel'].items():
        print(f'{resposta}:{dados_resposta}')
    print()

