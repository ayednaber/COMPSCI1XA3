$(document).ready(function () {
	$("#themebtn2").on("click", function() {
		$("#volunteer").toggle();
		if ($("#themebtn2").html() == "Show Image") {
			$("#themebtn2").html("Hide Image");
		} else {
			$("#themebtn2").html("Show Image");
		}
	});
});

// Code for Popping Up the Personal Photo and Closing it
var modal = document.getElementById("myModal");

var img = document.getElementById("personalImg");
var modalImg = document.getElementById("newImg");
var caption = document.getElementById("caption");
img.onclick = function() {
	modal.style.display = "block";
	modalImg.src = this.src;
	caption.innerHTML = this.alt;
}

var span = document.getElementsByClassName("close")[0];

span.onclick = function() {
	modal.style.display = "none";
}

function openContent(evt, cityName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("verticalTab");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}

document.getElementById("defaultOpen").click();


function lightFunction() {
	var element = document.body;
	element.classList.toggle("light-mode");
	var btn = document.getElementById("themebtn");
	var volunteerbtn = document.getElementById("themebtn2");
	var tech1 = document.getElementById("tech1");
	var tech2 = document.getElementById("tech2");
	var tech3 = document.getElementById("tech3");
	var tech4 = document.getElementById("tech4");
	var facebookicon = document.getElementById("facebookicon");
	var instagramicon = document.getElementById("instagramicon");
	var linkedinicon = document.getElementById("linkedinicon");
	var githubicon = document.getElementById("githubicon");
	var downloadicon = document.getElementById("downloadicon");
	var myname_header = document.getElementById("myname_header");
	var myname_desc = document.getElementById("myname_desc");
	if (btn.innerHTML == "Dark Mode") {
    btn.innerHTML = "Light Mode";
    btn.style.backgroundColor = "white";
    btn.style.color = "#251A18";
    volunteerbtn.style.backgroundColor = "white";
    volunteerbtn.style.color = "#251A18";

	} else {
    btn.innerHTML = "Dark Mode";
    btn.style.backgroundColor = "#251A18";
    btn.style.color = "white";
    volunteerbtn.style.backgroundColor = "#251A18";
    volunteerbtn.style.color = "white";
	}

	if (facebookicon.style.color == "black") {
		facebookicon.style.color = "white";
		instagramicon.style.color = "white";
		linkedinicon.style.color = "white";
		githubicon.style.color = "white";
		downloadicon.style.color = "white";
	} else {
		facebookicon.style.color = "black";
		instagramicon.style.color = "black";
		linkedinicon.style.color = "black";
		githubicon.style.color = "black";
		downloadicon.style.color = "black";
	}

	if (myname_header.style.color == "#251a18") {
		myname_header.style.color = "white";
	} else {
		myname_header.style.color == "#251a18";
	}

	

	tech1.style.color = "white";
	tech2.style.color = "white";
	tech3.style.color = "white";
	tech4.style.color = "white";

	


	/*btn.innerHTML = "Dark Mode";
	btn.style.backgroundColor = "black" ;
	btn.style.color = "white"; */
}
