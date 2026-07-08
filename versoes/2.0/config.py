import json
import os

CONFIG_FILE = "config.json"

# Configurações padrão
default_config = {
    "cor_texto": "cyan",
    "cor_fundo": "black",
    "fonte": "Consolas",
    "tamanho_fonte": 24,
    "posicao_x": 120,
    "posicao_y": 8
}

def carregar_config():
    """Carrega as configurações do arquivo JSON ou cria padrão."""
    if not os.path.exists(CONFIG_FILE):
        salvar_config(default_config)
        return default_config
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def salvar_config(config):
    """Salva as configurações no arquivo JSON."""
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)
