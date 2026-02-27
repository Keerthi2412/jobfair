document.addEventListener("DOMContentLoaded", function () {

    console.log("Dashboard JS Loaded");

    const buttons = document.querySelectorAll(".menu-btn");
    const sections = document.querySelectorAll(".section");

    buttons.forEach(function (button) {

        button.addEventListener("click", function (event) {

            event.preventDefault();

            // Remove active class from all buttons
            buttons.forEach(function (btn) {
                btn.classList.remove("active");
            });

            // Add active to clicked button
            this.classList.add("active");

            // Hide all sections
            sections.forEach(function (section) {
                section.classList.remove("active-section");
            });

            // Show selected section
            const targetSection = this.getAttribute("data-section");
            const selectedSection = document.getElementById(targetSection);

            if (selectedSection) {
                selectedSection.classList.add("active-section");
            }

        });

    });

});