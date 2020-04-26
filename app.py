# coding: utf-8
from flask import Flask, request, make_response
from flask_restful import Resource, Api
from models import Pessoas, Atividades, Usuarios
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)


# criei um dicionario pra teste de usuario
# USUARIOS = {
#     'claudinei': '123',
#     'poly': 'abc',
# }
#
# @auth.verify_password #estou dizendo que essa funcao que criei é a verificadora de senha
# def verificacao(login, senha):
#     print('validando usuario')
#     print(USUARIOS.get(login) == senha)
#     if not (login, senha):
#         return False
#         # se nao for informado nem login, nem senha, retorna falso os 2 tem que ser informados
#     return USUARIOS.get(login) == senha  # vai retornar verdadeiro se for igual


@auth.verify_password  # estou dizendo que essa funcao que criei é a verificadora de senha
def verificacao(login, senha):
    if not (login, senha):
        return False
        # se nao for informado nem login, nem senha, retorna falso os 2 tem que ser informados
    return Usuarios.query.filter_by(login=login, senha=senha).first()


class Pessoa(Resource):
    # decorador vai informar quais metodos passarao pela verificacao de senha
    @auth.login_required
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': u'Pessoa não encontrada'
            }
        return make_response(response)

    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade,
        }
        return response

    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        mensagem = 'Pessoa {} excluída com sucesso'.format(pessoa.nome)
        pessoa.delete()
        return {'status': 'sucesso', 'mensagem': mensagem}


class ListaPessoas(Resource):
    @auth.login_required
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'idade': i.idade} for i in pessoas]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response


class ListaAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'pessoa': i.pessoa.nome} for i in atividades]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa': atividade.pessoa.nome,
            'nome': atividade.nome,
            'id': atividade.id
        }
        print(dados)
        print(pessoa)
        print(response)
        return response


api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListaPessoas, '/pessoa/')
api.add_resource(ListaAtividades, '/atividades/')

if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False  # coloquei pra poder sair mensagem acentuada
    app.run(debug=True)
