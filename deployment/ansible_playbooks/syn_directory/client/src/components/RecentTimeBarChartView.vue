 <template>
 <div>
 <div class="display-3" style ="color:green">Recent game play Analysis</div>
    <v-row>
      
       <router-link to ="/RecentTimeBarChartView" tag="p"><v-btn text class = "title" style ="color:red">Recent time</v-btn></router-link>
        <router-link to ="/ReviewNumChartView" tag="p"><v-btn text class = "title" style ="color:red">Review number</v-btn></router-link>
         <router-link to ="/GameNumBarChartView" tag="p"><v-btn text class = "title" style ="color:red">Game Number</v-btn></router-link>
          <router-link to ="/TotalTimeBarChartView" tag="p"><v-btn text class = "title" style ="color:red">Total played time</v-btn></router-link>
      </v-row>
 <v-card v-if="dataLoading">
   <RecentTimeBarChart :Ararat = Ararat :Barinsdale = Barinsdale :Ballarat= Ballarat 
:Benalla= Benalla
:Bendigo= Bendigo
:Castlemaine= Castlemaine
:Clifton_Springs= Clifton_Springs
:Colac= Colac 
:Craigieburn= Craigieburn
:Cranbourne= Cranbourne
:Crib_Point= Crib_Point
:Geelong= Geelong
:Hamilton= Hamilton
:Hastings= Hastings
:Healesville= Healesville
:Horsham= Horsham
:Kyabram= Kyabram
:Lakes_Entrance= Lakes_Entrance
:Lara= Lara
:Leopold= Leopold
:Maryborough= Maryborough
:Melbourne= Melbourne
:Melton= Melton
:Mildura= Mildura
:Morwell= Morwell
:Pakenham= Pakenham
:Portland= Portland
:Sale= Sale
:Somerville= Somerville
:Stawell= Stawell
:Sunbury= Sunbury
:Swan_Hill= Swan_Hill
:Traralgon= Traralgon
:Wangaratta= Wangaratta
:Warragul= Warragul
:Warrnambool= Warrnambool
:Wodonga= Wodonga
:Wonthaggi= Wonthaggi></RecentTimeBarChart>
    </v-card>
 </div>
    </template>

    <script>
    import RecentTimeBarChart from './RecentTimeBarChart.vue'
    export default {
      components:{
        RecentTimeBarChart
      },

       data: function() {
      return {
        dataLoading:false,
          Ararat:0, 
          Barinsdale:0, 
          Ballarat:0, 
          Benalla:0,
          Bendigo:0, 
          Castlemaine:0, 
          Clifton_Springs:0,
          Colac:0, 
          Craigieburn:0, 
          Cranbourne:0,
          Crib_Point:0,
          Geelong:0,
          Hamilton:0,
          Hastings:0,
          Healesville:0,
          Horsham:0,
          Kyabram:0,
          Lakes_Entrance:0,
          Lara:0,
          Leopold:0,
          Maryborough:0,
          Melbourne:0,
          Melton:0,
          Mildura:0,
          Morwell:0,
          Pakenham:0,
          Portland:0,
          Sale:0,
          Somerville:0,
          Stawell:0,
          Sunbury:0,
          Swan_Hill:0,
          Traralgon:0,
          Wangaratta:0,
          Warragul:0,
          Warrnambool:0,
          Wodonga:0,
          Wonthaggi:0,
      }
      },
        
     mounted () {
   
      this.$axios({method:"GET", url:"http://localhost:3000/vicDistribute"
    }).then(response => {this.info = response.data
    
        this.Ararat = this.info.Ararat.recent_time 
        this.Clifton_Springs = this.info.Clifton_Springs.recent_time
        this.Crib_Point = this.info.Crib_Point.recent_time 
        this.Lakes_Entrance = this.info.Lakes_Entrance.recent_time 
        this.Swan_Hill = this.info.Swan_Hill.recent_time  
        this.Ballarat = this.info.Ballarat.recent_time
        this.Barinsdale = this.info.Ararat.recent_time  
        this.Benalla = this.info.Benalla.recent_time  
        this.Bendigo = this.info.Bendigo.recent_time  
        this.Castlemaine = this.info.Castlemaine.recent_time 
        this.Colac = this.info.Colac.recent_time  
        this.Craigieburn = this.info.Craigieburn.recent_time  
        this.Cranbourne = this.info.Cranbourne.recent_time     
        this.Geelong = this.info.Geelong.recent_time  
        this.Hamilton = this.info.Hamilton.recent_time
        this.Hastings = this.info.Hastings.recent_time  
        this.Healesville = this.info.Healesville.recent_time  
        this.Horsham = this.info.Horsham.recent_time  
        this.Kyabram = this.info.Kyabram.recent_time  
        this.Lara = this.info.Lara.recent_time  
        this.Leopold = this.info.Leopold.recent_time  
        this.Maryborough = this.info.Maryborough.recent_time 
        this.Melbourne = this.info.Melbourne.recent_time 
        this.Melton = this.info.Melton.recent_time 
        this.Mildura = this.info.Mildura.recent_time 
        this.Morwell = this.info.Morwell.recent_time 
        this.Pakenham = this.info.Pakenham.recent_time 
        this.Portland = this.info.Portland.recent_time
        this.Sale = this.info.Sale.recent_time
        this.Somerville = this.info.Somerville.recent_time
        this.Stawell = this.info.Stawell.recent_time
        this.Sunbury = this.info.Sunbury.recent_time
        this.Traralgon = this.info.Traralgon.recent_time
        this.Wangaratta = this.info.Wangaratta.recent_time
        this.Warragul = this.info.Warragul.recent_time
        this.Warrnambool = this.info.Warrnambool.recent_time
         this.Wodonga = this.info.Wodonga.recent_time
          this.Wonthaggi = this.info.Wonthaggi.recent_time
          this.dataLoading = true
  
    });
    

  },
    }
    
    </script>