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
# MÓDULOS UTILIZADOS NO PROGRAMA
import math        # math.exp(), math.sqrt() e math.pi   
import random      # random.seed(), random.choices()
import numpy as np # np.arange()
import matplotlib.pyplot as plt # plt.subplots(), plt.bar(),  plt.xlabel(),
                                # plt.ylabel(), plt.title(), plt.show()

#####################################################################
#  CONSTANTES
# 
SEED   = 123456 # para gerador aleatório; garante reproducibilidade dos experimentos
CARA   = 'H'    # possível valor em uma amostra aleatória produzida por random.choices()
COROA  = 'T'    # possível valor em uma amostra aleatória produzida por random.choices()
SIM    = 's'

#####################################################################
def main():
    '''(None) -> None

    A função main() serve como unidade de teste para as funções.
    Pode ser alterada à vontade.
    Não será avaliada, a menos que produza erros ao executarmos o programa.
    '''
    random.seed(SEED) # para efeito de reproducibilidade

    teste = True
    while teste:
        # leia parâmetros
        n = int(input("Digite o número n de lançamentos da moeda: "))
        p = float(input("Digite a probabilidade de obtermos cara: "))
        t = int(input("Digite o número t de amostras: "))
        s = input("Deseja que ver a distribuição normal? ('s' para sim e o resto para não): ")
        if s == SIM:
            mostre_normal = True
        else:
            mostre_normal = False
            
        # obtenha o número de caras em t amostra aleatórias de n lançamentos uma moeda
        caras = caras_em_amostras(n, t, p)

        # obtenha a frequência de cada valor k nas t amostras
        freq_obs = frequencias_observadas(caras, n)

        # construa a distribuição binomial Bnp[] para os parâmetros n e p.
        Bnp = distribuicao_binomial(n, p)

        # construa a lista freq_esp[] das frequências esperadas de caras em t amostras,
        # segundo a distribuição binomial
        freq_esp = frequencias_esperadas(Bnp, t)
        
        # apresente as frequências observadas e esperadas
        print("Frequências observadas (esperadas)")
        for i in range(n+1):
            print("%8d: %7d (%g)"%(i, freq_obs[i], freq_esp[i]))

        # desenhe os gráficos    
        plot(freq_obs, freq_esp, n, t, p, mostre_normal)

        resp = input("Deseja continuar? ('s' para sim e o resto para não): ")
        if resp != 's' and resp != 'S':
            teste = False

#####################################################################
def caras_em_amostra_aleatoria(n, p=0.5, mostra_amostras=False):
    '''(int, float) -> list

    RECEBE um inteiro n e a probabilidade p de observarmos cara em 1
    lançamento de uma moeda.

    A função gera uma amostra aleatória com os resutados de n lançamentos  
    de uma moeda em que a probabilidade de obter cara é p e RETORNA 
    o número observado de caras na amostra aleatoria gerada.
 
    Se mostra_amostras é True a função deve imprimir a amostra aleatoria
    gerada.

    Uma amostra será representada através de uma lista com as strings
    'H' e 'T'. A string 'H' deve ser interpretada como cara e a 
    string 'T' como coroa.

    Para gerar a amostra aleatória a função deve usar a função 
    random.choices() do módulo random. A linha

        amostra_aleatoria = random.choices("HT", weights=(p, 1-p), k=n) 

    atribui à variável amostra_aleatoria uma lista de comprimento n em 
    que cada posição contém 
        - a string 'H' com probabilidade p ou 
        - a string 'T' com probabilidade 1-p.

    '''
    k = 0
    m = 0
    amostra_aleatoria = random.choices("HT", weights=(p, 1-p), k=n)
    for i in amostra_aleatoria:
        m += 1
        if i == 'H':
           k += 1
           if m == len(amostra_aleatoria) - 1:
               if mostra_amostras:
                   print(amostra_aleatoria)
    # modifique o código abaixo para conter a sua solução.
    return k 

#####################################################################        
def caras_em_amostras(n, t, p=0.5, mostra_amostras=False):
    '''(int, int, float) -> list

    RECEBE inteiros positivos n e t e uma probabilidade p de observarmos
    cara em 1 lançamento de uma moeda. 

    RETORNA uma lista de comprimento t em que cada posição contém o 
    número observado de caras em uma amostra aleatória com os resultados
    de n lançamentos de uma moeda em que a probabilidade de obter cara é p.

    Se mostra_amostras é True a função deve imprimir cada uma das t amostras
    aleatorias geradas.
    '''
    # modifique o código abaixo para conter a sua solução.
    h = 0
    l = 0
    u = []
    for e in range(0,t,1):
        pedaco =  random.choices("HT", weights=(p, 1-p), k=n)
        for t in pedaco:
            h += 1
            if t == 'H':
                l += 1
                if h == len(pedaco)-1 and mostra_amostras:
                    print(pedaco)
        h = 0
        u += [l]
        l = 0
        
        
                        
    return u
    

#####################################################################
def frequencias_observadas(no_caras, n):
    '''(list, int) -> list

    RECEBE uma lista no_caras com os números observados de caras 
    em t amostras aleatorias com os resultados de n lançamentos 
    de uma moeda.

    RETORNA uma lista de comprimento n+1 em que cada posição k contém a
    frequência de k na lista.
    '''
    # modifique o código abaixo para conter a sua solução.
    b = n + 1
    a = b * [0]
    for w in no_caras:
        a[w] += 1
    return a


#####################################################################
def distribuicao_binomial(n, p=0.5):
    '''(int, float) -> list

    RECEBE um número n de lançamentos de uma moeda e uma probabilidade
    p de observarmos cara em 1 lançamento.

    RETORNA a distribuição binomial para os parâmetros n e p.
    '''
    # modifique o código abaixo para conter a sua solução.
    c = []
    for o in range(0,n+1,1):
        y = math.factorial(n) / (math.factorial(o) * math.factorial(n-o))
        s = math.pow(p,o) * math.pow(1-p,n - o)
        c += [y * s]
        y = 0
        s = 0
    
    return c



#####################################################################
def frequencias_esperadas(Bnp, t):
    '''(list, int) -> list

    RECEBE uma distribuição binomial Bnp e um inteiro t.

    RETORNA uma lista de comprimento n+1 em que cada posição k contém a
    frequência esperada de obtermos k caras em t amostras de n lançamentos
    de uma moeda SEGUNDO a distribuição binomial.
    '''
    # modifique o código abaixo para conter a sua solução.
    rista = []
    fep = 0
    for qt in range(0,len(Bnp),1):
        fep = t * Bnp[qt]
        rista += [fep]
        
        
        
        
    return rista

#####################################################################
#
#  Desse ponto em diante não há nada a ser feito
#
#####################################################################

#####################################################################
def phi(x, mu=0, sigma2=1):
    '''(float, float, float) -> float

    RECEBE reais x, mu e sigma2.

    RETORNA o valor da função "densidade de probabilidade" 
    da distribuição normal de média mu e variância sigma2 no 
    ponto x.
    '''
    return math.exp(-(x-mu)*(x-mu)/(2*sigma2)) / math.sqrt(2*math.pi*sigma2)

#-------------------------------------------------------------
def plot(y_obs, y_esp, n, t, p, mostre_normal=False):
    '''(list, list, int, int, float, bool) -> None

    Exibe o gráfico de barras (azuis) representando a frequência observada.

    Exibe um gráfico pontilhado (vermelha) representando a frequência
    esperada segundo a distribuição binomial.

    Se mostre_normal é True exibe um gráfico de pontos (verdes)
    próximos representando a frequência esperada segundo a função
    densidade (phi()) da distribuição normal.
    '''
    # crie um gráfico
    fig, ax = plt.subplots()
    x = np.arange(n+1)
    
    # desenhe barras para representar com a frequência observada
    plt.bar(x, y_obs)

    # desenhe o gráfico com as frequência esperadas obtidas através da distribuição binomial
    ax.plot(x, y_esp, color='red', marker='^', linestyle='dashed', linewidth=1, markersize=6)

    # devemos desenhar a distribuição normal?
    if mostre_normal:
        
        # média da distribuição binomail
        mu = n*p
        
        # variância de distribuição binomial
        sigma2 = n*p*(1-p)
        
        # domínimo para o cálculo dos valores da função densidade da distribuição (continua) normal
        z = np.arange(0, n+1, 0.1)
        
        # valores da distribuição normal
        N = [0]*len(z) # np.zeros(len(z))
        for i in range(len(z)):
            N[i] = phi(z[i], mu, sigma2) * t
            
        # desenhe os pontos
        ax.plot(z, N, color='green', marker='*', linestyle='solid', linewidth=.5, markersize=2)

    # rotulos
    plt.xlabel('no. de caras')
    plt.ylabel('frequências')
    plt.title('Histograma para n=%d, t=%d e p=%g'%(n,t,p))
    plt.grid(True)

    # desenhe
    plt.show()


#=====================================================================
# Não modifique as linhas abaixo
# Esse if serve para rodar a main() dentro do Spyder
# e não atrapalhar o corretor automático

if __name__ == '__main__':
    main()
