document.getElementById('jobApplicationForm').addEventListener('submit', function(e) {
    // e.preventDefault();
    
    // Clear previous errors
    document.querySelectorAll('.error').forEach(el => el.textContent = '');
    
    // Basic validation
    let isValid = true;
    
    // Validate full name
    const fullName = document.getElementById('full_name');
    if (!fullName.value.trim()) {
        document.getElementById('fullNameError').textContent = 'Full name is required';
        isValid = false;
    }
    
    // Validate email
    const email = document.getElementById('email');
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email.value)) {
        document.getElementById('emailError').textContent = 'Please enter a valid email address';
        isValid = false;
    }
    
    // Validate resume
    const resume = document.getElementById('resume');
    if (!resume.files.length) {
        document.getElementById('resumeError').textContent = 'Resume is required';
        isValid = false;
    } else {
        const file = resume.files[0];
        const allowedTypes = ['application/pdf', 'application/msword', 
                            'application/vnd.openxmlformats-officedocument.wordprocessingml.document'];
        if (!allowedTypes.includes(file.type)) {
            document.getElementById('resumeError').textContent = 'Only PDF or DOCX files are allowed';
            isValid = false;
        }
    }
    
    // Validate cover letter
    const coverLetter = document.getElementById('cover_letter');
    if (!coverLetter.value.trim()) {
        document.getElementById('coverLetterError').textContent = 'Cover letter is required';
        isValid = false;
    }
    
    if (isValid) {
        // Here you would send the form data to Django
        console.log('Form submitted:', {
            fullName: fullName.value,
            email: email.value,
            resume: resume.files[0],
            profilePic: document.getElementById('profile_pic').files[0],
            coverLetter: coverLetter.value
        });
        
        alert({fullName: fullName.value,
            email: email.value,
            resume: resume.files[0],
            profilePic: document.getElementById('profile_pic').files[0],
            coverLetter: coverLetter.value});
    }
});