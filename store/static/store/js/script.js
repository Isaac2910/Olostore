

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


  function updateFixedCartButton() {
    const cartTotal = document.querySelector('.cart-total');
    const items = document.querySelectorAll('tbody tr').length;
    cartTotal.textContent = items + ' articles';

    cartTotal.classList.add('animate__animated', 'animate__pulse');
    setTimeout(() => {
        cartTotal.classList.remove('animate__animated', 'animate__pulse');
    }, 1000);
}

updateCartCount(); // Initial update of the cart count
updateFixedCartButton(); // Initial update of the fixed cart button

// incrementation 
// Initialize cart functionality
let cartCount = 0;
const cartCountElement = document.getElementById('cart-count');
const cartButton = document.querySelector('#fixed-cart-button button');

function updateCartCount(count) {
  cartCount = count;
  cartCountElement.textContent = count;
  
  // Show/hide the count badge
  if (count > 0) {
    cartCountElement.classList.remove('hidden');
  } else {
    cartCountElement.classList.add('hidden');
  }
  
  // Add bump animation
  cartCountElement.classList.add('bump');
  setTimeout(() => {
    cartCountElement.classList.remove('bump');
  }, 300);
  
  // Optionally save to localStorage
  localStorage.setItem('cartCount', count);
}

// Load initial cart count from localStorage if exists
const savedCount = localStorage.getItem('cartCount');
if (savedCount) {
  updateCartCount(parseInt(savedCount));
}

// Add click handler to increment cart
cartButton.addEventListener('click', () => {
  updateCartCount(cartCount + 1);
  
  // Add bounce animation to cart icon
  cartButton.querySelector('i').classList.add('animate__animated', 'animate__bounce');
  setTimeout(() => {
    cartButton.querySelector('i').classList.remove('animate__animated', 'animate__bounce');
  }, 1000);
});