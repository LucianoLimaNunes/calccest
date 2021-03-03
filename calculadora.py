# -*- coding: UTF-8 -*-

def soma(adicao):
    adicao = a + b

def subtracao(diminuir):
    diminuir = a - b

def multiplicacao(multi):
    multi = a * b

def divisao(dividir):
    dividir = a / b

def entrada_valores():
    print 'Digite o valor de A'
    x = raw_input()
    a = float(x)
    print 'Digite o valor de B'
    y = raw_input()
    b = float(y)

def menu():
    escolha = ''
    while(escolha != '0'):
        print '[1] para soma'
        print '[2] para subtração'
        print '[3] para multiplicação'
        print '[4] para divisão'
        print '[0] FINALIZAR PROGRAMA'

        escolha = raw_input()
        if(escolha == '1'):
            entrada_valores()
            soma(adicao, a, b)
            print soma(adicao, a, b)

        if(escolha == '2'):
            entrada_valores(a,b)
            subtracao(diminuir)
            print subtracao(diminuir)

        if(escolha == '3'):
            entrada_valores(a,b)
            multiplicacao(multi)
            print multiplicacao(multi)

        if(escolha == '4'):
            entrada_valores(a,b)
            divisao(dividir)
            print divisao(dividir)

menu()
