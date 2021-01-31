<template>
  <v-app>
    <html>
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="style.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css">
      </head>
      <body>
        <section>
          <header>
            <h2><a href="#" class="logo" style="color: #19B3D3" onclick="location.href = '/';">Esport.se</a></h2>
            <div class="navigation">
              <a href="#" onclick="location.href = '/';">Home</a>
              <a href="#" onclick="location.href = '/jogos';">Jogos</a>
              <a href="#" onclick="location.href = '/busca';">Busca</a>
              <a href="#" onclick="location.href = '/quemsomos';">Sobre</a>
              <a href="#" v-if="!logged_user" @click="open_login_dialog($event)">Login</a>
              <v-menu v-if="logged_user" offset-y>
                <v-btn icon slot="activator" class="ma-0 ml-5">
                  <v-avatar size="36px">
                    <img src="https://graph.facebook.com/4/picture?width=300&height=300">
                  </v-avatar>
                </v-btn>
                <v-card class="no-padding">
                  <v-list two-line>
                    <v-list-tile avatar>
                      <v-list-tile-avatar>
                        <v-avatar>
                          <img src="https://graph.facebook.com/4/picture?width=300&height=300">
                        </v-avatar>
                      </v-list-tile-avatar>
                      <v-list-tile-content>
                        <v-list-tile-title>{{logged_user.first_name}} {{logged_user.last_name}}</v-list-tile-title>
                        <v-list-tile-sub-title>{{logged_user.email}}</v-list-tile-sub-title>
                      </v-list-tile-content>
                    </v-list-tile>
                  </v-list>
                  <v-divider />
                  <v-list>
                    <v-list-tile @click="switchMode()">
                      <v-list-tile-content>
                        <v-list-tile-title>Staff mode</v-list-tile-title>
                      </v-list-tile-content>
                    </v-list-tile>
                    <v-list-tile @click="logout()">
                      <v-list-tile-content>
                        <v-list-tile-title>Log out</v-list-tile-title>
                      </v-list-tile-content>
                    </v-list-tile>
                  </v-list>
                </v-card>
              </v-menu>
              <login-dialog ref="login_dialog" />
            </div>
          </header>
          <v-content>
            <v-container fluid>
              <nuxt />
            </v-container>
          </v-content>
        </section>
      </body>
      <le-footer />
    </html>
  </v-app>
</template>

<script>
import Vuex from 'vuex'
import footer from '~/components/footer.vue'
import loginDialog from '~/components/login-dialog.vue'
import Snacks from '~/helpers/Snacks.js'
import AppApi from '~api'

export default {
  components: {
    leFooter: footer,
    loginDialog
  },
  props: ['state'],
  data () {
    return {}
  },
  computed: Object.assign(
    {},
    Vuex.mapGetters([
      'logged_user'
    ])
  ),
  methods: {
    open_login_dialog (evt) {
      this.$refs.login_dialog.open()
      evt.stopPropagation()
    },
    logout () {
      AppApi.logout().then(() => {
        this.$store.commit('SET_LOGGED_USER', null)
        Snacks.show(this.$store, {text: 'Até logo!'})
      })
    // },
    // login () {
    //   AppApi.logout().then(() => {
    //     this.$store.commit('SET_LOGGED_USER', null)
    //     Snacks.show(this.$store, {text: 'Até logo!'})
    //   })
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');
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
header{
  position: relative;
  top: 0;
  width: 100%;
  padding: 30px 100px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
header .logo{
  position: relative;
  color: #000;
  font-size: 30px;
  text-decoration: none;
  text-transform: uppercase;
  font-weight: 800;
  letter-spacing: 1px;
}
header .navigation a{
  color: rgb(255, 255, 255);
  text-decoration: none;
  font-weight: 500;
  letter-spacing: 1px;
  padding: 2px 15px;
  border-radius: 20px;
  transition: 0.3s;
  transition-property: background;
}
header .navigation a:not(:last-child){
  margin-right: 30px;
}
header .navigation a:hover{
  background: #fff;
}
.container.container--fluid.contente{
  padding: 0;
}
.content{
  max-width: 650px;
  margin: 60px 100px;
}
.content .info h2{
  color: #ffffff;
  font-size: 55px;
  text-transform: uppercase;
  font-weight: 800;
  letter-spacing: 2px;
  line-height: 60px;
  margin-bottom: 30px;
}
.content .info h2 span{
  color: #fff;
  font-size: 50px;
  font-weight: 600;
}
.content .info p{
  font-size: 16px;
  font-weight: 500;
  margin-bottom: 40px;
}
.content .info-btn{
  color: #fff;
  background: #000000;
  text-decoration: none;
  text-transform: uppercase;
  font-weight: 500;
  letter-spacing: 2px;
  padding: 10px 20px;
  border-radius: 5px;
  transition: 0.3s;
  transition-property: background;
}
.content .info-btn:hover{
  background: #0c3760;
}
.media-icons{
  display: flex;
  justify-content: center;
  align-items: center;
  margin: auto;
  padding-bottom: 40px;
}
.media-icons a{
  position: relative;
  color: #111;
  font-size: 25px;
  transition: 0.3s;
  transition-property: transform;
}
.media-icons a:not(:last-child){
  margin-right: 60px;
}
.media-icons a:hover{
  transform: scale(1.5);
}
label{
  display: none;
}
#check{
  z-index: 3;
  display: none;
}
/* Responsive styles */

@media (max-width: 960px){
  header .navigation{
    display: none;
  }
  label{
    display: block;
    font-size: 25px;
    cursor: pointer;
    transition: 0.3s;
    transition-property: color;
  }
  label:hover{
    color: #fff;
  }
  label .close-btn{
    display: none;
  }
  #check:checked ~ header .navigation{
    z-index: 2;
    position: fixed;
    background: rgba(114, 223, 255, 0.9);
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  #check:checked ~ header .navigation a{
    font-weight: 700;
    margin-right: 0;
    margin-bottom: 50px;
    letter-spacing: 2px;
  }
  #check:checked ~ header label .menu-btn{
    display: none;
  }
  #check:checked ~ header label .close-btn{
    z-index: 2;
    display: block;
    position: fixed;
  }
  label .menu-btn{
    position: absolute;
  }
  header .logo{
    position: absolute;
    bottom: -6px;
  }
  .content .info h2{
    font-size: 45px;
    line-height: 50px;
  }
  .content .info h2 span{
    font-size: 40px;
    font-weight: 600;
  }
  .content .info p{
    font-size: 14px;
  }
}
@media (max-width: 560px){
  .content .info h2{
    font-size: 35px;
    line-height: 40px;
  }
  .content .info h2 span{
    font-size: 30px;
    font-weight: 600;
  }
  .content .info p{
    font-size: 14px;
  }
}
@media (max-width: 1060px){
  header .btn{
    display: block;
  }
  header .menu{
    position: fixed;
    background: #1483D5;
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
  header .menu a{
    display: block;
    font-size: 20px;
    margin: 20px;
    padding: 0 15px;
  }
}

</style>
