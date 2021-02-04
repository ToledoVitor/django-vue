<template>
  <v-dialog v-model="visible" class="modal" max-width="1000px">
    <v-card>
      <v-card-title class="title">Crie o Seu Jogo!</v-card-title>
      <v-card-text>
        <v-container fluid>
          <v-card-subtitle class="subtitle"> Qual jogo você quer jogar?</v-card-subtitle>
          <v-select :items="esportes" prepend-icon="mdi-basketball" outlined v-model="esporte" hide-details />
          <v-card-subtitle class="subtitle"> Que dia você quer jogar?</v-card-subtitle>
          <v-menu
            v-model="menu"
            :close-on-content-click="false"
            :nudge-right="40"
            transition="scale-transition"
            offset-y
            min-width="auto"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                v-model="dia"
                prepend-icon="mdi-calendar"
                readonly
                v-bind="attrs"
                v-on="on"
                outlined
                hide-details
              />
            </template>
            <v-date-picker
              v-model="dia"
              @input="menu = false"
            />
          </v-menu>
          <v-card-subtitle class="subtitle"> Que horas você quer jogar?</v-card-subtitle>
          <v-menu ref="menu" v-model="menu1" :close-on-content-click="false" :nudge-right="40" :return-value.sync="time" transition="scale-transition" offset-y max-width="290px" min-width="290px">
            <template v-slot:activator="{ on, attrs }">
              <v-text-field v-model="horas" outlined prepend-icon="mdi-clock-time-four-outline" readonly v-bind="attrs" v-on="on" hide-details />
            </template>
            <v-time-picker v-if="menu1" v-model="horas" full-width @click:minute="$refs.menu.save(time)" />
          </v-menu>
          <v-card-subtitle class="subtitle"> Quer colocar algo na sua descrição?</v-card-subtitle>
          <v-textarea rows="1" outlined prepend-icon="mdi-pencil" required v-model="descricao" hide-details />
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-spacer />
        <v-btn class="blue--text darken-1" text @click="close()">Cancelar</v-btn>
        <v-btn class="blue--text darken-1" text @click="create_jogo()" :loading="loading" :disabled="loading">Cadastrar</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import AppApi from '~api'

export default {
  data () {
    return {
      items: [],
      visible: false,
      criador: '',
      esporte: '',
      dia: '',
      horas: '',
      descricao: '',
      imagem: '',
      participantes: [],
      esportes: ['Baseball', 'Basquete', 'Futebol', 'Futebol Americano', 'Tênis', 'Vôlei'],
      loading: false,
      error: false,
      time: null,
      menu: false,
      menu1: false
    }
  },
  computed: {
    logged_user () {
      return this.$store.state.auth.currentUser
    }
  },
  methods: {
    open () {
      this.visible = true
    },
    close () {
      this.visible = false
    },
    create_jogo () {
      this.loading = true
      this.error = false
      this.criador = this.logged_user.username
      this.participantes = ''
      this.imagem = this.esporte.replace(/ /g, '') + '.jpg'
      const jogo = AppApi.create_jogo(this.criador, this.esporte, this.dia, this.horas, this.descricao, this.imagem, this.participantes).then(() => {
        document.location.reload()
      })
      if (jogo) {
        this.close()
      } else {
        this.error = true
      }
    }
  }
}
</script>

<style>
  .modal {
    position: fixed;
    z-index: 2;
  }
  .title {
    display: flex;
    text-transform: uppercase;
    font-weight: 800 !important;
    letter-spacing: 1px !important;
    justify-content: center;
    padding: 0
  }
  .subtitle {
    margin: 0px;
    padding: 4px !important;
    color: #fff !important;
    font-weight: 650 !important;
  }
  .v-text-field__details{
    height: 0;
  }
  .v-text-field{
    margin-bottom: 2px;
  }
</style>
