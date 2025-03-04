document.getElementById('contactForm').addEventListener('submit', function(e) {
    // e.preventDefault();
    
    // Reset error messages
    const errors = document.querySelectorAll('.error-message');
    errors.forEach(error => error.style.display = 'none');

    // Validate email
    const email = document.getElementById('email').value;
    if (!email.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)) {
        showError('email', 'Please enter a valid email address');
        return false;
    }

    // Submit form
    console.log('Form submitted:', {
        name: document.getElementById('name').value,
        email: email,
        message: document.getElementById('message').value
    });
});

function showError(fieldId, message) {
    const errorSpan = document.querySelector(`#${fieldId} ~ .error-message`);
    errorSpan.textContent = message;
    errorSpan.style.display = 'block';
}