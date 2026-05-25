# Timeless Tales Bookstore

This repository contains a static bookstore frontend for Timeless Tales, rebuilt as a modern HTML/CSS/JavaScript site with supporting deployment and DevOps artifacts (Dockerfile, docker-compose, Kubernetes manifests, CI/CD scripts).

What this repo contains
- Static website pages: `cart.html`, `login.html`, `register.html`, `product-detail.html`, `payment.html`, `profile.html`, etc.
- `Dockerfile`, `docker-compose.yml`, `nginx.conf` for containerized deployment
- Kubernetes manifests and CI/CD helpers in the repo root and docs
- Helpful docs: `DOCKER_GUIDE.md`, `KUBERNETES_SETUP.md`, `JENKINS_SETUP.md`, and more

Quick local run (static site)

1. From the repo root, serve the files using Python's simple HTTP server (Python 3):

```powershell
cd ECommerce-SOAP-MERN
python -m http.server 8000
```

2. Open your browser to `http://localhost:8000` to reach the shop homepage (`index.html` redirects to `soap-simple.html`).

The site also includes simple informational pages: `about.html`, `contact.html`, and `privacy.html`.

Docker (optional)

Build and run via Docker if you want the containerized setup:

```bash
docker build -t ecommerce-static:latest .
docker run -p 8080:80 ecommerce-static:latest
```

Notes
- This repo does not include a Node.js backend or `package.json` at the root; it's primarily a static frontend plus deployment tooling.
- For a full MERN stack run you'd need the backend API and a MongoDB instance — those are not present here.

License
- No license file originally included; add one if you plan to redistribute.
