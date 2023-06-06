let openShopping = document.querySelector('#cart-icon');
let closeShopping = document.querySelector('.closeShopping');
let list = document.querySelector('.list');
let listCard = document.querySelector('.listCard');
let body = document.querySelector('body');
let total = document.querySelector('.total');
let quantity = document.querySelector('.quantity');

openShopping.addEventListener('click', () => {
    body.classList.add('active');
});

closeShopping.addEventListener('click', () => {
    body.classList.remove('active');
});

let listCards = [];

function addToCart(productId) {
    fetch(`/get/product/${productId}`)
        .then(response => response.json())
        .then(product => {
            if (product) {
                const cartItem = listCards.find(item => item.product.id === product.id);
                if (cartItem) {
                    cartItem.quantity += 1;
                } else {
                    listCards.push({
                        product: product,
                        quantity: 1
                    });
                }
                reloadCard();
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function reloadCard() {
    listCard.innerHTML = '';
    let count = 0;
    let totalPrice = 0;

    listCards.forEach(item => {
        totalPrice += item.product.price * item.quantity;
        count += item.quantity;

        let newDiv = document.createElement('li');
        newDiv.innerHTML = `
            <div><img src="${item.product.image}" alt="Product Image"/></div>
            <div style="font-size: 18px;" >${item.product.name}</div>
            <div style="font-size: 18px;" >$ ${(item.product.price * item.quantity).toLocaleString()}</div>
            <div style="font-size: 18px;" >
                <button onclick="changeQuantity(${item.product.id}, ${item.quantity - 1})">-</button>
                <div class="count">${item.quantity}</div>
                <button onclick="changeQuantity(${item.product.id}, ${item.quantity + 1})">+</button>
            </div>`;
        listCard.appendChild(newDiv);
    });

    total.innerText = '$' + totalPrice.toLocaleString();
    quantity.innerText = count;
}

function changeQuantity(productId, quantity) {
    if (quantity === 0) {
        const index = listCards.findIndex(item => item.product.id === productId);
        if (index !== -1) {
            listCards.splice(index, 1);
        }
    } else {
        const cartItem = listCards.find(item => item.product.id === productId);
        if (cartItem) {
            cartItem.quantity = quantity;
        }
    }
    reloadCard();
}
