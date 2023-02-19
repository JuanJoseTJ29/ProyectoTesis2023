"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st

class MultiApp:
    """Framework for combining multiple streamlit applications.
    Usage:
        def foo():
            st.title("Hello Foo")
        def bar():
            st.title("Hello Bar")
        app = MultiApp()
        app.add_app("Foo", foo)
        app.add_app("Bar", bar)
        app.run()
    It is also possible keep each application in a separate file.
        import foo
        import bar
        app = MultiApp()
        app.add_app("Foo", foo.app)
        app.add_app("Bar", bar.app)
        app.run()
    """
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
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
        app = st.selectbox(
            'Elija el modelo de su preferencia',
            self.apps,
            format_func=lambda app: app['title'])

        app['function']()