/**
 * Created by changzhao619 on 5/19/16.
 */

function close_ele(id){
    //var obj = document.getElementById(id);
    //obj.style.display = "none";
    $("#card").hide();
}

function show_ele(id, par, res_content_left){
    //var obj = document.getElementById(id);
    //obj.style.display = "block";
    //$("#card").show();

    $("#card").show();
    clear_card_content();

    if(par == "more"){//如果更多数据
        var content = document.getElementById("card-p");   //内容
        var name = document.getElementById("card-title-content");   //姓名
        var str_a = "";
        for(var n=0; n<res_content_left.length; n++ ){
            var id_get = res_content_left[n]._type+"/"+res_content_left[n]._id+"|"+res_content_left[n]._source.name;
            str_a += '<a href="/force_open?id='+id_get+'" onmouseover="more_content_display(\''+id_get+'\');" target="_blank">'+res_content_left[n]._source.name+'</a>|';
        }
        document.getElementById("card-img").innerHTML = '<i id="op-icon" >&#xe61b;</i>';
        document.getElementById("more").innerHTML = str_a;
        name.innerHTML =  "更多相关数据";
    }else{//如果为正常显示数据
            //数据处理开始
        var type ; //ES查询数据类型
        var id; //ES查询ID
        type = par.split("|")[0].split("/")[0];
        id = par.split("|")[0].split("/")[1]

        var res = get_node_info_ajax(id, type)[0]; //返回的结果


        var name = document.getElementById("card-title-content");   //姓名
        var content = document.getElementById("card-p");   //内容
        var img = document.getElementById("card-img");
        name.innerHTML = "<a href='/force_open?id="+par+"' target='_blank'>"+res._source.name+"</a>";   // 插入姓名

        if(res._type == "Person"){//如果该实体为人
            if(res._source.worksFor){
                content.innerHTML = "<font color='red'>就职单位:</font>"+res._source.worksFor.split("|")[1];
                img.innerHTML = '<i id="op-icon" >&#xe619;</i>';
            }
        }else if(res._type == "ResearchOrganization" || res._type == "EducationalOrganization" || res._type == "Corporation"){ //实体为机构
            if(res._source.description){
                content.innerHTML = res._source.description;
                img.innerHTML = '<i id="op-icon" >&#xe617;</i>';
            }

            //细节描述
            var str_card = "";
            if(res._source['location']){
                str_card += '<span class="org-tips">地点:</span><span class="org-context">'+res._source['location']+'</span>&nbsp;&nbsp;';
            }
            if(res._source.level){
                str_card += '<span class="org-tips">等级:</span><span class="org-context">'+res._source.level+'</span>&nbsp;&nbsp;';
            }
            if(res._source.foundingDate){
                str_card += '<span class="org-tips">成立时间:</span><span class="org-context">'+res._source.foundingDate+'</span>';
            }
            document.getElementById("card-b-desc").innerHTML = str_card;

        }else {
            //document.getElementById("").innerHTML = "";
            if(res._source['author']){
                var str_au = '<span class="org-tips">作者:</span>';
                for(var au_i=0; au_i<res._source['author'].length; au_i++){
                    str_au += '<span class="org-context"><a href="/force_open?id='+res._source['author'][au_i]+'" target="_blank">'+res._source['author'][au_i].split("|")[1]+'</a></span>&nbsp;&nbsp;';
                }
                str_au += '</span>';
                document.getElementById("card-b-desc").innerHTML = str_au;

            }
            if(res._source.abstract){
                content.innerHTML = "<font color='red'>摘要:</font>"+res._source.abstract;
                img.innerHTML = '<i id="op-icon" >&#xe618;</i>';
            }


        }
    }
}


function insert_content(JSONObject){
    //document.getElementById('card-title-content').
}

  function get_node_info_ajax(id, type) //ajax 获取节点信息
{
    var JSONObject;
    var txt;
    var url = "get_node_info?id=" + id + "&type=" + type + "&";
    if (window.XMLHttpRequest){// code for IE7+, Firefox, Chrome, Opera, Safari
          xmlhttp=new XMLHttpRequest();
    }
    else {// code for IE6, IE5
          xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange=function(){
          if (xmlhttp.readyState==4 && xmlhttp.status==200)
            {

                txt = xmlhttp.responseText; //获取ajax请求的数据；
                JSONObject = eval ("(" + txt + ")"); //将json数据转换为js对象；
                return JSONObject;
            }
    }
    xmlhttp.open("GET",url+"rand="+Math.random(),false);
    xmlhttp.send();
    return JSONObject;

}






function generate_node(id, res, res_content_left){
    var node_link = new Array();
    var node = new Array();
    var link = new Array();
    if(res_content_left != "0"){
        for(var i=0; i<res.length+2; i++){
        node[i] = {};
        link[i] = {};
        }
    }else{
        for(var i=0; i<res.length+1; i++){
        node[i] = {};
        link[i] = {};
        }

    }


    node[0].id = 0;
    node[0].category = 0;
    node[0].name = id;
    node[0].label = id.split("|")[1];
    node[0].symbolSize = 40;
    node[0].ignore = false;
    node[0].flag = true;
    node[0]['symbol'] = display_img_type(id.split("/")[0]);


    //node[1].id = 1;
    //node[1].category = 0;
    //node[1].name = "2";
    //node[1].label = "22";
    //node[1].symbolSize = 60;
    //node[1].ignore = false;
    //node[1].flag = true;
    //node[1]['symbol'] = 'heart';


    for(var n=0; n<res.length; n++){

        node[n+1].id = n+1;
        node[n+1].category = 1;
        node[n+1].name = res[n]._type+"/"+res[n]._id+"|"+res[n]._source.name;
        node[n+1].label = res[n]._source.name;
        node[n+1].symbolSize = 25;
        node[n+1].ignore = false
        node[n+1].flag = true;
        node[n+1].symbol = display_img_type(res[n]._type);

        link[n].source = n+1;
        link[n].target = 0;
        console.log(node);

    }
    if(res_content_left != "0"){
        node[n+1].id = n+1;
        node[n+1].category = 1;
        node[n+1].name = "more";
        node[n+1].label = "更多";
        node[n+1].symbolSize = 30;
        node[n+1].ignore = false;
        node[n+1].flag = true;
        node[n+1].symbol = 'circle';

        link[n].source = n+1;
        link[n].target = 0;
    }

    node_link['node'] = node;
    node_link['link'] = link;

    return node_link;
}


function display_img_type(type){
    if(type == "Person"){
        return "image://statics/achievement_display/img/user.png";
    }else if(type == "ResearchOrganization" || type == "EducationalOrganization" || type == "Corporation"){
        return 'image://statics/achievement_display/img/force-icon/org.jpg';
    }else{
        return 'image://statics/achievement_display/img/paper.png';
    }
}

function clear_card_content(){
    document.getElementById("card-title-content").innerHTML = "";
    document.getElementById("card-b-desc").innerHTML = "";
    document.getElementById("card-p").innerHTML = "";
    document.getElementById("card-key").innerHTML = "";
}

function more_content_display(val){
     close_ele("card");
     show_ele("card", val, "none");

}