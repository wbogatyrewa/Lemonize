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
			
		    var price = parseInt(price_str.split(' ')[0]);
			var count = parseInt(row.querySelector('#count').innerHTML);
			sum += price * count;
		}
	}
	document.getElementById('total_sum').value = sum + ' ₽';
}
window.onload = Sum;
