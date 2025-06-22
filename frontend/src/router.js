import { createRouter, createWebHistory } from "vue-router";
import CursoList from "./components/CursoList.vue";
import AlunoList from "./components/AlunoList.vue";

// Definição das rotas
const routes = [
  { path: "/", component: CursoList },
  { path: "/alunos", component: AlunoList },
];

// Criação e exportação do roteador
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
