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

 var words = [
              {text: "图谱", weight: 0.1, link: 'http://github.com/mistic100/jQCloud'},
              {text: "同谱图", weight: 0.2, link: 'http://www.strangeplanet.fr'},
              {text: "特征值", weight: 0.3, link: 'http://piwigo.org'},
              {text: "弯曲疲劳应力", weight: 0.4, link: 'http://piwigo.org'},
              {text: "laplacian谱", weight: 0.5, link: 'http://github.com/mistic100/jQCloud'},
              {text: "健康教育", weight: 0.6, link: 'http://www.strangeplanet.fr'},
              {text: "土地利用变化", weight: 0.1, link: 'http://piwigo.org'},
              {text: "陈兰杰", weight: 0.3, link: 'http://piwigo.org'},
              {text: "姜春林", weight: 0.1, link: 'http://github.com/mistic100/jQCloud'},
              {text: "汤建民", weight: 0.2, link: 'http://www.strangeplanet.fr'},
              {text: "许振亮", weight: 0.3, link: 'http://piwigo.org'},
              {text: "陈悦", weight: 0.3, link: 'http://piwigo.org'}
            ];
$(function() {
        $('#rel-content').jQCloud(words,{
             autoResize: true,
            fontSize: {
                from: 0.15,
                to: 0.05
            }
        });

});

////////////////////////
// 处理返回结果数据
function deal_data(source){
    str = "";
    for(i=0;i<source.length;i++){
        //标题 name
        str += '<div class="sr-content"><h3 class="sr-title"><a href="" class="sr-title-a" target="_blank" alt="'+ source[i]._source.name +'">'+ judge_highlight('name', source[i]) +'</a></h3>';
        //作者+来源+年份
        str += '<div class="sr-info"><span><a href="" target="_blank" >'+ split_name(judge_highlight('author', source[i])) +'</a></span> &nbsp;-&nbsp; <span><a href="" target="_blank"  title="'+ source[i]._source.journal +'">《'+ source[i]._source.journal +'》</a></span> &nbsp;-&nbsp; <span class="sr-time" >'+ source[i]._source.yearNumber +'</span> &nbsp; </div>'
        //摘要
        str += '<div class="sr-abstract">'+ source[i].highlight.abstract +' </div>'
        //全部来源
        str += '<div class="sc_allversion"><span class="sr-gray">全部来源：</span>'
        str += '<span class="v_item_span"><a class="v_source" title="" target="_blank" href="'+ source[i]._source.dataSource +'" >'+ source[i]._source.tag +'</a></span>'

        str += '</div>'

        str += '</div>';
    }
}

//Pers/1000900418|凌荣辉   -> 凌荣辉
function split_name(data){
    if(data){
        if(typeof(data)  == "string"){
            return data.split('|')[1];
        }else if(typeof(data)  == "object") {
            return data[0].split('|')[1];
            //return data[0];
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
            if(source_i.highlight.author)
                return source_i.highlight.author;
            else
                return source_i._source.author;
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
function deal_paper_class_only_paper(obj){
    var input = document.getElementById('paper-type');
    var tab = document.getElementsByClassName("tab");
    for(i=0;i<tab.length;i++){
        tab[i].className = "tab";
    }
    obj.className = "selected tab";
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
        deal_paper_class_only_paper(paper_obj);
    }else if(paper == "ConferencePaper"){
        var paper_obj = document.getElementById("form-span-2");
        deal_paper_class_only_paper(paper_obj);
    }else if(paper == "JournalPaper"){
        var paper_obj = document.getElementById("form-span-3");
        deal_paper_class_only_paper(paper_obj);
    }else if(paper == "Thesis"){
        var paper_obj = document.getElementById("form-span-4");
        deal_paper_class_only_paper(paper_obj);
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
    console.log(body_obj.childNodes.length);
    console.log(body_obj.childNodes);
}