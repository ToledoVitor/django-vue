<template>
  <v-layout>
    <container>
      <div class="content">
        <div style="background-color: transparent !important;" class="info">
          <h2 style="color: #1976d2">Quem somos?</h2>
          <p> Nós da Sporte.se somos um exército de um homem só de desenvolvedores que tentam solucionar um problema real, a falta de pessoas para jogar.</p>
          <p> A idéia do site é que cada pessoa possa criar um perfil e com isso criar jogos, ou participar de jogos que outros usuários criaram. Assim, nós esperamos que você consiga finalmente organizar aquele futebol de quarta-feira que sempre quis, ou aquele basquete no sábado cedo, e isso sem nem precisar conhecer todas as pessoas que precisaria.</p>
          <p> Ou seja, você só cria uma conta e decide o que quer jogar e quando quer jogar. E se não tiver o jogo? É só criar, tudo isso em menos de um minuto.</p>
          <p> E o melhor de tudo, sabe quanto você paga por isso? Nada, é tudo de graça.</p>
        </div>
      </div>
      <div class="media-icons">
        <a href="#"><i class="fab fa-facebook-f" onclick="window.location.replace(&quot;https://www.facebook.com&quot;);" /></a>
        <a href="#"><i class="fab fa-twitter" onclick="window.location.replace(&quot;https://www.twitter.com&quot;);" /></a>
        <a href="#"><i class="fab fa-instagram" onclick="window.location.replace(&quot;https://www.instagram.com&quot;);" /></a>
      </div>
    </container>
  </v-layout>
</template>

<script>
export default {
  layout: 'complex'
}
</script>

<style>
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
</style>
