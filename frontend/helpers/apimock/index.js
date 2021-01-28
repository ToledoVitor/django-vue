import { zuck } from './db_people'
import { todos } from './db_todos'
import { mockasync } from './mockutils'

const keepLoggedIn = true

export default {
  login (username, password) {
    return mockasync(zuck)
  },
  logout () {
    return mockasync({})
  },
  whoami () {
    const iam = {authenticated: keepLoggedIn}
    if (iam.authenticated) {
      iam.user = zuck
    }
    return mockasync(iam)
  },
  settings () {
    return mockasync({
      SENTRY_DSN_FRONT: ''
      // SENTRY_DSN_FRONT: 'https://abcd1234@sentry.example.com/10'
    })
  },
  list_todos () {
    return mockasync(todos)
  },
  add_todo (newtask) {
    return mockasync({description: newtask, done: false})
  },
  list_jogos (username) {
    return mockasync({
      jogos: [
        {
          'Criador': 'Criador',
          'Esporte': 'Basquete',
          'Dia': '15/01',
          'Horas': '6 Horas',
          'Descricao': 'Traz alcool gel',
          'imagem': 'basquete.jpg'
        },
        {
          'Criador': 'Outro Cara',
          'Esporte': 'Futebol',
          'Dia': '18/01',
          'Horas': '8 Horas',
          'Descricao': 'Trazer 10zão pro churrasco',
          'imagem': 'futebol.jpg'
        },
        {
          'Criador': 'Mais um Cara',
          'Esporte': 'Futebol American',
          'Dia': '16/02',
          'Horas': '10 Horas',
          'Descricao': 'Só vem!',
          'imagem': 'futebolameric.jpg'
        },
        {
          'Criador': 'Outro Cara',
          'Esporte': 'Volei',
          'Dia': '20/01',
          'Horas': '8 Horas',
          'Descricao': 'Trazer 10zão pro churrasco',
          'imagem': 'volei.jpg'
        },
        {
          'Criador': 'Mais um Cara',
          'Esporte': 'Basquete',
          'Dia': '23/04',
          'Horas': '10 Horas',
          'Descricao': 'Só vem!',
          'imagem': 'baseball.jpg'
        },
        {
          'Criador': 'Criador',
          'Esporte': 'Basquete',
          'Dia': '15/01',
          'Horas': '6 Horas',
          'Descricao': 'Traz alcool gel',
          'imagem': 'basquete.jpg'
        },
        {
          'Criador': 'Outro Cara',
          'Esporte': 'Futebol',
          'Dia': '18/01',
          'Horas': '8 Horas',
          'Descricao': 'Trazer 10zão pro churrasco',
          'imagem': 'futebol.jpg'
        },
        {
          'Criador': 'Mais um Cara',
          'Esporte': 'Futebol American',
          'Dia': '16/02',
          'Horas': '10 Horas',
          'Descricao': 'Só vem!',
          'imagem': 'futebolameric.jpg'
        },
        {
          'Criador': 'Outro Cara',
          'Esporte': 'Volei',
          'Dia': '20/01',
          'Horas': '8 Horas',
          'Descricao': 'Trazer 10zão pro churrasco',
          'imagem': 'volei.jpg'
        }]
    })
  }
}
