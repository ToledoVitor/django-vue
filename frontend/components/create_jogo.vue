<template>
  <v-dialog v-model="visible" max-width="1000px">
    <v-card>
      <v-card-title>Crie o Seu Jogo</v-card-title>
      <v-card-text>
        <v-container fluid>
          <v-card-subtitle> Quem está criando?</v-card-subtitle>
          <v-textarea rows="1" outlined label="Breve descrição" required v-model="criador" />
          <v-card-subtitle> Qual jogo você quer jogar?</v-card-subtitle>
          <v-textarea rows="1" outlined required v-model="esporte" />
          <v-card-subtitle> Quando dia você quer jogar?</v-card-subtitle>
          <v-textarea rows="1" outlined label="Breve descrição" required v-model="data" />
          <v-card-subtitle> Que horas você quer jogar?</v-card-subtitle>
          <v-textarea rows="1" outlined label="Breve descrição" required v-model="horas" />
          <v-card-subtitle> Quer colocar algo na sua descrição?</v-card-subtitle>
          <v-textarea rows="1" outlined label="Breve descrição" required v-model="descricao" />
          <v-card-subtitle> Qual a foto do seu jogo?</v-card-subtitle>
          <v-textarea rows="1" outlined label="Breve descrição" required v-model="imagem" />
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
      const jogo = AppApi.create_jogo(this.criador, this.esporte, this.data, this.horas, this.descricao, this.imagem).then(() => {
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
  v-dialog{
    opacity: 0.5;
  }
</style>
