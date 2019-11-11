# coding: utf-8

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
import kivy
kivy.require("1.9.1")

class TelaInicial(FloatLayout):
    pass

class SeachGitHub(App):
    def build(self):
        return TelaInicial()

applicativo = SeachGitHub()
applicativo.run()