/**
 * Created by changzhao619 on 5/17/16.
 */

////////////////////////
//定义全局变量    ///////
                //////
///////////////////////
var card_data_org ;
var card_data_person;
var related_data_org = new Array();
var related_data_person = new Array();


function statics_data(data){//统计数组中相同的数据并记录
    var arr = new Array();
    for(var i=0; i<data.length; i++){
        if(data[i].text){//数组存在
            //var n = i + 1;
            var num = 0; //初始个数
            for(var n=0; n<data.length; n++){
                if(n > i) break;
                if(data[i]['text'] == data[n]['text']){
                    num = num + 1;
                }
            }
            arr[data[i]['text']] = num + "**" + data[i]['link'];
        }
    }
    return arr;
}
function card_ajax(type_id){ //ajax 获取节点信息

    var txt;
    var JSONObject;
    var type = type_id.split("/")[0]
    var id = type_id.split("/")[1]
    var url = "card_get_res?type="+type+"id="+id+"&";
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
            //console.log( eval(txt));
            //JSONObject = eval ("[" + txt + "]"); //将json数据转换为js对象；
            //document.getElementById('card-title-content').innerHTML = JSONObject;

        }
      }
    xmlhttp.open("GET",url+"rand="+Math.random(),true);
    xmlhttp.send();
    return txt;

}

function generate_word(arr){//生成标签云的word变量
    var data_array = new Array();
    var n = 0;
    for(var i in arr){
        data_array[n] = new Array();
        data_array[n]['text'] = i.split("|")[1];
        data_array[n]['weight'] = arr[i].split("**")[0] / 10;
        //data_array[n]['link'] = "/force_open?id="+i;
        data_array[n]['link'] = new Array();
        data_array[n]['link']['href'] = "/force_open?id="+i;
        data_array[n]['link']['target'] = "_blank";
        n = n + 1;
    }
    //console.log(data_array);

    return data_array;
}

function card_org_statistics(org_array){//统计出现最多的机构
    var new_arr = new Array();
    var recode_arr = new Array();
    var max = 0;

    for(i in org_array){
        new_arr[i] = Number(org_array[i].split("**")[0]);
    }
    //console.log(new_arr.sort());
    for(i in new_arr){
        if(max<new_arr[i]){
            recode_arr[new_arr[i]]= max = new_arr[i];
            recode_arr[new_arr[i]] = i;
        }

    }
    return recode_arr[max];
}
////////////////////////
// 处理返回结果数据
function deal_data(curr, source, card_res){
    var str = "";
    var max_related_num = 10; //获取N篇论文的相关机构和任务;
    var n = 0;
    var m = 0;
    //console.log(source);
    for(var l=0; l<max_related_num+100; l++){//动态初始化二位数组
        related_data_org[l] = new Array();
        related_data_person[l] = new Array();
    }
    for(var i=0;i<source.length;i++){
        //标题 name
        str += '<div class="sr-content"><h3 class="sr-title"><a href="'+ source[i]._source.dataSource +'"  class="sr-title-a" target="_blank" alt="'+ source[i]._source.name +'">'+ judge_highlight('name', source[i]) +'</a></h3>';
        //作者+来源+年份
        if(source[i]._source.author || source[i]._source.journal || source[i]._source.yearNumber)
            str += '<div class="sr-info"><span>'+ split_name(judge_highlight('author', source[i])) +'</span> <span><a href="" target="_blank"  title="'+ source[i]._source.journal +'">'+ judge_highlight('journal', source[i]) +'</a></span><span class="sr-time" >'+ judge_highlight('yearNumber', source[i]) +'</span></div>';
        //摘要
        str += '<div class="sr-abstract">'+ judge_highlight('abstract', source[i]) +'</div>';
        //全部来源
        str += '<div class="sc_allversion"><span class="sr-gray">全部来源：</span>';
        str += '<span class="v_item_span">'+all_source(source[i]._source._source)+'</span>';

        str += '</div>';

        str += '</div>';

           //将结果放入div中

        if(curr == 1 && i<max_related_num){ //拿前max_related_num数据集

            if(source[i] && source[i]._source && source[i]._source.sourceOrganization ){
                for(var s_o_i=0; s_o_i<source[i]._source.sourceOrganization.length; s_o_i++){
                    if(source[i]._source.sourceOrganization[s_o_i]){
                        related_data_org[m]['text'] = source[i]._source.sourceOrganization[s_o_i];
                        related_data_org[m]['weight'] = 1;
                        related_data_org[m]['link'] = '#';
                        //console.log(related_data_org[m]);
                        m = m + 1;
                    }

                }

            }
            if(source[i]&& source[i]._source && source[i]._source.author){
                for(var s_o_i_2=0; s_o_i_2<source[i]._source.author.length; s_o_i_2++){
                    if(source[i]._source.author[s_o_i_2]){
                        related_data_person[n]['text'] = source[i]._source.author[s_o_i_2];
                        //related_data_person[n]['text'] = 1;
                        related_data_person[n]['weight'] = 1;
                        related_data_person[n]['link'] = n;
                        //console.log(related_data_person[n]);
                        n = n + 1;
                    }

                }
            }
        }

    }
    document.getElementById('main-result').innerHTML =  str ;  //将搜索结果放到页面中
    //console.log(related_data_person);
    //console.log(related_data_org);
     var words_arry = generate_word(statics_data(related_data_person)).concat(generate_word(statics_data(related_data_org)));
    //console.log(words_arry);
    jq_word(words_arry); //标签云;


    ///知识卡片
    if(source.length > 0 && card_res[0]){//当查询有结果是出现卡片
        var name = document.getElementById("card-title-content");   //姓名
        var content = document.getElementById("card-p");   //内容
        var img = document.getElementById("card-img");
        var id_get = card_res[0]._type+"/"+card_res[0]._id+"|"+card_res[0]._source.name;
        name.innerHTML = "<a href='/force_open?id="+id_get+"' target='_blank'>"+card_res[0]._source.name+"</a>";   // 插入姓名

        var str_card = "";  //机构基本描述
        //console.log(card_res);
        //document.getElementById("card").style.display = "block";
        $("#card").fadeIn("100");
        //document.getElementById("card-close").innerHTML = '<i id="close-icon" onclick="close_ele();">&#xe616;</i>';

        if(card_res[0]._type == "Person"){//如果该实体为人
            if(card_res[0]._source.worksFor){
                content.innerHTML = "<font color='red'>就职单位:</font>"+card_res[0]._source.worksFor.split("|")[1];
                img.innerHTML = '<i id="op-icon" >&#xe619;</i>';
            }
            img.innerHTML = '<i id="op-icon" >&#xe619;</i>';
        }else if(card_res[0]._type == "ResearchOrganization" || card_res[0]._type == "EducationalOrganization" || card_res[0]._type == "Corporation"){ //实体为机构
            if(card_res[0]._source.description){
                content.innerHTML = "<font color='red'>简介:</font>"+card_res[0]._source.description;    //组织实体简介
                img.innerHTML = '<i id="op-icon" >&#xe617;</i>';
            }
            if(card_res[0]._source.keyDiscipline){
                document.getElementById("direction").innerHTML = "<font color='red'>研究方向:</font>"+card_res[0]._source.keyDiscipline;    //组织实体简介
            }

            //细节描述
            var str_card = "";
            if(card_res[0]._source['location']){
                str_card += '<span class="org-tips">地点:</span><span class="org-context">'+card_res[0]._source['location']+'</span>&nbsp;&nbsp;';
            }
            if(card_res[0]._source.level){
                str_card += '<span class="org-tips">等级:</span><span class="org-context">'+card_res[0]._source.level+'</span>&nbsp;&nbsp;';
            }
            if(card_res[0]._source.foundingDate){
                str_card += '<span class="org-tips">成立时间:</span><span class="org-context">'+card_res[0]._source.foundingDate+'</span>';
            }
            if(card_res[0]._source.head[0]){
                document.getElementById("card-head").innerHTML = '<span class="org-tips">负责人:</span><span class="org-context"><a href="/force_open?id='+card_res[0]._source.head[0]+'" target="_blank">'+card_res[0]._source.head[0].split("|")[1]+'</a></span>';
            }
            document.getElementById("card-b-desc").innerHTML = str_card;
            img.innerHTML = '<i id="op-icon" >&#xe617;</i>';

        }else if(card_res[0]._type == "weapon"){
            var str_card = "";
            if(card_res[0]._source['launchMass']){
                str_card += '<span class="org-tips">速度:</span><span class="org-context">'+card_res[0]._source['launchMass']+'</span>&nbsp;&nbsp;';
            }
            if(card_res[0]._source.state){
                str_card += '<span class="org-tips">状态:</span><span class="org-context">'+card_res[0]._source.state+'</span>&nbsp;&nbsp;';
            }
            if(card_res[0]._source.diameter){
                str_card += '<span class="org-tips">直径:</span><span class="org-context">'+card_res[0]._source.diameter+'</span>';
            }
            document.getElementById("card-b-desc").innerHTML = str_card;

            var str_card = "";
            if(card_res[0]._source['militaryEquipment']){
                str_card += '<span class="org-tips">所属军队:</span><span class="org-context">'+card_res[0]._source['militaryEquipment']+'</span>&nbsp;&nbsp;';
            }
            if(card_res[0]._source.enginePower){
                str_card += '<span class="org-tips">马力:</span><span class="org-context">'+card_res[0]._source.enginePower+'</span>&nbsp;&nbsp;';
            }
            document.getElementById("m-e").innerHTML = str_card;

            var str_card = "";
            if(card_res[0]._source['vehicle_range']){
                str_card += '<span class="org-tips">射程:</span><span class="org-context">'+card_res[0]._source['vehicle_range']+'</span>&nbsp;&nbsp;';
            }
            if(card_res[0]._source.category){
                str_card += '<span class="org-tips">类别:</span><span class="org-context">'+card_res[0]._source.category+'</span>&nbsp;&nbsp;';
            }
            if(card_res[0]._source.length){
                str_card += '<span class="org-tips">长度:</span><span class="org-context">'+card_res[0]._source.length+'</span>&nbsp;&nbsp;';
            }
            document.getElementById("v-c").innerHTML = str_card;


            if(card_res[0]._source.guidance){
                document.getElementById("card-gu").innerHTML = '<span class="org-tips">引导方式:</span><span class="org-context">'+card_res[0]._source.guidance+'</span>&nbsp;&nbsp;';
            }
            if(card_res[0]._source.feed){
                document.getElementById("card-feed").innerHTML = '<span class="org-tips">子弹:</span><span class="org-context">'+card_res[0]._source.feed+'</span>&nbsp;&nbsp;';
            }
            if(card_res[0]._source.description){
                document.getElementById("card-p").innerHTML = "<font color='red'>简介:</font>"+card_res[0]._source.description;
            }

            img.innerHTML = '<i id="op-icon" >&#xe60e;</i>';

        }

        //document.getElementById("card-img").innerHTML = '<i id="op-icon" >&#xe617;</i>';
        //var id_get = card_res[0]._type+"/"+card_res[0]._id+"|"+card_res[0]._source.name;
        //document.getElementById("card-title-content").innerHTML = '<a href="/force_open?id='+id_get+'" target="_blank">'+card_res[0]._source.name+'</a>';
        //
        //if(card_res[0]._source['location']){
        //    str_card += '<span class="org-tips">地点:</span><span class="org-context">'+card_res[0]._source['location']+'</span>&nbsp;&nbsp;';
        //}
        //if(card_res[0]._source.level){
        //     str_card += '<span class="org-tips">等级:</span><span class="org-context">'+card_res[0]._source.level+'</span>&nbsp;&nbsp;';
        //}
        //if(card_res[0]._source.foundingDate){
        //     str_card += '<span class="org-tips">成立时间:</span><span class="org-context">'+card_res[0]._source.foundingDate+'</span>';
        //}
        //
        //document.getElementById("card-b-desc").innerHTML = str_card;
        //
        //if(card_res[0]._source.description){
        //    document.getElementById("card-p").innerHTML = card_res[0]._source.description;
        //}
        //
        //if(card_res[0]._source.keyDiscipline){
        //    document.getElementById("card-key").innerHTML = '研究范围: <span id="org-keyDiscipline">'+card_res[0]._source.keyDiscipline+'</span>';
        //}

    }else{
        document.getElementById("rel-crap").style.marginTop = "0px";
    }




    ///标签云

}

//Pers/1000900418|凌荣辉   -> 凌荣辉
function split_name(data){
    var string_data = "";
    if(data){
        if(typeof(data)  == "string"){
            return data.split('|') ;
        }else if(typeof(data)  == "object") {
            for(n=0; n<data.length; n++){
                string_data += data[n].split("|")[1];
                string_data += "&nbsp;-&nbsp;"
            }
            return string_data;
        }else{
            return typeof(data[0]);
        }
    }else{
        return "";
    }

}

function judge_highlight(field, source_i){
    switch(field){
        case "name":
            if(source_i.highlight.name)
                return source_i.highlight.name;
            else
                return source_i._source.name;
            break;

        case "author":
            if(source_i.highlight.author) {
                //console.log(source_i.highlight.author);
                return source_i._source.author;
            }
            else
                return source_i._source.author;
            break;

        case "abstract":
            if(source_i.highlight.abstract)
                return source_i.highlight.abstract;
            else{
                if(source_i._source.abstract)return source_i._source.abstract;
                else return"";
            };
            break;

        case "yearNumber":
            if(source_i._source.yearNumber)
                return source_i._source.yearNumber;
            else
                return "";
            break;

        case "journal":
            if(source_i._source.journal)
                return '《'+source_i._source.journal+'》&nbsp;-&nbsp;';
            else
                return "";
            break;

    }
}
//处理全部来源 全部来源是一个列表
function all_source(obj){
    var str_all_source = "";
    for(var i=0; i<obj.length; i++){
        str_all_source += '<a class="v_source" title="" target="_blank" href="'+ obj[i].url +'" >'+ obj[i].tag +'</a>&nbsp;&nbsp;&nbsp;&nbsp;';
    }
    return str_all_source;
}

/////////////////////////////
//处理论文分类
function deal_paper_class(obj, data){
    var input = document.getElementById('paper-type');
    var tab = document.getElementsByClassName("tab");
    for(var i=0;i<tab.length;i++){
        tab[i].className = "tab";
    }
    obj.className = "selected tab";
    input.value = data;
}
function deal_paper_class_only_paper(obj, paper){
    var input1 = document.getElementById('paper-type');
    var tab = document.getElementsByClassName("tab");
    for(var i=0;i<tab.length;i++){
        tab[i].className = "tab";
    }
    obj.className = "selected tab";
    input1.value = paper;
}





////////////////////////////////
//go up
$('#scan-course-a').click(function(){
    $('html,body').animate({scrollTop:$('#course').offset().top}, 1000);
    return false;
});

$(document).ready(function () {
        $.goup({
            trigger: 100,
            bottomOffset: 150,
            locationOffset: 120,
            title: '回到顶部',
            titleAsText: true,
            arrowColor: '#fff',
            containerColor: '#4694D1',
            titleAsTextClass: 'go-up-title'

        });
    });

////////////////////////////
//记录结果状态
function rem_form_status(paper, body){
    if(paper == "all"){
        var paper_obj = document.getElementById("form-span-1");
        deal_paper_class_only_paper(paper_obj, paper);
    }else if(paper == "ConferencePaper"){
        var paper_obj = document.getElementById("form-span-2");
        deal_paper_class_only_paper(paper_obj, paper);
    }else if(paper == "JournalPaper"){
        var paper_obj = document.getElementById("form-span-3");
        deal_paper_class_only_paper(paper_obj, paper);
    }else if(paper == "Thesis"){
        var paper_obj = document.getElementById("form-span-4");
        deal_paper_class_only_paper(paper_obj, paper);
    }

    if(body == "all"){
        var body_obj = document.getElementById("option-0")
        body_obj.selected = true;
    }else if(body == "name"){
        var body_obj = document.getElementById("option-1")
        body_obj.selected = true;
    }else if(body == "author"){
        var body_obj = document.getElementById("option-2")
        body_obj.selected = true;
    }else if(body == "sourceOrganization"){
        var body_obj = document.getElementById("option-3")
        body_obj.selected = true;
    }else if(body == "abstract"){
        var body_obj = document.getElementById("option-4")
        body_obj.selected = true;
    }
}

////////////////////
//处理主题和机构
///////////////////
function get_agg(keyvalue, papertype, bodytype, fields, id){ //ajax 获取节点信息
    var txt;
    var url = "ajax_agg?keyvalue="+keyvalue+"&papertype="+papertype+"&bodytype="+bodytype+"&fields="+fields+"&";
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
            //console.log( eval(txt));
            //JSONObject = eval ("[" + txt + "]"); //将json数据转换为js对象；
            //console.log(txt);
            document.getElementById(id).innerHTML = txt;

        }
      }
    xmlhttp.open("GET",url+"rand="+Math.random(),false);
    xmlhttp.send();
}



////////////////////////////////////
//标签云
//function jq_word(words){
//    //console.log(words);
//    $(function() {
//        $('#rel-content').jQCloud(words,{
//             autoResize: true,
//            fontSize: {
//                from: 0.10,
//                to: 0.01
//            }
//        });
//
//    });
//}
function jq_word(words){


    $(function() {
        $('#rel-content').jQCloud(words,{
             autoResize: true,
            fontSize: {
                from: 0.10,
                to: 0.01
            }
        });

    });



}


function close_ele(){
    //var dom = document.getElementById("card");
    $("#card").hide();
    document.getElementById("rel-crap").style.marginTop = "0px";


}

function display_sort_fun(sorn_en){
    /*
    * 显示界面是哪种排序方式*/
    var id_obj = document.getElementById("drop-button");
    if(sorn_en == "none") {
        id_obj.innerHTML  = '相关性<span class="caret"></span>';
    }else{
        id_obj.innerHTML = '敏感性<span class="caret"></span>';
    }
}

