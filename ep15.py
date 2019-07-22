# -*- encoding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS OU ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS 
#------------------------------------------------------------------
     
'''
    Nome:Emanuel Hark Maciel
    NUSP:11221380

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

# 
# =================================================================------------------------------------------------------------------
# 
def main():
    '''
        Modifique essa função, escrevendo os seus testes.
    '''
    ## Coloque aqui os seus testes.
    maux = [ [1,2,3,4,5],[3,4,5,6,7],[2,4,6,8,1],[5,3,1,7,9],[9,6,3,1,7] ]
    print( 'Matriz maux:')
    print( maux )
    print()
    print( to_string(maux, '> maux' ) )
    
    nova = crie (5, 5, 10)
    print( to_string( nova, '> nova') )
    
    dif = subtraia( nova, maux)
    print( to_string( dif , '> dif = nova - maux') )
    
    clo = clone(dif)
    print( to_string( clo , '> clo') )
    limiarize(clo, 5)
    print( to_string( clo , '> clo apos limiarize') )
    print( to_string( dif , '> dif apos limiarize') )
    


#------------------------------------------------------------------
#
def crie ( nlins, ncols, vini = 0 ):
    ''' (int, int, int) -> list

    RECEBE três inteiros, `nlins`, `ncols` e `vini`. 
    RETORNA uma matriz de dimensão `nlins` x `ncols` em que o valor do elemento
    em cada posição [lin][col] deve ser valor `vini`.
    '''
    # Substitua o código abaixo com a sua solução
    matriz_igual = []
    for lin in range(nlins):
        matriz_igual.append([vini] * ncols)
    return matriz_igual

#------------------------------------------------------------------
#
def clone ( mat ):
    ''' (list) -> list

    RECEBE uma matriz bidimensional mat e RETORNA um clone de mat.
    '''
    # Substitua o código abaixo com a sua solução
    matriz_clone = []
    nlin = len(mat)
    ncol = len(mat[0])
    for lin in range(nlin):
        matriz_clone += [[]]
        for col in range(ncol):
            matriz_clone[lin].append(mat[lin][col])
    
    return matriz_clone

#------------------------------------------------------------------
#
def subtraia ( mat1, mat2 ):
    ''' (list) -> list

    RECEBE duas matrizes bidimensionais `mat1` e `mat2` de números inteiros 
    e de mesma dimensão.
    RETORNA uma a matriz dif de mesma dimensão das matrizes. O valor 
    de cada posição [lin][col] deve ser dado por
 
        dif[lin][col] = mat1[lin][col] - mat2[lin][col].
    '''
    # Substitua o código abaixo com a sua solução
    nlin1 = len(mat1)
    ncol1 = len(mat1[0])
    matr_diff = []
    for lin in range(nlin1):
        matr_diff += [[]]
        for col in range(ncol1):
            matr_diff[lin].append(mat1[lin][col]- mat2[lin][col])
    return matr_diff
    
#------------------------------------------------------------------
#
def to_string ( mat , nome = 'matriz' ):
    ''' (list, str) -> str

    RECEBE uma matriz bidimensional `mat` de números inteiros e uma string `nome`.  
    RETORNA uma string utilizada por print() para exibir a matriz, como por exemplo 
    em 

        print(to_string(bla, 'minha matriz bla'))

    que exibe o conteúdo da matriz bla.

    No que segue, por linha da string retornada entenda uma substring seguida 
    do caractere "\n" de mudança de linha.

    A string retornada deve ter o seguinte formato:

      - a primeira linha da string contém a string `nome`;
      - as demais linhas da string contém uma a uma as linhas da matriz
        `mat`.

    Os valores da matriz devem representados na string retornada por substring 
    de mesmo tamanho. O efeito será que ao exibirmos uma matriz bla através de
    print(to_string(bla)) os valores de cada coluna estarão alinhados.

    Reserve ao menos 4 posições para exibir cada número inteiro.
    '''
    # Substitua o código abaixo com a sua solução
    t_str = '%s \n'%(nome)
    for lin in mat:
        for elem in lin:
            t_str += '%4d'%(elem)
        t_str += '\n'
    return t_str

#------------------------------------------------------------------
#
def limiarize ( mat, limite, alto=255, baixo=0 ):
    ''' (list, int, int, int) -> None
    RECEBE uma matriz bidimensional `mat` de números inteiros e três inteiros
    `limite`, `alto` e baixo.

    A função deve MODIFICAR `mat` da sequinte forma.
 
    Cada posição [lin][col] de `mat` em que mat[lin][col] > `limite`,
    deve receber o valor `alto`. As demais posições devem receber o valor 
    `baixo`.
    '''
    # Substitua o código abaixo com a sua solução
    nlin = len(mat)
    ncol = len(mat[0])
    for lin in range(nlin):
        for col in range(ncol):
            if mat[lin][col] > limite:
                mat[lin][col] = alto
            else:
                mat[lin][col] = baixo


#######################################################
###                 FIM                             ###
#######################################################
# 
# Esse if serve para rodar a main() dentro do Spyder.

if __name__ == '__main__':
    main()
