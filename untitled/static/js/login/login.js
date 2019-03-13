// JavaScript Document
if('{{msg}}' != '')
	swal('用户名或密码错误','','error');

function student_win(){
	swal({
		title:'请选择',
		type:'success',
		buttons: {
			inquire:{
				text:'查询~',
				value:'inquire',

			},
			report: {
				text: "举报!",
				value: "report",
			},
		},

	})
	.then((value) => {
	  switch (value) {
		case "report":
		  window.open('html/report.html','newwindow','height=500, width=400, top=50,left=400, toolbar=no, menubar=no, scrollbars=no, resizable=no,location=no, status=no');
		  break;
		case "inquire":
		  window.open('html/inquire.html','newwindow','height=500, width=400, top=50,left=400, toolbar=no, menubar=no, scrollbars=no, resizable=no,location=no, status=no');
		  break;
	  }
	});
}