from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from utils.scraper import scrape_products
from utils.pricing import apply_pricing
from utils.image_processor import process_images
from utils.ai_descriptions import generate_description
import pandas as pd
import os, zipfile, random

app = FastAPI()  # FastAPI object at top-level

@app.get("/")
def home():
    return {"status": "Backend running"}

@app.post("/generate-csv")
def generate_csv(url: str = Form(...), mode: str = Form(...)):
    # 1️⃣ Scrape products
    products = scrape_products(url)

    rows = []
    images_folder = "images"
    os.makedirs(images_folder, exist_ok=True)

    # 2️⃣ Process each product
    for idx, p in enumerate(products):
        base_price = p['price']
        cost, selling = apply_pricing(base_price, shipping=50, min_margin=100, max_margin=150)
        description = generate_description(p['title'])
        image_path = process_images(p['image_url'], images_folder, idx)

        rows.append({
            "Product Name": p['title'],
            "Category": "Home & Kitchen",
            "Selling Price": selling,
            "Cost Price": cost,
            "Weight (kg)": 0.5,
            "Length (cm)": 20,
            "Breadth (cm)": 15,
            "Height (cm)": 10,
            "Material": "Plastic",
            "Country of Origin": "India",
            "Description": description,
            "Image 1": image_path
        })

    # 3️⃣ Generate CSV
    df = pd.DataFrame(rows)
    csv_name = "meesho_products.csv"
    df.to_csv(csv_name, index=False)

    # 4️⃣ Zip CSV + images
    zip_name = "meesho_products.zip"
    with zipfile.ZipFile(zip_name, "w") as zipf:
        zipf.write(csv_name)
        for f in os.listdir(images_folder):
            zipf.write(os.path.join(images_folder, f))

    return FileResponse(zip_name, filename=zip_name)
