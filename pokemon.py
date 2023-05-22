
import requests

class Pokemon:
    def __init__(self, nome):
        self.nome = nome
        self.tipo = None
        self.ataqueB = None
        self.defesaB = None
        self.ataqueS = None
        self.defesaS = None
        self.velocidade = None
        self.peso = None

        self.obter_dados_pokemon()

    def obter_dados_pokemon(self):
        url = f"https://pokeapi.co/api/v2/pokemon/{self.nome.lower()}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            self.tipo = data['types'][0]['type']['name']
            self.ataqueB = data['stats'][1]['base_stat']
            self.defesaB = data['stats'][2]['base_stat']
            self.ataqueS = data['stats'][3]['base_stat']
            self.defesaS = data['stats'][4]['base_stat']
            self.velocidade = data['stats'][5]['base_stat']
            self.peso = data['weight']
        else:
            print("Dados do Pokemon não disponiveis.")

nome_pokemon = input("Pokémon desejado: ")

pokemon = Pokemon(nome_pokemon)

print("Nome:", pokemon.nome)
print("Tipo:", pokemon.tipo)
print("Ataque Base:", pokemon.ataqueB)
print("Defesa Base:", pokemon.defesaB)
print("Ataque Especial:", pokemon.ataqueS)
print("Defesa Especial:", pokemon.defesaB)
print("Velocidade:", pokemon.velocidade)
print("Peso:", pokemon.peso)


        