 <template>
 <div>
 <div class="display-3" style ="color:green">Recent game play Analysis</div>
    <v-row>
       <router-link to ="/RecentTimeBarChartView" tag="p"><v-btn text class = "title" style ="color:red">Recent time</v-btn></router-link>
        <router-link to ="/ReviewNumChartView" tag="p"><v-btn text class = "title" style ="color:red">Review number</v-btn></router-link>
         <router-link to ="/GameNumBarChartView" tag="p"><v-btn text class = "title" style ="color:red">Game Number</v-btn></router-link>
          <router-link to ="/TotalTimeBarChartView" tag="p"><v-btn text class = "title" style ="color:red">Total played time</v-btn></router-link>
      </v-row>
 <v-card v-if="dataLoading" >
   <UserNamebarChart :Ararat = Ararat :Barinsdale = Barinsdale :Ballarat= Ballarat 
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
:Wonthaggi= Wonthaggi></UserNamebarChart>
    </v-card>
 </div>
    </template>

    <script>
    import UserNamebarChart from './UserNameBarChart.vue'
    export default {
      components:{
        UserNamebarChart
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
    
        this.Ararat = this.info.Ararat.user_num 
        this.Clifton_Springs = this.info.Clifton_Springs.user_num
        this.Crib_Point = this.info.Crib_Point.user_num 
        this.Lakes_Entrance = this.info.Lakes_Entrance.user_num 
        this.Swan_Hill = this.info.Swan_Hill.user_num  
        this.Ballarat = this.info.Ballarat.user_num
        this.Barinsdale = this.info.Ararat.user_num  
        this.Benalla = this.info.Benalla.user_num  
        this.Bendigo = this.info.Bendigo.user_num  
        this.Castlemaine = this.info.Castlemaine.user_num 
        this.Colac = this.info.Colac.user_num  
        this.Craigieburn = this.info.Craigieburn.user_num  
        this.Cranbourne = this.info.Cranbourne.user_num     
        this.Geelong = this.info.Geelong.user_num  
        this.Hamilton = this.info.Hamilton.user_num
        this.Hastings = this.info.Hastings.user_num  
        this.Healesville = this.info.Healesville.user_num  
        this.Horsham = this.info.Horsham.user_num  
        this.Kyabram = this.info.Kyabram.user_num  
        this.Lara = this.info.Lara.user_num  
        this.Leopold = this.info.Leopold.user_num  
        this.Maryborough = this.info.Maryborough.user_num 
        this.Melbourne = this.info.Melbourne.user_num 
        this.Melton = this.info.Melton.user_num 
        this.Mildura = this.info.Mildura.user_num 
        this.Morwell = this.info.Morwell.user_num 
        this.Pakenham = this.info.Pakenham.user_num 
        this.Portland = this.info.Portland.user_num
        this.Sale = this.info.Sale.user_num
        this.Somerville = this.info.Somerville.user_num
        this.Stawell = this.info.Stawell.user_num
        this.Sunbury = this.info.Sunbury.user_num
        this.Traralgon = this.info.Traralgon.user_num
        this.Wangaratta = this.info.Wangaratta.user_num
        this.Warragul = this.info.Warragul.user_num
        this.Warrnambool = this.info.Warrnambool.user_num
         this.Wodonga = this.info.Wodonga.user_num
          this.Wonthaggi = this.info.Wonthaggi.user_num
          this.dataLoading = true
  
    });
    

  },
    }
    
    </script>