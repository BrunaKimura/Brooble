import pickle
import dicionario
import matplotlib.pyplot as plt
import cv2
import argparse
import plotagem

dic_ori = dicionario.a
dic_id = pickle.load( open( "dict.p", "rb" ) )

parser = argparse.ArgumentParser(description = 'objeto buscado')
parser.add_argument('--partial', action='store_true')

parser.add_argument(action='store',dest='simple_value',
                    help='Store a simple value')

results = parser.parse_args()

term = results.simple_value

def achaid():
    lista_id=[]
    lista_name = []
    for id_item, name in dic_ori.items(): 
        if term in name:
            lista_id.append(id_item)
            lista_name.append(name)
    return lista_id, lista_name

def achaididentico():
    lista_id=[]
    lista_name = []
    for id_item, name in dic_ori.items(): 
        if term == name:
            lista_id.append(id_item)
            lista_name.append(name)
    return lista_id, lista_name

find = 0
indice = 0
if results.partial == True:
    id_itens, lista_name = achaid()
else:
    id_itens, lista_name = achaididentico()
    

if id_itens == []:
    print("utilize o argumento '--partial ' ou digite o nome da categoria completa")

for id_atual in id_itens:
    for key in dic_id:
        if key == id_atual:
            max_porc = sorted(dic_id[key], reverse=True)
            find =1
     
    if find == 1:
        plotagem.plota_img(max_porc[0][1])
        break

    else:
        print("termo não encontrado")
