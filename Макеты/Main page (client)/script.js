// Закрыть форму записи
function close_add_form() {
	var form = document.getElementById('add-session-form');
	form.style.display = 'none';
	var menu = document.getElementById('more-detailed-menu');
	menu.style.display = 'none';
}
// Открыть форму записи
function open_add_form() {
	var form = document.getElementById('add-session-form');
	form.style.display = 'block';
	var menu = document.getElementById('more-detailed-menu');
	menu.style.display = 'none';
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
<<<<<<< Updated upstream
	if (txtValue.toUpperCase().indexOf(filter) > -1) {
		a[i].style.display = "";
	} else {
		a[i].style.display = "none";
    }
  }
=======
		if (txtValue.toUpperCase().indexOf(filter) > -1) {
			a[i].style.display = "";
		} 
		else {
			a[i].style.display = "none";
		}
	}
>>>>>>> Stashed changes
}

// Выбор специалиста
function search_fill(a) {
	var input = document.getElementById("myInput");
	input.value = a.textContent;
	document.getElementById("myDropdown").style.display = 'none';
}
// Записаться
function form_show() {
<<<<<<< Updated upstream
	document.getElementById('add-session-form1').style.display = 'none';
	document.getElementById('add-session-btn').style.display = 'none';

	document.getElementById('confirm-session-btn').style.display = 'block';
	document.getElementById('time-variants-form').style.display = 'block';

=======
	document.getElementById('add-session-form').style.display = 'none';
	document.getElementById('time-container').style.display = 'block';
>>>>>>> Stashed changes
}

// Меню подробнее
function more_info(referral) {
	var menu = document.getElementById('more-detailed-menu');
	menu.style.display = 'block';
	var specialist = document.getElementById('specialist-name');
	specialist.innerText = referral.childNodes[9].innerHTML;
	var time = document.getElementById('time&date');
	time.innerText = referral.childNodes[3].innerHTML + '    ' + referral.childNodes[5].innerHTML;
}

// Выбор времени приема
function selection_time(button) {
	if (button.className == 'time-variant selected') {
		button.className = 'time-variant';
	} else {
		let buttons = document.getElementsByClassName('selected');
		for (let i = 0; buttons.length; i++) {
			buttons[i].className = 'time-variant';
		}
		button.className += ' selected';
	}
}