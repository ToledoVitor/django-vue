<template>
  <v-layout>
    <h2 class="busca">FAÇA SUA BUSCA</h2>
    <v-select :items="esportes" prepend-icon="mdi-basketball" label="Busque Aqui" outlined v-model="esporte" />
    <div class="buttonn">
      <a href="#" @click="search(esporte)" class="botao">Buscar</a>
    </div>
    <div v-if="searched">
      <v-card class="card-container mx-auto" width="98%">
        <v-img class="white--text align-end" height="200px" :src="esporte_searched + '.jpg'">
          <v-card-title class="esporte">{{esporte_searched}}</v-card-title>
        </v-img>
      </v-card>
      <h3 class="results"><span>Esses são os resultados da sua pesquisa!</span></h3>
      <div v-if="search_result.length == 0">
        <br>
        <h3 class="results">Não encontramos nenhum resultado da sua busca.</h3>
      </div>
      <v-flex d-flex :item="item" class="lista">
        <v-flex md4 v-for="(jogo, index) in search_result" v-bind:key="index" class="container">
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
  </v-layout>
</template>

<script>
import AppApi from '~api'

export default {
  data () {
    return {
      items: [],
      searched: false,
      search_result: [],
      esporte: '',
      esporte_searched: '',
      esportes: ['Baseball', 'Basquete', 'Futebol', 'Futebol Americano', 'Tênis', 'Volei']
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
    search (busca) {
      this.searched = true
      this.esporte_searched = busca
      AppApi.search_info(busca).then(response => {
        this.search_result = response
      })
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
      title: 'Busca'
    }
  },
  layout: 'complex'
}
</script>

<style scoped>
  .buttonn{
    display: flex;
    justify-content: flex-end;
    margin-right: 5%;
    font-size: 20px;
    font-weight: 1000 !important;
  }
  .buttonn .a{
    display: flex;
    position: relative;
    text-align: end;
    width: 40px;
    height: 20px;
    color: #fff;
    font-size: 20px;
    font-weight: 500;
    text-decoration: none;
    background-color: rgb(0, 0, 0);
    border-radius: 20px;
    transition: 0.3s;
    transition-property: color, background;
  }
  .buttonn .a :hover{
    color: rgb(0, 0, 0);
    background: #fff;
  }
  .botao {
    margin-bottom: 30px;
  }
  .busca{
    display: flex;
    justify-content: flex-start;
    text-transform: uppercase;
    width: 100%;
    margin-top: 2% ;
    margin-left: 2%;
    margin-bottom: 5px;
    font-size: 35px;
    line-height: 50px;
  }
  .v-select{
    width: 95%;
  }
  .results{
    margin-left: 2%;
  }
  .results span{
    color: rgb(255, 255, 255);
    font-size: 30px;
    font-weight: 1000;
    text-shadow: 3px 3px black;
    background-color: rgba(255, 255, 255, 0.100);
  }
</style>
