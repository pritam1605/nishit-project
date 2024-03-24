document.addEventListener('DOMContentLoaded', function() {
    var scrollLinks = document.querySelectorAll('a[href^="#"]'); // Get all links with href starting with #
    
    scrollLinks.forEach(function(link) {
        link.addEventListener('click', function(event) {
            event.preventDefault(); // Prevent default link behavior
            var targetId = this.getAttribute('href'); // Get the href attribute value
            scrollToSection(targetId); // Call the scrollToSection function
        });
    });
});

function scrollToSection(targetId) {
    var targetSection = document.querySelector(targetId); // Get the target section using the targetId
    if (targetSection) {
        var startY = window.pageYOffset; // Start position
        var stopY = targetSection.getBoundingClientRect().top + window.pageYOffset; // End position
        var distance = stopY - startY;
        var duration = 500; // Duration of the scroll animation in milliseconds

        var start;

        window.requestAnimationFrame(function step(timestamp) {
            if (!start) start = timestamp;
            var time = timestamp - start;
            var percent = Math.min(time / duration, 1); // Percent of duration elapsed

            // Apply easing function (linear interpolation)
            window.scrollTo(0, startY + distance * percent);

            if (time < duration) {
                window.requestAnimationFrame(step);
            }
        });
    }
}

document.getElementById("form-ai").addEventListener("click", function() {
    // Redirect to the form page
    window.location.href = "aiform.html";
});

document.getElementById("quizForm").addEventListener("submit", function(event) {
    event.preventDefault();
    
    var answers = {
        q1: document.querySelector('input[name="q1"]:checked').value,
    };
    console.log(answers);
    // window.location.href = "index.html";
});











