#4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#• SP – R$67.836,43
#• RJ – R$36.678,66
#• MG – R$29.229,88
#• ES – R$27.165,48
#• Outros – R$19.849,53
#
#Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  

def main():
    faturamento_sp = 67836.43
    faturamento_rj = 36678.66
    faturamento_mg = 29229.88
    faturamento_es = 27165.48
    faturamento_outros = 19849.53

    fat_total = faturamento_sp + faturamento_rj + faturamento_mg + faturamento_es + faturamento_outros

    print(f'Porcentagem SP:', obterPorcentagem(faturamento_sp, fat_total))
    print(f'Porcentagem RJ:', obterPorcentagem(faturamento_rj, fat_total))
    print(f'Porcentagem MG:', obterPorcentagem(faturamento_mg, fat_total))
    print(f'Porcentagem ES:', obterPorcentagem(faturamento_es, fat_total))
    print(f'Porcentagem outros:', obterPorcentagem(faturamento_outros, fat_total))

def obterPorcentagem(n1, n2):
    return f'{100*n1/n2:.2f}%'

if __name__ == '__main__':
    main()