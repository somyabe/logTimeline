window.onload = function () {	
    displayData();   
}

function displayData(){
		var timeline_obj = $('#my-data').data();
		var timeline_data = Object.values(timeline_obj['name']);		
		console.log("got data");
        console.log(timeline_data);
		//$('#imageDiv').hide();
		throwTable(timeline_data);
		throwChart(timeline_data);
       
}

function throwTable(timeline_data){
	console.log("inside throw table");
	timeline = timeline_data;
	var tbody = document.getElementById('tbody');
	for (var i = 0; i < timeline.length; i++) {
		if(timeline[i]["markerType"]=="cross"){
			var datepart = timeline[i].x;
			


			var tr = "<tr>";
			tr += "<td>" + moment(datepart).format("YYYY MMM DD HH:mm:ss.SSS") + "</td>" + "<td><a onclick='throwMiniChart("+datepart+");' style='cursor: pointer; color: #0000EE; text-decoration: underline;'>" + timeline[i].z.toString() + "</a></td></tr>";
			tbody.innerHTML += tr;
		}

	}
	console.log(tbody);
	if(tbody.rows.length==0){
		for (var i = 0; i < timeline.length; i++) {
			
			var datepart = timeline[i].x;
			


			var tr = "<tr>";
			tr += "<td>" + moment(datepart).format("YYYY MMM DD HH:mm:ss.SSS") + "</td>" + "<td>" + timeline[i].z.toString() + "</td></tr>";
			tbody.innerHTML += tr;
			
	
		}


	}
	else{
		console.log("noooo")
	}		
}

function throwMiniChart(datepart){
	console.log("inside throwminichart");
	
	console.log(timeline);
	var chartData = timeline;
	var errorTime = datepart;
	var errorTime1=errorTime+600000;
	var dur = 3600000;
	var lower = errorTime - dur;
	console.log(lower);
	var newChartData=[];
	for(var i=0; i<chartData.length; i++){
		 if((chartData[i].x<errorTime1) && (chartData[i].x>lower)){
			 newChartData.push(chartData[i]);



		 }
	 }
	console.log(newChartData);
	
	

	
	
	throwMiniTable(newChartData);
	
	
    var chart = new CanvasJS.Chart("chartContainer", {
	animationEnabled: true,
	backgroundColor: "#eeeded",	
	height: 320,
	zoomEnabled: true,
	title:{
		text: ""
		
	},
	subtitles:[
		{
			text: "1-Video  2-Notifications  3-Settings  4-Keypresses",			
			horizontalAlign: "left",
			fontStyle: "normal",
			//fontColor: "blue",
			fontFamily: "arial",
			padding: 30,
       					
		}
		
	
		],
	axisX: {
		title:"Time",
		labelAngle: -30
	},
	axisY:{
		title: "Timelines",
		interval: 1,
		minimum:0.1,
		maximum: 4.1,
		
	},
	data: [{
		type: "scatter",		
		color: "red",
		toolTipContent: "{z} ",
		name: "      ",		
        showInLegend: true,
        xValueType: "dateTime",
		dataPoints: newChartData,
		
	}
	]
});
chart.render();
	 
    

}
function throwMiniTable(newChartData){
	console.log("inside mini throw table");
	var newdata = newChartData;
	console.log(newdata)
	var tbody = document.getElementById('tbody1');
	tbody.innerHTML="";
	for (var i = 0; i < newdata.length; i++) {
		
			


		var tr = "<tr>";
		tr += "<td>" + moment(newdata[i].x).format("YYYY MMM DD HH:mm:ss.SSS") + "</td>" + "<td>" + newdata[i].z.toString() + "</td></tr>";
		tbody.innerHTML += tr;
		
    }		


}

function throwChart(TimelineData){
	

	console.log("inside throw chart");
    var chartData = TimelineData;
    var chart = new CanvasJS.Chart("chartContainer", {
	animationEnabled: true,
	backgroundColor: "#eeeded",	
	height: 320,
	zoomEnabled: true,
	title:{
		text: ""
		
	},
	subtitles:[
		{
			text: "1-Video  2-Notifications  3-Settings  4-Keypresses",			
			horizontalAlign: "left",
			fontStyle: "normal",
			//fontColor: "blue",
			fontFamily: "arial",
			padding: 30,
       					
		}
		
	
		],
	axisX: {
		title:"Time",
		labelAngle: -30
	},
	axisY:{
		title: "Timelines",
		interval: 1,
		minimum:0.1,
		maximum: 4.1,
		
	},
	data: [{
		type: "scatter",		
		color: "red",
		toolTipContent: "{z} ",
		name: "      ",		
        showInLegend: true,
        xValueType: "dateTime",
		dataPoints: chartData,
		
	}
	]
});
chart.render();
}

function refreshChart(){
	throwChart(timeline);



	
	

}
