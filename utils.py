from models import Pessoas, Usuarios


def insere_pessoas():
    pessoa1 = Pessoas(nome='Claudinei', idade=42)
    pessoa2 = Pessoas(nome='Polyana', idade=32)
    print(pessoa1, pessoa2)
    pessoa1.save()
    pessoa2.save()


def consulta_tudo():
    pessoa = Pessoas.query.all()
    print(pessoa)


def consulta_unica():
    pessoa = Pessoas.query.filter_by(nome='Claudinei').first()
    print('Nome: {}\nIdade: {}'.format(pessoa.nome, pessoa.idade))


def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Claudinei').first()
    pessoa.nome = 'Novo Claudinei Alterado'
    pessoa.idade = 18
    pessoa.save()
    print('Nome: {}\nIdade: {}'.format(pessoa.nome, pessoa.idade))


def exclui_pessoa():
    try:
        pessoa = Pessoas.query.filter_by(nome='Claudinei').first()
        print('Apagado !!\nNome: {}\nIdade: {}'.format(pessoa.nome, pessoa.idade))
        pessoa.delete()
    except AttributeError:
        print('Houve um erro ao encontrar a pessoa.')
#    finally:
#        consulta_tudo()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    insere_usuario('teste1', 'senha')
    insere_usuario('claudinei', '123')
    consulta_todos_usuarios()
    #insere_pessoas()
    #consulta_tudo()
    # consulta_unica()
    # altera_pessoa()
    #exclui_pessoa()
    #consulta_tudo()
