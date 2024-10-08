#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
#
#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json, xml.etree.ElementTree as ET

def main():

    with open('dados.json') as arquivo:
        dados_json : list = json.load(arquivo)

    #foram adicionadas tags para corrigir o arquivo original
    dados_xml = ET.parse('dados2.xml')

    valores_json = [i['valor'] for i in dados_json]
    valores_xml = [float(i.text) for i in dados_xml.getroot().iter('valor')]

    print('JSON')
    processar_valores(valores_json)
    print('\nXML')
    processar_valores(valores_xml)

    #print(valores_json)
    #print(valores_xml)


def processar_valores(valores : list[int]):
    menor_faturamento = valores[0]
    maior_faturamento = valores[0]
    soma_faturamento = 0
    dias_acima_media = 0
    dias_sem_faturamento = 0


    for dia in valores:
        if dia == 0:
            dias_sem_faturamento += 1
        elif dia > maior_faturamento:
            maior_faturamento = dia
        elif dia < menor_faturamento:
            menor_faturamento = dia

        soma_faturamento += dia


    media_faturamento = soma_faturamento/(len(valores) - dias_sem_faturamento)
    
    for dia in valores:
        if dia > media_faturamento:
            dias_acima_media+=1

    print('faturamento por dia ------------------------------')
    print(f'maior faturamento do mes: {maior_faturamento}')
    print(f'menor faturamento do mes: {menor_faturamento}')
    print(f'dias com faturamento acima da média: {dias_acima_media}')


if __name__ == '__main__':
    main()