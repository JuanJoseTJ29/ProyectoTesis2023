import streamlit as st
from multiapp import MultiApp

from apps import random_forest # import your app modules here

app = MultiApp()

app.add_app("PREDICCION DE VIOLENCIA FAMILIAR", random_forest.app)


# The main app
app.run()
