# coding: utf-8

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
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
        text_label = [parsed.get("name"), parsed.get("login"), parsed.get("id"), parsed.get("bio")]

        lb = Label(text="Teste de label")
        self.ids.grid_label.add_widget(lb)

        print(text_label)



class SearchGitHub(App):
    def build(self):
        return TelaInicial()

if __name__ == "__main__":
    janela = SearchGitHub()
    janela.run()
