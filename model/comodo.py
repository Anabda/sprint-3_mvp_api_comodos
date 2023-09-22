from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

class Comodo(Base):
    __tablename__ = 'comodo'

    nome = Column("Nome", String(140), primary_key=True)

    def __init__(self, nome:str):
        """
        Cria um comodo

        Arguments:
            nome: nome do comodo

        """
        self.nome = nome
        