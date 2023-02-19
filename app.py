import streamlit as st
from multiapp import MultiApp
from app import forestpractice # import your app modules here

app = MultiApp()

app.add_app("PREDICCION DE VIOLENCIA FAMILIAR", forestpractice.app)


# The main app
app.run()
