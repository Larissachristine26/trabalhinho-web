from pony.orm import Database, Required, Set

db = Database()

class Curso(db.Entity):
    nome = Required(str)
    descricao = Required(str)
    carga_horaria = Required(int)
    alunos = Set("Aluno")

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "carga_horaria": self.carga_horaria
        }

class Aluno(db.Entity):
    nome = Required(str)
    idade = Required(int)
    cidade = Required(str)
    curso = Required(Curso)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "cidade": self.cidade,
            "curso": self.curso.id  # retorna apenas o ID do curso
        }

db.bind(provider='sqlite', filename='db.sqlite', create_db=True)
db.generate_mapping(create_tables=True)

