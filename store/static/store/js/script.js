

const menuToggle = document.getElementById('menu-toggle');
const mobileMenu = document.getElementById('mobile-menu');
menuToggle.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden');
});



function initMap() {
    const location = { lat: 0.4162, lng: 9.4673 }; // Libreville, Gabon coordinates
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 15,
        center: location,
    });
    const marker = new google.maps.Marker({
        position: location,
        map: map,
    });
}


function increaseQuantity() {
    let quantity = document.getElementById("quantity");
    quantity.value = parseInt(quantity.value) + 1;
}

function decreaseQuantity() {
    let quantity = document.getElementById("quantity");
    if (parseInt(quantity.value) > 1) {
        quantity.value = parseInt(quantity.value) - 1;
    }
}

  // Cœur : Changement de couleur au clic
  const heartIcon = document.getElementById("heart-icon");
  heartIcon.addEventListener("click", () => {
    heartIcon.classList.toggle("liked"); // Ajoute/enlève la classe "liked"
  });

  // Panier : Mise à jour du badge
  const cartIcon = document.getElementById("cart-icon");
  const cartCount = document.getElementById("cart-count");
  let itemCount = 0;

  cartIcon.addEventListener("click", () => {
    itemCount++;
    cartCount.textContent = itemCount;
    cartCount.classList.remove("hidden"); // Affiche le badge
  });
