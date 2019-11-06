 <template>
 <div>
 <div class="display-3" style ="color:green">Total time play Analysis</div>
    <v-row>
       <router-link to ="/RecentTimeBarChartView" tag="p"><v-btn text class = "title" style ="color:red">Recent time</v-btn></router-link>
        <router-link to ="/ReviewNumChartView" tag="p"><v-btn text class = "title" style ="color:red">Review number</v-btn></router-link>
         <router-link to ="/GameNumBarChartView" tag="p"><v-btn text class = "title" style ="color:red">Game Number</v-btn></router-link>
          <router-link to ="/TotalTimeBarChartView" tag="p"><v-btn text class = "title" style ="color:red">Total played time</v-btn></router-link>
      </v-row>
 <v-card v-if="dataLoading">
   <TotalTimeBarChart :Ararat = Ararat :Barinsdale = Barinsdale :Ballarat= Ballarat 
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
:Wonthaggi= Wonthaggi></TotalTimeBarChart>
    </v-card>
 </div>
    </template>

    <script>
    import TotalTimeBarChart from './TotalTimeBarChart.vue'
    export default {
      components:{
        TotalTimeBarChart
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
    
        this.Ararat = this.info.Ararat.total_time 
        this.Clifton_Springs = this.info.Clifton_Springs.total_time
        this.Crib_Point = this.info.Crib_Point.total_time 
        this.Lakes_Entrance = this.info.Lakes_Entrance.total_time 
        this.Swan_Hill = this.info.Swan_Hill.total_time  
        this.Ballarat = this.info.Ballarat.total_time
        this.Barinsdale = this.info.Ararat.total_time  
        this.Benalla = this.info.Benalla.total_time  
        this.Bendigo = this.info.Bendigo.total_time  
        this.Castlemaine = this.info.Castlemaine.total_time 
        this.Colac = this.info.Colac.total_time  
        this.Craigieburn = this.info.Craigieburn.total_time  
        this.Cranbourne = this.info.Cranbourne.total_time     
        this.Geelong = this.info.Geelong.total_time  
        this.Hamilton = this.info.Hamilton.total_time
        this.Hastings = this.info.Hastings.total_time  
        this.Healesville = this.info.Healesville.total_time  
        this.Horsham = this.info.Horsham.total_time  
        this.Kyabram = this.info.Kyabram.total_time  
        this.Lara = this.info.Lara.total_time  
        this.Leopold = this.info.Leopold.total_time  
        this.Maryborough = this.info.Maryborough.total_time 
        this.Melbourne = this.info.Melbourne.total_time 
        this.Melton = this.info.Melton.total_time 
        this.Mildura = this.info.Mildura.total_time 
        this.Morwell = this.info.Morwell.total_time 
        this.Pakenham = this.info.Pakenham.total_time 
        this.Portland = this.info.Portland.total_time
        this.Sale = this.info.Sale.total_time
        this.Somerville = this.info.Somerville.total_time
        this.Stawell = this.info.Stawell.total_time
        this.Sunbury = this.info.Sunbury.total_time
        this.Traralgon = this.info.Traralgon.total_time
        this.Wangaratta = this.info.Wangaratta.total_time
        this.Warragul = this.info.Warragul.total_time
        this.Warrnambool = this.info.Warrnambool.total_time
         this.Wodonga = this.info.Wodonga.total_time
          this.Wonthaggi = this.info.Wonthaggi.total_time
          this.dataLoading = true
  
    });
    

  },
    }
    
    </script>