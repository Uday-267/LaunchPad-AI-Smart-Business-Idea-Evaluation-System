// ======================================================
// LaunchPad AI
// Frontend Script
// ======================================================

document.addEventListener("DOMContentLoaded", () => {

    // ==========================================
    // Loading Overlay
    // ==========================================

    const form = document.getElementById("startupForm");

    if (form) {

        form.addEventListener("submit", function () {

            const overlay = document.getElementById("loadingOverlay");

            if (overlay) {
                overlay.style.display = "flex";
            }

            const btn = form.querySelector("button[type='submit']");

            if (btn) {
                btn.disabled = true;
                btn.innerHTML = "🤖 Analyzing...";
            }

        });

    }

    // ==========================================
    // Character Counter
    // ==========================================

    const startupIdea = document.querySelector(
        "textarea[name='startup_idea']"
    );

    if (startupIdea) {

        // Create counter
        const counter = document.createElement("small");

        counter.className = "text-muted";

        counter.style.display = "block";

        counter.style.marginTop = "8px";

        startupIdea.parentNode.appendChild(counter);

        function updateCounter() {

            counter.innerHTML =
                startupIdea.value.length +
                " / 2000 characters";

        }

        updateCounter();

        startupIdea.addEventListener(
            "input",
            updateCounter
        );

    }

    // ==========================================
    // Client Validation
    // ==========================================

    if (form) {

        form.addEventListener("submit", function (e) {

            const startupName =
                document.querySelector(
                    "input[name='startup_name']"
                ).value.trim();

            const startupIdea =
                document.querySelector(
                    "textarea[name='startup_idea']"
                ).value.trim();

            if (startupName.length < 3) {

                alert(
                    "Startup name must contain at least 3 characters."
                );

                e.preventDefault();

                hideLoading();

                return;

            }

            if (startupIdea.length < 50) {

                alert(
                    "Startup Idea should contain at least 50 characters."
                );

                e.preventDefault();

                hideLoading();

                return;

            }

        });

    }

    // ==========================================
    // Auto Hide Alerts
    // ==========================================

    const alerts =
        document.querySelectorAll(".alert");

    alerts.forEach(function (alert) {

        setTimeout(function () {

            alert.style.transition = "0.5s";

            alert.style.opacity = "0";

            setTimeout(function () {

                alert.remove();

            }, 500);

        }, 4000);

    });

});


// ==========================================
// Hide Loading Overlay
// ==========================================

function hideLoading() {

    const overlay =
        document.getElementById("loadingOverlay");

    if (overlay) {

        overlay.style.display = "none";

    }

}
