<template>
  <v-layout class="layout">
    <div class="padrao">
      <h1 class="titulo">Bem vindo ao perfil do usuário</h1>
      <h1 class="titulo"><span>{{username}}!</span></h1>
      <v-spacer />
      <h2 class="subtitulo">Confira os jogos que <span>{{username}}</span> vai jogar:</h2>
      <h3 v-if="user_jogos.length == 0" class="mensagemm"> Pelo visto o usuário não criou nenhum jogo ainda.</h3>
      <v-flex d-flex :items="items" class="lista">
        <v-flex md4 v-for="(jogo, indexx) in user_participando" v-bind:key="indexx" class="container">
          <v-card class="card-container mx-auto" width="100%">
            <v-img class="white--text align-end" height="200px" :src="formata(jogo.imagem)">
              <v-card-title>{{jogo.esporte}}</v-card-title>
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
            <v-card-actions>
              <div v-if="logged_user == null">
                <v-btn color="orange" text>Participe</v-btn>
                <v-btn color="orange" text>Compartilhe</v-btn>
              </div>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-flex>
      <h2 class="subtitulo">Confira os jogos criados por<span> {{username}}</span>!</h2>
      <h3 v-if="user_jogos.length == 0" class="mensagemm"> Opa, parece que você não criou nenhum jogo ainda.</h3>
      <v-flex d-flex :items="items" class="lista">
        <v-flex md4 v-for="(jogo, index) in user_jogos" v-bind:key="index" class="container">
          <v-card class="card-container mx-auto" width="100%">
            <v-img class="white--text align-end" height="200px" :src="formata(jogo.imagem)">
              <v-card-title>{{jogo.esporte}}</v-card-title>
            </v-img>
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
  computed: {
    logged_user () {
      return this.$store.state.auth.currentUser
    }
  },
  asyncData (context) {
    const username = context.params.username
    return {
      username
    }
  },
  created () {
    AppApi.list_for_user().then(response => {
      this.items = response
      let counter = 0
      for (counter = 0; counter < this.items.length; counter++) {
        if (this.items[counter].criador === this.username) { this.user_jogos.push(this.items[counter]) }
        if (this.items[counter].participantes.includes(this.username)) { this.user_participando.push(this.items[counter]) }
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
    },
    formata (imagem) {
      imagem = 'http://localhost/' + imagem
      return imagem
    }
  },
  head () {
    return {
      title: 'Usuário'
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
    color:#1976d2;
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
