menu.onclick = function ShowMenu() {
	var x = document.getElementById('myTopnav');

	if (x.className === "topnav") {
		x.className += " responsive";
	} else {
		x.className = "topnav";
	}
}

var i = 0;
var time = 5000;
var countImages = 7;

function SlideShow() {
	document.slideshow.src = '/static/main/images/main/' + i + '.jpg';
	if (i < countImages - 1) {
		i++;
	} else {
		i = 0;
	}
	setTimeout(SlideShow, time);
}

window.onload = SlideShow;

