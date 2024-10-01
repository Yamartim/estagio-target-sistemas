#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
#IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;


def main():
    entrada = abs(int(input('informe o número: ')))
    print('calculando sequencia de fibonacci...')

    sequencia = [0, 1]
    while sequencia[-1] < entrada:
        sequencia.append(sequencia[-1] + sequencia[-2])

    print(sequencia)

    if entrada in sequencia:
        print(f'o número {entrada} está na sequência de fibonacci')
    else:
        print(f'o número {entrada} não está na sequência de fibonacci')

if __name__ == '__main__':
    main()