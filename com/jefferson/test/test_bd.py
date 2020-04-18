import pytest
from bd import bancodedados

def test_criando_tabela():
    banco = bancodedados()
    assert  banco.criando_tabela("'id'","pk",1) == True, "Deveria ser True"