

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




  document.addEventListener("DOMContentLoaded", function () {
    const cardSlider = document.querySelector(".card-slider");
    const totalCards = document.querySelectorAll(".card-slider .bg-white").length;

    let currentIndex = 0;

    function randomSlide() {
      const randomDirection = Math.random() > 0.5 ? 1 : -1; // Choisit aléatoirement la direction
      const newIndex = (currentIndex + randomDirection + totalCards) % totalCards;
      cardSlider.style.transform = `translateX(-${newIndex * 100}%)`;
      currentIndex = newIndex;
    }

    // Fonction qui active le défilement seulement en mode mobile/tablette
    function checkScreenSizeAndStartSliding() {
      if (window.innerWidth <= 1024) { // 1024px pour inclure mobile et tablette
        // Lancer le défilement aléatoire
        setInterval(randomSlide, 3000);
      } else {
        // Si l'écran est trop large, on s'assure que l'animation ne s'exécute pas
        clearInterval(randomSlide);
      }
    }

    // Initialisation du contrôle du défilement à la taille de l'écran
    checkScreenSizeAndStartSliding();

    // Vérifier la taille de l'écran à chaque redimensionnement
    window.addEventListener("resize", checkScreenSizeAndStartSliding);
  });


  document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.getElementById('menu-toggle');
    const mobileMenu = document.getElementById('mobile-menu');
    
    menuToggle.addEventListener('click', function() {
        const isExpanded = menuToggle.getAttribute('aria-expanded') === 'true';
        menuToggle.setAttribute('aria-expanded', !isExpanded);
        mobileMenu.classList.toggle('hidden');
        
        if (!mobileMenu.classList.contains('hidden')) {
            gsap.from(mobileMenu, {
                y: -50,
                opacity: 0,
                duration: 0.5,
                ease: "elastic.out(1, 0.75)"
            });
        }
    });

    });