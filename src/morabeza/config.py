"""Leitura da configuração do projeto (Sessão 3)."""
from pathlib import Path

import yaml


CHAVES_OBRIGATORIAS = ("ficheiro_vendas", "moeda")


class ConfigInvalida(Exception):
    """O ficheiro de configuração não existe ou falta-lhe alguma chave obrigatória."""


def carregar_config(caminho: str) -> dict:
    """Lê o ficheiro YAML e devolve um dicionário com a configuração."""
    # TODO 1: se o ficheiro não existir (Path(caminho).exists()), levanta ConfigInvalida.
    if not Path(caminho).exists():
        raise ConfigInvalida(f"O ficheiro {caminho} não existe.")
    # TODO 2: abre o ficheiro com with open(...) e lê-o com yaml.safe_load(ficheiro).
    with open(caminho, "r") as f:
        config = yaml.safe_load(f) or {}
    # TODO 3: vê que chaves de CHAVES_OBRIGATORIAS faltam (compreensão de lista)
    #         e, se faltar alguma, levanta ConfigInvalida com os nomes em falta.
    chaves_faltando = [chave for chave in CHAVES_OBRIGATORIAS if chave not in config]
    if chaves_faltando:
        raise ConfigInvalida(f"Faltam as seguintes chaves: {', '.join(chaves_faltando)}")
    # TODO 4: devolve o dicionário.
    return config
