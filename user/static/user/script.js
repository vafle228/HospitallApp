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

function next_date(id, csrf_token) {
	date += 1; month = month; year = year; day += 1;
	var next_date = new Date(year, month, date);
	date_build(next_date.getDate(), next_date.getMonth(), next_date.getFullYear(), next_date.getDay());
	getVariants(id, csrf_token)
}

function previous_date(id, csrf_token) {
	if(now.getDate() < date && now.getMonth() <= month && now.getFullYear() <= year){
		date -= 1; month = month; year = year; day -= 1;
		var previous_date = new Date(year, month, date);
		date_build(previous_date.getDate(), previous_date.getMonth(), previous_date.getFullYear(), previous_date.getDay());
		getVariants(id, csrf_token)
	}
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

	$("#doctor")[0].value = '';
	$("#appeal")[0].value = '';
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

// генерация html представление вариантов
function createVariantsTable(variants, csrf_token, id, appeal){
	clearVariants()
	for(let doctor_name in variants){
		let button = document.createElement('button');
		let btn_img = document.createElement('img');
		let table = document.createElement('table');
		
		btn_img.src = arrow;
		btn_img.className = 'left-arrow';

		button.className = 'disactive';
		button.onclick = function() { specialist_table(button) };
		button.innerHTML = doctor_name;

		for(let i in variants[doctor_name]){
			let appointment_date = variants[doctor_name][i]['date'].split('-')

			let tr = document.createElement('tr');
			let specialist_td = document.createElement('td');
			let date_td = document.createElement('td');
			let time_td = document.createElement('td');
			let confirm_td = document.createElement('td');
			let confirm_img = document.createElement('img');


			specialist_td.className = 'variant-specialist-name';
			specialist_td.innerHTML = doctor_name;

			date_td.className = 'variant-date';
			date_td.innerHTML = appointment_date[2] + '.' + appointment_date[1];

			time_td.className = 'variant-time';
			time_td.innerHTML = variants[doctor_name][i]['time'];

			confirm_img.src = confirm;
			confirm_img.height = '90';

			confirm_td.className = 'variant-confirm';
			confirm_td.appendChild(confirm_img);
			confirm_td.onclick = function() { sendVariant(csrf_token, id, variants[doctor_name][i], appeal) };

			tr.appendChild(specialist_td);
			tr.appendChild(date_td);
			tr.appendChild(time_td);
			tr.appendChild(confirm_td);
			table.appendChild(tr);
		}
		button.appendChild(btn_img)
		$("#variants")[0].appendChild(button)
		$("#variants")[0].appendChild(table)
	}
}

// Функция отправки данных на сервер
function sendVariant(csrf_token, id, variant, appeal){
	$.post({
		url: "/main/appointment_create/" + String(id),
		data: {
			specialist: variant['doctor'],
			appeal: appeal,
			date: variant['date'],
			time: variant['time'],
			endTime: variant['endTime'],
			csrfmiddlewaretoken: csrf_token
		},
		success: function(response) { location.href = location.origin + response }
	})
}

function getData(){
	let specialist = $("#doctor")[0].value
	let appeal = $("#appeal")[0].value
	let appointment_date = String(year) + '-' + String(month + 1) + '-' + String(date)

	return [specialist, appeal, appointment_date]
}

// Функция получения вариантов с сервера
function getVariants(id, csrf_token){
	data = getData()
	$.ajax({
		type: "POST",
		url: "/main/appointment_check/" + String(id),
		data: {
			specialist: data[0],
			appeal: data[1],
			date: data[2],
			csrfmiddlewaretoken: csrf_token
		},
		cache: false,
		success: function(response) { 
			createVariantsTable(response, csrf_token, id, data[1]);
		}
	})
}

function clearVariants(){
	let variants = document.getElementById("variants");
	while (variants.firstChild) {
	    variants.removeChild(variants.firstChild);
	}
}