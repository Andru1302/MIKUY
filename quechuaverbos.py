## ñleemos el excel
import pandas as pd

verbos = pd.read_excel('verbos.xlsl')

##diccionario

quechua = list(verbos['quechua'])
español = list(verbos['español'])

dict_que_esp = dict(zip(quechua,español))

##importamos streamlit
import streamlit as st

option = st.selectbox(
    "hola rei seleccione un verbo en quechua",
    (quechua))
st.write("el verbo en español obviamente es", dict_que_esp[option])

persona = st.selectbox(
    "escoge la persona que va a devorar rei",
    ('Primera','Segunda','Tercera','Cuarta'))

número = st.selectbox(
    "escoge la nuemero rei y soporta",
    ('Singular','Plural'))

tiempo = st.selectbox(
    "elige el tiempo, a mal tiempo buena puchaina",
    ('Presente','Pasado'))
