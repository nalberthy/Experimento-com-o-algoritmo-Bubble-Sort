import os
import re
import psutil
import time


def prog_100():
    print('\n'+"Em Execução, Por favor aguarde !")
    #estatistica
    qt_trocas = 0
    qt_comparacoes = 0

    time_inicio = time.time()
    pid = os.getpid()
    py = psutil.Process(pid)

    with open('entrada100.csv') as csv_file:
        l = csv_file.read()
        l = re.split('\n|,',l)

    for j in range(len(l)):
        for i in range(len(l)-1):
            qt_comparacoes += 1
            if l[i] > l[i+1]:
                aux = l[i]
                l[i] = l[i+1]
                l[i+1] = aux
                qt_trocas += 1

    time_fim = time.time()
    time_execucao = (time_fim - time_inicio)

    print('\n'+ '======================Entrada com 100 dados===========================')
    print('Quantidade de comparações : '+str(qt_comparacoes) + '\n' + 'Quantidade de trocas : '+str(qt_trocas) + '\n' + 'Tempo de execução : '+str(time_execucao) + '\n' + 'Consumo de CPU : '+str(py.cpu_times()[0]) + '\n' + 'Consumo de memória : '+str(py.memory_info()[0]/8000000000))
    print('\n'+'\n')
def prog_10000():
    print('\n'+"Em Execução, Por favor aguarde !")
    #estatistica
    qt_trocas = 0
    qt_comparacoes = 0

    time_inicio = time.time()
    pid = os.getpid()
    py = psutil.Process(pid)

    with open('entrada10000.csv') as csv_file:
        l = csv_file.read()
        l = re.split('\n|,',l)

    for j in range(len(l)):
        for i in range(len(l)-1):
            qt_comparacoes += 1
            if l[i] > l[i+1]:
                aux = l[i]
                l[i] = l[i+1]
                l[i+1] = aux
                qt_trocas += 1

    time_fim = time.time()
    time_execucao = (time_fim - time_inicio)
    print('\n'+ '======================Entrada com 10.000 dados===========================')
    print('Quantidade de comparações : '+str(qt_comparacoes) + '\n' + 'Quantidade de trocas : '+str(qt_trocas) + '\n' + 'Tempo de execução : '+str(time_execucao) + '\n' + 'Consumo de CPU : '+str(py.cpu_times()[0]) + '\n' + 'Consumo de memória : '+str(py.memory_info()[0]/8000000000))
    print('\n'+'\n')
def prog_100000():
    print('\n'+"Em Execução, Por favor aguarde !")
    #estatistica
    qt_trocas = 0
    qt_comparacoes = 0

    time_inicio = time.time()
    pid = os.getpid()
    py = psutil.Process(pid)

    with open('entrada100000.csv') as csv_file:
        l = csv_file.read()
        l = re.split('\n|,',l)

    for j in range(len(l)):
        for i in range(len(l)-1):
            qt_comparacoes += 1
            if l[i] > l[i+1]:
                aux = l[i]
                l[i] = l[i+1]
                l[i+1] = aux
                qt_trocas += 1

    time_fim = time.time()
    time_execucao = (time_fim - time_inicio)

    print('\n'+ '======================Entrada com 10.000 dados===========================')
    print('Quantidade de comparações : '+str(qt_comparacoes) + '\n' + 'Quantidade de trocas : '+str(qt_trocas) + '\n' + 'Tempo de execução : '+str(time_execucao) + '\n' + 'Consumo de CPU : '+str(py.cpu_times()[0]) + '\n' + 'Consumo de memória : '+str(py.memory_info()[0]/8000000000))
    print('\n'+'\n')

op = input("Escolha qual programa executar:" +"\n"+ "1 = Entrada com 100 dados aleatórios" + "\n" + "2 = Entrada com 10.000 dados aleatórios"+"\n"+"3 = Entrada com 100.000 dados aleatórios"+ "\n"+ "Qualquer entrada diferente das apresentadas encerra a execução !" + "\n" +"\n"+ "Digite a entrada :  " )
while op == str(1) or op == str(2)or op==str(3):
    if op == str(1):
        prog_100()
    elif op == str(2):
        prog_10000()
    elif op == str(3):
        prog_10000()
    else:
        break
    op = input("Escolha qual programa executar:" +"\n"+ "1 = Entrada com 100 dados aleatórios" + "\n" + "2 = Entrada com 10.000 dados aleatórios"+"\n"+"3 = Entrada com 100.000 dados aleatórios"+ "\n"+"\n"+"\n"+ "Qualquer entrada diferente das apresentadas encerra a execução!" + "\n" +"\n"+ "Digite a entrada :  " )

    
