# coding: utf-8

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class TelaInicial(BoxLayout):
    pass


class SearchGitHub(App):
    def build(self):
        return TelaInicial()

if __name__ == "__main__":
    janela = SearchGitHub()
    janela.run()
