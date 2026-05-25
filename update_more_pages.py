from pathlib import Path
base = Path('.')
files = {}
files['cart.html'] = """<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>BookNest | Cart</title>
    <link href=\"https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap\" rel=\"stylesheet\">
    <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css\">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Poppins', sans-serif; background: #f3f4f6; color: #111827; }
        .container { max-width: 1100px; margin: 0 auto; padding: 24px; }
        header { background: white; box-shadow: 0 10px 30px rgba(15,23,42,0.08); position: sticky; top: 0; z-index: 1000; }
        .header-inner { display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px; padding: 18px 24px; }
        .logo { font-size: 1.6rem; font-weight: 800; color: #1f2937; text-decoration: none; display: inline-flex; align-items: center; gap: 10px; }
        .nav { display: flex; gap: 12px; flex-wrap: wrap; }
        .nav a { color: #4b5563; text-decoration: none; padding: 10px 16px; border-radius: 999px; transition: background 0.2s ease; }
        .nav a:hover { background: #e0e7ff; }
        .page-title { margin: 28px 0 18px; font-size: 2rem; font-weight: 700; }
        .cart-grid { display: grid; gap: 24px; grid-template-columns: 1.35fr 0.65fr; }
        .cart-items, .order-summary { background: white; border-radius: 24px; padding: 24px; box-shadow: 0 16px 40px rgba(15,23,42,0.06); }
        .cart-item { display: grid; grid-template-columns: 120px 1fr 100px; gap: 18px; align-items: center; padding: 18px 0; border-bottom: 1px solid #e5e7eb; }
        .cart-item:last-child { border-bottom: none; }
        .cart-item img { width: 100%; border-radius: 18px; object-fit: cover; }
        .item-info { display: grid; gap: 8px; }
        .item-title { font-weight: 700; color: #111827; }
        .item-meta { color: #6b7280; font-size: 0.95rem; }
        .quantity-controls { display: flex; gap: 10px; align-items: center; }
        .quantity-controls button { width: 30px; height: 30px; border-radius: 8px; border: 1px solid #d1d5db; background: white; color: #111827; cursor: pointer; }
        .quantity-count { min-width: 24px; text-align: center; }
        .remove-button { color: #ef4444; cursor: pointer; background: none; border: none; font-weight: 600; }
        .summary-row { display: flex; justify-content: space-between; margin-bottom: 16px; color: #4b5563; }
        .summary-row.total { font-weight: 700; color: #111827; font-size: 1.1rem; }
        .checkout-button { width: 100%; border: none; padding: 16px 20px; border-radius: 16px; background: #4338ca; color: white; font-size: 1rem; font-weight: 700; cursor: pointer; transition: background 0.2s ease; }
        .checkout-button:hover { background: #3730a3; }
        .empty-state { text-align: center; color: #6b7280; padding: 60px 20px; }
        .empty-state a { color: #4338ca; font-weight: 600; }
        footer { margin-top: 40px; text-align: center; color: #6b7280; }
        @media (max-width: 860px) { .cart-grid { grid-template-columns: 1fr; } }
    </style>
</head>
<body>
    <header>
        <div class=\"container header-inner\">
            <a class=\"logo\" href=\"index.html\"><span>📚</span> BookNest</a>
            <nav class=\"nav\">
                <a href=\"index.html\">Home</a>
                <a href=\"soap-simple.html\">Books</a>
                <a href=\"blog.html\">Blog</a>
                <a href=\"about.html\">About</a>
                <a href=\"contact.html\">Contact</a>
            </nav>
        </div>
    </header>
    <main class=\"container\">
        <h1 class=\"page-title\">Shopping Cart</h1>
        <div class=\"cart-grid\">
            <section class=\"cart-items\">
                <div id=\"cartContent\"></div>
            </section>
            <aside class=\"order-summary\">
                <h2 style=\"margin-bottom:18px;\">Order Summary</h2>
                <div class=\"summary-row\"><span>Subtotal</span><span id=\"subtotal\">₹0</span></div>
                <div class=\"summary-row\"><span>Delivery</span><span id=\"deliveryFee\">₹49</span></div>
                <div class=\"summary-row total\"><span>Total</span><span id=\"orderTotal\">₹0</span></div>
                <button class=\"checkout-button\" onclick=\"location.href='payment.html'\">Proceed to Checkout</button>
            </aside>
        </div>
        <footer>&copy; 2026 BookNest. All rights reserved.</footer>
    </main>
    <script>
        const cartKey = 'booknestCart';

        function getCart() {
            return JSON.parse(localStorage.getItem(cartKey) || '[]');
        }

        function saveCart(cart) {
            localStorage.setItem(cartKey, JSON.stringify(cart));
        }

        function updateCartCount() {
            const count = getCart().reduce((sum, item) => sum + item.quantity, 0);
            const badge = document.querySelector('.cart-count');
            if (badge) {
                badge.textContent = count;
                badge.classList.toggle('empty', count === 0);
            }
        }

        function formatPrice(value) {
            return `₹${value}`;
        }

        function renderCart() {
            const cart = getCart();
            const cartContent = document.getElementById('cartContent');
            const subtotalEl = document.getElementById('subtotal');
            const orderTotalEl = document.getElementById('orderTotal');
            if (!cartContent || !subtotalEl || !orderTotalEl) return;
            if (cart.length === 0) {
                cartContent.innerHTML = `<div class=\"empty-state\"><p>Your cart is empty.</p><p><a href=\"soap-simple.html\">Continue shopping</a></p></div>`;
                subtotalEl.textContent = '₹0';
                orderTotalEl.textContent = '₹0';
                return;
            }
            let subtotal = 0;
            cartContent.innerHTML = cart.map(item => {
                const itemTotal = item.price * item.quantity;
                subtotal += itemTotal;
                return `
                    <div class=\"cart-item\">
                        <img src=\"${item.image}\" alt=\"${item.name}\">
                        <div class=\"item-info\">
                            <div class=\"item-title\">${item.name}</div>
                            <div class=\"item-meta\">by ${item.author}</div>
                            <div class=\"item-meta\">${formatPrice(item.price)} each</div>
                            <button class=\"remove-button\" onclick=\"removeItem(${item.id})\">Remove</button>
                        </div>
                        <div class=\"quantity-controls\">
                            <button onclick=\"changeQuantity(${item.id}, -1)\">-</button>
                            <span class=\"quantity-count\">${item.quantity}</span>
                            <button onclick=\"changeQuantity(${item.id}, 1)\">+</button>
                        </div>
                    </div>
                `;
            }).join('');
            subtotalEl.textContent = formatPrice(subtotal);
            orderTotalEl.textContent = formatPrice(subtotal + 49);
            updateCartCount();
        }

        function changeQuantity(id, delta) {
            const cart = getCart();
            const item = cart.find(entry => entry.id === id);
            if (!item) return;
            item.quantity += delta;
            if (item.quantity < 1) {
                const index = cart.findIndex(entry => entry.id === id);
                cart.splice(index, 1);
            }
            saveCart(cart);
            renderCart();
        }

        function removeItem(id) {
            const cart = getCart().filter(entry => entry.id !== id);
            saveCart(cart);
            renderCart();
        }

        document.addEventListener('DOMContentLoaded', renderCart);
    </script>
</body>
</html>"""

files['payment.html'] = """<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>BookNest | Checkout</title>
    <link href=\"https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap\" rel=\"stylesheet\">
    <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css\">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Poppins', sans-serif; background: #eef2ff; color: #111827; }
        .container { max-width: 1020px; margin: 0 auto; padding: 24px; }
        header { background: white; box-shadow: 0 10px 30px rgba(15,23,42,0.08); position: sticky; top: 0; z-index: 1000; }
        .header-inner { display: flex; flex-wrap: wrap; gap: 12px; align-items: center; justify-content: space-between; padding: 18px 24px; }
        .logo { font-size: 1.6rem; font-weight: 800; color: #1f2937; text-decoration: none; display: inline-flex; align-items: center; gap: 10px; }
        .nav { display: flex; gap: 12px; flex-wrap: wrap; }
        .nav a { color: #4b5563; text-decoration: none; padding: 10px 16px; border-radius: 999px; transition: background 0.2s ease; }
        .nav a:hover { background: #e0e7ff; }
        .page-title { margin: 28px 0 18px; font-size: 2rem; font-weight: 700; }
        .checkout-grid { display: grid; gap: 24px; grid-template-columns: 1.25fr 0.75fr; }
        .panel { background: white; border-radius: 24px; padding: 24px; box-shadow: 0 16px 40px rgba(15,23,42,0.06); }
        .panel h2 { margin-bottom: 20px; }
        .field { margin-bottom: 18px; }
        .field label { display: block; margin-bottom: 8px; color: #4b5563; font-weight: 600; }
        .field input, .field select { width: 100%; padding: 14px 16px; border: 1px solid #d1d5db; border-radius: 16px; }
        .summary-row { display: flex; justify-content: space-between; margin-bottom: 16px; color: #4b5563; }
        .summary-row.total { font-weight: 700; color: #111827; font-size: 1.1rem; }
        .pay-button { width: 100%; padding: 16px 20px; border: none; border-radius: 16px; background: #4338ca; color: white; font-size: 1rem; font-weight: 700; cursor: pointer; transition: background 0.2s ease; }
        .pay-button:hover { background: #3730a3; }
        .note { color: #6b7280; margin-top: 18px; line-height: 1.7; }
        footer { margin-top: 40px; text-align: center; color: #6b7280; }
        @media (max-width: 900px) { .checkout-grid { grid-template-columns: 1fr; } }
    </style>
</head>
<body>
    <header>
        <div class=\"container header-inner\">
            <a class=\"logo\" href=\"index.html\"><span>📚</span> BookNest</a>
            <nav class=\"nav\">
                <a href=\"index.html\">Home</a>
                <a href=\"soap-simple.html\">Books</a>
                <a href=\"cart.html\">Cart</a>
                <a href=\"blog.html\">Blog</a>
            </nav>
        </div>
    </header>
    <main class=\"container\">
        <h1 class=\"page-title\">Checkout</h1>
        <div class=\"checkout-grid\">
            <section class=\"panel\">
                <h2>Billing Details</h2>
                <div class=\"field\">
                    <label for=\"fullName\">Full Name</label>
                    <input type=\"text\" id=\"fullName\" placeholder=\"e.g. Priya Sharma\">
                </div>
                <div class=\"field\">
                    <label for=\"email\">Email</label>
                    <input type=\"email\" id=\"email\" placeholder=\"you@example.com\">
                </div>
                <div class=\"field\">
                    <label for=\"address\">Shipping Address</label>
                    <input type=\"text\" id=\"address\" placeholder=\"Street, city, state, pincode\">
                </div>
                <div class=\"field\">
                    <label for=\"paymentMethod\">Payment Method</label>
                    <select id=\"paymentMethod\">
                        <option>Credit / Debit Card</option>
                        <option>UPI</option>
                        <option>Net Banking</option>
                    </select>
                </div>
                <button class=\"pay-button\" onclick=\"handlePayment()\">Pay Now</button>
                <p class=\"note\">Your payment is secure. We use industry-standard encryption to protect your information.</p>
            </section>
            <aside class=\"panel\">
                <h2>Order Summary</h2>
                <div class=\"summary-row\"><span>Subtotal</span><span id=\"subtotal\">₹0</span></div>
                <div class=\"summary-row\"><span>Delivery</span><span>₹49</span></div>
                <div class=\"summary-row total\"><span>Total</span><span id=\"orderTotal\">₹0</span></div>
                <div id=\"cartItemsSummary\" style=\"margin-top: 18px;\"></div>
            </aside>
        </div>
        <footer>&copy; 2026 BookNest. All rights reserved.</footer>
    </main>
    <script>
        const cartKey = 'booknestCart';

        function getCart() {
            return JSON.parse(localStorage.getItem(cartKey) || '[]');
        }

        function updateSummary() {
            const cart = getCart();
            const subtotalEl = document.getElementById('subtotal');
            const orderTotalEl = document.getElementById('orderTotal');
            const itemsSummary = document.getElementById('cartItemsSummary');
            let subtotal = 0;
            if (!itemsSummary || !subtotalEl || !orderTotalEl) return;
            itemsSummary.innerHTML = cart.map(item => {
                subtotal += item.price * item.quantity;
                return `<div style=\"margin-bottom:14px;\"><strong>${item.name}</strong><br><span style=\"color:#6b7280;\">₹${item.price} x ${item.quantity}</span></div>`;
            }).join('');
            if (cart.length === 0) {
                itemsSummary.innerHTML = '<p style=\"color:#6b7280;\">Your cart is empty. Add books before checking out.</p>';
            }
            subtotalEl.textContent = `₹${subtotal}`;
            orderTotalEl.textContent = `₹${subtotal + (cart.length ? 49 : 0)}`;
        }

        function handlePayment() {
            const cart = getCart();
            if (!cart.length) {
                alert('Your cart is empty. Add books first.');
                return;
            }
            const name = document.getElementById('fullName').value.trim();
            const email = document.getElementById('email').value.trim();
            const address = document.getElementById('address').value.trim();
            if (!name || !email || !address) {
                alert('Please complete all billing fields.');
                return;
            }
            localStorage.removeItem(cartKey);
            alert('Payment successful! Your order is confirmed.');
            window.location.href = 'index.html';
        }

        document.addEventListener('DOMContentLoaded', updateSummary);
    </script>
</body>
</html>"""

files['product-detail.html'] = """<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title id=\"pageTitle\">BookNest | Book Detail</title>
    <link href=\"https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap\" rel=\"stylesheet\">
    <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css\">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Poppins', sans-serif; background: #f3f4f6; color: #111827; }
        .container { max-width: 1120px; margin: 0 auto; padding: 24px; }
        header { background: white; box-shadow: 0 10px 30px rgba(15,23,42,0.08); position: sticky; top: 0; z-index: 1000; }
        .header-inner { display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px; padding: 18px 24px; }
        .logo { font-size: 1.6rem; font-weight: 800; color: #1f2937; text-decoration: none; display: inline-flex; align-items: center; gap: 10px; }
        .nav { display: flex; gap: 12px; flex-wrap: wrap; }
        .nav a { color: #4b5563; text-decoration: none; padding: 10px 16px; border-radius: 999px; transition: background 0.2s ease; }
        .nav a:hover { background: #e0e7ff; }
        .detail-grid { display: grid; gap: 30px; grid-template-columns: 1fr 0.9fr; margin-top: 30px; }
        .image-card { background: white; border-radius: 24px; overflow: hidden; box-shadow: 0 18px 40px rgba(15,23,42,0.06); }
        .image-card img { width: 100%; display: block; }
        .detail-panel { background: white; border-radius: 24px; padding: 28px; box-shadow: 0 18px 40px rgba(15,23,42,0.06); }
        .detail-panel h1 { font-size: 2rem; margin-bottom: 14px; }
        .detail-panel .meta { color: #6b7280; margin-bottom: 20px; }
        .detail-panel .price { font-size: 1.6rem; font-weight: 800; color: #ef4444; margin-bottom: 20px; }
        .detail-panel .description { line-height: 1.8; color: #475569; margin-bottom: 24px; }
        .btn-primary { display: inline-flex; align-items: center; justify-content: center; gap: 10px; padding: 14px 22px; border-radius: 16px; border: none; background: #4338ca; color: white; font-weight: 700; cursor: pointer; transition: background 0.2s ease; }
        .btn-primary:hover { background: #3730a3; }
        .related { margin-top: 40px; }
        .related h2 { margin-bottom: 20px; }
        .related-grid { display: grid; gap: 18px; grid-template-columns: repeat(auto-fit,minmax(220px,1fr)); }
        .related-card { background: white; border-radius: 22px; overflow: hidden; box-shadow: 0 16px 40px rgba(15,23,42,0.06); }
        .related-card img { width: 100%; aspect-ratio: 3/4; object-fit: cover; }
        .related-body { padding: 18px; }
        .related-title { font-weight: 700; margin-bottom: 8px; }
        .related-author { color: #6b7280; margin-bottom: 12px; }
        .related-link { color: #4338ca; font-weight: 700; }
        footer { margin-top: 40px; text-align: center; color: #6b7280; }
        @media (max-width: 900px) { .detail-grid { grid-template-columns: 1fr; } }
    </style>
</head>
<body>
    <header>
        <div class=\"container header-inner\">
            <a class=\"logo\" href=\"index.html\"><span>📚</span> BookNest</a>
            <nav class=\"nav\">
                <a href=\"index.html\">Home</a>
                <a href=\"soap-simple.html\">Books</a>
                <a href=\"cart.html\">Cart</a>
                <a href=\"blog.html\">Blog</a>
            </nav>
        </div>
    </header>
    <main class=\"container\">
        <div class=\"detail-grid\">
            <div class=\"image-card\"><img id=\"mainImage\" src=\"https://picsum.photos/seed/book17/900/1200\" alt=\"Book image\"></div>
            <div class=\"detail-panel\">
                <h1 id=\"bookName\">Book Title</h1>
                <div class=\"meta\">by <span id=\"bookAuthor\">Author Name</span> · <span id=\"bookGenre\">Genre</span></div>
                <div class=\"price\" id=\"bookPrice\">₹0</div>
                <p class=\"description\" id=\"bookDescription\">Book description goes here. Learn more about the story, why readers love it, and what makes it unique.</p>
                <button class=\"btn-primary\" onclick=\"addToCart()\"><i class=\"fas fa-shopping-cart\"></i> Add to Cart</button>
            </div>
        </div>
        <section class=\"related\">
            <h2>Related Books</h2>
            <div id=\"relatedGrid\" class=\"related-grid\"></div>
        </section>
        <footer>&copy; 2026 BookNest. All rights reserved.</footer>
    </main>
    <script>
        const cartKey = 'booknestCart';
        const products = [
            { id: 1, name: 'The Silent Patient', author: 'Alex Michaelides', genre: 'Thriller', price: 399, image: 'https://picsum.photos/seed/book1/900/1200', description: 'A thrilling psychological mystery about silence, secrets, and a shocking truth.' },
            { id: 2, name: 'Atomic Habits', author: 'James Clear', genre: 'Self-help', price: 499, image: 'https://picsum.photos/seed/book2/900/1200', description: 'Build better habits one day at a time with simple, effective behavior changes.' },
            { id: 3, name: 'The Alchemist', author: 'Paulo Coelho', genre: 'Fiction', price: 319, image: 'https://picsum.photos/seed/book3/900/1200', description: 'A timeless tale of dreams, destiny, and the courage to follow your heart.' },
            { id: 4, name: 'Becoming', author: 'Michelle Obama', genre: 'Memoir', price: 549, image: 'https://picsum.photos/seed/book4/900/1200', description: 'An intimate memoir of growth, family, and leadership from the former First Lady.' },
            { id: 5, name: 'Dune', author: 'Frank Herbert', genre: 'Sci-Fi', price: 449, image: 'https://picsum.photos/seed/book5/900/1200', description: 'Epic science fiction of desert worlds, political intrigue, and destiny.' },
            { id: 6, name: 'The Midnight Library', author: 'Matt Haig', genre: 'Fantasy', price: 379, image: 'https://picsum.photos/seed/book6/900/1200', description: 'One library, infinite lives, and the choice to discover what truly matters.' }
        ];

        function getCart() {
            return JSON.parse(localStorage.getItem(cartKey) || '[]');
        }

        function saveCart(cart) {
            localStorage.setItem(cartKey, JSON.stringify(cart));
        }

        function getBookId() {
            return parseInt(new URLSearchParams(window.location.search).get('id')) || 1;
        }

        function loadBook() {
            const id = getBookId();
            const book = products.find(item => item.id === id) || products[0];
            document.getElementById('pageTitle').textContent = `BookNest | ${book.name}`;
            document.getElementById('bookName').textContent = book.name;
            document.getElementById('bookAuthor').textContent = book.author;
            document.getElementById('bookGenre').textContent = book.genre;
            document.getElementById('bookPrice').textContent = `₹${book.price}`;
            document.getElementById('bookDescription').textContent = book.description;
            document.getElementById('mainImage').src = book.image;
            renderRelated(book.id);
        }

        function renderRelated(currentId) {
            const relatedGrid = document.getElementById('relatedGrid');
            if (!relatedGrid) return;
            relatedGrid.innerHTML = products.filter(book => book.id !== currentId).slice(0, 4).map(book => `
                <div class=\"related-card\">
                    <img src=\"${book.image}\" alt=\"${book.name}\">
                    <div class=\"related-body\">
                        <div class=\"related-title\">${book.name}</div>
                        <div class=\"related-author\">by ${book.author}</div>
                        <a class=\"related-link\" href=\"product-detail.html?id=${book.id}\">View details</a>
                    </div>
                </div>
            `).join('');
        }

        function addToCart() {
            const id = getBookId();
            const book = products.find(item => item.id === id);
            if (!book) return;
            const cart = getCart();
            const existing = cart.find(item => item.id === id);
            if (existing) {
                existing.quantity += 1;
            } else {
                cart.push({ id: book.id, name: book.name, author: book.author, price: book.price, image: book.image, quantity: 1 });
            }
            saveCart(cart);
            alert(`${book.name} added to cart.`);
        }

        document.addEventListener('DOMContentLoaded', loadBook);
    </script>
</body>
</html>"""

files['login.html'] = """<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>BookNest | Login</title>
    <link href=\"https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap\" rel=\"stylesheet\">
    <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css\">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Poppins', sans-serif; background: linear-gradient(135deg, #eef2ff 0%, #e0e7ff 100%); color: #111827; min-height: 100vh; display: flex; align-items: center; justify-content: center; }
        .auth-wrapper { width: 100%; max-width: 420px; background: white; border-radius: 28px; box-shadow: 0 20px 60px rgba(15,23,42,0.12); padding: 40px; }
        .logo { display: inline-flex; align-items: center; gap: 10px; font-size: 1.8rem; font-weight: 800; color: #1f2937; text-decoration: none; margin-bottom: 24px; }
        .auth-title { font-size: 2rem; margin-bottom: 10px; }
        .auth-subtitle { color: #6b7280; margin-bottom: 28px; }
        .field { margin-bottom: 18px; }
        .field label { display: block; margin-bottom: 8px; font-weight: 600; color: #374151; }
        .field input { width: 100%; padding: 14px 16px; border: 1px solid #d1d5db; border-radius: 16px; }
        .btn { width: 100%; padding: 14px 16px; border: none; border-radius: 16px; background: #4338ca; color: white; font-weight: 700; cursor: pointer; margin-top: 12px; }
        .links { margin-top: 20px; text-align: center; color: #6b7280; }
        .links a { color: #4338ca; text-decoration: none; font-weight: 600; }
    </style>
</head>
<body>
    <div class=\"auth-wrapper\">
        <a class=\"logo\" href=\"index.html\"><span>📚</span> BookNest</a>
        <div class=\"auth-title\">Welcome back</div>
        <p class=\"auth-subtitle\">Sign in to continue shopping books and tracking your orders.</p>
        <div class=\"field\">
            <label for=\"email\">Email</label>
            <input id=\"email\" type=\"email\" placeholder=\"you@example.com\">
        </div>
        <div class=\"field\">
            <label for=\"password\">Password</label>
            <input id=\"password\" type=\"password\" placeholder=\"Enter your password\">
        </div>
        <button class=\"btn\" onclick=\"alert('Login feature is not implemented in this demo yet.')\">Sign In</button>
        <p class=\"links\">Don’t have an account? <a href=\"register.html\">Register</a></p>
    </div>
</body>
</html>"""

files['register.html'] = """<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>BookNest | Register</title>
    <link href=\"https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap\" rel=\"stylesheet\">
    <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css\">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Poppins', sans-serif; background: linear-gradient(135deg, #eef2ff 0%, #e0e7ff 100%); color: #111827; min-height: 100vh; display: flex; align-items: center; justify-content: center; }
        .auth-wrapper { width: 100%; max-width: 460px; background: white; border-radius: 28px; box-shadow: 0 20px 60px rgba(15,23,42,0.12); padding: 40px; }
        .logo { display: inline-flex; align-items: center; gap: 10px; font-size: 1.8rem; font-weight: 800; color: #1f2937; text-decoration: none; margin-bottom: 24px; }
        .auth-title { font-size: 2rem; margin-bottom: 10px; }
        .auth-subtitle { color: #6b7280; margin-bottom: 28px; }
        .field { margin-bottom: 18px; }
        .field label { display: block; margin-bottom: 8px; font-weight: 600; color: #374151; }
        .field input { width: 100%; padding: 14px 16px; border: 1px solid #d1d5db; border-radius: 16px; }
        .btn { width: 100%; padding: 14px 16px; border: none; border-radius: 16px; background: #4338ca; color: white; font-weight: 700; cursor: pointer; margin-top: 12px; }
        .links { margin-top: 20px; text-align: center; color: #6b7280; }
        .links a { color: #4338ca; text-decoration: none; font-weight: 600; }
    </style>
</head>
<body>
    <div class=\"auth-wrapper\">
        <a class=\"logo\" href=\"index.html\"><span>📚</span> BookNest</a>
        <div class=\"auth-title\">Create your account</div>
        <p class=\"auth-subtitle\">Sign up to save your favorite books, access your cart, and checkout faster.</p>
        <div class=\"field\">
            <label for=\"name\">Full Name</label>
            <input id=\"name\" type=\"text\" placeholder=\"Your name\">
        </div>
        <div class=\"field\">
            <label for=\"email\">Email</label>
            <input id=\"email\" type=\"email\" placeholder=\"you@example.com\">
        </div>
        <div class=\"field\">
            <label for=\"password\">Password</label>
            <input id=\"password\" type=\"password\" placeholder=\"Choose a password\">
        </div>
        <button class=\"btn\" onclick=\"alert('Registration is not implemented in this demo yet.')\">Create Account</button>
        <p class=\"links\">Already have an account? <a href=\"login.html\">Login</a></p>
    </div>
</body>
</html>"""

files['profile.html'] = """<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>BookNest | Profile</title>
    <link href=\"https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap\" rel=\"stylesheet\">
    <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css\">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Poppins', sans-serif; background: #eef2ff; color: #111827; }
        .container { max-width: 1000px; margin: 0 auto; padding: 24px; }
        header { background: white; box-shadow: 0 10px 30px rgba(15,23,42,0.08); position: sticky; top: 0; z-index: 1000; }
        .header-inner { display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px; padding: 18px 24px; }
        .logo { font-size: 1.6rem; font-weight: 800; color: #1f2937; text-decoration: none; display: inline-flex; align-items: center; gap: 10px; }
        .nav { display: flex; gap: 12px; flex-wrap: wrap; }
        .nav a { color: #4b5563; text-decoration: none; padding: 10px 16px; border-radius: 999px; transition: background 0.2s ease; }
        .nav a:hover { background: #e0e7ff; }
        .profile-panel { display: grid; gap: 24px; grid-template-columns: 1fr 1fr; margin-top: 28px; }
        .card { background: white; border-radius: 24px; padding: 28px; box-shadow: 0 18px 40px rgba(15,23,42,0.06); }
        .card h2 { margin-bottom: 18px; }
        .info-row { margin-bottom: 14px; }
        .info-label { color: #6b7280; font-weight: 600; margin-bottom: 6px; display: block; }
        .info-value { color: #111827; }
        .recent-orders { display: grid; gap: 16px; }
        .order-item { padding: 18px; border: 1px solid #e5e7eb; border-radius: 20px; }
        .order-title { font-weight: 700; margin-bottom: 6px; }
        .order-meta { color: #6b7280; }
        footer { margin-top: 40px; text-align: center; color: #6b7280; }
        @media (max-width: 820px) { .profile-panel { grid-template-columns: 1fr; } }
    </style>
</head>
<body>
    <header>
        <div class=\"container header-inner\">
            <a class=\"logo\" href=\"index.html\"><span>📚</span> BookNest</a>
            <nav class=\"nav\">
                <a href=\"index.html\">Home</a>
                <a href=\"soap-simple.html\">Books</a>
                <a href=\"blog.html\">Blog</a>
                <a href=\"cart.html\">Cart</a>
            </nav>
        </div>
    </header>
    <main class=\"container\">
        <div class=\"card\">
            <h2>Your Profile</h2>
            <div class=\"info-row\"><span class=\"info-label\">Name</span><div class=\"info-value\">BookNest Reader</div></div>
            <div class=\"info-row\"><span class=\"info-label\">Email</span><div class=\"info-value\">reader@booknest.in</div></div>
            <div class=\"info-row\"><span class=\"info-label\">Membership</span><div class=\"info-value\">BookNest member since 2026</div></div>
        </div>
        <section class=\"card recent-orders\">
            <h2>Recent Orders</h2>
            <div class=\"order-item\">
                <div class=\"order-title\">The Midnight Library</div>
                <div class=\"order-meta\">Order #BNE-4582 · Delivered</div>
            </div>
            <div class=\"order-item\">
                <div class=\"order-title\">Atomic Habits</div>
                <div class=\"order-meta\">Order #BNE-4471 · Delivered</div>
            </div>
        </section>
        <footer>&copy; 2026 BookNest. All rights reserved.</footer>
    </main>
</body>
</html>"""

for name, content in files.items():
    (base / name).write_text(content, encoding='utf-8')
    print(f'Updated {name}')
