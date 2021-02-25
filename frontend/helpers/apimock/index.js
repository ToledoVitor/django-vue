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
  }
}
