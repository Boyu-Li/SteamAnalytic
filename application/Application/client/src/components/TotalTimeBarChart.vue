  <template>
 <v-card >
 <div id="chart">
      <apexchart type=bar height=1200 :options="chartOptions" :series="series" />
    </div>
    </v-card>
    </template>

    <script>
    export default {
         props: ['Ararat', 'Barinsdale', 'Ballarat', 'Benalla', 'Bendigo', 'Castlemaine', 'Clifton_Springs',
              'Colac', 'Craigieburn', 'Cranbourne','Crib_Point', 'Geelong','Hamilton','Hastings','Healesville',
              'Horsham','Kyabram','Lakes_Entrance','Lara','Leopold','Maryborough','Melbourne','Melton','Mildura',
              'Morwell','Pakenham','Portland','Sale','Somerville','Stawell','Sunbury','Swan_Hill','Traralgon',
              'Wangaratta','Warragul','Warrnambool','Wodonga','Wonthaggi'],
       data: function() {
      return {
          
        series: [{
          data: [this.Ararat, 
          this.Barinsdale, 
          this.Ballarat, 
        this.Benalla,
        this.Bendigo, 
        this.Castlemaine, 
        this.Clifton_Springs,
        this.Colac, 
        this.Craigieburn, 
        this.Cranbourne,
        this.Crib_Point,
        this.Geelong,
        this.Hamilton,
        this.Hastings,
        this.Healesville,
        this.Horsham,
        this.Kyabram,
        this.Lakes_Entrance,
        this.Lara,
        this.Leopold,
        this.Maryborough,
        this.Melbourne,
        this.Melton,
        this.Mildura,
        this.Morwell,
        this.Pakenham,
        this.Portland,
        this.Sale,
        this.Somerville,
        this.Stawell,
        this.Sunbury,
        this.Swan_Hill,
        this.Traralgon,
        this.Wangaratta,
        this.Warragul,
        this.Warrnambool,
        this.Wodonga,
        this.Wonthaggi]
        }],
        chartOptions: {
          plotOptions: {
            bar: {
              horizontal: true,
            }
          },
          dataLabels: {
            enabled: false
          },
          xaxis: {
            categories: ['Ararat', 'Barinsdale', 'Ballarat', 'Benalla', 'Bendigo', 'Castlemaine', 'Clifton Springs',
              'Colac', 'Craigieburn', 'Cranbourne','Crib Point', 'Geelong','Hamilton','Hastings','Healesville',
              'Horsham','Kyabram','Lakes Entrance','Lara','Leopold','Maryborough','Melbourne','Melton','Mildura',
              'Morwell','Pakenham','Portland','Sale','Somerville','Stawell','Sunbury','Swan Hill','Traralgon',
              'Wangaratta','Warragul','Warrnambool','Wodonga','Wonthaggi'
            ],
          }
        }
      }
       }
    }
    
    </script>