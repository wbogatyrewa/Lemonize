menu.onclick = function ShowMenu() {
	var x = document.getElementById('myTopnav');

	if (x.className === "topnav") {
		x.className += " responsive";
	} else {
		x.className = "topnav";
	}
}

function Sum() {
	let table = document.querySelector('#cart');
	
	var sum = 0;
	for (let row of table.rows) {
		if (row.querySelector('#price') != null &&
			row.querySelector('#count') != null) {
		    var price_str = row.querySelector('#price').innerHTML;
			console.log(price_str);
		    var price = parseInt(price_str.split(' ')[0]);
			var count = row.querySelector('#count').value;
			sum += price * count;
		}
	}
	document.getElementById('total_sum').value = sum + ' ₽';
}
window.onload = Sum;
