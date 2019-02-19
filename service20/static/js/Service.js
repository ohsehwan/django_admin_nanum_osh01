
var figmaPx = 1920;
var windowWidth= window.innerWidth;
var px1= window.innerWidth / figmaPx; // Figma 1 px
const baseURL = "http://localhost:8000";
const todoBaseApi = "/";
$(document).ready(function() {	
	let root = document.documentElement;
	root.style.setProperty('--px1', px1);
	root.style.setProperty('--windowWidth', windowWidth);
});




//todoBaseApi -> /
/********************
* find 함수
*	id   => 주소 		ex) 'article' => 최종결정 url : http://114.202.247.167:8000/article
*	v1   => 데이터
*	type => 메소드(기본은 get)
********************/
function find(id,v1,type){	


	if(type==null) type = 'get';
	var v_data = "";

	
	$.ajax({
	    url:baseURL+todoBaseApi+id, //request 보낼 서버의 경로
	    type:type, // 메소드(get, post, put 등)
	    contentType: 'application/x-www-form-urlencoded; charset=UTF-8', 
	    sendDataType : 'json',
	    async:false,	// ture: 비동기, false: 동기
	    data:v1, //보낼 데이터
	    success: function(data) {
	    	if(data != null){
		        //서버로부터 정상적으로 응답이 왔을 때 실행
		        // console.log(data);
		        v_data = data;
	    	}
	    },
	    error: function(err) {
	        //서버로부터 응답이 정상적으로 처리되지 못햇을 때 실행
	        // v_data = err;
	    }
	});
	return v_data;
}



/*********************
* Null 체크
*********************/
function isNull(v_id){
	var v_return = false;
	if(v_id == null || v_id == "NULL"){
		v_return = true;
	}
	if(v_id.length < 1){
		v_return = true;	
	}
	return v_return;
}

