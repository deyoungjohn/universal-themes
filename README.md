# Telemorph (Telegram Theme Converter)

Convert Telegram themes between **Android** (`.attheme` / `t.me/addtheme/...`) and **iOS** (`.tgios-theme`).

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new)

---

## Features

- ⇄ **Bidirectional Conversion**: Convert `.attheme` (Android) to `.tgios-theme` (iOS) and vice versa.
- 🔗 **Direct URL & Telegram Link Support**: Paste any `https://t.me/addtheme/<slug>` link or direct `.attheme` link.
- 🎨 **Live Chat Mockup & Preview**: Color swatches and real-time interactive preview showing action bar, message bubbles, wallpapers, and status bar.
- 🌈 **Gradient Wallpaper Support**: Extracts 4-color gradient wallpapers from Telegram cloud themes.
- 🖼️ **Wallpaper Extraction**: Automatically extracts embedded background images (JPEG, PNG, WEBP) from `.attheme` files.
- 🌗 **Luminance Auto-Detection**: Dynamically configures iOS `statusBarStyle` (`black` / `white`) and `keyboardColor` (`light` / `dark`).
- ⚡ **Deploy Anywhere**: Works as a static web app, on Vercel with Serverless Functions, or locally with Python.

---

## Quick Start (Local)

### Option 1: Open Directly
Open `index.html` in your favorite web browser.

### Option 2: Run Local Server (Zero-CORS)
To enable instant scraping of `t.me/addtheme/...` links locally without browser CORS restrictions:

```bash
# Windows
start_server.bat

# Or using Python
python server.py
```
Then visit `http://localhost:8080`.

---

## Deploy to Vercel

1. Push this repository to GitHub.
2. Go to [Vercel Dashboard](https://vercel.com) and click **"Add New Project"**.
3. Import your repository and click **Deploy**.
4. The frontend and serverless API functions (`/api/theme-info` and `/api/fetch`) will deploy automatically.

---

## Architecture

| Component | Description |
|---|---|
| `index.html` | Client-side application with parser, converter, and preview engine |
| `api/theme-info.js` | Vercel Serverless Function to fetch and scrape `t.me/addtheme/<slug>` metadata |
| `api/fetch.js` | Vercel Serverless Function for proxying remote theme files |
| `server.py` | Standalone Python standard library server for local development |
| `vercel.json` | Vercel deployment routes and clean URL configuration |

---

## License

MIT License
