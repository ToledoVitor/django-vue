<template>
  <v-layout>
    <h2 class="busca">FAÇA SUA BUSCA</h2>
    <v-textarea rows="1" outlined label="Digite o que quer buscar" required v-model="info" />
    <div class="buttonn">
      <a href="#" @click="search(info)">Buscar</a>
    </div>
    <div v-if="searched">
      <h3 class="results"><span>Esses são os resultados da sua pesquisa!</span></h3>
      <div v-if="search_result.length == 0">
        <br>
        <h3 class="results">Não encontramos nenhum resultado da sua busca.</h3>
      </div>
    </div>
    <div>{{search_result}}</div>
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
      info: ''
    }
  },
  created () {
    AppApi.list_jogos().then(response => {
      this.items = response
    })
  },
  methods: {
    search (info) {
      this.searched = true
      AppApi.search_info(info).then(response => {
        this.search_result = response
      })
    }
  },
  layout: 'complex'
}
</script>

<style>
  .buttonn{
    display: flex;
    justify-content: flex-end;
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
  .results{
    margin-left: 2%;
  }
  .results span{
    color: rgb(25, 118, 210);
    font-size: 30px;
    font-weight: 1000;
  }
</style>
