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





