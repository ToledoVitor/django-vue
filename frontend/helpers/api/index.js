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
  list_for_user () {
    return get('/api/list_for_user')
  },
  create_jogo (criador, esporte, dia, horas, descricao, imagem, participantes = []) {
    return post('/api/creategame', {criador, esporte, dia, horas, descricao, imagem, participantes})
  },
  search_info (info) {
    return get(`/api/search_info/${info}`)
  },
  participate (username, jogo) {
    return post(`/api/participate/username=${username}/jogo=${jogo}`)
  },
  unparticipate (username, jogo) {
    return post(`/api/unparticipate/username=${username}/jogo=${jogo}`)
  }
}
