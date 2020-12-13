function reg_form() {
	document.getElementById('choice').style.bottom = '-100%';
	document.getElementById('reg-form').style.bottom = '0';
	document.getElementsByTagName('body')[0].style.backgroundColor = 'rgba(0, 0, 0, 0.2)';
	document.getElementById('logo').style.filter = 'brightness(0.5)';
}
function log_form() {
	document.getElementById('choice').style.bottom = '-100%';
	document.getElementById('log-form').style.bottom = '0';
	document.getElementsByTagName('body')[0].style.backgroundColor = 'rgba(0, 0, 0, 0.2)';
	document.getElementById('logo').style.filter = 'brightness(0.5)';
}
function close_form() {
	document.getElementById('log-form').style.bottom = '-100%';
	document.getElementById('reg-form').style.bottom = '-100%';
	document.getElementById('choice').style.bottom = '0';
	document.getElementsByTagName('body')[0].style.backgroundColor = '#fff';
	document.getElementById('logo').style.filter = 'none';
}