from pydantic import BaseModel
from typing import Optional, List
from model.comodo import Comodo
from datetime import datetime


class ComodoSchema(BaseModel):
    """ Define como um novo comodo a ser inserido deve ser representado
    """
    nome: str
        
class ComodoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do comodo.
    """
    nome: str = "Quarto"

class ListagemComodosSchema(BaseModel):
    """ Define como uma listagem de comodos será retornada.
    """
    comodos:List[ComodoSchema]

def apresenta_comodos(comodos: List[Comodo]):
    """ Retorna uma representação do comodo.
    """
    lista_comodos = []
    for comodo in comodos:
        lista_comodos.append({ 
            "nome": comodo.nome
        })

    return {"comodos": lista_comodos}

def apresenta_comodo(comodo: Comodo):
    """ Retorna uma representação do comodo.
    """
    return {
        "nome": comodo.nome,
    }



class ComodoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

class ComodoViewSchema(BaseModel):
    """ Define como um comodo será retornado.
    """
    nome: str = "Play Station 5"
