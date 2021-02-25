<template>
  <v-layout class="layout">
    <h1 class="titulo">Bem Vindo ao</h1>
    <h1 class="titulo"><span>Seu Perfil!</span></h1>
    <v-spacer />
    <div v-if="logged_user">
      <h2 class="subtitulo">Confira os jogos que você <span>vai jogar</span>:</h2>
      <h3 v-if="user_participando.length == 0" class="mensagemm"> Opa, parece que você ainda não decidiu jogar nada.</h3>
      <v-flex d-flex :items="items" class="lista">
        <v-flex md4 v-for="(jogo, index) in user_participando" v-bind:key="index" class="container">
          <v-card class="card-container mx-auto" width="100%">
            <v-img class="white--text align-end" height="200px" :src="jogo.imagem">
              <v-card-title class="jogo">{{jogo.esporte}}</v-card-title>
            </v-img>
            <v-card-subtitle class="pb-0" @click="change_page(jogo.criador)">{{jogo.criador}}</v-card-subtitle>
            <v-card-text class="text--primary">
              <div>Jogo {{jogo.dia}} as {{jogo.horas}}</div>
              <div>{{jogo.descricao}}</div>
            </v-card-text>
            <v-card-actions>
              <div v-if="logged_user">
                <v-btn v-if="jogo.participantes.includes(logged_user.username)" color="orange" @click="desparticipar(logged_user.username, JSON.stringify(jogo))" text>Não Participar</v-btn>
                <v-btn v-if="!(jogo.participantes.includes(logged_user.username))" color="orange" @click="participar(logged_user.username, JSON.stringify(jogo))" text>Participar</v-btn>
                <v-btn color="orange" @click="send_message(jogo)" text>Compartilhe</v-btn>
              </div>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-flex>
      <h2 class="subtitulo">Confira os jogos criados <span>por você!</span></h2>
      <h3 v-if="user_jogos.length == 0" class="mensagemm"> Opa, parece que você não criou nenhum jogo ainda.</h3>
      <v-flex d-flex :items="items" class="lista">
        <v-flex md4 v-for="(jogo, indexx) in user_jogos" v-bind:key="indexx" class="container">
          <v-card class="card-container mx-auto" width="100%">
            <v-img class="white--text align-end" height="200px" :src="jogo.imagem">
              <v-card-title>{{jogo.esporte}}</v-card-title>
            </v-img>
            <v-card-text class="text--primary">
              <div>Data: {{jogo.dia}}</div>
              <div>Horário: {{jogo.horas}}</div>
              <div>{{jogo.descricao}}</div>
            </v-card-text>
            <v-card-actions>
              <div v-if="logged_user">
                <v-btn v-if="jogo.participantes.includes(logged_user.username)" color="orange" @click="desparticipar(logged_user.username, JSON.stringify(jogo))" text>Não Participar</v-btn>
                <v-btn v-if="!(jogo.participantes.includes(logged_user.username))" color="orange" @click="participar(logged_user.username, JSON.stringify(jogo))" text>Participar</v-btn>
                <v-btn color="orange" @click="send_message(jogo)" text>Compartilhe</v-btn>
              </div>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-flex>
    </div>
    <div v-if="logged_user == null">
      <h2 class="subtitulo">Você Pecisa Fazer Login Antes de Ver Seu Perfil!</h2>
    </div>
  </v-layout>
</template>

<script>
import AppApi from '~api'

export default {
  data () {
    return {
      items: [],
      user_jogos: [],
      user_participando: []
    }
  },
  computed: {
    logged_user () {
      return this.$store.state.auth.currentUser
    }
  },
  created () {
    AppApi.list_for_user().then(response => {
      this.items = response
      let counter = 0
      for (counter = 0; counter < this.items.length; counter++) {
        if (this.items[counter].criador === this.logged_user.username) { this.user_jogos.push(this.items[counter]) }
        if (this.items[counter].participantes.includes(this.logged_user.username)) { this.user_participando.push(this.items[counter]) }
      }
      return {}
    })
  },
  methods: {
    participar (username, jogo) {
      AppApi.participate(username, jogo).then(result => {
        document.location.reload()
      })
    },
    desparticipar (username, jogo) {
      AppApi.unparticipate(username, jogo).then(result => {
        document.location.reload()
      })
    },
    change_page (criador) {
      const dist = criador
      if (dist !== '') {
        window.location.href = '/user/' + dist
      }
    },
    send_message (item) {
      AppApi.send_message(item)
    }
  },
  head () {
    return {
      title: 'Perfil'
    }
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
    color: #1976d2;
  }
  .subtitulo{
    margin: 30px 0px 5px 30px !important;
    text-size-adjust: auto;
  }
  .subtitulo span{
    color: #1976d2;
  }
  .lista{
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    max-width: 35%;
    margin: 5px;
  }
  .mensagemm{
    display: flex;
    justify-content: flex-start;
    margin-left: 5%;
    color: #d1d1d1;
  }
  .container{
    padding: 0;
    margin: 5px, 5px, 5px, 5px;
  }
  .jogo{
    font-size: 15px;
  }
</style>
