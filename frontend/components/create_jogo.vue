<template>
  <v-dialog v-model="visible" class="modal" max-width="1000px">
    <v-card>
      <v-card-title class="title">Crie o Seu Jogo!</v-card-title>
      <v-card-text>
        <v-container fluid>
          <v-card-subtitle class="subtitle"> Quem está criando?</v-card-subtitle>
          <v-textarea rows="1" outlined label="Coloque seu Nome" required v-model="criador" />
          <v-card-subtitle class="subtitle"> Qual jogo você quer jogar?</v-card-subtitle>
          <v-textarea input rows="1" outlined label="Coloque o Jogo" required v-model="esporte" />
          <v-card-subtitle class="subtitle"> Que dia você quer jogar?</v-card-subtitle>
          <v-textarea rows="1" outlined label="Coloque a Data" required v-model="data" />
          <v-card-subtitle class="subtitle"> Que horas você quer jogar?</v-card-subtitle>
          <v-textarea rows="1" outlined label="Coloque a Hora" required v-model="horas" />
          <v-card-subtitle class="subtitle"> Quer colocar algo na sua descrição?</v-card-subtitle>
          <v-textarea rows="1" outlined label="Uma Breve descrição" required v-model="descricao" />
          <v-card-subtitle class="subtitle"> Qual a foto do seu jogo?</v-card-subtitle>
          <v-textarea rows="1" outlined label="seuesporte.png" required v-model="imagem" />
          <small class="erro" v-if="error">FALHOU</small>
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
      data: '',
      horas: '',
      descricao: '',
      imagem: '',
      participantes: [],
      loading: false,
      error: false
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
</style>
