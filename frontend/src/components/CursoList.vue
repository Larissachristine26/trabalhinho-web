<template>
  <div>
    <h2>Cursos</h2>

    <form @submit.prevent="criarCurso">
      <input v-model="curso.nome" placeholder="Nome" required />
      <input v-model="curso.descricao" placeholder="Descrição" required />
      <input v-model.number="curso.carga_horaria" type="number" placeholder="Carga Horária" required />
      <button type="submit">Criar</button>
    </form>

    <ul>
      <li v-for="c in cursos" :key="c.id">
        {{ c.nome }} ({{ c.carga_horaria }}h)
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      cursos: [],
      curso: {
        nome: "",
        descricao: "",
        carga_horaria: null, // 🔧 Usar `null` para campo numérico
      },
    };
  },
  methods: {
    async listarCursos() {
      const res = await axios.get("http://localhost:5000/cursos");
      this.cursos = res.data;
    },
    async criarCurso() {
      await axios.post("http://localhost:5000/cursos", this.curso);
      this.curso = { nome: "", descricao: "", carga_horaria: null };
      this.listarCursos();
    },
  },
  mounted() {
    this.listarCursos();
  },
};
</script>
