// Закрыть форму записи
function close_form() {
	var form = document.getElementById('add-session-form');
	form.style.bottom = '-100%';
	form.className = 'disactive';
	var menu = document.getElementById('more-detailed-menu');
	menu.style.bottom = '-100%';
	menu.className = 'disactive';
	document.getElementsByTagName('body')[0].style.backgroundColor = '#fff';
	document.getElementsByTagName('main')[0].style.filter = 'none';
	document.getElementsByTagName('header')[0].style.filter = 'none';
}
// Открыть форму записи
function open_add_form() {
	var form = document.getElementById('add-session-form');
	form.style.bottom = '0';
	form.className = 'active';
	var menu = document.getElementById('more-detailed-menu');
	menu.style.bottom = '-100%';
	document.getElementsByTagName('body')[0].style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
	document.getElementsByTagName('main')[0].style.filter = 'brightness(0.6)';
	document.getElementsByTagName('header')[0].style.filter = 'brightness(0.6)';
}

// Поиск специалиста
function filterFunction() {
	document.getElementById("myDropdown").style.display = 'block';
	var input, filter, ul, li, a, i;
	input = document.getElementById("myInput");
	filter = input.value.toUpperCase();
	div = document.getElementById("myDropdown");
	a = div.getElementsByTagName("a");
	for (i = 0; i < a.length; i++) {
		txtValue = a[i].textContent || a[i].innerText;
		if (txtValue.toUpperCase().indexOf(filter) > -1) {
			a[i].style.display = "";
		} 
		else {
			a[i].style.display = "none";
		}
	}
}

// Выбор специалиста
function search_fill(a) {
	var input = document.getElementById("myInput");
	input.value = a.textContent;
	document.getElementById("myDropdown").style.display = 'none';
}
// Перейти к выбору времени
function form_show() {
	document.getElementById('add-session-form1').style.display = 'none';
	document.getElementById('add-session-btn').style.display = 'none';

	document.getElementById('add-session-form2').style.display = 'block';
	document.getElementById('confirm-session-btn').style.display = 'block';	
}

// Вернуться к началу формы
function form_back() {
	document.getElementById('add-session-form2').style.display = 'none';
	document.getElementById('confirm-session-btn').style.display = 'none';

	document.getElementById('add-session-form1').style.display = 'block';
	document.getElementById('add-session-btn').style.display = 'block';
}


// Меню подробнее
function more_info(referral) {
	var form = document.getElementById('add-session-form');
	var menu = document.getElementById('more-detailed-menu');
	if (menu.className == 'disactive' && form.className == 'disactive') {
		menu.className = 'active';
		menu.style.bottom = '0';
		var specialist = document.getElementById('specialist-name');
		specialist.innerText = referral.childNodes[9].innerHTML;
		var time = document.getElementById('time&date');
		time.innerText = referral.childNodes[3].innerHTML + '    ' + referral.childNodes[5].innerHTML;
		document.getElementsByTagName('body')[0].style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
		document.getElementsByTagName('main')[0].style.filter = 'brightness(0.6)';
		document.getElementsByTagName('header')[0].style.filter = 'brightness(0.6)';
	}
}

function specialist_table(specialist) {
	if (specialist.className == 'disactive') {
		specialist.childNodes[3].style.display = 'block';
		specialist.className = 'active';
		specialist.childNodes[1].childNodes[1].style.transform = 'rotate(180deg)';
	} else {
		specialist.childNodes[3].style.display = 'none';
		specialist.className = 'disactive';
		specialist.childNodes[1].childNodes[1].style.transform = 'rotate(90deg)';
	}
}