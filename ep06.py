# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------

'''
    Nome:Emanuel Hakr Maciel
    NUSP: 11221380

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

    Abaixo descreva qualquer ajuda que você recebeu para fazer este
    EP.  Inclua qualquer ajuda recebida por pessoas (inclusive
    monitores e colegas). Com exceção de material de MAC0110, caso
    você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

'''

##################################################################
def main():
    '''(None) -> None

    Coloque sua solução individual abaixo, seguindo o enunciado do
    exercício disponível na página da disciplina.

    Siga as instruções para entrega disponíveis em:
    https://paca.ime.usp.br/mod/page/view.php?id=42515
    '''
    # escreva o corpo da função main() a seguir
    n = int(input("Digite N: "))
    a = int(input("Digite dígito para A: "))
    e = input(("Digite dígito para E: "))
    i = 0
    m = True
    while n > i:
        x = float(input("Digite x: "))
        y = float(input("Digite y: "))
        m = acertou_tiro(x,y)
        if m:
            print("    Acertou")
            if i == 0:
                j = str(a)
            else:
                j += str(a)
        else:
            print("    Errou")
            if i == 0:
                j = str(e)
            else:
                j += str(e)
        i += 1
    
    print("Código: ",j)
        
    # cuidado com a tabulação
    
##################################################################
def acertou_tiro(x, y):
    '''(float ou int, float ou int) -> bool

    Veja a descrição e exemplos dessa função no enunciado. Depois disso,
    remova esses comentários e coloque aqui uma descrição sua 
    sobre o que faz essa função.
    '''
    # escreva o corpo de sua função acertou_tiro() a seguir
    m = True
    if -4.0 <= x <= -1.0 and 10.0 < y <= 12.0:
        m = True
    else:
        m = False
        if 1.0 <= x <= 6.0 and 10.0 < y <= 12.0:
            m = True
        elif -0.5 <= x <= 0.5 and 9.5 <= y < 10.5:
            m = True
        elif -1.0 <= x <= 1.0 and 11.0 < y < 12.0:
            m = True
        elif -2.0 < x <= -1.0 and 8.0 < y < 10.0:
            m = True
        elif 1.0 <= x < 2.0 and 9.0 < y < 10.0:
            m = True
        elif 1.0 <= x < 2.0 and 10.0 < y < 9.0:
            m = True
        elif x == 1.0 and 9.0 < y < 11.0:
            m = True
        elif x == -1.0 and 9.0 < y < 11.0:
            m = True
        elif -1.0 <= x <= 1.0 and y == 11.0:
            m = True
        elif -1.0 <= x <= 1.0 and 8.0 < y < 9.0:
            m = True
        elif 6.0 <= y <= 8.0  and -4.0 <= x <= -2.0  and x + y <= 4.0:
            m = True
        elif 4.0 <= y <= 6.0  and -2.0 <= x <= 0.0  and x + y <= 4.0:
            m = True
        elif 4.0 <= y <= 6.0  and 0.0 <= x <= 2.0  and -y + x <= 4.0:
            m = True
        elif 6.0 <= y <= 4.0  and 0.0 <= x <= 2.0  and -y + x <= 4.0:
            m = True
        elif 2.0 < y < 4.0  and -4.0 < x < -2.0  and x + y  < 0.0:
            m = True
        elif 0.0 < y < 2.0  and -1.0 < x < 0.0  and x + y  < 0.0:
            m = True
        elif 0.0 < y < 2.0  and 0.0 < x < 2.0  and  -y + x < 0.0:
            m = True
        elif 2.0 < y < 4.0  and 2.0 < x < 4.0  and -y + x  < 0.0:
            m = True
        elif 4.0 < y < 6.0  and 4.0 < x < 6.0  and -y + x  < 0.0:
            m = True
        elif 4.0 <= y <= 6.0  and -4.0 < x < -3.0:
            m = True
        elif 4.0 < y <= 5.0  and -3.0 <= x <= -2.0:
            m = True
        elif 2.0 < y < 4.0  and -2.0 < x <= -1.0:
            m = True
        elif 3.0 <= y <= 4.0  and -1.0 <= x < 0.0:
            m = True
        elif 3.0 < y < 4.0  and 0.0 < x < 1.0:
            m = True
        elif 3.0 <= y <= 4.0  and 0.0 < x < 1.0:
            m = True
        elif 2.0 < y < 4.0  and 1.0 < x < 2.0:
            m = True
        elif 4.0 < y < 6.0  and 3.0 < x < 4.0:
            m = True
        elif 5.0 < y < 6.0  and 2.0 <= x <= 3.0:
            m = True
        elif 6.0 < y <= 8.0  and 5.0 <= x <= 6.0:
            m = True
        elif 7.0 <= y <= 8.0  and 4.0 <= x <= 5.0:
            m = True
        elif y == 2.0 and -1.0 < x < 1.0:
            m = True
        elif y == 5.0 and 2.0 <= x <= 3.0:
            m = True
        elif y == 7.0 and 4.0 <= x <= 5.0:
            m = True
        elif x == -2.0 and -4.0 <= y <= -3.0:
            m = True
        elif x == 2.0 and 2.0 <= y <= 3.0:
            m = True
        elif x == 4.0 and 4.0 <= y <= 5.0:
            m = True
        elif -1.0 <= x <= 1.0 and 3.0 < y < 4.0:
            m = True
        
    return m
    # cuidado com a tabulação

#######################################################
###                 FIM   DA   MAIN()               ###
#######################################################
#
#  Não modifique as linhas abaixo
#
# Esse if serve para rodar a main() dentro do Spyder
# e não atrapalhar o corretor automático

if __name__ == '__main__':
    main()
