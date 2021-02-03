<template>
  <v-layot class="layout">
    <h1 class="titulo">Bem Vindo ao</h1>
    <h1 class="titulo"><span>Seu Perfil!</span></h1>
    <v-spacer />
    <div v-if="logged_user">
      <h2 class="subtitulo">Confira os jogos criados <span>por você!</span></h2>
      <h3 v-if="user_jogos.length == 0" class="mensagemm"> Opa, parece que você não criou nenhum jogo ainda.</h3>
      <v-flex d-flex :items="items" class="lista">
        <v-flex md4 v-for="jogo in user_jogos" :key="jogo" class="container">
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
              <v-btn color="orange" text>Participe</v-btn>
              <v-btn color="orange" text>Compartilhe</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-flex>
      <h2 class="subtitulo">Confira os jogos que você <span>vai jogar</span>:</h2>
      <h3 v-if="user_participando.length == 0" class="mensagemm"> Opa, parece que você ainda não decidiu jogar nada.</h3>
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
      <h3>{{logged_user}}</h3>
      <h3>{{items}}</h3>
    </div>
    <div v-if="logged_user == null">
      <h2 class="subtitulo">Você Pecisa Fazer Login Antes de Ver Seu Perfil!</h2>
    </div>
  </v-layot>
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
    AppApi.list_jogos().then(response => {
      this.items = response
      let counter = 0
      for (counter = 0; counter < this.items.length; counter++) {
        if (this.items[counter].criador === this.logged_user.username) { this.user_jogos.push(this.items[counter]) }
        if (this.logged_user.username in this.items[counter].participantes) { this.user_participando.push(this.items[counter]) }
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
</style>
