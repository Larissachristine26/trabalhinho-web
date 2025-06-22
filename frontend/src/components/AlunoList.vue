<template>
  <div>
    <h2>Alunos</h2>

    <form @submit.prevent="criarAluno">
      <input v-model="aluno.nome" placeholder="Nome" required />
      <input v-model.number="aluno.idade" type="number" placeholder="Idade" required />
      <input v-model="aluno.cidade" placeholder="Cidade" required />

      <!-- Select de cursos -->
      <select v-model="aluno.curso" required>
        <option disabled value="">Selecione um curso</option>
        <option v-for="curso in cursos" :key="curso.id" :value="curso.id">
          {{ curso.nome }}
        </option>
      </select>

      <button type="submit">Cadastrar</button>
    </form>

    <ul>
      <li v-for="a in alunos" :key="a.id">
        {{ a.nome }} ({{ a.idade }} anos) - {{ a.cidade }} -
        Curso: {{ nomeCurso(a.curso) }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      alunos: [],
      cursos: [],
      aluno: { nome: "", idade: null, cidade: "", curso: "" },
    };
  },
  methods: {
    async listarAlunos() {
      const res = await axios.get("http://localhost:5000/alunos");
      this.alunos = res.data;
    },
    async listarCursos() {
      const res = await axios.get("http://localhost:5000/cursos");
      this.cursos = res.data;
    },
    async criarAluno() {
      await axios.post("http://localhost:5000/alunos", this.aluno);
      this.aluno = { nome: "", idade: null, cidade: "", curso: "" };
      this.listarAlunos();
    },
    nomeCurso(idCurso) {
      const curso = this.cursos.find(c => c.id === idCurso);
      return curso ? curso.nome : "Desconhecido";
    },
  },
  mounted() {
    this.listarAlunos();
    this.listarCursos();
  },
};
</script>
