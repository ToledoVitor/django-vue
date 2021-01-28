<template>
  <body>
    <div class="padrao">
      <h1 class="titulo">Bem vindo ao perfil do usuário <span>{{username}}!</span></h1>
      <v-spacer />
      <h3 class="subtitulo">Confira os jogos criados por {{username}}:</h3>
      <!-- <v-for jogo in jogos :key="jogo">
          <v-if jogo.criador = "username">Nenhum jogo criado pelo usuário</v-if> -->
      <v-if jogos="">
        <h3 class="subtitulo">Nenhum jogo criado pelo usuário</h3>
      </v-if>
    </div>
  </body>
</template>

<script>
export default {
  data () {
    return {
      jogos: ''
    }
  },
  asyncData (context) {
    const username = context.params.username
    return {
      username
    }
    //     return Promise.all(
    //     })
    //       username: context.params.username
    //     }
  }
}
</script>

<style>
  .padrao{
    margin-top: 60px;
    margin-left: 60px;
  }
  .titulo{
    display: flex;
    justify-content: center;
    margin: 20px;
  }
  .titulo span{
    color: #19B3D3;
  }
  .subtitulo{
    margin: 10px;
  }
</style>
