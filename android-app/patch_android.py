"""Tweaks the freshly generated Capacitor Android project: icon, fullscreen, version. Never fails the build."""
import os, re, subprocess, shutil, glob

A = "android/app/src/main"
run = os.environ.get("RUN_NUMBER", "1")
vname = os.environ.get("VERSION_NAME", "1.0")

def edit(path, fn):
    try:
        s = open(path, encoding="utf-8").read()
        t = fn(s)
        if t != s:
            open(path, "w", encoding="utf-8").write(t); print("patched", path)
        else:
            print("no change", path)
    except Exception as e:
        print("could not patch", path, e)

# version: each build gets a higher versionCode so it installs over the last one
edit("android/app/build.gradle", lambda s: re.sub(r'versionName\s+"[^"]*"', 'versionName "%s.%s"' % (vname, run), re.sub(r"versionCode\s+\d+", "versionCode %s" % run, s)))

# fullscreen, drawn under the camera cut-out
def fs(s):
    if "windowFullscreen" in s: return s
    return re.sub(r'(<style name="AppTheme\.NoActionBar"[^>]*>)', r'\1\n        <item name="android:windowFullscreen">true</item>\n        <item name="android:windowLayoutInDisplayCutoutMode">shortEdges</item>', s, count=1)
edit(A + "/res/values/styles.xml", fs)

# dark launch background
edit(A + "/res/values/ic_launcher_background.xml", lambda s: re.sub(r"#[0-9A-Fa-f]{6}", "#08161C", s))

# launcher icons from the game's own icon
conv = shutil.which("magick") or shutil.which("convert")
if conv:
    sizes = {"mdpi": (48, 108), "hdpi": (72, 162), "xhdpi": (96, 216), "xxhdpi": (144, 324), "xxxhdpi": (192, 432)}
    for d, (ic, fg) in sizes.items():
        out = A + "/res/mipmap-" + d
        if not os.path.isdir(out): continue
        for name, src, px in (("ic_launcher.png", "www/icon-512.png", ic), ("ic_launcher_round.png", "www/icon-512.png", ic), ("ic_launcher_foreground.png", "www/icon-maskable-512.png", fg)):
            try:
                subprocess.run([conv, src, "-resize", "%dx%d" % (px, px), os.path.join(out, name)], check=True)
            except Exception as e:
                print("icon failed", d, name, e)
    print("icons done")
else:
    print("ImageMagick not found; keeping the default icons")
