print()
print('Texto explicativo')

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '6',
        },
        'resposta_certa': 'b'
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3x2? ',
        'respostas': {
            'a': '4',
            'b': '101',
            'c': '6',
        },
        'resposta_certa': 'c'
    },
}
print()

respostas_certas = 0
for pergunta, dados_pergunta in perguntas.items():
    print(f'{pergunta}:{dados_pergunta["pergunta"]}')

    print('Respostas: ')
    for resposta, dados_resposta in dados_pergunta['respostas'].items():
        print(f'[{resposta}]: {dados_resposta}')

    resposta_utilizador = input('Sua resposta: ')

    if resposta_utilizador == dados_pergunta['resposta_certa']:
        print('Acertou!')
        respostas_certas += 1
    else:
        print('Errou!')

    print()

quantidade_perguntas = len(perguntas)
percentagem_certas = respostas_certas / quantidade_perguntas * 100
print(f'Acertou {respostas_certas} respostas.')
print(f'A sua percentagem foi {percentagem_certas}%.')