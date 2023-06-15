function openSecondaryMenu(menuName) {
    const secondaryMenuContainer = document.getElementById('secondaryMenuContainer');
    const secondaryMenuContent = getSecondaryMenuContent(menuName);
  
    if (secondaryMenuContent) {
      const mainMenu = document.querySelector('.menu');
      mainMenu.style.display = 'none';
  
      secondaryMenuContainer.innerHTML = secondaryMenuContent;
  
      const backButton = document.createElement('button');
      backButton.innerText = 'Return to Main Menu';
      backButton.onclick = function() {
        mainMenu.style.display = 'flex';
        secondaryMenuContainer.innerHTML = '';
      };
  
      secondaryMenuContainer.appendChild(backButton);
    }
  }
  
  function getSecondaryMenuContent(menuName) {
    switch (menuName) {
      case 'register_product':
        return `
          <div class="secondary-menu">
            <h2>Register products</h2>
            <form action="app.cgi" method="post">
              <label for="product_sku">Product SKU:</label>
              <input type="text" name="reg_product_sku" id="product_sku" required>
              <br><br>
              <label for="product_name">Product Name:</label>
              <input type="text" name="get_product_name" id="product_name" required>
              <br><br>
              <label for="product_description">Product Description:</label>
              <textarea name="get_product_description" id="product_description" required></textarea>
              <br><br>
              <label for="product_price">Product Price:</label>
              <input type="text" name="get_product_price" id="product_price" required>
              <br><br>
              <label for="product_ean">Product EAN:</label>
              <input type="text" name="get_product_ean" id="product_ean">
              <br><br>
              <input type="submit" value="Register Product">
            </form>
          </div>
        `;
  
      case 'remove_product':
        return `
          <div class="secondary-menu">
            <h2>Remove Products</h2>
            <!-- Add your form for removing products here -->
          </div>
        `;
  
      // Add other menu options with their respective HTML content
  
      default:
        return '';
    }
  }
  