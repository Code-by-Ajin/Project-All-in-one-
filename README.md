# 🚀 Project All-in-One (`OmniUtils`)

> **"Simplicity is the ultimate sophistication."**

**Project All-in-One (OmniUtils)** is a modern, privacy-first web platform that unifies essential everyday micro-utilities—such as QR code engines, file manipulators, cryptography, and image processors—into a single, high-performance, ad-free dashboard.

Unlike traditional web converters that rely on heavy cloud servers, **OmniUtils processes everything directly inside your web browser**. Your files, images, and text never leave your local device, ensuring lightning-fast execution and absolute data privacy.

---

## 🌟 Key Features

* **🔒 Absolute Privacy & Local Processing:** 100% client-side computation. Zero cloud uploads, zero processing queues, and zero tracking.
* **⚡ Lightning Fast (SPA Architecture):** Built as a single-page application with lightweight, modular scripts.
* **🎨 Modern UI & Dual Theme:** Default sleek dark mode with high-contrast light mode overrides, glassmorphism navigation, and responsive card layouts.
* **🔍 Instant Search:** Live search filter to find tools instantaneously.
* **📡 WebRTC P2P Data Channels:** Direct browser-to-browser encrypted transfers for sharing larger files safely.

---

## 🛠️ The 5 Core Utilities

| Tool | Processing Engine | Functionality |
| :--- | :--- | :--- |
| **📱 QR Code Engine** | `qrcode.js` / `jsQR` | Generate, customize, and scan QR codes directly from text, links, or live webcam feeds. |
| **📻 Morse Code Hub** | Native JavaScript | Instant bidirectional text-to-Morse translation with real-time Web Audio API sound playback. |
| **👁️ Stegano Crypt** | HTML5 Canvas LSB | Encrypt and hide private text messages invisibly inside image pixel buffers offline. |
| **📄 PDF Transformer** | `pdf-lib.js` | Merge, split, rotate, and reorder PDF documents locally inside the browser memory. |
| **🖼️ Image Optimizer** | Canvas API / Micro-AI | Crop, resize, compress, and perform AI-driven background removal via local browser models (`Transformers.js`). |

---

## 🏗️ Project Architecture & Folder Structure

To ensure scalability and keep the codebase clean, tools are isolated into dedicated modular subdirectories:

```text
omniutils-app/
├── index.html                 # Main dashboard UI shell
├── favicon.ico                # Site tab icon
├── assets/                    # Core static visual assets
│   ├── css/
│   │   └── global.css         # Fallback custom layout styles & keyframes
│   └── images/
│       └── logo.png           # System logo asset
│
└── src/                       # Client Application Modules
    ├── router.js              # Single-page view switcher
    ├── core.js                # Global logic (theme toggle, live search)
    │
    └── tools/                 # Unified tool functional folders
        ├── qr-engine/         # QR Generator & Scanner
        ├── morse-hub/          # Text-to-Morse & Audio Playback
        ├── stegano-crypt/     # LSB Image Cryptography
        ├── pdf-transformer/   # Client-side PDF Merger/Splitter
        └── image-optimizer/   # Canvas Compressor & Background Remover
