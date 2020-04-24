from models import Pessoas


def insere_pessoas():
    pessoa = Pessoas(nome='Claudinei', idade=42)
    print(pessoa)
    pessoa.save()


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


if __name__ == '__main__':
    # insere_pessoas()
    consulta_tudo()
    # consulta_unica()
    # altera_pessoa()
    exclui_pessoa()
    consulta_tudo()
