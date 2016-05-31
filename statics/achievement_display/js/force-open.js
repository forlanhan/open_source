/**
 * Created by changzhao619 on 5/19/16.
 */



function close_ele(id){
    var obj = document.getElementById(id);
    obj.style.display = "none";
}

function show_ele(id, par){
    var obj = document.getElementById(id);
    obj.style.display = "block";
    var test = document.getElementById("test");

    test.innerHTML = par;
}


function insert_content(JSONObject){
    //document.getElementById('card-title-content').
}

  function ajax(id) //ajax 获取节点信息
{
    var JSONObject;
  var txt;
    var url = "get_node_info?id=" + id + "&";
if (window.XMLHttpRequest)
  {// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  }
else
  {// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
xmlhttp.onreadystatechange=function()
  {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {

        txt = xmlhttp.responseText; //获取ajax请求的数据；
        JSONObject = eval ("(" + txt + ")"); //将json数据转换为js对象；



    }
  }
xmlhttp.open("GET",url+"rand="+Math.random(),false);
xmlhttp.send();

}



function test(){
    require.config({
            paths : {
                echarts : 'http://echarts.baidu.com/build/dist'
            }
        });
        //var nod = "{
        //                     id:0,
        //                     category:0,
        //                     name:'E0000012_93993993',
        //                     label:'中国科学院信息工程研究所',
        //                     symbolSize:60,
        //                     ignore:false,
        //                     flag:false,
        //                     symbol: 'image://statics/achievement_display/img/force-icon/org.jpg'
        //
        //             }";


        require([ "echarts", "echarts/chart/force"], function(ec) {
            var myChart = ec.init(document.getElementById('demo1'), 'macarons');
            var nod;
            var option = {
                tooltip : {
                    show : false
                },
                name: "知识图谱",
                minRadius : 15,
                maxRadius : 25,
                density : 0.8,
                attractiveness: 0.8,
                gravity: 1,
                roam: true,
                steps: 1,

                legend: {
                    x: 'left',
                    selected:{'学校':true,'校区':true,'学院':true,'班级':true},
                    data:['学校','校区','学院','班级']
                },
                series : [ {
                    type : 'force',
                    name : "Force tree",

                    itemStyle: {

                        normal: {
                            label: {
                                show: true,
                                position: 'right',
                                textStyle: {
                                    color: '#000000',
                                    fontWeight: 900,
                                    align: "right",
                                    baseline: "top",
                                }
                            },
                            nodeStyle : {
                                brushType : 'both',
                                strokeColor : 'rgba(255,215,0,0.4)',
                                lineWidth : 1
                            },
                            linkStyle:{
                                type:"curve",
                                width: 4
                             }

                        },emphasis:{
                            linkStyle : { strokeColor : '#5182AB'}
                        }
                    },
                    categories : [
                        {
                            name : '学校',
                            itemStyle: {
                                normal: {
                                color : '#ff7f50'
                                }
                            }
                        }, {
                            name : '校区',
                             itemStyle: {
                                normal: {
                                color : '#87cdfa'
                                }
                            }
                        }, {
                            name : '学院',
                            itemStyle: {
                                normal: {
                                color : '#ff7f50'
                                }
                            }
                        }, {
                            name : '班级',
                            itemStyle: {
                                normal: {
                                color : '#87cdfa'
                                }
                            }
                        }
                    ],
                     nodes :
                     [
                         {
                             id:0,
                             category:0,
                             name:'E0000012_93993993',
                             label:'中国科学院信息工程研究所',
                             symbolSize:60,
                             ignore:false,
                             flag:false,
                             symbol: 'image://statics/achievement_display/img/force-icon/org.jpg'

                     },
                         //nod,
                     {id:1,category:1,name:'1',label:'中国科学院信息工程研究所',symbolSize:30,ignore:false,flag:true,
                     symbol: 'heart'},
                     {id:2,category:2,name:'2',label:'学院1',symbolSize:20,ignore:true,flag:true,
                     symbol: 'star'},
                     {id:3,category:2,name:'3',label:'学院2',symbolSize:20,ignore:true,flag:true},
                     {id:4,category:1,name:'4',label:'白春礼',symbolSize:30,ignore:false,flag:true},
                     {id:5,category:2,name:'5',label:'学院1',symbolSize:20,ignore:true,flag:true},
                     {id:6,category:2,name:'6',label:'学院2',symbolSize:20,ignore:true,flag:true},
                     {id:7,category:2,name:'7',label:'学院3',symbolSize:20,ignore:true,flag:true},
                     {id:8,category:1,name:'8',label:'中科院计算技术研究所',symbolSize:30,ignore:false,flag:true},
                     {id:9,category:2,name:'9',label:'学院1',symbolSize:20,ignore:true,flag:true},
                     {id:10,category:2,name:'10',label:'学院2',symbolSize:20,ignore:true,flag:true},
                     {id:11,category:2,name:'11',label:'学院3',symbolSize:20,ignore:true,flag:true},
                     {id:12,category:2,name:'12',label:'学院4',symbolSize:20,ignore:true,flag:true},
                     {id:13,category:3,name:'13',label:'一班',number:45,techear:'张三',symbolSize:10,ignore:true,flag:true},
                     {id:14,category:3,name:'14',label:'二班',number:52,techear:'李四',symbolSize:10,ignore:true,flag:true}
                     ],
                     links : [ {source : 1,target : 0}, {source : 4,target : 0}, {source : 8,target : 0},
                              {source : 2,target : 1}, {source : 3,target : 1}, {source : 5,target : 4},
                              {source : 6,target : 4}, {source : 7,target : 4}, {source : 9,target : 8},
                              {source : 10,target : 8}, {source : 11,target : 8}, {source : 12,target : 8},
                              {source : 13,target : 6}, {source : 14,target : 13},{source : 14,target : 12} ]
                } ]
            };
            myChart.setOption(option);
            var ecConfig = require('echarts/config');
            function openOrFold(param) {
                var option = myChart.getOption();
                var nodesOption = option.series[0].nodes;
                var linksOption = option.series[0].links;
                var data = param.data;
                var linksNodes = [];

                var categoryLength = option.series[0].categories.length;

                //if (data.category == (categoryLength - 1)) {
                  //  alert(data.label);
                //}

                if (data != null && data != undefined) {
                    if (data.flag) {

                        for ( var m in linksOption) {

                            if (linksOption[m].target == data.id) {
                                linksNodes.push(linksOption[m].source);
                            }
                        }
                        if (linksNodes != null && linksNodes != undefined) {
                            for ( var p in linksNodes) {
                                nodesOption[linksNodes[p]].ignore = false;
                                nodesOption[linksNodes[p]].flag = true;
                            }
                        }
                        nodesOption[data.id].flag = false;
                        myChart.setOption(option);
                    } else {

                        for ( var m in linksOption) {

                            if (linksOption[m].target == data.id) {
                                linksNodes.push(linksOption[m].source);
                            }
                            if (linksNodes != null && linksNodes != undefined) {
                                for ( var n in linksNodes) {
                                    if (linksOption[m].target == linksNodes[n]) {
                                        linksNodes.push(linksOption[m].source);
                                    }
                                }
                            }
                        }
                        if (linksNodes != null && linksNodes != undefined) {
                            for ( var p in linksNodes) {
                                nodesOption[linksNodes[p]].ignore = true;
                                nodesOption[linksNodes[p]].flag = true;
                            }
                        }
                        nodesOption[data.id].flag = true;
                        myChart.setOption(option);
                    }
                }
            }
            myChart.on(ecConfig.EVENT.CLICK, openOrFold);
            /////////////////////////////////////////////////
            var show_info = function show_info(param) {
                var option = myChart.getOption();
                var nodesOption = option.series[0].nodes;
                var linksOption = option.series[0].links;
                var data = param.data;
                var linksNodes = [];
                var categoryLength = option.series[0].categories.length;
                if(data.label){
                    close_ele("card");
                    show_ele("card", data.name);
                }


               // if (data.category == (categoryLength - 1)) {
                    //alert(data.category);
               // }

            }
            myChart.on(ecConfig.EVENT.HOVER, show_info);
            ////////////////////////////////////////////////
        });
}

