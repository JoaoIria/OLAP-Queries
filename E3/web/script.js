function openSecondaryMenu(menuName) {
  const secondaryMenuContainer = document.getElementById('secondaryMenuContainer');
  const secondaryMenuContent = getSecondaryMenuContent(menuName);

  if (secondaryMenuContent) {
    const mainMenu = document.querySelector('.menu');
    mainMenu.style.display = 'none';

    secondaryMenuContainer.innerHTML = secondaryMenuContent;
    secondaryMenuContainer.appendChild(backButton);
  }
}

function getSecondaryMenuContent(menuName) {
  switch (menuName) {
    case 'register_product':
      return `
        <div class="secondary-menu">
          <h2>Register Products</h2>
          <form action="register_product.cgi" method="post">
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
            <input type="submit" value="Submit">
          </form>
        </div>
      `;

    case 'remove_product':
      return `
        <div class="secondary-menu">
          <h2>Remove Products</h2>
          <form action="remove_product.cgi" method="post">
            <label for="product_sku">Product SKU:</label>
            <input type="text" name="remove_product_sku" id="product_sku" required>
            <br><br>
            <input type="submit" value="Remove">
          </form>
        </div>
      `;

    case 'register_supplier':
      return `
        <div class="secondary-menu">
          <h2>Register Supplier</h2>
          <form action="register_supplier.cgi" method="post">
            <label for="reg_supplier_tin">Supplier TIN:</label>
            <input type="text" name="reg_supplier_tin" id="reg_supplier_tin" required>
            <br><br>
            <label for="reg_supplier_name">Supplier Name:</label>
            <input type="text" name="reg_supplier_name" id="reg_supplier_name" required>
            <br><br>
            <label for="reg_supplier_adress">Supplier Address:</label>
            <textarea name="reg_supplier_address" id="reg_supplier_address" required></textarea>
            <br><br>
            <label for="product_sku">Product SKU:</label>
            <input type="text" name="reg_product_sku" id="product_sku" required>
            <br><br>
            <label for="order_date">Order Date:</label>
            <input type="date" name="order_date" id="order_date" required>
            <br><br>
            <input type="submit" value="Submit">
          </form>
        </div>
      `;

      case 'remove_supplier':
            return `
              <div class="secondary-menu">
                <h2>Remove Supplier</h2>
                <form action="remove_supplier.cgi" method="post">
                <div class="secondary-menu">
                  <label for="reg_supplier_tin">Supplier TIN:</label>
                  <input type="text" name="reg_supplier_tin" id="reg_supplier_tin" required>
                  <br><br>
                  <input type="submit" value="Remove">
                  </form>
              </div>
            `;

      case 'change_product':
            return `
              <div class="secondary-menu">
              <h2>Change Product</h2>
              <form action="change_products.cgi" method="post">
                <label for="product_sku">Product SKU:</label>
                <input type="text" name="change_product_sku" id="product_sku" required>
                <br><br>
                <label for="product_price">New Product Price:</label>
                <input type="text" name="change_product_price" id="product_price">
                <br><br>
                <label for="product_description">New Product Description:</label>
                <textarea name="change_product_description" id="product_description"></textarea>
                <br><br>
                <input type="submit" value="Submit">
              </form>
              </div>
            `;


      case 'register_client':
            return `
              <div class="secondary-menu">
                <h2>Register Client</h2>
                <form action="register_client.cgi" method="post">
                <label for="customer_id">Customer ID:</label>
                <input type="text" name="customer_id" id="customer_id" required>
                <br><br>
                <label for="name">Name:</label>
                <input type="text" name="reg_name" id="name" required>
                <br><br>
                <label for="email">Email:</label>
                <input type="email" name="reg_email" id="email" required>
                <br><br>
                <label for="phone">Phone:</label>
                <input type="text" name="reg_phone" id="phone" required>
                <br><br>
                <label for="address">Address:</label>
                <textarea name="reg_address" id="address" required></textarea>
                <br><br>
                <input type="submit" value="Submit">
                </form>
              </div>
            `;


      case 'remove_client':
            return `
              <div class="secondary-menu">
                <h2>Remove Client</h2>
                <form action="remove_client.cgi" method="post">
                <label for="customer_id">Customer ID:</label>
                <input type="text" name="customer_id" id="customer_id" required>
                  <br><br>
                  <input type="submit" value="Remove">
                </form>
              </div>
            `;
  
      case 'make_order':
            return `
              <div class="secondary-menu">
                <h2>Make Order</h2>
                <form action="make_order.cgi" method="post">
                <label for="order_id">Order ID:</label>
                <input type="text" name="order_id" id="order_id" required>
                <br><br>
                <label for="customer_id">Customer ID:</label>
                <input type="text" name="customer_id" id="customer_id" required>
                <br><br>
                <label for="product_sku">Product SKU:</label>
                <input type="text" name="product_sku" id="product_sku" required>
                <br><br>
                <label for="order_date">Order Date:</label>
                <input type="date" name="order_date" id="order_date" required>
                <br><br>
                <label for="quantity">Quantity:</label>
                <input type="number" name="quantity" id="quantity" required>
                <br><br>
                <input type="submit" value="Submit">
                </form>
              </div>
            `;

      case 'pay_order':
            return `
              <div class="secondary-menu">
                <h2>Pay Order</h2>
                <form action="pay_order.cgi" method="post">
                <label for="order_id">Order ID:</label>
                <input type="text" name="order_id" id="order_id" required>
                <br><br>
                <label for="customer_id">Customer ID:</label>
                <input type="text" name="customer_id" id="customer_id" required>
                <br><br>
                <input type="submit" value="Pay">
                </form>
              </div>
            `;
  
      // Add other menu options with their respective HTML content
  
      default:
        return '';
    }
  }
  