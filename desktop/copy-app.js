// Copies the game files next to main.js so the installer can bundle them.
const fs = require("fs"), path = require("path");
const src = path.join(__dirname, ".."), dst = path.join(__dirname, "app");
fs.rmSync(dst, { recursive: true, force: true }); fs.mkdirSync(dst, { recursive: true });
for (const f of fs.readdirSync(src)) {
  if (["desktop", "serve.py", "README.txt", "sw.js"].includes(f) || /^Play /.test(f)) continue;
  fs.cpSync(path.join(src, f), path.join(dst, f), { recursive: true });
}
// The desktop app needs React and Three.js bundled; download them if vendor/ is empty.
const https = require("https");
const libs = [["three", "vendor/three.min.js", "https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"], ["react", "vendor/react.production.min.js", "https://cdnjs.cloudflare.com/ajax/libs/react/18.3.1/umd/react.production.min.js"], ["react-dom", "vendor/react-dom.production.min.js", "https://cdnjs.cloudflare.com/ajax/libs/react-dom/18.3.1/umd/react-dom.production.min.js"]];
fs.mkdirSync(path.join(dst, "vendor"), { recursive: true });
const get = (url, to) => new Promise((ok, no) => https.get(url, (r) => {
  if (r.statusCode !== 200) return no(new Error(url + " -> " + r.statusCode));
  const out = fs.createWriteStream(to); r.pipe(out); out.on("finish", () => out.close(ok));
}).on("error", no));
(async () => { for (const [, local, url] of libs) { const to = path.join(dst, local); if (!fs.existsSync(to) || fs.statSync(to).size < 1000) { console.log("downloading", url); await get(url, to); } } })().catch((e) => { console.error(e); process.exit(1); });
