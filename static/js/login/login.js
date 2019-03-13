// JavaScript Document
if('{{msg}}' != '')
	swal('{{msg}}','','error');

function student_win(){
	swal({
		title:'请选择',
		type:'success',
		buttonsStyling:false,
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
		  window.open('./report','newwindow','height=624px, width=568px, top=50,left=400, toolbar=no, menubar=no, scrollbars=no, resizable=no,location=no, status=no');
		  break;
		case "inquire":
		  window.open('./inquire','newwindow','height=624px, width=568px, top=50,left=400, toolbar=no, menubar=no, scrollbars=no, resizable=no,location=no, status=no');
		  break;
	  }
	});
}