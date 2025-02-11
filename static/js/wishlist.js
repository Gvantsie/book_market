document.addEventListener("DOMContentLoaded", function () {
    const wishlistButtons = document.querySelectorAll(".wishlist-btn");

    wishlistButtons.forEach(button => {
        button.addEventListener("click", function (event) {
            event.preventDefault();

            const bookId = this.getAttribute("data-book-id");
            if (!bookId) {
                console.error("Book ID not found on button element.");
                return;
            }

            const icon = this.querySelector("i");

            // Send AJAX request before updating UI
            fetch("/wishlist/toggle/", {
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
                        if (icon.classList.contains("bi-heart")) {
                            icon.classList.remove("bi-heart");
                            icon.classList.add("bi-heart-fill");
                            button.classList.add("wishlist-btn-active");
                        } else {
                            icon.classList.remove("bi-heart-fill");
                            icon.classList.add("bi-heart");
                            button.classList.remove("wishlist-btn-active");
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
// // Function to update the wishlist modal
// function updateWishlistModal(updatedBooks) {
//     const modalBody = document.querySelector("#wishlistModal .modal-body");
//     const wishlistList = modalBody.querySelector(".wishlist-list");
//
//     // Clear existing list items
//     wishlistList.innerHTML = "";
//
//     // Add updated books to the modal
//     updatedBooks.forEach(book => {
//         const listItem = document.createElement("li");
//         listItem.classList.add("list-group-item");
//         listItem.textContent = book.title;
//         wishlistList.appendChild(listItem);
//     });
// }