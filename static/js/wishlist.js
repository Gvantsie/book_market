document.addEventListener("DOMContentLoaded", function () {
    console.log("Cart JS loaded!"); // Debugging

    const cartButtons = document.querySelectorAll(".cart-btn");
    console.log("Found cart buttons:", cartButtons.length); // Debugging

    cartButtons.forEach(button => {
        button.addEventListener("click", function (event) {
            event.preventDefault();
            console.log("Cart button clicked"); // Debugging

            const bookId = this.getAttribute("data-book-id");
            if (!bookId) {
                console.error("Book ID not found on button element.");
                return;
            }

            const icon = this.querySelector("i");

            // Send AJAX request before updating UI
            fetch("/cart/toggle/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie("csrftoken"),
                },
                body: JSON.stringify({ book_id: bookId }),
            })
            .then(response => response.json())
            .then(data => {
                console.log("Response from server:", data);

                // Only toggle the icon if the server request was successful
                if (data.message) {
                    if (icon) {
                        if (icon.classList.contains("bi-cart")) {
                            icon.classList.remove("bi-cart");
                            icon.classList.add("bi-cart-fill");
                            button.classList.add("cart-btn-active");
                        } else {
                            icon.classList.remove("bi-cart-fill");
                            icon.classList.add("bi-cart");
                            button.classList.remove("cart-btn-active");
                        }
                    }
                }
            })
            .catch(error => {
                console.error("Error:", error);
            });
        });
    });
});

// Function to get the value of a cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
