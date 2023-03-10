import streamlit as st

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        # app = st.sidebar.radio(
        # st.markdown('''
        #         <a href='https://www.youtube.com/watch?v=hoPvOIJvrb8' target="_self">HOME</a>
        # ''', unsafe_allow_html=True)
        st.markdown('''
                # Proyecto de TESIS
                ### Rodrigo Ervin Quinteros Peralta
                ### Juan Jose Tirado Julca
        ''')
        st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://www.todofondos.net/wp-content/uploads/hq-todofondos-colorespasteles8.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
        
        )
        app = st.selectbox(
            'Elija el modelo de su preferencia',
            self.apps,
            format_func=lambda app: app['title'])

        app['function']()