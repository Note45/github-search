# coding: utf-8

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
import json
import requests

api_url_base = 'https://api.github.com/'
headers = {'Content-Type': 'application/json',
           'User-Agent': 'Python Student',
           'Accept': 'application/vnd.github.v3+json'}

class TelaInicial(BoxLayout):
    def get_user(self, nome):
        api = "{}users/{}".format(api_url_base, nome)

        response = requests.get(api, headers=headers)

        if response.status_code == 200:
            parsed = json.loads(response.content)

            return parsed
        else:
            raise ValueError

    def print_user(self):
        parsed = self.get_user(self.ids.entrada.text)
        text_label = [parsed.get("name"), parsed.get("login"),  parsed.get("avatar_url"), parsed.get("bio")]

        avatar = AsyncImage(source=text_label[2])
        self.ids.grid_label.add_widget(avatar)

        lb = Label(text="Nome: " + text_label[0] + " \nBiografia: " + text_label[3])
        self.ids.grid_label.add_widget(lb)

class SearchGitHub(App):
    def build(self):
        return TelaInicial()

if __name__ == "__main__":
    janela = SearchGitHub()
    janela.run()
