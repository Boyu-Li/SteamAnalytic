 <template>
 <div>
 <div class="display-3" style ="color:green">Review Number Analysis</div>
    <v-row>
       <router-link to ="/RecentTimeBarChartView" tag="p"><v-btn text class = "title" style ="color:red">Recent time</v-btn></router-link>
        <router-link to ="/ReviewNumChartView" tag="p"><v-btn text class = "title" style ="color:red">Review number</v-btn></router-link>
         <router-link to ="/GameNumBarChartView" tag="p"><v-btn text class = "title" style ="color:red">Game Number</v-btn></router-link>
          <router-link to ="/TotalTimeBarChartView" tag="p"><v-btn text class = "title" style ="color:red">Total played time</v-btn></router-link>
      </v-row>
 <v-card  v-if="dataLoading">
   <ReviewNumBarChart 
:Ararat = Ararat :Barinsdale = Barinsdale :Ballarat= Ballarat 
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
:Wonthaggi= Wonthaggi></ReviewNumBarChart>
    </v-card>
 </div>
    </template>

    <script>
    import ReviewNumBarChart from './ReviewNumBarChart.vue'
    export default {
      components:{
        ReviewNumBarChart
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
    
        this.Ararat = this.info.Ararat.review_num 
        this.Clifton_Springs = this.info.Clifton_Springs.review_num
        this.Crib_Point = this.info.Crib_Point.review_num 
        this.Lakes_Entrance = this.info.Lakes_Entrance.review_num 
        this.Swan_Hill = this.info.Swan_Hill.review_num  
        this.Ballarat = this.info.Ballarat.review_num
        this.Barinsdale = this.info.Ararat.review_num  
        this.Benalla = this.info.Benalla.review_num  
        this.Bendigo = this.info.Bendigo.review_num  
        this.Castlemaine = this.info.Castlemaine.review_num 
        this.Colac = this.info.Colac.review_num  
        this.Craigieburn = this.info.Craigieburn.review_num  
        this.Cranbourne = this.info.Cranbourne.review_num     
        this.Geelong = this.info.Geelong.review_num  
        this.Hamilton = this.info.Hamilton.review_num
        this.Hastings = this.info.Hastings.review_num  
        this.Healesville = this.info.Healesville.review_num  
        this.Horsham = this.info.Horsham.review_num  
        this.Kyabram = this.info.Kyabram.review_num  
        this.Lara = this.info.Lara.review_num  
        this.Leopold = this.info.Leopold.review_num  
        this.Maryborough = this.info.Maryborough.review_num 
        this.Melbourne = this.info.Melbourne.review_num 
        this.Melton = this.info.Melton.review_num 
        this.Mildura = this.info.Mildura.review_num 
        this.Morwell = this.info.Morwell.review_num 
        this.Pakenham = this.info.Pakenham.review_num 
        this.Portland = this.info.Portland.review_num
        this.Sale = this.info.Sale.review_num
        this.Somerville = this.info.Somerville.review_num
        this.Stawell = this.info.Stawell.review_num
        this.Sunbury = this.info.Sunbury.review_num
        this.Traralgon = this.info.Traralgon.review_num
        this.Wangaratta = this.info.Wangaratta.review_num
        this.Warragul = this.info.Warragul.review_num
        this.Warrnambool = this.info.Warrnambool.review_num
         this.Wodonga = this.info.Wodonga.review_num
          this.Wonthaggi = this.info.Wonthaggi.review_num
          this.dataLoading = true
  
    });
    

  },
    }
    
    </script>