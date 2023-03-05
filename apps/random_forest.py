#import matplotlib.pyplot as plt
#import numpy as np
#import pandas as pd
#import seaborn as sb
import time
import datetime
import streamlit as st

def app():
    
    st.title('Prediccion de la Violencia Familiar') 
    st.subheader('Pregunta 01: Su esposo/compañero se pone (ponía) celoso o molesto si usted conversa (conversaba) con otro hombre')
    pregunta_1 = st.radio("", ('SI','NO'),key = "1")
    st.subheader('Pregunta 02: Su esposo/compañero la acusa (acusaba) frecuentemente de ser infiel')
    pregunta_2 = st.radio("", ('SI','NO'),key = "2")
    st.subheader('Pregunta 03: Su esposo/compañero le impide (impedia) que visite o la visiten sus amistades')
    pregunta_3 = st.radio("", ('SI','NO'),key = "3")
    st.subheader('Pregunta 04: Su esposo/compañero trata (trataba) de limitar las visitas/contactos a su familia')
    pregunta_4 = st.radio("", ('SI','NO'),key = "4")   
    st.subheader('Pregunta 05: Su esposo/compañero insiste (insistía) siempre en saber todos los lugares dónde usted va (iba)')
    pregunta_5 = st.radio("", ('SI','NO'),key = "5")
    st.subheader('Pregunta 06: Su esposo/compañero desconfía (desconfiaba) de Ud. con el dinero')
    pregunta_6 = st.radio("", ('SI','NO'),key = "6")
    st.subheader('Pregunta 07: Su esposo/compañero alguna vez le ha dicho o le ha hecho cosas para humillarla delante de los demás')
    pregunta_7 = st.radio("", ('SI','NO'),key = "7")
    st.subheader('Pregunta 08: Su esposo/compañero la ha amenazado con hacerle daño a usted o a alguien cercano a usted')
    pregunta_8 = st.radio("", ('SI','NO'),key = "8")    
    st.subheader('Pregunta 09: Su esposo/compañero la ha amenzado con irse de casa, quitarle a las hijas e hijos o la ayuda económica')
    pregunta_9 = st.radio("", ('SI','NO'),key = "9")

    if st.button('Analizar'):
        st.write('Usted sufre violencia intrafamiliar')
    else:
        st.write('NO Sufre violencia intrafamiliar')