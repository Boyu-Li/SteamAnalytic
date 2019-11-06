<template>
  <v-container fluid>
    <v-row > 
      
      <v-col
        v-for="game in gameDeck"
        :key="game.id"
        cols="12"
        sm="4"
      >
      <v-row align-self="start">
         <steamcard :gameName = game.gameName :gameid = game.id :steamid = game.gameId :imageUrl = game.imageUrl :gameRateState = game.gameRateState ></steamcard>
      </v-row>
      </v-col>
    </v-row>
  </v-container>

</template>

<script>
import steamcard from './steamcard.vue';

export default {
  name: 'App',
  components: {
    steamcard
  },
  
   mounted () {
   
      this.$axios({method:"GET", url:"http://localhost:3000/gameDetail"
    }).then(response => {this.info = response.data
    var i;
   //response.data.data.rows
    for (i = 0; i<21; i++) {
        var tempfile = this.info[i].value
        var testName = tempfile.name
        var gameRate = tempfile.rate
        var gameId = tempfile.id
        var gameRateState = tempfile.rate_state
        var imageUrl = tempfile.image
        var gamePos = tempfile.pos
        var gameNeg = tempfile.neg
        var gameTotal = tempfile.total
        var gameAuPlayer = tempfile.au_num
        var gameRecent = tempfile.recent_num
        var gameLength = tempfile.length
        var gameRlength = tempfile.rlength
        var gameType = tempfile.type
        this.gameDeck.push({'id':i,'gameName':testName,'gameAuPlayer':gameAuPlayer,'imageUrl':imageUrl,'gameRate':gameRate,'gameId':gameId,'gameRateState':gameRateState,'gamePos':gamePos,'gameNeg':gameNeg,'gameTotal':gameTotal,'gameRecent':gameRecent,'gameLength':gameLength,'gameRlength':gameRlength,'gameType':gameType})
  
   }
 
    });
    

  },
  data: () => ({
    gameDeck: [
    ]
    
  }), 
  



}

</script>
