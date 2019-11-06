<template>
<div id = 'app' >
  <v-app>
<v-card class="overflow-hidden">
    <v-content>
      <navigationbar/>
  </v-content>
   <div class = back>
    <v-sheet
      id="scrolling-techniques-2"
      class= overflow-y-auto
      style= "opacity:0.9"
      max-height="700"
      color = black

    >
   
      <v-container style="height: 1200px;"
>


<v-content>
   <router-view/>
  </v-content>
      </v-container>
    
    </v-sheet>
    </div>
  </v-card>
   </v-app>
  </div>
</template>
<script>
import navigationbar from'./components/navigationbar';
export default {
  name: 'App',
  components: {
    navigationbar
  },
  data: () => ({
    //
  }),
};
</script>
<style scoped>
.back {
  background-image: url(https://images2.alphacoders.com/786/786551.png);
  background-size: contain;
  background-repeat: repeat;
  width: 100%;
}
#inspire {
  background: none;
}
</style>