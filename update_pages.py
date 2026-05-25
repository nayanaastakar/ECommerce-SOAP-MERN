from pathlib import Path
base = Path('.')
files = {}
files['soap-simple.html'] = """<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"utf-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>BookNest | Online Bookstore</title>
    <link href=\"https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap\" rel=\"stylesheet\">
    <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css\">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Poppins', sans-serif; background: #f4f6fb; color: #222831; }
        a { color: inherit; text-decoration: none; }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        header { position: sticky; top: 0; z-index: 1000; background: rgba(255,255,255,0.96); backdrop-filter: blur(10px); box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
        .header-inner { display: flex; align-items: center; justify-content: space-between; gap: 16px; padding: 18px 20px; flex-wrap: wrap; }
        .logo { display: inline-flex; align-items: center; gap: 10px; font-size: 1.6rem; font-weight: 800; color: #2b2d42; }
        .logo-mark { font-size: 1.8rem; }
        .nav { display: flex; gap: 12px; flex-wrap: wrap; align-items: center; }
        .nav a { font-weight: 600; padding: 10px 16px; border-radius: 999px; transition: background 0.2s ease, color 0.2s ease; }
        .nav a:hover { background: #edf2ff; }
        .hero { background: linear-gradient(135deg, #3f72af 0%, #112d4e 100%); color: white; padding: 70px 20px; border-radius: 28px; margin: 24px 0; overflow: hidden; }
        .hero h1 { font-size: clamp(2.6rem, 5vw, 4rem); line-height: 1.05; margin-bottom: 16px; }
        .hero p { max-width: 700px; font-size: 1.05rem; color: rgba(255,255,255,0.87); margin-bottom: 24px; }
        .hero .hero-actions { display: flex; gap: 16px; flex-wrap: wrap; align-items: center; }
        .btn { display: inline-flex; align-items: center; justify-content: center; gap: 10px; border: none; border-radius: 999px; padding: 14px 26px; font-weight: 700; cursor: pointer; transition: transform 0.2s ease, background 0.2s ease; }
        .btn-primary { background: #ef233c; color: white; }
        .btn-secondary { background: white; color: #112d4e; }
        .btn:hover { transform: translateY(-1px); }
        .search-card { background: white; border-radius: 20px; padding: 18px 22px; display: flex; align-items: center; gap: 12px; box-shadow: 0 15px 40px rgba(15,23,42,0.08); max-width: 780px; margin-top: 20px; }
        .search-card input { flex: 1; border: none; outline: none; font-size: 1rem; color: #2b2d42; }
        .search-card button { width: 52px; height: 52px; border-radius: 50%; border: none; background: #ef233c; color: white; cursor: pointer; display: grid; place-items: center; }
        .section-title { font-size: 1.6rem; font-weight: 700; margin-bottom: 18px; color: #112d4e; }
        .small-text { color: #4f5d75; }
        .category-grid { display: grid; grid-template-columns: repeat(auto-fit,minmax(180px,1fr)); gap: 18px; margin-top: 28px; }
        .category-card { background: white; padding: 24px; border-radius: 22px; box-shadow: 0 18px 40px rgba(15,23,42,0.06); transition: transform 0.2s ease; }
        .category-card:hover { transform: translateY(-3px); }
        .category-card h3 { margin-bottom: 10px; font-size: 1.05rem; }
        .category-card p { color: #5f6c7b; line-height: 1.7; }
        .product-grid { display: grid; grid-template-columns: repeat(auto-fit,minmax(240px,1fr)); gap: 22px; margin-top: 24px; }
        .card { background: white; border-radius: 24px; overflow: hidden; box-shadow: 0 16px 40px rgba(15,23,42,0.06); display: flex; flex-direction: column; }
        .card img { width: 100%; aspect-ratio: 3/4; object-fit: cover; }
        .card-body { padding: 20px; display: flex; flex-direction: column; gap: 12px; }
        .book-title { font-size: 1.05rem; font-weight: 700; color: #112d4e; }
        .book-author { color: #4f5d75; font-size: 0.95rem; }
        .book-genre { color: #9b9fb4; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.08em; }
        .book-description { color: #5f6c7b; font-size: 0.95rem; line-height: 1.6; min-height: 68px; }
        .card-footer { margin-top: auto; display: flex; justify-content: space-between; align-items: center; gap: 12px; flex-wrap: wrap; }
        .price { font-weight: 800; color: #ef233c; }
        .actions { display: flex; gap: 10px; flex-wrap: wrap; }
        .small-btn { border: 1px solid #ef233c; background: transparent; color: #ef233c; padding: 10px 16px; border-radius: 999px; cursor: pointer; transition: background 0.2s ease; }
        .small-btn:hover { background: #ef233c; color: white; }
        footer { margin-top: 50px; padding: 30px 0; text-align: center; color: #4f5d75; }
        @media (max-width: 820px) { .header-inner { justify-content: center; } .hero { text-align: center; } .hero .hero-actions { justify-content: center; } }
    </style>
</head>
<body>
    <header>
        <div class=\"container header-inner\">
            <a class=\"logo\" href=\"index.html\"><span class=\"logo-mark\">📚</span> BookNest</a>
            <nav class=\"nav\">
                <a href=\"soap-simple.html\">Books</a>
                <a href=\"blog.html\">Blog</a>
                <a href=\"about.html\">About</a>
                <a href=\"contact.html\">Contact</a>
                <a href=\"privacy.html\">Privacy</a>
                <a href=\"cart.html\"><i class=\"fas fa-shopping-cart\"></i></a>
                <a href=\"login.html\">Login</a>
            </nav>
        </div>
    </header>

    <main class=\"container\">
        <section class=\"hero\">
            <h1>Find your next adventure in every chapter.</h1>
            <p>Discover bestselling fiction, inspiring memoirs, practical self-help, and curated books for every reader.</p>
            <div class=\"hero-actions\">
                <a href=\"soap-simple.html\" class=\"btn btn-primary\">Browse Books</a>
                <a href=\"blog.html\" class=\"btn btn-secondary\">Read our Blog</a>
            </div>
            <div class=\"search-card\">
                <input id=\"productSearch\" type=\"search\" placeholder=\"Search books, authors, or genres...\" aria-label=\"Search books\">
                <button onclick=\"searchProducts()\" aria-label=\"Search\"><i class=\"fas fa-search\"></i></button>
            </div>
        </section>

        <section>
            <div class=\"section-title\">Featured Categories</div>
            <div class=\"category-grid\">
                <div class=\"category-card\"><h3>Thrillers</h3><p>Fast-paced stories with suspense, twists, and unforgettable endings.</p></div>
                <div class=\"category-card\"><h3>Self-Help</h3><p>Daily habits and proven routines for growth, focus, and wellbeing.</p></div>
                <div class=\"category-card\"><h3>Fiction</h3><p>Classic and contemporary novels that transport you to other worlds.</p></div>
                <div class=\"category-card\"><h3>Memoir</h3><p>True stories told by voices that inspire, challenge, and uplift.</p></div>
            </div>
        </section>

        <section style=\"margin-top: 40px;\">
            <div class=\"section-title\">Best Sellers</div>
            <div id=\"productGrid\" class=\"product-grid\"></div>
        </section>
    </main>

    <footer>
        <div class=\"container\">&copy; 2026 BookNest. A modern online bookstore.</div>
    </footer>

    <script>
        const products = [
            { id: 1, name: 'The Silent Patient', author: 'Alex Michaelides', price: 399, image: 'https://picsum.photos/seed/book1/420/560', description: 'A thrilling psychological mystery about silence, secrets, and a shocking truth.', genre: 'Thriller' },
            { id: 2, name: 'Atomic Habits', author: 'James Clear', price: 499, image: 'https://picsum.photos/seed/book2/420/560', description: 'Build better habits one day at a time with simple, effective behavior changes.', genre: 'Self-help' },
            { id: 3, name: 'The Alchemist', author: 'Paulo Coelho', price: 319, image: 'https://picsum.photos/seed/book3/420/560', description: 'A timeless tale of dreams, destiny, and the courage to follow your heart.', genre: 'Fiction' },
            { id: 4, name: 'Becoming', author: 'Michelle Obama', price: 549, image: 'https://picsum.photos/seed/book4/420/560', description: 'An intimate memoir of growth, family, and leadership from the former First Lady.', genre: 'Memoir' },
            { id: 5, name: 'Dune', author: 'Frank Herbert', price: 449, image: 'https://picsum.photos/seed/book5/420/560', description: 'Epic science fiction of desert worlds, political intrigue, and destiny.', genre: 'Sci-Fi' },
            { id: 6, name: 'The Midnight Library', author: 'Matt Haig', price: 379, image: 'https://picsum.photos/seed/book6/420/560', description: 'One library, infinite lives, and the choice to discover what truly matters.', genre: 'Fantasy' },
            { id: 7, name: 'Educated', author: 'Tara Westover', price: 429, image: 'https://picsum.photos/seed/book7/420/560', description: 'A powerful memoir about family, freedom, and the journey toward knowledge.', genre: 'Memoir' },
            { id: 8, name: 'Where the Crawdads Sing', author: 'Delia Owens', price: 389, image: 'https://picsum.photos/seed/book8/420/560', description: 'A mystery and coming-of-age story set in the wild marshlands of the South.', genre: 'Fiction' }
        ];

        function getCart() {
            return JSON.parse(localStorage.getItem('booknestCart') || '[]');
        }

        function saveCart(cart) {
            localStorage.setItem('booknestCart', JSON.stringify(cart));
        }

        function updateHeaderCartCount() {
            const count = getCart().reduce((sum, item) => sum + item.quantity, 0);
            const cartLink = document.querySelector('header .nav a[href=\"cart.html\"]');
            if (cartLink) {
                cartLink.innerHTML = `<i class=\"fas fa-shopping-cart\"></i> Cart <span style=\"background:#ef233c;color:white;padding:2px 8px;border-radius:999px;font-size:0.85rem;margin-left:6px;\">${count}</span>`;
            }
        }

        function setSearchUrl(query) {
            const params = new URLSearchParams(window.location.search);
            if (query) { params.set('search', query); } else { params.delete('search'); }
            const newUrl = `${window.location.pathname}?${params.toString()}`;
            history.replaceState(null, '', newUrl);
        }

        function getSearchTerm() {
            return new URLSearchParams(window.location.search).get('search') || '';
        }

        function searchProducts() {
            const query = document.getElementById('productSearch').value.trim();
            setSearchUrl(query);
            renderProducts(query);
        }

        function renderProducts(query = '') {
            const normalized = query.trim().toLowerCase();
            const filtered = normalized
                ? products.filter(book => book.name.toLowerCase().includes(normalized) || book.author.toLowerCase().includes(normalized) || book.genre.toLowerCase().includes(normalized) || book.description.toLowerCase().includes(normalized))
                : products;
            const grid = document.getElementById('productGrid');
            if (!grid) return;
            if (filtered.length === 0) {
                grid.innerHTML = '<div style=\"grid-column:1/-1;text-align:center;color:#4f5d75;padding:80px 0;\">No books matched your search. Try another title or author.</div>';
                return;
            }
            grid.innerHTML = filtered.map(book => `
                <div class=\"card\">
                    <img src=\"${book.image}\" alt=\"${book.name}\">
                    <div class=\"card-body\">
                        <div class=\"book-genre\">${book.genre}</div>
                        <div class=\"book-title\">${book.name}</div>
                        <div class=\"book-author\">by ${book.author}</div>
                        <div class=\"book-description\">${book.description}</div>
                        <div class=\"card-footer\">
                            <div class=\"price\">₹${book.price}</div>
                            <div class=\"actions\">
                                <button class=\"small-btn\" onclick=\"addToCart(${book.id})\">Add to Cart</button>
                                <a class=\"small-btn\" href=\"product-detail.html?id=${book.id}\">View Details</a>
                            </div>
                        </div>
                    </div>
                </div>
            `).join('');
        }

        function addToCart(id) {
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
            updateHeaderCartCount();
            alert(`Added \"${book.name}\" to your cart.`);
        }

        document.addEventListener('DOMContentLoaded', () => {
            const term = getSearchTerm();
            const input = document.getElementById('productSearch');
            if (input) input.value = term;
            renderProducts(term);
            updateHeaderCartCount();
        });
    </script>
</body>
</html>"""

files['index.html'] = """<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"utf-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>BookNest | Home</title>
    <link href=\"https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap\" rel=\"stylesheet\">
    <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css\">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Poppins', sans-serif; background: #eef2ff; color: #1f2937; }
        .container { max-width: 1140px; margin: 0 auto; padding: 24px; }
        header { padding: 18px 0; }
        .logo { font-size: 1.75rem; font-weight: 800; text-decoration: none; color: #1f2937; display: inline-flex; align-items: center; gap: 12px; }
        nav { margin-top: 16px; display: flex; flex-wrap: wrap; gap: 12px; }
        nav a { color: #374151; text-decoration: none; padding: 10px 16px; border-radius: 999px; transition: background 0.2s ease; }
        nav a:hover { background: #e0e7ff; }
        .hero { display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 32px; align-items: center; margin-top: 40px; }
        .hero h1 { font-size: clamp(2.5rem, 5vw, 4rem); line-height: 1.05; margin-bottom: 20px; }
        .hero p { font-size: 1.05rem; color: #4b5563; margin-bottom: 28px; }
        .hero-buttons { display: flex; gap: 14px; flex-wrap: wrap; }
        .btn { border: none; border-radius: 999px; padding: 14px 28px; font-weight: 700; cursor: pointer; transition: transform 0.2s ease, background 0.2s ease; }
        .btn-primary { background: #4338ca; color: white; }
        .btn-secondary { background: #e0e7ff; color: #1f2937; }
        .hero-image { width: 100%; border-radius: 30px; overflow: hidden; box-shadow: 0 20px 50px rgba(15,23,42,0.12); }
        .hero-image img { width: 100%; display: block; }
        .features { margin-top: 60px; display: grid; grid-template-columns: repeat(auto-fit,minmax(220px,1fr)); gap: 20px; }
        .feature-card { background: white; padding: 26px; border-radius: 24px; box-shadow: 0 16px 40px rgba(15,23,42,0.06); }
        .feature-card h3 { margin-bottom: 14px; }
        .feature-card p { color: #4b5563; line-height: 1.8; }
        footer { margin-top: 60px; padding: 24px 0; text-align: center; color: #6b7280; }
        @media (max-width: 900px) { .hero { grid-template-columns: 1fr; } }
    </style>
</head>
<body>
    <div class=\"container\">
        <header>
            <a class=\"logo\" href=\"index.html\"><span>📚</span> BookNest</a>
            <nav>
                <a href=\"soap-simple.html\">Shop</a>
                <a href=\"blog.html\">Blog</a>
                <a href=\"about.html\">About</a>
                <a href=\"contact.html\">Contact</a>
                <a href=\"privacy.html\">Privacy</a>
            </nav>
        </header>

        <main class=\"hero\">
            <div>
                <h1>Welcome to BookNest — your digital bookstore for curated books.</h1>
                <p>Browse bestsellers, discover hidden gems, and add beautiful books to your shelves with a modern shopping experience.</p>
                <div class=\"hero-buttons\">
                    <a href=\"soap-simple.html\" class=\"btn btn-primary\">Browse Books</a>
                    <a href=\"blog.html\" class=\"btn btn-secondary\">Read the Blog</a>
                </div>
            </div>
            <div class=\"hero-image\">
                <img src=\"https://picsum.photos/seed/bookstore-hero/900/700\" alt=\"Bookstore hero image\">
            </div>
        </main>

        <section class=\"features\">
            <div class=\"feature-card\"><h3>Curated Collections</h3><p>Selected books across genres so you can find your next favorite title faster.</p></div>
            <div class=\"feature-card\"><h3>Fast Delivery</h3><p>Enjoy quick shipping across India with free delivery on orders above ₹499.</p></div>
            <div class=\"feature-card\"><h3>Secure Checkout</h3><p>Our checkout is designed to keep your payment and order details safe.</p></div>
            <div class=\"feature-card\"><h3>Support 24/7</h3><p>Have questions? Our customer support is always ready to help.</p></div>
        </section>

        <footer>&copy; 2026 BookNest. Shop your next book today.</footer>
    </div>
</body>
</html>"""

files['about.html'] = """<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"utf-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>About BookNest</title>
    <link href=\"https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap\" rel=\"stylesheet\">
    <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css\">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Poppins', sans-serif; background: #f8fafc; color: #1f2937; }
        .container { max-width: 1100px; margin: 0 auto; padding: 24px; }
        header, footer { background: white; box-shadow: 0 10px 30px rgba(15,23,42,0.08); }
        .header-inner, .footer-inner { display: flex; flex-wrap: wrap; gap: 12px; align-items: center; justify-content: space-between; padding: 18px 24px; }
        .logo { color: #1f2937; font-size: 1.6rem; font-weight: 700; text-decoration: none; display: inline-flex; gap: 10px; }
        .nav { display: flex; flex-wrap: wrap; gap: 12px; }
        .nav a { color: #475569; text-decoration: none; padding: 10px 14px; border-radius: 999px; transition: background 0.2s ease; }
        .nav a:hover { background: #eef2ff; }
        .hero { padding: 48px 0; }
        .hero h1 { font-size: clamp(2.4rem, 4vw, 3.4rem); margin-bottom: 18px; }
        .hero p { max-width: 760px; line-height: 1.8; color: #475569; }
        .grid { display: grid; gap: 20px; margin-top: 32px; grid-template-columns: repeat(auto-fit,minmax(240px,1fr)); }
        .card { background: white; border-radius: 24px; padding: 28px; box-shadow: 0 18px 40px rgba(15,23,42,0.06); }
        .card h3 { margin-bottom: 14px; }
        .card p { color: #475569; line-height: 1.75; }
        footer { padding: 24px 0; text-align: center; color: #6b7280; margin-top: 40px; }
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
                <a href=\"contact.html\">Contact</a>
                <a href=\"privacy.html\">Privacy</a>
            </nav>
        </div>
    </header>

    <main class=\"container\">
        <section class=\"hero\">
            <h1>About BookNest</h1>
            <p>BookNest is a modern online bookstore built to make book discovery simple, fast, and delightful. We curate the finest books across genres so you can find great reads for every mood.</p>
        </section>

        <section class=\"grid\">
            <div class=\"card\">
                <h3>Our mission</h3>
                <p>We believe in making reading accessible to every reader with curated collections, trusted reviews, and a sleek shopping experience.</p>
            </div>
            <div class=\"card\">
                <h3>What we offer</h3>
                <p>From thrillers to memoirs and business guides, our catalog is designed for both avid readers and gift shoppers.</p>
            </div>
            <div class=\"card\">
                <h3>Customer care</h3>
                <p>Fast delivery, easy returns, and support that answers your questions quickly — we are here to help at every step.</p>
            </div>
            <div class=\"card\">
                <h3>Our promise</h3>
                <p>Quality books, secure checkout, and honest service. No clutter, no confusion — just a better way to shop for books online.</p>
            </div>
        </section>
    </main>

    <footer>
        <div class=\"container footer-inner\">&copy; 2026 BookNest. All rights reserved.</div>
    </footer>
</body>
</html>"""

files['contact.html'] = """<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"utf-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Contact BookNest</title>
    <link href=\"https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap\" rel=\"stylesheet\">
    <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css\">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Poppins', sans-serif; background: #f8fafc; color: #1f2937; }
        .container { max-width: 1100px; margin: 0 auto; padding: 24px; }
        header, footer { background: white; box-shadow: 0 10px 30px rgba(15,23,42,0.08); }
        .header-inner, .footer-inner { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 12px; padding: 18px 24px; }
        .logo { font-size: 1.6rem; font-weight: 700; color: #1f2937; text-decoration: none; display: inline-flex; gap: 8px; }
        .nav { display: flex; flex-wrap: wrap; gap: 12px; }
        .nav a { color: #475569; text-decoration: none; padding: 10px 14px; border-radius: 999px; transition: background 0.2s ease; }
        .nav a:hover { background: #eef2ff; }
        .hero { padding: 48px 0; }
        .hero h1 { font-size: clamp(2.4rem, 4vw, 3.4rem); margin-bottom: 18px; }
        .hero p { max-width: 760px; color: #475569; line-height: 1.8; }
        .card { background: white; border-radius: 24px; padding: 32px; box-shadow: 0 18px 40px rgba(15,23,42,0.06); margin-top: 28px; }
        .contact-grid { display: grid; gap: 24px; grid-template-columns: repeat(auto-fit,minmax(260px,1fr)); margin-top: 28px; }
        .contact-item { display: flex; gap: 14px; align-items: flex-start; }
        .contact-icon { color: #4338ca; font-size: 1.5rem; margin-top: 4px; }
        .contact-label { font-weight: 700; margin-bottom: 6px; }
        .contact-text { color: #475569; line-height: 1.8; }
        .footer { margin-top: 40px; }
    </style>
</head>
<body>
    <header>
        <div class=\"container header-inner\">
            <a class=\"logo\" href=\"index.html\"><span>📚</span> BookNest</a>
            <nav class=\"nav\">
                <a href=\"index.html\">Home</a>
                <a href=\"soap-simple.html\">Books</a>
                <a href=\"about.html\">About</a>
                <a href=\"blog.html\">Blog</a>
                <a href=\"privacy.html\">Privacy</a>
            </nav>
        </div>
    </header>

    <main class=\"container\">
        <section class=\"hero\">
            <h1>Contact BookNest</h1>
            <p>Have a question about an order, a book, or our services? Get in touch and our friendly support team will help you right away.</p>
        </section>

        <div class=\"card\">
            <div class=\"contact-grid\">
                <div>
                    <div class=\"contact-item\">
                        <div class=\"contact-icon\"><i class=\"fas fa-phone\"></i></div>
                        <div>
                            <div class=\"contact-label\">Phone</div>
                            <div class=\"contact-text\">+91 98765 43210</div>
                        </div>
                    </div>
                    <div class=\"contact-item\">
                        <div class=\"contact-icon\"><i class=\"fas fa-envelope\"></i></div>
                        <div>
                            <div class=\"contact-label\">Email</div>
                            <div class=\"contact-text\">support@booknest.in</div>
                        </div>
                    </div>
                    <div class=\"contact-item\">
                        <div class=\"contact-icon\"><i class=\"fas fa-map-marker-alt\"></i></div>
                        <div>
                            <div class=\"contact-label\">Address</div>
                            <div class=\"contact-text\">42 Reading Lane, Bangalore, India</div>
                        </div>
                    </div>
                </div>
                <div>
                    <h2 style=\"margin-bottom: 16px; color: #111827;\">Send us a message</h2>
                    <p style=\"color: #475569; line-height: 1.75;\">Use our contact form below to ask about shipping, book availability, or recommendations. We’ll respond within one business day.</p>
                </div>
            </div>
        </div>
    </main>

    <footer>
        <div class=\"container footer-inner\">&copy; 2026 BookNest. All rights reserved.</div>
    </footer>
</body>
</html>"""

files['privacy.html'] = """<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"utf-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Privacy Policy | BookNest</title>
    <link href=\"https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap\" rel=\"stylesheet\">
    <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css\">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Poppins', sans-serif; background: #f8fafc; color: #1f2937; }
        .container { max-width: 1000px; margin: 0 auto; padding: 24px; }
        header, footer { background: white; box-shadow: 0 10px 30px rgba(15,23,42,0.08); }
        .header-inner, .footer-inner { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 12px; padding: 18px 24px; }
        .logo { font-size: 1.6rem; font-weight: 700; color: #1f2937; text-decoration: none; display: inline-flex; gap: 8px; }
        .nav { display: flex; flex-wrap: wrap; gap: 12px; }
        .nav a { color: #475569; text-decoration: none; padding: 10px 14px; border-radius: 999px; transition: background 0.2s ease; }
        .nav a:hover { background: #eef2ff; }
        .hero { padding: 48px 0; }
        .hero h1 { font-size: clamp(2.4rem, 4vw, 3.2rem); margin-bottom: 18px; }
        .hero p { max-width: 780px; color: #475569; line-height: 1.8; }
        .content { margin-top: 32px; background: white; border-radius: 24px; box-shadow: 0 18px 40px rgba(15,23,42,0.06); padding: 32px; }
        .content h2 { font-size: 1.35rem; margin-top: 24px; margin-bottom: 14px; }
        .content p, .content li { color: #475569; line-height: 1.8; margin-bottom: 14px; }
        .content ul { margin-left: 20px; }
        .footer { margin-top: 40px; }
    </style>
</head>
<body>
    <header>
        <div class=\"container header-inner\">
            <a class=\"logo\" href=\"index.html\"><span>📚</span> BookNest</a>
            <nav class=\"nav\">
                <a href=\"index.html\">Home</a>
                <a href=\"soap-simple.html\">Books</a>
                <a href=\"about.html\">About</a>
                <a href=\"contact.html\">Contact</a>
                <a href=\"blog.html\">Blog</a>
            </nav>
        </div>
    </header>

    <main class=\"container\">
        <section class=\"hero\">
            <h1>Privacy Policy</h1>
            <p>BookNest is committed to protecting your privacy and handling your personal data with care.</p>
        </section>

        <article class=\"content\">
            <h2>What information we collect</h2>
            <p>We collect information you provide during account creation, order placement, and customer support interactions. This may include your name, email, shipping address, and payment details.</p>
            <h2>How we use your information</h2>
            <ul>
                <li>To process and deliver orders.</li>
                <li>To communicate order updates and customer support replies.</li>
                <li>To improve our website and personalize your experience.</li>
            </ul>
            <h2>Data security</h2>
            <p>We take reasonable measures to protect your information. We do not sell your personal data to third parties.</p>
            <h2>Cookies</h2>
            <p>Our site uses cookies for essential functionality and analytics. You can manage cookies through your browser settings.</p>
            <h2>Contact</h2>
            <p>If you have questions or want to request changes to your data, please contact us at support@booknest.in.</p>
        </article>
    </main>

    <footer>
        <div class=\"container footer-inner\">&copy; 2026 BookNest. All rights reserved.</div>
    </footer>
</body>
</html>"""

files['blog.html'] = """<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"utf-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>BookNest Blog</title>
    <link href=\"https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap\" rel=\"stylesheet\">
    <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css\">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Poppins', sans-serif; background: #f8fafc; color: #1f2937; }
        .container { max-width: 1100px; margin: 0 auto; padding: 24px; }
        header, footer { background: white; box-shadow: 0 10px 30px rgba(15,23,42,0.08); }
        .header-inner, .footer-inner { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 12px; padding: 18px 24px; }
        .logo { font-size: 1.6rem; font-weight: 700; color: #1f2937; text-decoration: none; display: inline-flex; gap: 8px; }
        .nav { display: flex; flex-wrap: wrap; gap: 12px; }
        .nav a { color: #475569; text-decoration: none; padding: 10px 14px; border-radius: 999px; transition: background 0.2s ease; }
        .nav a:hover { background: #eef2ff; }
        .hero { padding: 48px 0; }
        .hero h1 { font-size: clamp(2.4rem, 4vw, 3.4rem); margin-bottom: 18px; }
        .hero p { max-width: 760px; color: #475569; line-height: 1.8; }
        .posts { display: grid; gap: 24px; margin-top: 32px; }
        .post-card { background: white; border-radius: 24px; overflow: hidden; box-shadow: 0 18px 40px rgba(15,23,42,0.06); display: grid; grid-template-columns: 1.1fr 0.9fr; }
        .post-card img { width: 100%; height: 100%; object-fit: cover; }
        .post-content { padding: 28px; display: flex; flex-direction: column; gap: 16px; }
        .post-title { font-size: 1.45rem; font-weight: 700; }
        .post-text { color: #475569; line-height: 1.8; }
        .read-more { color: #4338ca; font-weight: 700; }
        @media (max-width: 860px) { .post-card { grid-template-columns: 1fr; } }
        .footer { margin-top: 40px; }
    </style>
</head>
<body>
    <header>
        <div class=\"container header-inner\">
            <a class=\"logo\" href=\"index.html\"><span>📚</span> BookNest</a>
            <nav class=\"nav\">
                <a href=\"index.html\">Home</a>
                <a href=\"soap-simple.html\">Books</a>
                <a href=\"about.html\">About</a>
                <a href=\"contact.html\">Contact</a>
                <a href=\"privacy.html\">Privacy</a>
            </nav>
        </div>
    </header>

    <main class=\"container\">
        <section class=\"hero\">
            <h1>BookNest Blog</h1>
            <p>Read tips on reading, book recommendations, and stories behind the books you love.</p>
        </section>

        <div class=\"posts\">
            <article class=\"post-card\">
                <div class=\"post-content\">
                    <div class=\"post-title\">5 Books to Read This Year</div>
                    <p class=\"post-text\">From gripping thrillers to inspiring memoirs, discover a balanced reading list for every mood.</p>
                    <a class=\"read-more\" href=\"soap-simple.html\">Explore our collection →</a>
                </div>
                <img src=\"https://picsum.photos/seed/blog1/800/600\" alt=\"Book reading\">
            </article>
            <article class=\"post-card\">
                <div class=\"post-content\">
                    <div class=\"post-title\">How to Build a Reading Habit</div>
                    <p class=\"post-text\">Small daily routines make it easy to read more. Learn how to create time for books with simple steps.</p>
                    <a class=\"read-more\" href=\"soap-simple.html\">Start reading today →</a>
                </div>
                <img src=\"https://picsum.photos/seed/blog2/800/600\" alt=\"Reading routine\">
            </article>
            <article class=\"post-card\">
                <div class=\"post-content\">
                    <div class=\"post-title\">Why Memoirs Matter</div>
                    <p class=\"post-text\">Real stories from real lives can shift your perspective. Discover memoirs that inspire, challenge, and comfort.</p>
                    <a class=\"read-more\" href=\"soap-simple.html\">Explore memoirs →</a>
                </div>
                <img src=\"https://picsum.photos/seed/blog3/800/600\" alt=\"Memoir books\">
            </article>
        </div>
    </main>

    <footer>
        <div class=\"container footer-inner\">&copy; 2026 BookNest. All rights reserved.</div>
    </footer>
</body>
</html>"""

for name, content in files.items():
    (base / name).write_text(content, encoding='utf-8')
    print(f'Updated {name}')
