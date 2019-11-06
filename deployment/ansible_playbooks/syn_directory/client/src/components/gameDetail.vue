<template>
<div id = "gameDetail">
   <div class="display-3 font-weight-bold	" style="color:white;">Game Name:  {{gameDeck[id].gameName}}</div>
  
  <v-row>
      <v-col cols="12">
        <v-row
          align="center"
          justify="center"
        style="height: 300px;"
        >
        <v-spacer></v-spacer>
          <v-card
          height = 150
          width = 300
          >
          <v-col>
          <v-row>
                <v-spacer></v-spacer>
            <p class="text-left display-1">
               Game ID:
           </p>
           <v-spacer></v-spacer>
            <v-spacer></v-spacer> 
               
          </v-row>

          <div class = "display-2 text-right grey--text font-weight-bold" align="center">{{gameDeck[id].gameId}}</div>
          </v-col>
          </v-card>
           <v-spacer></v-spacer>
            <v-card
          height = 150
          width = 300
          >
          <v-col>
          <v-row>
                <v-spacer></v-spacer>
            <p class="text-left display-1">
               Game Rate:
           </p>
           <v-spacer></v-spacer>
            <v-spacer></v-spacer> 
               
          </v-row>
          <v-row>
          <v-spacer></v-spacer> 
          <v-spacer></v-spacer>
          <div class = "display-2 text-right grey--text font-weight-bold" align="center">{{gameDeck[id].gameRate}}</div>
            
            <v-spacer></v-spacer> 
          </v-row>
          </v-col>
          </v-card>
           <v-spacer></v-spacer>
           <v-card
          height = 150
          width = 300
          >
          <v-col>
          <v-row>
                <v-spacer></v-spacer>
            <p class="text-left display-1">
               Recent Player(AU):
           </p>
           <v-spacer></v-spacer>
            <v-spacer></v-spacer> 
               
          </v-row>
          <v-row>
          <v-spacer></v-spacer> 
          <v-spacer></v-spacer>
          <div class = "display-2 text-right grey--text font-weight-bold" align="center">{{gameDeck[id].gameAuPlayer}}</div>
            
            <v-spacer></v-spacer> 
          </v-row>
          </v-col>
          </v-card>
           <v-spacer></v-spacer>
        </v-row>
      </v-col>
  </v-row>
 
 <v-col>
   
   </v-col> 
  <v-row>
<v-spacer></v-spacer>
<v-card>
<firstChart :gamePos = gameDeck[id].gamePos :gameNeg = gameDeck[id].gameNeg></firstChart>
</v-card>
<v-spacer></v-spacer>

</v-row>
<v-col>
   
   </v-col> 
<v-row>
  <v-spacer></v-spacer>
<v-card height = 350 width = 800>
<radialChart :gameTotal = gameDeck[id].gameTotal :gameAuPlayer = gameDeck[id].gameAuPlayer :gameRecent = gameDeck[id].gameRecent ></radialChart>
</v-card>
<v-spacer></v-spacer>
</v-row>
  
</div>
</template>

<script>
import firstChart from './myfirstChart.vue'
import barChart from './myBarChart.vue'
import radialChart from './myRadialBarChart'

export default {
  name: 'gameDetail',
  components: {
  firstChart,
  barChart,
  radialChart
  },
  
  data: function(){
    return{
        id:this.$route.params.id,
        info:'',
        testName:'',
        header:{
          headers: {'Accept':'application/json',
            'Content-Type':'application/json'}
        },
         gameDeck: []
    }
    },
     mounted () {
   
      this.$axios({method:"GET", url:"http://localhost:3000/gameDetail"
    }).then(response => {this.info = response.data
    var i;
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
        var gameRecent = tempfile.recent_num
        var gameLength = tempfile.length
        var gameRlength = tempfile.rlength
        var gameType = tempfile.type
        var gameAuPlayer = tempfile.au_num
        this.gameDeck.push({'id':i,'gameName':testName,'gameAuPlayer':gameAuPlayer,'imageUrl':imageUrl,'gameRate':gameRate,'gameId':gameId,'gameRateState':gameRateState,'gamePos':gamePos,'gameNeg':gameNeg,'gameTotal':gameTotal,'gameRecent':gameRecent,'gameLength':gameLength,'gameRlength':gameRlength,'gameType':gameType})
    }
  
    });
    

  },
    
    
    watch:{
        '$route'(to){
            this.id = to.params.id
        }
  
  }
};



</script>

