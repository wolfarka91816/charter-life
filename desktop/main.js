const { app, BrowserWindow, globalShortcut, Menu } = require("electron");
const path = require("path");
let win;
function create() {
  Menu.setApplicationMenu(null);
  win = new BrowserWindow({ width: 1280, height: 800, backgroundColor: "#08161c", title: "Charter Life Demo", icon: path.join(__dirname, "app", "icon-512.png"), autoHideMenuBar: true, webPreferences: { backgroundThrottling: false } });
  win.loadFile(path.join(__dirname, "app", "index.html"));
  win.on("closed", () => { win = null; });
}
app.whenReady().then(() => {
  create();
  globalShortcut.register("F11", () => win && win.setFullScreen(!win.isFullScreen()));
  globalShortcut.register("CommandOrControl+Shift+I", () => win && win.webContents.toggleDevTools());
});
app.on("window-all-closed", () => app.quit());
