/**
 * Created by changzhao619 on 5/19/16.
 */


function close_ele(id){
    var obj = document.getElementById(id);
    obj.style.display = "none";
}

function show_ele(id){
    var obj = document.getElementById(id);
    obj.style.display = "block";
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

        txt = xmlhttp.responseText;	//获取ajax请求的数据；
        JSONObject = eval ("(" + txt + ")"); //将json数据转换为js对象；



    }
  }
xmlhttp.open("GET",url+"rand="+Math.random(),false);
xmlhttp.send();

}

