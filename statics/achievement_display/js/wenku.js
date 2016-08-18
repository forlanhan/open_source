

function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}
	function ajax(id) //ajax 获取节点信息
{
    //alert(id);
    var txt;
    var url = "convert_id_name?id=" + id + "&";
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

            txt = xmlhttp.responseText;	//获取ajax请求的数据；
            return txt;

        }
      }
    xmlhttp.open("GET",url+"rand="+Math.random(),false);
    xmlhttp.send();
    return txt;

}


function datatable_1(){
    $(document).ready( function () {
            var txt;
            var oTable = $('#table-content').dataTable({
            // ...
                "processing": true,
                "serverSide": true,
                //"ajax": "/data"
                "ajax": {
                    "url": "/datatable_1",
                    "type": "GET",
                },
                "columns": [
                    {
                        "data": 0,
                        "class": "bm_check_0"
                    }, {
                        "data": 0,
                        "class": "bm_check_1",
                        "render": function(data, type, row) {
                            txt = ajax(data);
                            if(txt) {
                                return txt;
                            }
                            else{
                                return "暂无";
                            }

                        }
                    },
                    {
                        "data": 1,
                        "class": "bm_check_2",
                        "render": function(data, type, row) {
                            return '<span class="badge">' +data+ '</span>'
                        }
                    },{
                        "data": 2,
                        "class": "bm_check_3"
                    },{
                        "data": 3,
                        "class": "bm_check_4"
                    },{
                        "data": 0,
                        "class": "bm_check_5",
                        "render": function(data, type, row) {
                            return '<a type="button" target="_blank" class="btn btn-success" href="http://192.168.120.234:8888/view-detail/?type=1&id='+ data +'"/>详情</a>'
                        }
                    }
                ]
             });



          } );
    }

function datatable_2(){
    $(document).ready( function () {
            var txt;
            var oTable = $('#table-content').dataTable({
            // ...
                "processing": true,
                "serverSide": true,
                //"ajax": "/data"
                "ajax": {
                    "url": "/datatable_2",
                    "type": "GET",
                },
                "columns": [
                    {
                        "data": 0,
                        "class": "bm_0"
                    },
                    {
                        "data": 1,
                        "class": "bm_2",
                        "render": function(data, type, row) {
                            return '<span class="badge">' +data+ '</span>'
                        }
                    },{
                        "data": 2,
                        "class": "bm_3"
                    },{
                        "data": 3,
                        "class": "bm_4"
                    },{
                        "data": 4,
                        "class": "bm_5",
                        "render": function(data, type, row) {
                            if(data){
                                return '<button type="button" class="btn btn-danger">有问题</button>'
                            }else{
                                return '<button type="button" class="btn btn-success">无问题</button>'
                            }
                        }
                    }
                ]
             });



          } );
    }


function datatable_3(){
    $(document).ready( function () {
            var txt;
            var oTable = $('#table-content').dataTable({
            // ...
                "processing": true,
                "serverSide": true,
                //"ajax": "/data"
                "ajax": {
                    "url": "/datatable_3",
                    "type": "GET",
                },
                "columns": [
                    {
                        "data": 0,
                        "class": "yx_0"
                    },
                    {
                        "data": 1,
                        "class": "yx_1",
                        "render": function(data, type, row) {
                            return '<span class="badge">' +data+ '</span>'
                        }
                    },{
                        "data": 2,
                        "class": "yx_2"
                    },{
                        "data": 3,
                        "class": "yx_3"
                    },{
                        "data": 4,
                        "class": "yx_5",
                        "render": function(data, type, row) {
                            if(data){
                                return data
                            }else{
                                return '无'
                            }
                        }

                    },{
                        "data": 5,
                        "class": "yx_4"
                    }
                ]
             });



          } );
    }


function datatable_4(){
    $(document).ready( function () {
            var txt;
            var oTable = $('#table-content').dataTable({
            // ...
                "processing": true,
                "serverSide": true,
                //"ajax": "/data"
                "ajax": {
                    "url": "/datatable_4",
                    "type": "GET",
                },
                "columns": [
                    {
                        "data": 0,
                        "class": "yx_0"
                    },
                    {
                        "data": 1,
                        "class": "yx_1"
                    },{
                        "data": 2,
                        "class": "yx_2"
                    },{
                        "data": 3,
                        "class": "yx_3"
                    },{
                        "data": 4,
                        "class": "yx_5",

                    },{
                        "data": 5,
                        "class": "yx_4",
                        "render": function(data, type, row) {
                            if(data){
                                return '<a type="button" target="_blank" class="btn btn-success" href="#"/>详情</a>'
                            }else{
                                return '无'
                            }
                        }
                    }
                ]
             });



          } );
    }
