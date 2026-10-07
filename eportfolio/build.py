"""Export the Flask ePortfolio site as plain static files.

Run from inside the eportfolio folder:  python build.py
Output goes to ./build  (index.html, dashboard/index.html, story/index.html,
portfolio/index.html and a copy of ./static).
"""
import shutil
from pathlib import Path

from app import app

OUT = Path("build")

# URL in the Flask app  ->  file written in the build folder
PAGES = {
    "/": "index.html",
    "/dashboard": "dashboard/index.html",
    "/story": "story/index.html",
    "/portfolio": "portfolio/index.html",
}

if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir()

client = app.test_client()
for url, target in PAGES.items():
    response = client.get(url)
    if response.status_code != 200:
        raise SystemExit(f"{url} returned {response.status_code}")
    path = OUT / target
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(response.data)
    print("wrote", path)

shutil.copytree("static", OUT / "static")
print("copied static/")
print("done -> build/")
