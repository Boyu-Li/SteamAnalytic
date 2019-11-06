<template>
<div id = "gamecard">
  <v-card
    max-width="344"
    color = #003D73
  >
    <v-list-item three-line>
      <v-list-item-content>
       
        <div class="overline mb-4" style = "color:white">gameid: {{steamid}}</div>
        <v-list-item-title class="headline mb-1" style = "color:white">{{gameName}}</v-list-item-title>
        <v-list-item-subtitle style = "color:white">{{gameRateState}}</v-list-item-subtitle>
        
      </v-list-item-content>

      <v-list-item-avatar
        tile
        size="80"
    
      > <v-img :src= "imageUrl" aspect-ratio="1.4" contain></v-img></v-list-item-avatar>
    </v-list-item>

    <v-card-actions>
      <router-link :to ="'/gameDetail/'+gameid.toString()" tag="p">
      <v-btn text style = "color:white">game Detail
      </v-btn>
       </router-link>
    </v-card-actions>
  </v-card>
</div>
</template>

<script>
export default {
  name: 'gamecard',
  props: ['gameName','gameid','steamid','imageUrl','gameRateState'],
  components: {
  
  },
  
  data: function(){
    return{
    }
  
  }
};
</script>


