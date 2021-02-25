<template>
  <v-layout class="layout">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Responsive Sticky NavBar | For a Website</title>
      <link rel="stylesheet" href="style.css">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
    </head>
    <div class="content">
      <div style="background-color: transparent !important;" class="info">
        <h2>Encontre seu Jogo.<br><span style="color: #1976d2">Comece Agora!</span></h2>
        <p>Estamos desde 2021 juntando pessoas que querem jogar com pessoas que não tem com quem jogar. Entre agora para a comunidade do Esport.se e começe a jogar também!</p>
        <a href="#" class="info-btn" onclick="location.href = 'jogos';">Bora Jogar!</a>
      </div>
    </div>
    <div class="media-icons">
      <a href="#"><i class="fab fa-facebook-f" style="color: white" onclick="window.location.replace(&quot;https://www.facebook.com&quot;);" /></a>
      <a href="#"><i class="fab fa-twitter" style="color: white" onclick="window.location.replace(&quot;https://www.twitter.com&quot;);" /></a>
      <a href="#"><i class="fab fa-instagram" style="color: white" onclick="window.location.replace(&quot;https://www.instagram.com&quot;);" /></a>
    </div>
  </v-layout>
</template>

<script>
export default {
  data () {
    return {}
  },
  head () {
    return {
      title: 'Home'
    }
  },
  layout: 'complex'
}
</script>

<style>
*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}
a{
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
  color:  #0c3760;
  background: #0c3760;
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
  color: rgb(255, 255, 255);
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
</style>
