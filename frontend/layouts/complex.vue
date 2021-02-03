<template>
  <v-app>
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="style.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
      </head>
      <body>
        <section>
          <header>
            <a href="#" class="brand">Esporte.se</a>
            <div class="menu">
              <div class="btn">
                <i class="fas fa-times close-btn" />
              </div>
              <a href="#" onclick="location.href = '/';">Home</a>
              <a href="#" onclick="location.href = '/perfil';">Perfil</a>
              <a href="#" onclick="location.href = '/jogos';">Jogos</a>
              <a href="#" onclick="location.href = '/busca';">Busca</a>
              <a href="#" onclick="location.href = '/quemsomos';">Sobre</a>
              <a href="#" v-if="!logged_user" @click="open_login_dialog($event)">Login</a>
              <v-menu v-if="logged_user" offset-y>
                <template v-slot:activator="{ on }">
                  <v-btn icon v-on="on" class="ma-0 ml-5">
                    <v-avatar size="36px">
                      <img src="profile.jpg">
                    </v-avatar>
                  </v-btn>
                </template>
                <v-card class="no-padding">
                  <v-list two-line>
                    <v-list-item>
                      <v-list-item-avatar>
                        <v-avatar>
                          <img src="profile.jpg">
                        </v-avatar>
                      </v-list-item-avatar>
                      <v-list-item-content>
                        <v-list-item-title>{{logged_user.first_name}} {{logged_user.last_name}}</v-list-item-title>
                        <v-list-item-subtitle>{{logged_user.email}}</v-list-item-subtitle>
                      </v-list-item-content>
                    </v-list-item>
                  </v-list>
                  <v-divider />
                  <v-list>
                    <v-list-item @click="logout()">
                      <v-list-item-content>
                        <v-list-item-title>Log out</v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                  </v-list>
                </v-card>
              </v-menu>
              <login-dialog ref="login_dialog" /><login-dialog ref="login_dialog" />
            </div>
            <div class="btn">
              <i class="fas fa-bars menu-btn" />
            </div>
          </header>
          <v-content margin->
            <v-container fluid>
              <nuxt />
            </v-container>
          </v-content>
        </section>
      </body>
    </html>
    <le-footer />
  </v-app>
</template>

<script>
import footer from '~/components/footer.vue'
import loginDialog from '~/components/login-dialog.vue'
import Snacks from '~/helpers/Snacks.js'
import api from '~api'

export default {
  components: {
    leFooter: footer,
    loginDialog
  },
  props: ['state'],
  data () {
    return {}
  },
  computed: {
    logged_user () {
      return this.$store.state.auth.currentUser
    }
  },
  mounted () {
    window.addEventListener('scroll', () => {
      const header = document.querySelector('header')
      header.classList.toggle('sticky', window.scrollY > 0)
    })
    const menu = document.querySelector('.menu')
    const menuBtn = document.querySelector('.menu-btn')
    const closeBtn = document.querySelector('.close-btn')
    menuBtn.addEventListener('click', () => {
      menu.classList.add('active')
    })
    closeBtn.addEventListener('click', () => {
      menu.classList.remove('active')
    })
  },
  methods: {
    open_login_dialog (evt) {
      this.$refs.login_dialog.open()
      evt.stopPropagation()
    },
    async logout () {
      await api.logout()
      this.$store.commit('auth/setCurrentUser', null)
      Snacks.show(this.$store, {text: 'Até logo!'})
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;500;600;700;800;900&display=swap');

*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}
section{
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  background: url(../static/bg.jpg)no-repeat;
  background-size: cover;
  background-position: center;
}
body{
  min-height: 100vh;
}
.section-main{
  position: relative;
  width: 100%;
  min-height: 100vh;
  background: url('../static/bg.jpg') no-repeat;
  background-size: cover;
  background-position: center;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px 100px;
}

.section-main h1{
  color: rgba(255, 255, 255, 0.5);
  font-size: 60px;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 2px;
  line-height: 80px;
}

header{
  z-index: 999;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 100px;
  transition: 0.6s;
}

header.sticky{
  background: #000000;
  padding: 15px 100px;
}

header .brand{
  color: #fff;
  font-size: 30px;
  font-weight: 700;
  text-transform: uppercase;
  text-decoration: none;
  letter-spacing: 2px;
}

header .menu{
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
}

header .menu a{
  color: #fff;
  font-size: 16px;
  font-weight: 500;
  text-decoration: none;
  margin: 0 30px;
  padding: 0 10px;
  border-radius: 20px;
  transition: 0.3s;
  transition-property: color, background;
}

header .menu a:hover{
  color: #000;
  background: #fff;
}

header .btn{
  color: #fff;
  font-size: 25px;
  cursor: pointer;
  display: none;
}

@media (max-width: 1060px){
  header .btn{
    display: block;
  }

  header .menu{
    position: fixed;
    background: #000000;
    flex-direction: column;
    min-width: 400px;
    height: 100vh;
    top: 0;
    right: -100%;
    padding: 80px 50px;
    transition: 0.5s;
    transition-property: right;
  }

  header .menu.active{
    right: 0;
  }

  header .menu .close-btn{
    position: absolute;
    top: 0;
    left: 0;
    margin: 25px;
  }

  header .menu a{
    display: block;
    font-size: 20px;
    margin: 20px;
    padding: 0 15px;
  }
}

@media (max-width: 630px){
  .section-main h1{
    font-size: 50px;
    line-height: 60px;
  }
}
</style>
