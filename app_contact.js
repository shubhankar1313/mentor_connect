document.addEventListener('DOMContentLoaded', function() {
    console.log("Welcome to MentorConnect!");

    // Contact form submission handling
    const form = document.getElementById('contact-form');
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        // Collect form data
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const message = document.getElementById('message').value;

        // Simple validation
        if (name && email && message) {
            alert(`Thank you, ${name}! Your message has been received.`);
            form.reset(); // Clear the form fields
        } else {
            alert("Please fill in all fields.");
        }
    });
});