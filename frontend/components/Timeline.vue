<template>
  <div>
    <div>
      <v-layout justify-center align-center>
        <v-btn color="success" width="96%" :to="{name: 'todos'}">Partiu Jogar?</v-btn>
      </v-layout>
    </div>
    <div class="cards">
      <v-card max-width="45%" v-for="jogo in jogos" :key="jogo">
        <v-container class="cards" grid-list-xl>
          <v-img class="white--text align-end" width="100%" :src="jogo.imagem" height="200px" />
          <v-card-subtitle class="pb-0"><router-link :to="{name: 'username', params:{username: jogo.Criador}}">Por: {{jogo.Criador}}</router-link></v-card-subtitle>
          <v-card-text class="text--primary">
            <div>{{jogo.Esporte}}</div>
            <div>{{jogo.Horas}}</div>
            <div>{{jogo.Descricao}}</div>
          </v-card-text>
          <v-card-actions class="column_wrapper">
            <v-btn color="orange" text>Participar</v-btn>
            <v-btn color="orange" text>Compartilhar</v-btn>
            <v-btn color="orange" text>Comentar</v-btn>
          </v-card-actions>
        </v-container>
      </v-card>
    </div>
  </div>
</template>

<script>
export default {
  props: ['jogos'],
  data () {
    return {
    }
  }
}
</script>

<style>
  .column_wrapper{
    column-count: 3;
    justify-content: flex-end;
  }
  .v-btn{
    min-width: none;
    max-width: 90%;
    font-size: 0.8em !important;
    justify-content: space-between;
  }
  .v-card{
    margin-block: 20px;
    padding-block: 5px;
  }
  .cards{
    display: flex;
    justify-content: space-around;
    flex-direction: row;
    flex-wrap: wrap;
  }
  .criador{
    padding: 5px;
  }
  .image{
    height: 50px;
    background-repeat: no-repeat;
  }
</style>
