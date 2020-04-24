from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# engine é pra definir o banco de dados, unicode true é pra usar acentos
engine = create_engine('sqlite:///atividades.db',
                       convert_unicode=True)
# vai criar a sessao do banco de dados, com comitt falso no caso, preciso criar uma funcao pra salvar
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))  # engine é o banco que vai usar a sessao

# Base é default do sqlalchemy
# cria a base pra ser usada nos models
Base = declarative_base()
Base.query = db_session.query_property()


class Pessoas(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)

    def __repr__(self):
        return '<Pessoa {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Atividades(Base):
    __tablename__ = 'atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship("Pessoas")

    def __repr__(self):
        return '<Atividade {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


def init_db():
    # esse comando vai criar o banco de dados
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
    #so vai criar o banco se rodar esse arquivo como main