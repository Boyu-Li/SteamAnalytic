const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const NodeCouchDb = require('node-couchdb');

const couch = new NodeCouchDb({
    host: '45.113.232.65',
    port: 5984,
    auth:{
        user:'user',
        password:'pass'
    }
});
const dbName = 'multiplayer_game';
const viewUrl = '_design/all_multigame/_view/all';
couch.listDatabases().then(function(dbs){
console.log(dbs);
});
const app = express();
app.set('view engine','ejs');
app.set('views',path.join(__dirname,'views'));
app.use((req, res, next) => {
    res.append('Access-Control-Allow-Origin', ['*']);
    res.append('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE');
    res.append('Access-Control-Allow-Headers', 'Content-Type');
    next();
});
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}));

app.get('/',function(req,res){
    couch.get(dbName,viewUrl).then(
        function(data,headers,status){
            //console.log(data.data.rows);
          res.render('index',{
              game:JSON.stringify(data)
          });
        },
        function(err){
            res.send(err);
        });
    
});
const dbName2 = 'game_detail';
const viewUrl2 = '_design/all_gameDetail/_view/all';

app.get('/gameDetail',function(req,res){
    couch.get(dbName2,viewUrl2).then(
        function(data,headers,status){
          //console.log(data.data.rows);
          var tempfile = data.data.rows
          var sorted = tempfile.sort(function(a, b) {
            var x = a.value.au_num; var y = b.value.au_num;
            if (x > y) {return -1;}
            if (x < y) {return 1;}
            return 0;
        });
          res.render('gameDetail',{
            
              gameDetail:JSON.stringify(sorted)
          });
        },
        function(err){
            res.send(err);
        });
    
});


const dbname3 = 'au_user';
const dbname4 = 'multi_game_user';
const dbname5 = 'single_game_user';
const terms = ["game_num","recent_time","review_num","total_time","user_num"];
const terms1 = ["recent_time","total_time"];
const viewUrlA = "_design/au_user/_view/";
const viewUrlAm = "_design/multi_game_user/_view/";
const viewUrlAs = "_design/single_game_user/_view/";
const viewUrlB = "?group_level=1";
const viewUrlC = "?group_level=2";



app.get('/gameDistribute',function(req,res){
    var dict = {};
    dict["ACT"] = {};
    dict["NSW"] = {};
    dict["NT"] = {};
    dict["QLD"] = {};
    dict["SA"] = {};
    dict["TAS"] = {};
    dict["VIC"] = {};
    dict["WA"] = {};
    function out(dict){
        terms.some(function (name){
            var url = viewUrlA+name+viewUrlB;
            couch.get(dbname3,url).then(
                function(data,headers,status){
                    var data1 = data.data.rows;
                    for (var k in data1){
                        var tmp = data1[k];
                        dict[tmp["key"]][name] = tmp["value"];
                    };
                    if(Object.keys(dict["WA"]).length==9){
                        for (var key in dict) {
                            if(Object.keys(dict[key]).length==0){
                                delete dict[key];
                            };
                        };
                        res.render('gameDistribute',{
                            
                            gameDistribute:JSON.stringify(dict)
                        });
                        return true;

                        
                    };
                },
                function(err){
                    res.send(err);
                }
                
            )
            
    })
    }
    function sin(dict,callback){
        terms1.some(function (name){
            var url = viewUrlAs+name+viewUrlB;
            couch.get(dbname5,url).then(
                function(data,headers,status){
                    var data1 = data.data.rows;
                    for (var k in data1){
                        var tmp = data1[k];
                        dict[tmp["key"]]['single_'+name] = tmp["value"];
                    };
                    if(Object.keys(dict["WA"]).length==4){
                        for (var key in dict) {
                            if(Object.keys(dict[key]).length==0){
                                delete dict[key];
                            };
                        };
                        callback(dict);
                        return true;

                        
                    };
                },
                function(err){
                    console.log('error2');
                }
                
            )
            
    })
    }
    terms1.some(function (name){
            var url = viewUrlAm+name+viewUrlB;
            couch.get(dbname4,url).then(
                function(data,headers,status){
                    var data1 = data.data.rows;
                    for (var k in data1){
                        var tmp = data1[k];
                        dict[tmp["key"]]['multiple_'+name] = tmp["value"];
                    };
                    if(Object.keys(dict["WA"]).length==2){
                        for (var key in dict) {
                            if(Object.keys(dict[key]).length==0){
                                delete dict[key];
                            };
                        };
                        sin(dict,out)
                        return true;

                        
                    };
                },
                function(err){
                    console.log('error1');
                }
                
            )
            
    })
    
});




app.get('/mulDistribute',function(req,res){
    var dict = {};
    dict["ACT"] = {};
    dict["NSW"] = {};
    dict["NT"] = {};
    dict["QLD"] = {};
    dict["SA"] = {};
    dict["TAS"] = {};
    dict["VIC"] = {};
    dict["WA"] = {};
    terms.some(function (name){
            var url = viewUrlAm+name+viewUrlB;
            couch.get(dbname4,url).then(
                function(data,headers,status){
                    var data1 = data.data.rows;
                    for (var k in data1){
                        var tmp = data1[k];
                        dict[tmp["key"]][name] = tmp["value"];
                    };
                    if(Object.keys(dict["WA"]).length==5){
                        for (var key in dict) {
                            if(Object.keys(dict[key]).length==0){
                                delete dict[key];
                            };
                        };
                        res.render('mulDistribute',{
                            
                            mulDistribute:JSON.stringify(dict)
                        });
                        return true;

                        
                    };
                },
                function(err){
                    res.send(err);
                }
                
            )
            
    })
    
});




var vicMap = {
"4893":"Ararat",            "4898":"Barinsdale",        "4899":"Ballarat",
"4902":"Benalla",           "4903":"Bendigo",           "4925":"Castlemaine",
"4928":"Clifton_Springs",   "4930":"Colac",             "4937":"Craigieburn",  

"4938":"Cranbourne",        "4939":"Crib_Point",        "4951":"Geelong",   
"4960":"Hamilton",          "4961":"Hastings",          "4962":"Healesville",
"4964":"Horsham",           "4975":"Kyabram",           "4976":"Lakes_Entrance",

"4977":"Lara",              "4980":"Leopold",           "4988":"Maryborough",
"4990":"Melbourne",         "4991":"Melton",            "4992":"Mildura",   
"4996":"Morwell",           "5015":"Pakenham",          "5022":"Portland",

"5031":"Sale",              "5034":"Somerville",        "5035":"Stawell",
"5036":"Sunbury",           "5037":"Swan_Hill",         "5045":"Traralgon",
"5052":"Wangaratta",        "5053":"Warragul",          "5054":"Warrnambool",
"5058":"Wodonga",           "5060":"Wonthaggi"};

app.get('/vicDistribute',function(req,res){
    var dict1 = {};
    dict1["Ararat"] = {};
    dict1["Barinsdale"] = {};
    dict1["Ballarat"] = {};
    dict1["Benalla"] = {};
    dict1["Bendigo"] = {};
    dict1["Castlemaine"] = {};
    dict1["Clifton_Springs"] = {};
    dict1["Colac"] = {};
    dict1["Craigieburn"] = {};

    dict1["Cranbourne"] = {};
    dict1["Crib_Point"] = {};
    dict1["Geelong"] = {};
    dict1["Hamilton"] = {};
    dict1["Hastings"] = {};
    dict1["Healesville"] = {};
    dict1["Horsham"] = {};
    dict1["Kyabram"] = {};
    dict1["Lakes_Entrance"] = {};

    dict1["Lara"] = {};
    dict1["Leopold"] = {};
    dict1["Maryborough"] = {};
    dict1["Melbourne"] = {};
    dict1["Melton"] = {};
    dict1["Mildura"] = {};
    dict1["Morwell"] = {};
    dict1["Pakenham"] = {};
    dict1["Portland"] = {};

    dict1["Sale"] = {};
    dict1["Somerville"] = {};
    dict1["Stawell"] = {};
    dict1["Sunbury"] = {};
    dict1["Swan_Hill"] = {};
    dict1["Traralgon"] = {};
    dict1["Wangaratta"] = {};
    dict1["Warragul"] = {};
    dict1["Warrnambool"] = {};

    dict1["Wodonga"] = {};
    dict1["Wonthaggi"] = {};
    
    terms.some(function (name){
            var url = viewUrlA+name+viewUrlC;
            couch.get(dbname3,url).then(
                function(data,headers,status){
                    var data1 = data.data.rows;
                    for (var k in data1){
                        var tmp = data1[k];
                        
                        
                        if(tmp["key"][0]=="VIC"&&tmp["key"][1]!=null){
                            dict1[vicMap[tmp["key"][1]]][name] = tmp["value"];
                            

                        }
                    };

                    if(Object.keys(dict1["Melbourne"]).length==5){
                        for (var key in dict1) {
                            if(Object.keys(dict1[key]).length==0){
                                delete dict1[key];
                            };
                        };
                        res.render('vicDistribute',{
                            
                            vicDistribute:JSON.stringify(dict1)
                        });
                        return true;
                        
                    }
                },
                function(err){
                    res.send(err);
                }
                
            )
            
    })

});

dict0={};
dict0["Ararat"] = {};
dict0["Barinsdale"] = {};
dict0["Ballarat"] = {};
dict0["Benalla"] = {};
dict0["Bendigo"] = {};
dict0["Castlemaine"] = {};
dict0["Clifton_Springs"] = {};
dict0["Colac"] = {};
dict0["Craigieburn"] = {};

dict0["Cranbourne"] = {};
dict0["Crib_Point"] = {};
dict0["Geelong"] = {};
dict0["Hamilton"] = {};
dict0["Hastings"] = {};
dict0["Healesville"] = {};
dict0["Horsham"] = {};
dict0["Kyabram"] = {};
dict0["Lakes_Entrance"] = {};

dict0["Lara"] = {};
dict0["Leopold"] = {};
dict0["Maryborough"] = {};
dict0["Melbourne"] = {};
dict0["Melton"] = {};
dict0["Mildura"] = {};
dict0["Morwell"] = {};
dict0["Pakenham"] = {};
dict0["Portland"] = {};

dict0["Sale"] = {};
dict0["Somerville"] = {};
dict0["Stawell"] = {};
dict0["Sunbury"] = {};
dict0["Swan_Hill"] = {};
dict0["Traralgon"] = {};
dict0["Wangaratta"] = {};
dict0["Warragul"] = {};
dict0["Warrnambool"] = {};

dict0["Wodonga"] = {};
dict0["Wonthaggi"] = {};

var json = require('./data.json');
var a = [];
var c = {};
a = json['features'];
for(var i in a){
    for(var b in dict0){
        if(a[i]['properties']['lga_name06'].toString().toLowerCase().indexOf(b.toString().toLowerCase()) != -1){
            c[b] = a[i]['properties']['numeric'];
        }
    }
}

app.get('/sleepDistribute',function(req,res){
    dict2={};
    dict2["Ararat"] = {};
    dict2["Barinsdale"] = {};
    dict2["Ballarat"] = {};
    dict2["Benalla"] = {};
    dict2["Bendigo"] = {};
    dict2["Castlemaine"] = {};
    dict2["Clifton_Springs"] = {};
    dict2["Colac"] = {};
    dict2["Craigieburn"] = {};

    dict2["Cranbourne"] = {};
    dict2["Crib_Point"] = {};
    dict2["Geelong"] = {};
    dict2["Hamilton"] = {};
    dict2["Hastings"] = {};
    dict2["Healesville"] = {};
    dict2["Horsham"] = {};
    dict2["Kyabram"] = {};
    dict2["Lakes_Entrance"] = {};

    dict2["Lara"] = {};
    dict2["Leopold"] = {};
    dict2["Maryborough"] = {};
    dict2["Melbourne"] = {};
    dict2["Melton"] = {};
    dict2["Mildura"] = {};
    dict2["Morwell"] = {};
    dict2["Pakenham"] = {};
    dict2["Portland"] = {};

    dict2["Sale"] = {};
    dict2["Somerville"] = {};
    dict2["Stawell"] = {};
    dict2["Sunbury"] = {};
    dict2["Swan_Hill"] = {};
    dict2["Traralgon"] = {};
    dict2["Wangaratta"] = {};
    dict2["Warragul"] = {};
    dict2["Warrnambool"] = {};

    dict2["Wodonga"] = {};
    dict2["Wonthaggi"] = {};
    var s=0;
    var t=0;
    var r=0;
    terms1.some(function (name){
            var url = viewUrlA+name+viewUrlC;
            couch.get(dbname3,url).then(
                function(data,headers,status){
                    var data1 = data.data.rows;
                    for (var k in data1){
                        var tmp = data1[k];
                        
                        
                        if(tmp["key"][0]=="VIC"&&vicMap[tmp["key"][1]] in c){
                            if(name=='total_time'){
                                t = t+ tmp['value'];
                                s = s + c[vicMap[tmp["key"][1]]];
                                dict2[vicMap[tmp["key"][1]]][name] = tmp["value"];
                                dict2[vicMap[tmp["key"][1]]]["sleep"] = c[vicMap[tmp["key"][1]]];
                            };
                            if(name=='recent_time'){
                                r = r+ tmp['value'];
                                dict2[vicMap[tmp["key"][1]]][name] = tmp["value"];
                            };
                            
                            
                            

                        }
                    };
                    if(Object.keys(dict2["Melbourne"]).length==3){
                        var rate1 = t/s;
                        var rate2 = r/s;
                        for (var key in dict2) {
                            if(Object.keys(dict2[key]).length==0){
                                delete dict2[key];
                            }
                            else{
                                dict2[key]['total_time']=(dict2[key]['total_time']/rate1).toFixed(2);
                                dict2[key]['recent_time']=(dict2[key]['recent_time']/rate2).toFixed(2);
                            };
                            
                        };
                        res.render('sleepDistribute',{
                            
                            sleepDistribute:JSON.stringify(dict2)
                        });
                        return true;
                    }
                },
                function(err){
                    res.send(err);
                }
                
            )
            
    })

});










app.listen(3000,function(){
console.log('Server Started on Port 3000');
});