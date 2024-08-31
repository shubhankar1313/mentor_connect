// app_login.js

document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.getElementById('login-form');

    loginForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent the default form submission

        const role = document.getElementById('login-role').value;
        const identifier = document.getElementById('login-identifier').value;
        const password = document.getElementById('login-password').value;

        // Basic validation checks
        if (!role) {
            alert('Please select your role (mentee or mentor).');
            return;
        }

        if (!identifier) {
            alert('Please enter your email address or phone number.');
            return;
        }

        if (!password) {
            alert('Please enter your password.');
            return;
        }

        // If all fields are filled, you can proceed with the login logic
        // For example, send the data to a server or check it against a stored value
        console.log('Logging in as:', role);
        console.log('Identifier:', identifier);
        console.log('Password:', password);

        // Redirect or perform further actions upon successful login
        // window.location.href = "dashboard.html"; // Example redirection after login
    });
});