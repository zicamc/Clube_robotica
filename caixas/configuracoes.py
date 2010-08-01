# -*- coding: utf-8 -*-
import yaml

class config_caixa():
    data = yaml.load(file("texto_caixas.yaml","r"))

class config_selecao():
    data = yaml.load(file("texto_selecao.yaml","r"))

class all_config():
    data = yaml.load(file("configuracoes.yaml","r"))

class config_botoes:
    data = yaml.load(file("botoes.yaml","r"))