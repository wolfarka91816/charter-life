Charter Life Demo  -  app package  (build 0.34, demo)

THREE WAYS TO RUN IT
====================

1. PHONE OR TABLET  (best for you: installs like a real app)
   Put this whole folder on any web host that uses https. The easiest:
     - Netlify Drop:  go to app.netlify.com/drop and drag this folder onto the page. You get a link.
       (Cloudflare Pages and GitHub Pages work the same way.)
   Then open that link on the phone:
     - Android (Chrome):  menu (three dots) > Install app  (or "Add to Home screen")
     - iPhone / iPad (Safari):  Share button > Add to Home Screen
   It opens fullscreen with its own icon. The first launch needs internet; after that it works offline.
   To update it later: run build.py again and drag the new folder onto the same site. The app picks up the new version the next time it is opened online.

2. COMPUTER, NO INSTALL
   Windows: double-click  "Play Charter Life Demo.bat"
   Mac:     double-click  "Play Charter Life Demo.command"   (first time: right-click > Open)
   Linux:   python3 serve.py
   Needs Python 3 (already on Mac and Linux; free from python.org for Windows).
   It starts a small local server, downloads the game libraries once, and opens your browser.
   In Chrome or Edge you can then use the install icon in the address bar to make it a desktop app.

3. REAL DESKTOP APP / INSTALLER (.exe, .dmg, AppImage)
   Needs Node.js (nodejs.org).  In the desktop/ folder:
     npm install
     npm start        (runs it in its own window; F11 toggles fullscreen)
     npm run dist     (builds an installer into desktop/dist)

SAVES
   The game saves inside the browser or app that runs it. The phone app, the browser on a computer and the desktop app each have their own save.
   Dev, standard and demo builds each use a different save slot.

The game libraries (React 18.3.1, Three.js r128) are not bundled in this package, they are fetched once and cached. Option 2 and 3 download them into vendor/.
