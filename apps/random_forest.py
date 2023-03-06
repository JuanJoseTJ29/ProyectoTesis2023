import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sb
import time
import datetime
import streamlit as st
from PIL import Image
import joblib
import sklearn.externals as extjoblib

from service import service

def app():
    
#    modelo_nuevo = joblib.load('modelo_entrenado.pkl')
    st.title('Pcredicion de la Violencia Familiar') 
    image = Image.open('./image/Violencia-family.jpg')
    #st.sidebar.image('./image/violencia_intrafamiliar.jpg')
    lista_pregunta = ['0','0','0','0','0','0','0','0','0']
    st.image(image,width=570)  
    st.subheader('Pregunta 01: Su esposo(a)/compañero(a) se pone (ponía) celoso o molesto si usted conversa (conversaba) con otro hombre')
    pregunta_1 = st.radio("", ('SI','NO'),key = "1")
    if pregunta_1 == "SI":
        lista_pregunta[0] = '1'  
    st.subheader('Pregunta 02: Su esposo(a)/compañero(a) la acusa (acusaba) frecuentemente de ser infiel')
    pregunta_2 = st.radio("", ('SI','NO'),key = "2")
    if pregunta_2 == "SI":
        lista_pregunta[1] = '1'
    st.subheader('Pregunta 03: Su esposo(a)/compañero(a) le impide (impedia) que visite o la visiten sus amistades')
    pregunta_3 = st.radio("", ('SI','NO'),key = "3")
    if pregunta_3 == "SI":
        lista_pregunta[2] = '1'
    st.subheader('Pregunta 04: Su esposo(a)/compañero(a) trata (trataba) de limitar las visitas/contactos a su familia')
    pregunta_4 = st.radio("", ('SI','NO'),key = "4")
    if pregunta_4 == "SI":
        lista_pregunta[3] = '1'
    st.subheader('Pregunta 05: Su esposo(a)/compañero(a) insiste (insistía) siempre en saber todos los lugares dónde usted va (iba)')
    pregunta_5 = st.radio("", ('SI','NO'),key = "5")
    if pregunta_5 == "SI":
        lista_pregunta[4] = '1' 
    st.subheader('Pregunta 06: Su esposo(a)/compañero(a) desconfía (desconfiaba) de Ud. con el dinero')
    pregunta_6 = st.radio("", ('SI','NO'),key = "6")
    if pregunta_6 == "SI":
        lista_pregunta[5] = '1'
    st.subheader('Pregunta 07: Su esposo(a)/compañero(a) alguna vez le ha dicho o le ha hecho cosas para humillarla delante de los demás')
    pregunta_7 = st.radio("", ('SI','NO'),key = "7")
    if pregunta_7 == "SI":
        lista_pregunta[6] = '1'
    st.subheader('Pregunta 08: Su esposo(a)/compañero(a) la ha amenazado con hacerle daño a usted o a alguien cercano a usted')
    pregunta_8 = st.radio("", ('SI','NO'),key = "8")
    if pregunta_8 == "SI":
        lista_pregunta[7] = '1' 
    st.subheader('Pregunta 09: Su esposo(a)/compañero(a) la ha amenzado con irse de casa, quitarle a las hijas e hijos o la ayuda económica')
    pregunta_9 = st.radio("", ('SI','NO'),key = "9")
    if pregunta_9 == "SI":
        lista_pregunta[8] = '1'

    if st.button('Analizar'):
        resultado_prediccion = servicio_prediccion(lista_pregunta)
        st.write(lista_pregunta)
    else:
        st.write('NO Sufre violencia intrafamiliar')