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
      this.text += `Ae, se liga nesse jogo aqui \n \n`
      this.text += `A galera vai jogar *${item.esporte}*, `
      this.text += `e jogo vai ser dia *${item.data}* as *${item.horas}* \n`
      this.text += `Ah, e quem criou o jogo foi *${item.criador}*. \n`
      this.text += `Bora jogar também??\n \n`
      this.text += `Quer achar mais jogos como esse? \n`
      this.text += `*https://esporte.se*`
      this.apilink = 'http://'
      this.apilink += 'web'
      this.apilink +=
        '.whatsapp.com/send?phone=5511974648475' +
        '&text=' +
        encodeURI(this.text)
      window.open(this.apilink)
    },
    isMobile () {
      let check = false;
      (function (a) {
        if (
          /(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce|xda|xiino/i.test(
            a
          ) ||
          /1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw-(n|u)|c55\/|capi|ccwa|cdm-|cell|chtm|cldc|cmd-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc-s|devi|dica|dmob|do(c|p)o|ds(12|-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(-|_)|g1 u|g560|gene|gf-5|g-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd-(m|p|t)|hei-|hi(pt|ta)|hp( i|ip)|hs-c|ht(c(-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i-(20|go|ma)|i230|iac( |-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|-[a-w])|libw|lynx|m1-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|-([1-8]|c))|phil|pire|pl(ay|uc)|pn-2|po(ck|rt|se)|prox|psio|pt-g|qa-a|qc(07|12|21|32|60|-[2-7]|i-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h-|oo|p-)|sdk\/|se(c(-|0|1)|47|mc|nd|ri)|sgh-|shar|sie(-|m)|sk-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h-|v-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl-|tdg-|tel(i|m)|tim-|t-mo|to(pl|sh)|ts(70|m-|m3|m5)|tx-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas-|your|zeto|zte-/i.test(
            a.substr(0, 4)
          )
        ) {}
        check = true
      })(navigator.userAgent || navigator.vendor || window.opera)
      return check
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
