<template>
  <v-layout class="layout">
    <h2 class="titulo">Confira os jogos.<br>Encontre o seu!</h2>
    <v-flex d-flex :items="items" class="lista">
      <v-flex md4 v-for="item in items" :key="item" class="container">
        <v-card class="card-container mx-auto" width="100%">
          <v-img class="white--text align-end" height="200px" :src="item.imagem">
            <v-card-title>{{item.esporte}}</v-card-title>
          </v-img>
          <v-card-subtitle class="pb-0">{{item.criador}}</v-card-subtitle>
          <v-card-text class="text--primary">
            <div>Jogo {{item.eia}} as {{item.horas}}</div>
            <div>{{item.descricao}}</div>
          </v-card-text>
          <v-card-actions>
            <v-btn color="orange" text>Participe</v-btn>
            <v-btn color="orange" text>Compartilhe</v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-flex>
    <h2 class="titulo">Não achou o jogo que estava procurando?</h2>
    <div>
      <link rel="stylesheet" href="style.css">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css">
      <div class="create">
        <a href="#" onclick="location.href = '/';">Crie ele Agora!</a>
      </div>
    </div>
  </v-layout>
</template>

<script>
import AppApi from '~api'

export default {
  data () {
    return {
      items: []
    }
  },
  created () {
    AppApi.list_jogos().then(response => {
      console.log(response)
      debugger
      this.items = response
    })
  },
  layout: 'complex'
}
</script>

<style>
  .titulo{
      display: flex;
      width: 100%;
      justify-content: center;
      text-transform: uppercase;
      font-size: 45px;
      line-height: 50px;
  }
  .layout{
    display: flex;
    flex-direction: column;
  }
  .lista{
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    max-width: 35%;
    margin: 5px;
  }
  .container{
    padding: 0;
    margin: 5px, 5px, 5px, 5px;
  }
  .create a{
    position: relative;
    color: #fff;
    left: 33%;
    width: 34%;
    display: flex;
    justify-content: center;
    font-size: 50px;
    font-weight: 500;
    text-decoration: none;
    margin: 0 30px;
    border-radius: 20px;
    transition: 0.3s;
    transition-property: color, background;
  }
  .create a:hover{
    color: rgb(0, 0, 0);
    background: #fff;
  }
</style>
