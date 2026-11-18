
const searchInput = document.getElementById("searchInput");
const searchButton = document.getElementById("searchButton");
const productsGrid = document.getElementById("productsGrid");
const productCards = document.querySelectorAll(".product-card");
const categoryLinks = document.querySelectorAll(".category-link");
const emptySearch = document.getElementById("emptySearch");

let selectedCategory = "All";


function filterProducts() {
    const searchValue = searchInput.value.toLowerCase().trim();

    let visibleCount = 0;

    productCards.forEach((card) => {
        const productName = card.dataset.name;
        const productCategory = card.dataset.category;

        const matchesSearch = productName.includes(searchValue);

        const matchesCategory =
            selectedCategory === "All" ||
            productCategory === selectedCategory;

        if (matchesSearch && matchesCategory) {
            card.style.display = "";
            visibleCount++;
        } else {
            card.style.display = "none";
        }
    });

    emptySearch.hidden = visibleCount !== 0;
    productsGrid.style.display = visibleCount === 0 ? "none" : "grid";
}


searchInput.addEventListener("input", filterProducts);

searchButton.addEventListener("click", filterProducts);


categoryLinks.forEach((link) => {
    link.addEventListener("click", (event) => {
        event.preventDefault();

        categoryLinks.forEach((item) => {
            item.classList.remove("active");
        });

        link.classList.add("active");

        selectedCategory = link.dataset.category;

        filterProducts();
    });
});


const checkoutButton = document.getElementById("checkoutButton");

if (checkoutButton) {
    checkoutButton.addEventListener("click", () => {
        alert("Checkout functionality will be added soon!");
    });
}
    