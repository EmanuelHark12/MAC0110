# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS OU ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS 
#------------------------------------------------------------------
     
'''
    Nome:
    NUSP:

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

import ep12

# Constantes
# use essas constantes caso desejar
DNA = 'ATCG'
GAP = '_'

#------------------------------------------------------------------
def main():
    '''
        Modifique essa função, escrevendo os seus testes.
    '''

    ## exemplos de chamada da função do módulo ep12
    print('Testes das funções do módulo ep12:')
    print(ep12.gera_gaps('T'))
    print(ep12.gera_gaps( 'CA' ))
    print(ep12.gera_gaps( 'AT_G' ))

    print(ep12.pontuacao(5, 5, 3, 'T_CGTAC', 'ATCG___'))
    print(ep12.pontuacao(1, 5, 3, 'T_CGTAC', 'ATCG___'))
    print(ep12.pontuacao(5, 5, 3,  'T_CGTA',  'ATCG__'))
    print()
    
    print(gera_n_gaps('T',2))
    print(gera_n_gaps( 'CA', 2 ))
    print(gera_n_gaps( 'C_A', 2))
    print(pontuacao_max(5, 5, 3, 'T_CG', 'ATCG'))
    print(pontuacao_max(1, 5, 3, 'T_CGTAC', 'ATCG___', 2))
    print(pontuacao_max(5, 1, 0, 'AT_', 'A_T', 2))
    

    ## Escreva aqui os testes para a função gera_n_gaps
    # 
    ## Escreva aqui os testes para a função pontuação_max
    #         

    print("Fim dos meus testes.")

#------------------------------------------------------------------
#
def gera_n_gaps( dna, n = 1 ):
    ''' ( str, int ) -> list
    Recebe uma string representando uma fita de DNA com os
    símbolos 'A', 'T', 'C', 'G' e '_' (um gap), e um inteiro n>0 
    com o número de gaps extras a serem inseridos, um a um, usando a 
    função gera_gaps do ep12. Retorna uma
    lista com todas as variações de dna com 0 a n gaps a mais, 
    sem repetição.

    exemplos: 
    In  [1]: gera_n_gaps( 'T', 2 )
    Out [1]: ['T', '_T', 'T_', '__T', '_T_', 'T__']
    
    In  [2]: gera_n_gaps( 'CA', 2 )
    Out [2]: ['CA', '_CA', 'C_A', 'CA_', '__CA', '_C_A', '_CA_', 'C__A', 'C_A_', 'CA__']
    
    In  [3]: gera_n_gaps( 'C_A', 2)
    Out [3]: ['C_A', '_C_A', 'C__A', 'C_A_', '__C_A', '_C__A', '_C_A_', 'C___A', 'C__A_', 'C_A__']
    '''
    # modifique o código abaixo para conter a sua solução.
    lista2 = []
    lista3 = []
    lista = [dna]
    dan = ep12.gera_gaps(dna)
    lista += dan
    while n > 1:
        for k in lista:
            adn = ep12.gera_gaps(k)
            lista2 += adn
        n -= 1
        lista += lista2
    for u in lista:
        if u not in lista3:
            lista3.append(u)
    return lista3
#------------------------------------------------------------------
#
def pontuacao_max(m, d, g, s, t, n = 1):
    ''' (int, int, int str, str, int) -> int, list, list
    Recebe:
    - 3 inteiros não negativos m, d, e g (semelhante ao EP12);
    - duas strings representando fitas de DNA de mesmo tamanho com zero ou mais gaps;
    - um inteiro n > 0 representando o número máximo de gaps que podem ser inseridos em s e t. 

    A função gera todas as variações de s e t com até n gaps a mais em s e em t, e calcula 
    as pontuações de todos os pares de mesmo tamanho. A função retorna um inteiro e duas listas:
    - um inteiro com a pontuação máxima encontrada, 
    - uma lista com todas as variações de s, sem repetição, que resultaram na pontuação máxima.
         Pode haver mais de 1 em caso de empates.
    - uma lista correspondente com as variações de t que resultaram na pontuação máxima

    Exemplos:
    In  [1]: pontuacao_max(5, 5, 3, 'T_CG', 'ATCG')
    Out [1]: (9, ['_T_CG'], ['AT_CG'])

    In  [2]: pontuacao_max(1, 5, 3, 'T_CGTAC', 'ATCG___', 2)
    Out [2]: (-12, ['_T_CGTAC'], ['AT_CG___'])
    
    In  [3]: pontuacao_max(5, 1, 0, 'AT_', 'A_T', 2)
    Out [3]: (10, ['A_T_', '_A_T_', 'A__T_', 'A_T__'], ['A_T_', '_A_T_', 'A__T_', 'A_T__'])
    '''
    # modifique o código abaixo para conter a sua solução.
    lista5 = gera_n_gaps(s,n)
    lista6 = gera_n_gaps(t,n)
    lista7 = []
    lista8 = []
    x = ep12.pontuacao(m,d,g,s,t)
    for j in lista6:
        for k in lista5:
            if len(k) == len(j):
                y = ep12.pontuacao(m,d,g,k,j)
            if y > x:
                r = y
                lista7 += [k]
                lista8 += [j]
    x = y             
    return r, lista7,lista8
#######################################################
###                 FIM                             ###
#######################################################
# 
# Esse if serve para rodar a main() dentro do Spyder.

if __name__ == '__main__':
    main()
