<template>
  <v-dialog v-model="visible" class="modal" max-width="1000px">
    <v-card>
      <v-card-title class="title">Crie o Seu Jogo!</v-card-title>
      <v-card-text>
        <v-container fluid>
          <v-card-subtitle class="subtitle"> Qual jogo você quer jogar?</v-card-subtitle>
          <v-select :items="esportes" prepend-icon="mdi-basketball" label="Outlined style" outlined v-model="esporte" />
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
                v-model="date"
                label="Picker without buttons"
                prepend-icon="mdi-calendar"
                readonly
                v-bind="attrs"
                v-on="on"
                outlined
              />
            </template>
            <v-date-picker
              v-model="date"
              @input="menu = false"
            />
          </v-menu>
          <v-card-subtitle class="subtitle"> Que horas você quer jogar?</v-card-subtitle>
          <v-menu ref="menu" v-model="menu1" :close-on-content-click="false" :nudge-right="40" :return-value.sync="time" transition="scale-transition" offset-y max-width="290px" min-width="290px">
            <template v-slot:activator="{ on, attrs }">
              <v-text-field v-model="time" label="Picker in menu" outlined prepend-icon="mdi-clock-time-four-outline" readonly v-bind="attrs" v-on="on" />
            </template>
            <v-time-picker v-if="menu1" v-model="time" full-width @click:minute="$refs.menu.save(time)" />
          </v-menu>
          <v-card-subtitle class="subtitle"> Quer colocar algo na sua descrição?</v-card-subtitle>
          <v-textarea rows="1" outlined prepend-icon="mdi-pencil" label="Uma Breve descrição" required v-model="descricao" />
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
      esportes: ['Baseball', 'Basquete', 'Futebol', 'Futebol Americano', 'Tênis', 'Volei'],
      loading: false,
      error: false,
      time: null,
      date: new Date().toISOString().substr(0, 10),
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
      this.esporte = this.esporte.toLowerCase()
      this.criador = this.logged_user.username
      this.imagem = this.esporte.replace(/ /g, '') + 'jpg'
      this.participantes = [this.logged_user.username]
      const jogo = AppApi.create_jogo(this.criador, this.esporte, this.data, this.horas, this.descricao, this.imagem, this.participantes).then(() => {
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
</style>
