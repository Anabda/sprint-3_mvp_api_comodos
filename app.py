from flask_openapi3 import OpenAPI, Info, Tag
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS
from flask import redirect

from model import Session, Comodo
from schemas import *

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)


# tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
comodo_tag = Tag(name="Comodo", description="Cria, lista e remove comodos da base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/comodo', tags=[comodo_tag],
          responses={"200": ComodoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_comodo(form: ComodoSchema):
    """Adiciona um novo comodo à base de dados
    """
    comodo = Comodo(
        nome=form.nome)
    
    try:
        session = Session()
        session.add(comodo)
        session.commit()
        return apresenta_comodo(comodo), 200

    except IntegrityError as e:
        error_msg = "Não foi possível cadastrar o comodo, pois já existe um comodo com esse código"
        print("erro: comodo já cadastrado")
        return {"mesage": error_msg}, 409

    except Exception as e:
        error_msg = "Erro inesperado, o comodo inserido não foi cadastrado"
        return {"mesage": error_msg}, 400

@app.get('/comodos', tags=[comodo_tag],
         responses={"200": ListagemComodosSchema, "404": ErrorSchema})
def get_comodos():
    """Retorna uma listagem de comodos cadastrados na base.
    """
    
    session = Session()
    comodos = session.query(Comodo).all()

    if not comodos:
        return {"comodos": []}, 200
    return apresenta_comodos(comodos), 200

@app.get('/comodo', tags=[comodo_tag],
            responses={"200": ComodoViewSchema, "404": ErrorSchema})
def get_comodo(query: ComodoBuscaSchema):
    """Encontra um comodo a partir do nome informado

    Retorna o comodo.
    """
    nome = query.nome
    session = Session()
    comodo = session.query(Comodo).filter(Comodo.nome == nome).first()
    if comodo:
        return apresenta_comodo(comodo), 200
    error_msg = "Comodo não encontrado"
    return {"mesage": error_msg}, 404
 
@app.delete('/comodo', tags=[comodo_tag],
            responses={"200": ComodoDelSchema, "404": ErrorSchema})
def del_comodo(query: ComodoBuscaSchema):
    """Deleta um comodo a partir do nome informado

    Retorna uma mensagem de confirmação da remoção.
    """
    nome = query.nome
    session = Session()
    count = session.query(Comodo).filter(Comodo.nome == nome).delete()
    session.commit()

    if count:
        return {"mesage": "Comodo removido", "comodo": nome}
    error_msg = "Comodo não encontrado"
    return {"mesage": error_msg}, 404
    