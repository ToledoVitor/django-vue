import {get, post} from './ajaxutils'

export default {
  login (username, password) {
    return post('/api/login', {username, password})
  },
  logout () {
    return post('/api/logout')
  },
  whoami () {
    return get('/api/whoami')
  },
  settings () {
    return get('/api/settings')
  },
  list_jogos () {
    return get('/api/list_jogos')
  },
  create_jogo (criador, esporte, data, horas, descricao, imagem, participantes) {
    return post('api/creategame', {criador, esporte, data, horas, descricao, imagem, participantes})
  }
}
