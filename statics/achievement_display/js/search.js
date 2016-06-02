/**
 * Created by changzhao619 on 5/17/16.
 */

//	//以下将以jquery.ajax为例，演示一个异步分页
//function demo(curr, key){
//    $.getJSON('/ajax_page', {
//        page: curr || 1 ,//向服务端传的参数，此处只是演示
//        keyvalue: key
//
//    }, function(res){
//        //此处仅仅是为了演示变化的内容1
//
//
//        document.getElementById('s-c-all').innerHTML =  (res.result_content)[0]._source.description ;
//        //显示分页
//        laypage({
//            cont: 'page1', //容器。值支持id名、原生dom对象，jquery对象。【如该容器为】：<div id="page1"></div>
//            pages: res.total, //通过后台拿到的总页数
//            curr: curr || 1, //当前页
//            jump: function(obj, first){ //触发分页后的回调
//                if(!first){ //点击跳页触发函数自身，并传递当前页：obj.curr
//                    demo(obj.curr);
//                }
//            }
//        });
//    });
//};
////运行
//demo(1, "中国科学院");

////////////////////////
//定义全局变量    ///////
                //////
///////////////////////
var card_data_org ;
var card_data_person;
var related_data_org = new Array();
var related_data_person = new Array();
//var words = 1 ;

 //var words = [
 //             {text: "图谱", weight: 0.1, link: 'http://github.com/mistic100/jQCloud'},
 //             {text: "同谱图", weight: 0.2, link: 'http://www.strangeplanet.fr'},
 //             {text: "特征值", weight: 0.3, link: 'http://piwigo.org'},
 //             {text: "弯曲疲劳应力", weight: 0.4, link: 'http://piwigo.org'},
 //             {text: "laplacian谱", weight: 0.5, link: 'http://github.com/mistic100/jQCloud'},
 //             {text: "健康教育", weight: 0.6, link: 'http://www.strangeplanet.fr'},
 //             {text: "土地利用变化", weight: 0.1, link: 'http://piwigo.org'},
 //             {text: "陈兰杰", weight: 0.3, link: 'http://piwigo.org'},
 //             {text: "姜春林", weight: 0.1, link: 'http://github.com/mistic100/jQCloud'},
 //             {text: "汤建民", weight: 0.2, link: 'http://www.strangeplanet.fr'},
 //             {text: "许振亮", weight: 0.3, link: 'http://piwigo.org'},
 //             {text: "陈悦", weight: 0.3, link: 'http://piwigo.org'},
 //           ];

/////////////////////知识图谱 and 卡片
function statics_data(data){//统计数组中相同的数据并记录
    var arr = new Array();
    for(i=0; i<data.length; i++){
        if(data[i].text){//数组存在
            //var n = i + 1;
            var num = 0; //初始个数
            for(n=0; n<data.length; n++){
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

function generate_word(arr){//生成标签云的word变量
    var data_array = new Array();
    var n = 0;
    for(var i in arr){
        data_array[n] = new Array();
        data_array[n]['text'] = i.split("|")[1];
        data_array[n]['weight'] = arr[i].split("**")[0] / 10;
        data_array[n]['link'] = arr[i].split("**")[1];
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
function deal_data(curr, source){
    str = "";
    var max_related_num = 10; //获取N篇论文的相关机构和任务;
    var n = 0;
    var m = 0;
    for(l=0; l<max_related_num; l++){//动态初始化二位数组
        related_data_org[l] = new Array();
        related_data_person[l] = new Array();
    }
    for(i=0;i<source.length;i++){
        //标题 name
        str += '<div class="sr-content"><h3 class="sr-title"><a href="'+ source[i]._source.dataSource +'"  class="sr-title-a" target="_blank" alt="'+ source[i]._source.name +'">'+ judge_highlight('name', source[i]) +'</a></h3>';
        //作者+来源+年份
        str += '<div class="sr-info"><span>'+ split_name(judge_highlight('author', source[i])) +'</span> &nbsp;-&nbsp; <span><a href="" target="_blank"  title="'+ source[i]._source.journal +'">《'+ judge_highlight('journal', source[i]) +'》</a></span> &nbsp;-&nbsp; <span class="sr-time" >'+ judge_highlight('yearNumber', source[i]) +'</span> &nbsp; </div>'
        //摘要
        str += '<div class="sr-abstract">'+ judge_highlight('abstract', source[i]) +'</div>'
        //全部来源
        str += '<div class="sc_allversion"><span class="sr-gray">全部来源：</span>'
        str += '<span class="v_item_span"><a class="v_source" title="" target="_blank" href="'+ source[i]._source.dataSource +'" >'+ source[i]._source._source.tag +'</a></span>'

        str += '</div>'

        str += '</div>';

        //console.log(card_data);
        //console.log(curr);
        //console.log(source[i]._source.sourceOrganization);
        //console.log(source[i]._source.author);
        if(curr == 1 && i < max_related_num){ //拿前max_related_num数据集

            if(source[i]._source.sourceOrganization){
                related_data_org[m]['text'] = source[i]._source.sourceOrganization[0];
                related_data_org[m]['weight'] = 1;
                related_data_org[m]['link'] = '#';
                //console.log(related_data_org[m]);
                m = m + 1;
            }
            if(source[i]._source.author){
                related_data_person[n]['text'] = source[i]._source.author[0] ;//split_name(source[i]._source.author);
                related_data_person[n]['weight'] = 1;
                related_data_person[n]['link'] = '#';
                //console.log(related_data_person[n][0]);
                n = n + 1;
            }
        }

    }
    console.log(statics_data(related_data_org));
    document.getElementById('card-title-content').innerHTML = card_org_statistics(statics_data(related_data_org)).split("|")[1]; //获取相关卡片
    var words_arry = generate_word(statics_data(related_data_person)).concat(generate_word(statics_data(related_data_org)));
    jq_word(words_arry); //标签云;
}

//Pers/1000900418|凌荣辉   -> 凌荣辉
function split_name(data){
    var string_data = "";
    if(data){
        if(typeof(data)  == "string"){
            return data.split('|');
        }else if(typeof(data)  == "object") {
            for(n=0; n<data.length; n++){
                string_data += data[n].split("|")[1];
                string_data += "&nbsp;&nbsp;"
            }
            return string_data;
        }else{
            return typeof(data[0]);
        }
    }else{
        return "无";
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
            else
                return source_i._source.abstract;
            break;

        case "yearNumber":
            if(source_i._source.yearNumber)
                return source_i._source.yearNumber;
            else
                return "无";
            break;

        case "journal":
            if(source_i._source.journal)
                return source_i._source.journal;
            else
                return "无";
            break;

    }
}

/////////////////////////////
//处理论文分类
function deal_paper_class(obj, data){
    var input = document.getElementById('paper-type');
    var tab = document.getElementsByClassName("tab");
    for(i=0;i<tab.length;i++){
        tab[i].className = "tab";
    }
    obj.className = "selected tab";
    input.value = data;
}
function deal_paper_class_only_paper(obj, paper){
    var input1 = document.getElementById('paper-type');
    var tab = document.getElementsByClassName("tab");
    for(i=0;i<tab.length;i++){
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
////////////////////////////////////
//标签云
function jq_word(words){
    //console.log(words);
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
