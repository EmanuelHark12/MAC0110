# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
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

def main():
    '''(None) -> None 

    Coloque sua solução individual abaixo, seguindo o enunciado do 
    exercício EP01 na página da disciplina.

    Siga as instruções para entrega disponíveis em:
    https://paca.ime.usp.br/mod/page/view.php?id=42515

    SUGESTÃO: Simule o programa antes de executar 
    cada exemplo. Em particular, para cada expressão, 
    além do valor do resultado, você deve saber se o 
    tipo do resultado é int, float ou str.

    '''
    # escreva seu programa a seguir
    PROMPT_1 = "Digite uma palavra p:"
    PROMPT_2 =  "Digite um inteiro i:"
    PROMPT_3 =  "Digite um real r:"
    
    p = input(PROMPT_1)
    i = int(input(PROMPT_2))
    r = float(input(PROMPT_3))    
    
    soma = p + p
    soma1 = i + i
    soma2 = r + r
    mul =  i * p
    mul1 = i * i
    mul2 = i * r
    div1 = r / i
    div2 = 2 * r / r
    div3 = r / r * 2
    
    print()
    print("Resultado de p + p:", soma)
    print("Resultado de i + i ", soma1)    
    print("Resultado de r + r:", soma2)
    print("Resultado de i * p:", mul)
    print("Resultado de i * i:", mul1)
    print("Resultado de i * r:", mul2)
    print("Resultado de r / i:", div1)
    print("Resultado de 2 * r / r:", div2)
    print("Resultado de i / i * 2:", div3)

    # fim da main()

# =========================================================
# NÃO MODIFIQUE AS LINHAS ABAIXO
# ELAS SÃO NECESSÁRIAS PARA O CORRETOR AUTOMÁTICO
# =========================================================

if __name__ == "__main__":
    main()
    

