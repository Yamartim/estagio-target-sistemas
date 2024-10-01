#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
#
#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

def main():
    with open('faturamento.json') as arquivo:
        vetor : list = json.load(arquivo)

    menor_faturamento = vetor[0]
    maior_faturamento = vetor[0]
    soma_faturamento = 0
    dias_acima_media = 0

    for dia in vetor:
        if dia > maior_faturamento:
            maior_faturamento = dia
        if dia < menor_faturamento:
            menor_faturamento = dia
        soma_faturamento += dia

    media_faturamento = soma_faturamento/len(vetor)
    
    for dia in vetor:
        if dia > media_faturamento:
            dias_acima_media+=1

    print('faturamento por dia:')
    print(vetor)
    print(f'maior faturamento do mes: {maior_faturamento}')
    print(f'menor faturamento do mes: {menor_faturamento}')
    print(f'dias com faturamento acima da média: {dias_acima_media}')


if __name__ == '__main__':
    main()