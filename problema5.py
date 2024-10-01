#5) Escreva um programa que inverta os caracteres de um string.
#
#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

def main():
    entrada = input('informe uma string para reverter: ')
    print('revertendo string...')

    string_revertida = ''

    i = len(entrada)-1
    while i >= 0:
        string_revertida += entrada[i]
        i-=1

    print(string_revertida)
    

if __name__ == '__main__':
    main()