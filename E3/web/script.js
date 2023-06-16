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
      window.location.replace("register_product.html");
      return;

    case 'remove_product':
      window.location.replace("remove_product.html");
      return;

    case 'register_supplier':
      window.location.replace("register_supplier.html");
      return;

    case 'remove_supplier':
      window.location.replace("remove_supplier.html");
      return;

    case 'change_product':
      window.location.replace("change_product.html");
      return;

    case 'register_client':
      window.location.replace("register_client.html");
      return;

    case 'remove_client':
      window.location.replace("remove_client.html");
      return;

    case 'make_order':
      window.location.replace("make_order.html");
      return;

    case 'pay_order':
      window.location.replace("pay_order.html");
      return;


    default:
      return '';
    }
  }
  