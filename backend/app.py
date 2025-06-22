from flask import Flask, request, jsonify
from flask_cors import CORS
from pony.orm import db_session, flush
from database import db, Curso, Aluno

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({"message": "API Flask está rodando na porta 5000."})

# ===== ROTAS CURSO =====
@app.route('/cursos', methods=['POST'])
@db_session
def criar_curso():
    data = request.json
    curso = Curso(**data)
    flush()
    return jsonify({"id": curso.id}), 201

@app.route('/cursos', methods=['GET'])
@db_session
def listar_cursos():
    return jsonify([c.to_dict() for c in Curso.select()])

@app.route('/cursos/<int:curso_id>', methods=['GET'])
@db_session
def obter_curso(curso_id):
    curso = Curso.get(id=curso_id)
    return jsonify(curso.to_dict()) if curso else ("Not Found", 404)

@app.route('/cursos/<int:curso_id>', methods=['PUT'])
@db_session
def atualizar_curso(curso_id):
    data = request.json
    curso = Curso.get(id=curso_id)
    if not curso:
        return ("Not Found", 404)
    curso.set(**data)
    return jsonify({"message": "Atualizado com sucesso"})

@app.route('/cursos/<int:curso_id>', methods=['DELETE'])
@db_session
def deletar_curso(curso_id):
    curso = Curso.get(id=curso_id)
    if not curso:
        return ("Not Found", 404)
    curso.delete()
    return jsonify({"message": "Curso deletado"})

# ===== ROTAS ALUNO =====
@app.route('/alunos', methods=['POST'])
@db_session
def criar_aluno():
    data = request.json
    curso = Curso.get(id=data["curso"])
    if not curso:
        return jsonify({"error": "Curso não encontrado"}), 404
    aluno = Aluno(nome=data["nome"], idade=data["idade"], cidade=data["cidade"], curso=curso)
    flush()
    return jsonify({"id": aluno.id}), 201

@app.route('/alunos', methods=['GET'])
@db_session
def listar_alunos():
    return jsonify([a.to_dict() for a in Aluno.select()])

@app.route('/alunos/<int:aluno_id>', methods=['GET'])
@db_session
def obter_aluno(aluno_id):
    aluno = Aluno.get(id=aluno_id)
    return jsonify(aluno.to_dict()) if aluno else ("Not Found", 404)

@app.route('/alunos/<int:aluno_id>', methods=['PUT'])
@db_session
def atualizar_aluno(aluno_id):
    data = request.json
    aluno = Aluno.get(id=aluno_id)
    if not aluno:
        return ("Not Found", 404)
    if "curso" in data:
        curso = Curso.get(id=data["curso"])
        if not curso:
            return jsonify({"error": "Curso não encontrado"}), 404
        aluno.curso = curso
    aluno.set(**{k: v for k, v in data.items() if k != "curso"})
    return jsonify({"message": "Atualizado com sucesso"})

@app.route('/alunos/<int:aluno_id>', methods=['DELETE'])
@db_session
def deletar_aluno(aluno_id):
    aluno = Aluno.get(id=aluno_id)
    if not aluno:
        return ("Not Found", 404)
    aluno.delete()
    return jsonify({"message": "Aluno deletado"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
