// app_signup.js

document.addEventListener('DOMContentLoaded', function() {
    // Form handling for the signup page
    const signupForm = document.getElementById('signup-form');
    const roleSelect = document.getElementById('role');
    const menteeFields = document.getElementById('mentee-fields');
    const mentorFields = document.getElementById('mentor-fields');

    roleSelect.addEventListener('change', function() {
        if (roleSelect.value === 'mentee') {
            menteeFields.style.display = 'block';
            mentorFields.style.display = 'none';
        } else if (roleSelect.value === 'mentor') {
            mentorFields.style.display = 'block';
            menteeFields.style.display = 'none';
        } else {
            menteeFields.style.display = 'none';
            mentorFields.style.display = 'none';
        }
    });

    signupForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        const role = roleSelect.value;
        if (role === 'mentee') {
            // Generate mentee ID and show confirmation
            const menteeId = 'MNT-' + Math.floor(Math.random() * 10000);
            alert(`Mentee registered successfully! Your ID is ${menteeId}`);
            signupForm.reset();
        } else if (role === 'mentor') {
            // Prepare mentor data for manual verification
            alert('Thank you for signing up as a mentor! We will review your details and get back to you soon.');
            signupForm.reset();
        }
    });
});