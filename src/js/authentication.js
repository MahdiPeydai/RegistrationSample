document.getElementById('registrationBtn').addEventListener('click', function() {
    document.getElementById('loginForm').classList.add('d-none');
    document.getElementById('registerForm').classList.remove('d-none');
    document.getElementById('loginBtn').parentElement.classList.add('bg-light');
    document.getElementById('registrationBtn').parentElement.classList.remove('bg-light');
    document.getElementById('loginBtn').parentElement.classList.add('shadow');
    document.getElementById('registrationBtn').parentElement.classList.remove('shadow');
});

document.getElementById('loginBtn').addEventListener('click', function() {
    document.getElementById('loginForm').classList.remove('d-none');
    document.getElementById('registerForm').classList.add('d-none');
    document.getElementById('loginBtn').parentElement.classList.remove('bg-light');
    document.getElementById('registrationBtn').parentElement.classList.add('bg-light');
    document.getElementById('loginBtn').parentElement.classList.remove('shadow');
    document.getElementById('registrationBtn').parentElement.classList.add('shadow');
});