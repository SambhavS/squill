// Setup
var url_string = window.location.href;
var idNum = parseInt(url_string.split('/').slice(-1)[0]);
var myname = prompt("Name? ");
var color_dict = {"white":"#FFFFFF", "blue":"#0000FF", "red":"#FF0000"}
col_info = {"red": null, "blue": null}
gboards = null;
$("#submission").hide();
$("#results").hide();

// Functions 
function draw_boards(){
	if(gboards!= null){
		console.log(gboards);
		var canvas = document.getElementById("myCanvas");
		var ctx = canvas.getContext("2d");
		ctx.clearRect(0, 0, canvas.width, canvas.height);
		var frameNum = document.getElementById("frameNum").value;
		ctx.font = "12px Arial";
		var y_offset = 0;
		board = gboards[frameNum];
		for(var i = 0; i < board.length; i+=1){
			var x_offset = 0;
			for(var j=0; j<board[0].length; j+=1){
				var color = board[i][j][0];
				ctx.fillStyle = color_dict[color];
				ctx.fillRect(y_offset, x_offset, 50, 50);
				ctx.fillStyle = "white";
				ctx.fillText(board[i][j][1].toString(), y_offset + 15, x_offset + 15);
				x_offset += 50;	
			}
			y_offset += 50;
		}
	}
}

function update_info(){
	$.get("/info/"+idNum.toString(), data => {
		col_info["red"] = null;
		col_info["blue"] = null;
 		JSON.parse(data).forEach(tup => {
 			col_info[tup[0]] = tup[1];
 		});
	});
	if(col_info["red"] != null){
	 	document.getElementById("red_info").innerHTML = '<b style="color:red;">Red</b> Player: '+col_info["red"];		
	}
	else{
	 	document.getElementById("red_info").innerHTML = '-';
	}
	if(col_info["blue"] != null){
	 	document.getElementById("blue_info").innerHTML = '<b style="color:blue;">Blue</b> Player: '+col_info["blue"];	
	}
	else{
	 	document.getElementById("blue_info").innerHTML = '-';
	}
	if(col_info["red"] != null && col_info["blue"] != null){
	 	$("#submission").show();
	}else{
		$("#submission").hide();	
	}
}
	
// Interval methods
setInterval(draw_boards, 500)
setInterval(update_info, 5000)
//** Onclick methods **

//Upload
$('#upload').click(() => {
  let fileReader = new FileReader();
  fileReader.onload = fileLoadedEvent => {
      let codeText = fileLoadedEvent.target.result;
      $.post("/upload/"+idNum.toString(), {username: myname, code_text: codeText}, data => {
	 		console.log("upload");
		});
  };
  fileReader.readAsText(document.getElementById("fileToLoad").files[0], "UTF-8");
});

// Run game
$("#run_code").click(() => {
	$.get("/init/"+idNum.toString(), boards => {
		gboards = JSON.parse(boards);
	});
	$("#prerun").hide();
	$("#results").show();
});

// Reset
$("#resetButton").click(() =>{
	$.get("/reset/"+idNum.toString(), msg => {
	console.log(msg);
	});
	location.reload();
})
