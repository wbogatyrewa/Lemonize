menu.onclick = function ShowMenu() {
	var x = document.getElementById('myTopnav');

	if (x.className === "topnav") {
		x.className += " responsive";
	} else {
		x.className = "topnav";
	}
}

function mult() {
	var price_str = document.getElementById('price').innerHTML;
	var price = price_str.split(' ')[0];
	var count = document.getElementById('count').value;

	var mult = parseInt(price) * count;
	document.getElementById('total').innerHTML = mult + ' ₽';
}