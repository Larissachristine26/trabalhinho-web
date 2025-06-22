<template>
  <div>
    <nav>
      <router-link to="/">Cursos</router-link> |
      <router-link to="/alunos">Alunos</router-link>
    </nav>
    <main>
      <router-view></router-view>
    </main>
  </div>
</template>

<style>
nav {
  padding: 10px;
  background-color: #eee;
}
nav a {
  margin: 0 10px;
  text-decoration: none;
  color: #333;
}
nav a.router-link-active {
  font-weight: bold;
  color: #000;
}
main {
  padding: 20px;
}
</style>
