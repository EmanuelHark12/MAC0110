# -*- coding: utf-8 -*-
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
        
        Eu precisei da ajuda de um amigo,Emerson, para a necessidade de usar o 
        while ao  invés do for.

'''

# constantes
SIM = 's'

#------------------------------------------------------------------
def main():
    '''
        Modifique essa função, escrevendo outros testes.

        Para saber mais sobre como manipular arquivos:

        https://panda.ime.usp.br/cc110/static/cc110/11-strings.html
    '''
    nome  = input("Digite o nome de um arquivo texto: ")
    opcao = input("Digite '%s' se deseja ver o texto lido: "%(SIM))
    if opcao == SIM:
        mostre_texto = True
    else:
        mostre_texto = False
    with open(nome, 'w', encoding='utf-8') as arq:
    # CORPO DO WITH
        x = arq.write("ana e mariana compraram bananas")
    
    # leia texto do arquivo nome
    with open(nome, 'r', encoding='utf-8') as arquivos:
        texto = arquivos.read()

    # deseja que o texto seja exibido?    
    if mostre_texto:
        print("\nConteudo do arquivo '%s':"%(nome))
        print(texto)

    palavra      = input("Digite uma palavra a ser substituída: ")
    nova_palavra = input("Digite uma palavra substituta: ")
        
    # encontre as posições onde a palavra ocorre    
    ocorrencias = busque( palavra, texto )

    # mostre as posições encontradas
    print("\nAchei '%s' nos seguintes lugares: "%(palavra))
    print(ocorrencias)

    # crie um texto onde as ocorrências de `palavra` foram substituídas por
    # `nova_palavra`
    novo_texto = substitua( palavra, nova_palavra, texto )

    # exiba o texto criado
    print("\nNovo texto:")
    print(novo_texto)

    print("Fim dos testes.")

#------------------------------------------------------------------
#
def busque( palavra, texto ):
    ''' (str, str) -> list

    RECEBE duas strings, `palavra` e `texto`, e RETORNA uma lista
    contendo o início de cada ocorrência de `palavra` em `texto`.

    No caso de haver sobreposições de ocorrências de `palavra`, apenas
    menor índice dentre as ocorrências sobrepostas deverá ser inserido 
    na lista.

    Exemplos:
        
    In [4]: busque("mana", "ana e mariana compraram bananas")
    Out[4]: []

    In [5]: busque("bana", "ana e mariana compraram bananas")
    Out[5]: [24]

    In [6]: busque("ana", "ana e mariana compraram bananas")
    Out[6]: [0, 10, 25]

    In [7]: busque("AA", "ACAAAGTCAAAATTGTGTAGTGTGACGTTTT")
    Out[7]: [2, 8, 10]
    '''
    # modifique o código abaixo para conter a sua solução.
    dista = [] 
    i = 0
    while i < len(texto):
        if texto[i:len(palavra)+i] == palavra:
            dista +=[i]
            i += len(palavra) 
        else:
            i += 1
    return dista
    
#------------------------------------------------------------------
#
def substitua( palavra, nova_palavra, texto ):
    ''' (str, str, str) -> str

    RECEBE as strings `palavra`, `nova` e `texto` e
    RETORNA uma string onde todas as ocorrências de `palavra`
    foram substituídas pela `nova_pal`.

    No caso de haver sobreposições de ocorrências de `palavra`, apenas
    a de menor índice dentre as ocorrências sobrepostas deverá ser 
    substituída por `nova_palavra`.

    Exemplos:

    In [1]: substitua("compraram","venderem","ana e mariana compraram bananas")
    Out[1]: 'ana e mariana venderem bananas'

    In [2]: substitua("ana","ely","ana e mariana compraram bananas")
    Out[2]: 'ely e mariely compraram belynas'

    In [3]: substitua("AA", "????", "ACAAAGTCAAAATTGTGTAGTGTGACGTTTT")
    Out[3]: 'AC????AGTC????????TTGTGTAGTGTGACGTTTT'

    In [4]: substitua("TGT", "X", "ACAAAGTCAAAATTGTGTAGTGTGACGTTTT")
    Out[4]: 'ACAAAGTCAAAATXGTAGXGACGTTTT'
    '''
    # modifique o código abaixo para conter a sua solução.
    i = 0
    qw = ''
    while i < len(texto):
        if texto[i:len(palavra)+i] == palavra:
            qw += nova_palavra 
            i += len(palavra)
        else:
            qw += texto[i]
            i += 1
    return qw
                    


#######################################################
###                 FIM                             ###
#######################################################
# 
# Esse if serve para rodar a main() dentro do Spyder.

if __name__ == '__main__':
    main()
