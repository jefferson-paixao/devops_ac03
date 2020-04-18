import pytest
from com.jefferson.bd import bancodedados

def test_criando_tabela():
    banco = bancodedados()
    assert  banco.criando_tabela("'id'","pk",1) == True, "Deveria ser True"
    #1º parametro = qual coluna da tabela criada você quer testar ("id", "nome" ou "email")
    #2º parametro = qual atributo da coluna você quer testar ("pk" ou "notnull")
    #3º parametro = qual valor esperado no teste (1 ou 0)