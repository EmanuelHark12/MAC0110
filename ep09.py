# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
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
#####################################################################
# MÓDULOS A SEREM UTILIZADOS NO PROGRAMA
import random
import time

#####################################################################
def main():
    '''
    Essa função testa as funções pedidas para o EP.
    Escreva outros testes que desejar.

    Siga as instruções para entrega disponíveis em:
    https://paca.ime.usp.br/mod/page/view.php?id=42515
    '''

    print("Testes do EP09")

    # testes da função tem_indice_inconveniente
    print()
    print("Função tem_indice_inconveniente()")
    amigos1 = [1,2,3,4,0]
    amigos2 = [2,1,0,3,4]
    print(" -- tem_indice_inconveniente(%s) = %s"%(amigos1, tem_indice_inconveniente(amigos1)))
    print(" -- tem_indice_inconveniente(%s) = %s"%(amigos2, tem_indice_inconveniente(amigos2)))

    # parâmetros para os experimentos
    print()
    print("Função novo_experimento()")
    semente = int(input("Digite o valor da semente do gerador de números pseudo-aleatórios: "))
    random.seed(semente)
    MINN  = int(input("Qual o número mínimo de pessoas: "))
    MAXN  = int(input("Qual o número máximo de pessoas: "))
    passo = int(input("Qual o passo: "))
    T     = int(input("Qual o número de tentativas em cada experimento: "))
    SHOW  = input("Você quer ver as listas com índice inconveniente [s/n]: ")

    n = MINN
    while n <= MAXN:
        instante_inicial = time.time() # para medir o tempo transcorrido
        qn, inconvenientes = novo_experimento(n, T)
        print("q(%d) = %f"%(n, qn))
        if SHOW == 's' or SHOW == 'S':
            print("   permutações com índices inconvenientes para q(%d): "%(n))
        tamanho = len(inconvenientes)
        if tamanho == 0:
            print("      nenhuma lista com índice inconveniente.")
        else:
                for i in range(0, len(inconvenientes), 1):
                    print("    -- antes  --", inconvenientes[i])
                    permuta_sem_inconvenientes( inconvenientes[i] )
                    print("    ++ depois ++", inconvenientes[i])
        instante_final = time.time()
        print("    tempo decorrido: %7.2f ms"%((instante_final - instante_inicial)*1000 ))
        n = n + passo

    # teste permuta_sem_inconvenientes para n grande
    print()
    muito_grande = 1000000
    amigos3 = cria_lista_embaralhada(muito_grande)
    amigos3 += [muito_grande]
    print(" -- tem_indice_inconveniente com lista de %d = %s"%(muito_grande, tem_indice_inconveniente(amigos3)))
    instante_inicial = time.time()
    permuta_sem_inconvenientes(amigos3)
    instante_final = time.time()
    print(" ++ tem_indice_inconveniente com lista de %d = %s"%(muito_grande, tem_indice_inconveniente(amigos3)))
    print("    tempo decorrido: %7.2f ms"%((instante_final - instante_inicial)*1000 ))
###################################################################
def cria_lista_embaralhada( n ):
    ''' (int) -> list
    Retorna uma lista de tamanho n,
    contendo os números de 0 a n em ordem aleatória.
    '''
    lista = []
    i = 0
    while i < n:
        lista += [i]
        i += 1
    random.shuffle(lista)
    return lista

###################################################################
def tem_indice_inconveniente(amigo_de):
    ''' (list) -> bool
    Recebe uma lista de "amigo secreto" e retorna True caso 
    exista um índice i que seja igual ao valor de amigo_de[i].
    Retorna False caso contrário.
    '''
    # modifique o código abaixo para conter a sua solução.
    n = len(amigo_de) - 1
    for i in range(0,n+1,1):
        if amigo_de[i] == i:
            return True
    return False

###################################################################
def novo_experimento(N, T):
    ''' (int, int) -> float, list
    Calcula a probabilidade q(N) de uma lista de "amigo secreto" com 
    N participantes NÃO ter um índice inconveniente, ou seja, com
    i = amigo_de[i]. Essa probabilidade deve ser calculada a partir 
    de T sorteios de listas de tamanho N e calculando a 
    frequência relativa das listas sem nenhum índice inconveniente.
    Além de q(N), a função deve retornar também uma lista com
    todas as permutações inconvenientes encontradas.
    '''
    # modifique o código abaixo para conter a sua solução.
    i = 0
    nincon = []
    r = 0
    while i < T:
        y = cria_lista_embaralhada(N)
        u = tem_indice_inconveniente(y)
        if not u:
            r += 1
        else:
            nincon += [[y]]
        i += 1
    q = r / T
    return q, nincon  # retorna uma probabilidade e uma lista

###################################################################
def permuta_sem_inconvenientes( amigo_de ):
    ''' (list) -> None
    Recebe uma lista amigo_de e transforma a lista 
    de forma a não conter nenhum elemento com índice
    inconveniente, ou seja, que não tenha i = amigo_de[i].
    '''
    # modifique o código abaixo para conter a sua solução.
    if len(amigo_de) == 0:
        a = amigo_de[0]
        k = []
        for t in amigo_de:
            k += t
        n = len(a) - 1
        for i in range(0,n+1,1):
            if a[i] == i:
                if n == i:
                    a[n] = k[n - i]
                    a[n -i] = k[n]
                if n != i:
                    a[i] = k[i+1]
                    a[i+1] = k[i]
    else:
        n = len(amigo_de)-1
        a = []
        for j in amigo_de:
            a += [j]
        for i in range(0,n+1,1):
            if amigo_de[i] == i:
                if n == i:
                    amigo_de[n] = a[n - i]
                    b[n -i] = a[n]
                else:
                    amigo_de[i] = a[i+1]
                    amigo_de[i+1] = a[i]
                
        
            
        
        
                    
                    
                    



    return 

#=====================================================================
# Não modifique as linhas abaixo
# Esse if serve para rodar a main() dentro do Spyder
# e não atrapalhar o corretor automático

if __name__ == '__main__':
    main()
