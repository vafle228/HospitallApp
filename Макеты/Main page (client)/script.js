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
function filterFunction(input) {
	input.nextElementSibling.style.display = 'block';
	var filter = input.value.toUpperCase();
	var drops = input.nextElementSibling;
	var a = drops.getElementsByTagName("a");
	for (var i = 0; i < a.length; i++) {
		txtValue = a[i].textContent || a[i].innerText;
		if (txtValue.toUpperCase().indexOf(filter) > -1) {
			a[i].style.display = "block";
		} else {
			a[i].style.display = "none";
		}
	}
}

// Выбор специалиста
function search_fill(a) {
	var input = a.parentElement.previousElementSibling;
	input.value = a.textContent;
	a.parentElement.style.display = 'none';
}


var now = new Date();
var date = now.getDate();
var month = now.getMonth();
var year = now.getFullYear();
var day = now.getDay()

// Построение и установка на слайдер даты
function date_build(date, month, year, day) {
	var days = ['ВС', 'ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ'];
	document.getElementById('date-slider').innerHTML = 
	String(date) + '.' + String(month + 1) + '.' + 
	String(year) + ' ' + days[day];
}

function next_date() {
	date += 1; month = month; year = year; day += 1;
	var next_date = new Date(year, month, date);
	date_build(next_date.getDate(), next_date.getMonth(), next_date.getFullYear(), next_date.getDay());
}
function previous_date() {
	date -= 1; month = month; year = year; day -= 1;
	var previous_date = new Date(year, month, date);
	date_build(previous_date.getDate(), previous_date.getMonth(), previous_date.getFullYear(), previous_date.getDay());
}

// Перейти к выбору времени
function form_show() {

	date_build(date, month, year, day);

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
		specialist.nextElementSibling.style.display = 'block';
		specialist.className = 'active';
		specialist.childNodes[1].style.transform = 'rotate(180deg)';
	} else {
		specialist.nextElementSibling.style.display = 'none';
		specialist.className = 'disactive';
		specialist.childNodes[1].style.transform = 'rotate(90deg)';
	}
}

function cancel_session(btn1) {
	btn1.style.display = 'none';
	document.getElementById('cancel2').style.display = 'block';
}