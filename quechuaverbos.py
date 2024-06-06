############################################################# 
#############################################################
## usamos pandas
import pandas as pd

## abrimos el excel
quechua = pd.read_excel('quechuaCA.xlsx')

quechua

## un solo acceso a todas las hojas de excel
quechua = pd.ExcelFile('quechuaCA.xlsx')
D = {}
for hoja in quechua.sheet_names:
    df = pd.read_excel('quechuaCA.xlsx', sheet_name = hoja)
    c = df.columns
    df.set_index(c[0], inplace = True)
    d = df.to_dict()
    D[hoja] = d

## diccionario
D

## ahora conjugamos los verbos
def conjugador(base,numero,persona,tiempo):
  return base + D[tiempo][numero][persona]

conjugador('miku', 'singular', 'segunda', 'Presente simple')

## excel con pronombres en quechua
## usamos pandas
import pandas as pd

## abrimos el excel
pronombres = pd.read_excel('pronombresCA.xlsx')

pronombres = pd.ExcelFile('pronombresCA.xlsx')
DP = {}
for hoja in pronombres.sheet_names:
    dfp = pd.read_excel('quechuaCA.xlsx')
    c = df.columns
    dfp.set_index(c[0], inplace = True)
    dp = df.to_dict()

dp

def conjtotal(base,numero,persona,tiempo):
  return dp[numero][persona] + ' ' + base + D[tiempo][numero][persona]




###############################################################################
###############################################################################

import pandas as pd

verbos = pd.read_excel('verbos.xlsl')

##diccionario

quechua = list(verbos['quechua'])
espanol = list(verbos['espanol'])

dict_que_esp = dict(zip(quechua,espanol))

##importamos streamlit
import streamlit as st

option = st.selectbox(
    "hola rei seleccione un verbo en quechua",
    (quechua))
st.write("el verbo en español obviamente es", dict_que_esp[option])

persona = st.selectbox(
    "escoge la persona que va a devorar rei",
    ('Primera','Segunda','Tercera','Cuarta'))

numero = st.selectbox(
    "escoge la nuemero rei y soporta",
    ('Singular','Plural'))

tiempo = st.selectbox(
    "elige el tiempo, a mal tiempo buena puchaina",
    ('Presente','Pasado'))

st.write("el verbo conjugado es",conjugador(option,persona,numero,tiempo))