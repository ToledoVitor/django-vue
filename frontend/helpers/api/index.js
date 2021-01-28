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
  }
  // add_jogos (newtask) {
  //   return post('/api/add_jogos', {new_task: newtask})
  // }
}
