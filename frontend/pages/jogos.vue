<template>
  <v-layout class="layout">
    <h2 class="titulo">Confira os jogos.<br>Encontre o seu!</h2>
    <div class="links">
      <a href="#Baseball">Baseball</a>
      <a href="#Basquete">Basquete</a>
      <a href="#Futebol">Futebol</a>
      <a href="#Futebol Americano">Futebol Americano</a>
      <a href="#Tenis">Tênis</a>
      <a href="#Vôlei">Vôlei</a>
    </div>
    <div v-for="(item, indexxx) in items" v-bind:key="indexxx">
      <a :id="item.esporte" />
      <v-card class="card-container mx-auto" width="98%">
        <v-img class="white--text align-end" height="200px" :src="item.esporte + '.jpg'">
          <v-card-title class="esporte">{{item.esporte}}</v-card-title>
        </v-img>
      </v-card>
      <v-flex d-flex class="lista">
        <v-flex md4 v-for="(jogo, indexx) in item.jogos" v-bind:key="indexx" class="container">
          <v-card class="card-container mx-auto" width="100%">
            <v-card-subtitle class="pb-0" @click="change_page(jogo.criador)">{{jogo.criador}}</v-card-subtitle>
            <v-card-text class="text--primary" padding="0px 16px 0px 16px;">
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
            <v-card-actions>
              <div v-if="logged_user == null">
                <v-btn color="orange" text>Participe</v-btn>
                <v-btn color="orange" text>Compartilhe</v-btn>
              </div>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-flex>
    </div>
    <h2 class="titulo">Não achou o jogo que estava procurando?</h2>
    <div>
      <link rel="stylesheet" href="style.css">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css">
      <div v-if="logged_user" class="create">
        <a href="#" @click="open_button($event)">Crie ele Agora!</a>
        <createjogo ref="create_jogo" />
      </div>
      <div v-if="logged_user == null" class="create">
        <a href="#">Crie ele Agora!</a>
        <h3>Opa, parece que você não está logado ainda. Faça login primeiro!</h3>
      </div>
    </div>
  </v-layout>
</template>

<script>
import AppApi from '~api'
import createjogo from '~/components/create_jogo.vue'

export default {
  components: {
    createjogo
  },
  data () {
    return {
      items: [],
      criador: '',
      esporte: '',
      data: '',
      horas: '',
      descricao: '',
      imagem: '',
      participantes: [],
      text: '',
      game: '',
      esporte_list: [{esporte: 'Baseball', jogos: []}, {esporte: 'Basquete', jogos: []}, {esporte: 'Futebol', jogos: []}, {esporte: 'Futebolameric', jogos: []}, {esporte: 'Tenis', jogos: []}, {esporte: 'Volei', jogos: []}]
    }
  },
  computed: {
    logged_user () {
      return this.$store.state.auth.currentUser
    }
  },
  created () {
    AppApi.list_jogos().then(response => {
      this.items = response
    })
  },
  methods: {
    open () {
      this.visible = true
    },
    close () {
      this.visible = false
    },
    open_button (clique) {
      this.$refs.create_jogo.open()
      clique.stopPropagation()
    },
    change_page (criador) {
      const dist = criador
      if (dist !== '') {
        window.location.href = '/user/' + dist
      }
    },
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
    send_message (item) {
      AppApi.send_message(item)
    }
  },
  head () {
    return {
      title: 'Jogos'
    }
  },
  layout: 'complex'
}
</script>

<style>
  .titulo{
    display: flex;
    justify-content: center;
    text-align: center;
    text-transform: uppercase;
    width: 100%;
    font-size: 45px;
    line-height: 50px;
    margin-top: 20px;
  }
  .links{
    flex-direction: column;
    justify-content: center;
    margin-top: 20px;
  }
  .layout{
    display: flex;
    flex-direction: column;
    margin-top: 60px;
  }
  .lista{
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    max-width: 35%;
    margin: 5px;
  }
  .mensagem{
    display: flex;
    justify-content: center;
  }
  .container{
    padding: 0;
    margin: 5px, 5px, 5px, 5px;
  }
  .create a{
    display: flex;
    position: relative;
    justify-content: center;
    flex-grow: 0;
    color: #fff;
    font-size: 50px;
    font-weight: 500;
    text-decoration: none;
    border-radius: 20px;
    transition: 0.3s;
    transition-property: color, background;
    max-width: 450px;
  }
  .create a:hover{
    color: rgb(0, 0, 0);
    background: #fff;
  }
  .v-card__text.text--primary{
    padding: 0px 16px 0px 16px;
  }
  .create{
    display: flex;
    justify-content: center;
  }
  .esporte{
    margin-top: -120px;
    font-size: 50px !important;
    font-weight: 800 !important;
    justify-content: center;
    text-shadow: 5px 5px black;
  }
</style>
