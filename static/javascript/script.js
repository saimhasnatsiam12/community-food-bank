
document.addEventListener("DOMContentLoaded", function () {

    // Mobile Sidebar
    const menuToggle = document.getElementById("menuToggle");
    const sidebar = document.getElementById("sidebar");

    if (menuToggle && sidebar) {

        menuToggle.addEventListener("click", function () {
            sidebar.classList.toggle("open");
        });

        document.addEventListener("click", function (event) {

            if (
                window.innerWidth <= 768 &&
                sidebar.classList.contains("open") &&
                !sidebar.contains(event.target) &&
                !menuToggle.contains(event.target)
            ) {
                sidebar.classList.remove("open");
            }

        });
    }

    // Close Notifications
    document.querySelectorAll(".alert-close").forEach(function (button) {

        button.addEventListener("click", function () {
            button.parentElement.remove();
        });

    });

    // Automatically Hide Notifications
    document.querySelectorAll(".alert").forEach(function (alertBox) {

        setTimeout(function () {

            alertBox.style.opacity = "0";
            alertBox.style.transform = "translateY(-10px)";

            setTimeout(function () {
                alertBox.remove();
            }, 300);

        }, 5000);

    });

    // Form Validation
    document.querySelectorAll("form").forEach(function (form) {

        form.addEventListener("submit", function (event) {

            const numberInputs = form.querySelectorAll(
                'input[type="number"]'
            );

            for (const input of numberInputs) {

                if (
                    input.value.trim() === "" ||
                    !Number.isInteger(Number(input.value)) ||
                    Number(input.value) <= 0
                ) {

                    event.preventDefault();

                    input.focus();

                    alert("Please enter a valid positive whole number.");

                    return;
                }

            }

        });

    });

});
