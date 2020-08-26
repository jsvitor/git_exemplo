''' 
Entrada A entrada contém um único conjunto de testes, que deve ser lido do dispositivo de entrada padrão (normalmente o teclado). A entrada contém 2 linhas. A primeira linha contém um inteiro N (2 ≤ N ≤ 1.000). A segunda linha contém N - 1 inteiros numerados de 1 a N (sem repetições).
Entrada
3
3 1

Saída
2
Entrada: 4
2 4 3
Saída: 1
'''


def main():
    n = int(input('line 1: \n'))
    line_two = input('line 2: \n')
    if 2 <= n <= 1000:
        line_two = line_two.split(' ')
        if ((n - 1) == len(line_two)):
            for i in line_two:
                if not(i <= n):
                    return
        line_two += n

        return line_two


if __name__ == '__main__':
    print(main())
