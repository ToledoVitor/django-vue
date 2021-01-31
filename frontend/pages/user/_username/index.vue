<template>
  <v-layout class="layout">
    <div class="padrao">
      <h1 class="titulo">Bem vindo ao perfil do usuário</h1>
      <h1 class="titulo"><span>{{username}}!</span></h1>
      <v-spacer />
      <h2 class="subtitulo">Confira os jogos criados por <span>{{username}}</span>:</h2>
      <v-flex d-flex :items="items" class="lista">
        <v-flex md4 v-for="jogo in user_jogos" :key="jogo" class="container">
          <v-card class="card-container mx-auto" width="100%">
            <v-img class="white--text align-end" height="200px" :src="jogo.imagem">
              <v-card-title>{{jogo.esporte}}</v-card-title>
            </v-img>
            <v-card-subtitle class="pb-0">{{jogo.criador}}</v-card-subtitle>
            <v-card-text class="text--primary">
              <div>Jogo {{jogo.dia}} as {{jogo.horas}}</div>
              <div>{{jogo.descricao}}</div>
            </v-card-text>
            <v-card-actions>
              <v-btn color="orange" text>Participe</v-btn>
              <v-btn color="orange" text>Compartilhe</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-flex>
      <h2 class="subtitulo">Confira os Jogos Que {{username}} <span>Vai Jogar</span>:</h2>
      <v-flex d-flex :items="items" class="lista">
        <v-flex md4 v-for="jogo in user_participando" :key="jogo" class="container">
          <v-card class="card-container mx-auto" width="100%">
            <v-img class="white--text align-end" height="200px" :src="jogo.imagem">
              <v-card-title>{{jogo.esporte}}</v-card-title>
            </v-img>
            <v-card-subtitle class="pb-0">{{jogo.criador}}</v-card-subtitle>
            <v-card-text class="text--primary">
              <div>Jogo {{jogo.dia}} as {{jogo.horas}}</div>
              <div>{{jogo.descricao}}</div>
            </v-card-text>
            <v-card-actions>
              <v-btn color="orange" text>Participe</v-btn>
              <v-btn color="orange" text>Compartilhe</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-flex>
    </div>
  </v-layout>
</template>

<script>
import AppApi from '~api'

export default {
  components: {
  },
  data () {
    return {
      items: [],
      user_jogos: [],
      user_participando: []
    }
  },
  asyncData (context) {
    const username = context.params.username
    return {
      username
    }
  },
  created () {
    AppApi.list_jogos().then(response => {
      this.items = response
      let counter = 0
      for (counter = 0; counter < this.items.length; counter++) {
        if (this.items[counter].criador === this.username) { this.user_jogos.push(this.items[counter]) }
        if (this.username in this.items[counter].participantes) { this.user_participando.push(this.items[counter]) }
      }
      return {}
    })
  },
  layout: 'complex'
}
</script>

<style>
  .titulo{
    display: flex;
    justify-content: center;
    margin: 0px;
  }
  .titulo span{
    color: #19B3D3;
  }
  .subtitulo{
    margin: 30px;
    text-size-adjust: auto;
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
</style>
