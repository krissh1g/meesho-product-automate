import requests, os
from removebg import RemoveBg

RMBG_API_KEY = "YOUR_REMOVE_BG_API_KEY"

def process_images(image_url, folder, idx):
    # Download image
    img_data = requests.get(image_url).content
    temp_path = os.path.join(folder, f"temp_{idx}.png")
    with open(temp_path, "wb") as f:
        f.write(img_data)

    # Remove background
    rmbg = RemoveBg(RMBG_API_KEY, "error.log")
    rmbg.remove_background_from_img_file(temp_path)

    # Save final
    output_path = os.path.join(folder, f"product_{idx}.png")
    os.rename(temp_path, output_path)
    return output_path
