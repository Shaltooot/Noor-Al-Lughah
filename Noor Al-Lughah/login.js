const togglePassword = document.getElementById('togglePassword');
const passwordField = document.getElementById('password');

togglePassword.addEventListener('click', function() {
  const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
  passwordField.setAttribute('type', type);
  // Change icon based on the password field type
  if (type === 'password') {
    togglePassword.classList.remove('bxs-hide');
    togglePassword.classList.add('bxs-show');
  } else {
    togglePassword.classList.remove('bxs-show');
    togglePassword.classList.add('bxs-hide');
  }
});


    // Function to simulate login
    function login() {
        // Perform login validation here
        // For simplicity, let's assume the login is successful
        // You'll need to replace this with actual authentication logic
        showCourses();
    }

    // Function to simulate signup
    function signup() {
        // Perform signup validation here
        // For simplicity, let's assume the signup is successful
        // You'll need to replace this with actual signup logic
        showCourses();
    }

    // Function to show signup form
    function showSignupForm() {
        document.getElementById("loginForm").style.display = "none";
        document.getElementById("signupForm").style.display = "block";
    }

    // Function to show courses after login/signup
    function showCourses() {
        document.getElementById("loginForm").style.display = "none";
        document.getElementById("courses").style.display = "block";
    }

    // Function to mark a course as completed
    function completeCourse(courseId) {
        // Send a request to the backend to mark the course as completed
        // Upon successful completion, move the course to the "Completed Courses" section
        const course = document.querySelector(`#courses .course:nth-child(${courseId})`);
        course.style.display = "none"; // Hide the course from available courses

        const completedCourses = document.getElementById("completedCourses");
        completedCourses.style.display = "block";

        completedCourses.innerHTML += `<div class="course">
            <h3>Completed Course ${courseId}</h3>
        </div>`;
    }

w
        // Function to handle login form submission
        document.getElementById("loginForm").addEventListener("submit", function(event) {
            event.preventDefault(); // Prevent the form from submitting normally

            // Get the values from the login form
            const email = document.getElementById("loginEmail").value;
            const password = document.getElementById("loginPassword").value;

            // Here, you would typically send a request to the backend to verify the credentials
            // For demonstration purposes, we'll just log the values to the console
            console.log("Login submitted with email:", email, "and password:", password);
        });

        // Function to handle signup form submission
        document.getElementById("signupForm").addEventListener("submit", function(event) {
            event.preventDefault(); // Prevent the form from submitting normally

            // Get the values from the signup form
            const username = document.getElementById("signupUsername").value;
            const email = document.getElementById("signupEmail").value;
            const password = document.getElementById("signupPassword").value;

            // Here, you would typically send a request to the backend to create a new user account
            // For demonstration purposes, we'll just log the values to the console
            console.log("Signup submitted with username:", username, "email:", email, "and password:", password);
        });