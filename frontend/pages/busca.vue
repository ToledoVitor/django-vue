<template>
  <v-layout>
    <v-input>Insira aqui</v-input>
    <v-textarea rows="1" outlined label="Digite o que quer buscar" required v-model="criador" />
    <div class="create">
      <a href="#" @click="search()">Buscar</a>
    </div>
    <div v-if="searched">
      <h3>Esse são os resultados da sua pesquisa!</h3>
    </div>
  </v-layout>
</template>

<script>
export default {
  data () {
    return {
      searched: false
    }
  },
  methods: {
    search (info) {
      this.searched = true
      return info
    }
  },
  layout: 'complex'
}
</script>

<style>
  .create .a{
    display: flex;
    text-align: end;
    width: 40px;
    height: 20px;
    background-color: rgb(0, 0, 0);
    border-radius: 20px;
    transition: 0.3s;
    transition-property: color, background;
  }
  .create .a :hover{
    color: rgb(0, 0, 0);
    background: #fff;
  }
</style>
