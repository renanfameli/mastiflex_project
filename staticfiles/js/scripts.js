// When the DOM is ready
$(document).ready(function() {

  $('.navbar-nav>li>a').on('click', function(){
    $('.navbar-collapse').collapse('hide');
  });

  // Added event listener for search button click
  document.querySelector('.search-btn').addEventListener('click', function () {
    searchProducts();
  });

  // Initialize B2B checkbox toggle
  toggleB2bField();
});

// B2B checkbox toggle function
function toggleB2bField() {
  const isB2bCheckbox = document.getElementById('is_b2b');
  const b2bField = document.querySelector('.b2b-field');

  if (isB2bCheckbox) {
    if (isB2bCheckbox.checked) {
      b2bField.style.display = 'block';
    } else {
      b2bField.style.display = 'none';
    }
  }
}


// Search js
function searchProducts() {
  const input = document.getElementById("searchInput");
  const filter = input.value.toUpperCase();
  const productList = document.getElementById("productList");
  const products = productList.getElementsByClassName("product");

  for (let i = 0; i < products.length; i++) {
    const productName = products[i].getElementsByClassName("product-name")[0];
    const textValue = productName.textContent || productName.innerText;
    if (textValue.toUpperCase().indexOf(filter) > -1) {
      products[i].style.display = "";
    } else {
      products[i].style.display = "none";
    }
  }
}

// Send data to server js
const contactForm = document.getElementById("contact-form");

if (contactForm) {
  contactForm.addEventListener("submit", function (event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    // Add your code here to send the form data to your server
  });
}

// Handle submission and update user's profile
document.getElementById("profile-update-form").addEventListener("submit", function (event) {
  event.preventDefault();
  const formData = new FormData(event.target);
  // Add your code here to update the user's profile with the form data
});

// Category filtering
const categoryLinks = document.querySelectorAll('.category-link');
categoryLinks.forEach(link => {
  link.addEventListener('click', (event) => {
    event.preventDefault();
    const categorySlug = event.target.dataset.category;
    filterProducts(categorySlug);
  });
});

function filterProducts(categorySlug) {
  const products = document.querySelectorAll('.product');

  products.forEach(product => {
    if (product.dataset.category === categorySlug) {
      product.style.display = '';
    } else {
      product.style.display = 'none';
    }
  });
}