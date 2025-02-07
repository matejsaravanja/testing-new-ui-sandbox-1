import svgwrite
import uuid
import json

def generate_nft():
    nft_id = str(uuid.uuid4())
    dwg = svgwrite.Drawing(f"../nft_images/{nft_id}.svg", size=(200, 200))
    dwg.add(dwg.rect(insert=(0, 0), size=(200, 200), fill="orange"))
    dwg.add(dwg.text("NFT", insert=(50, 100), font_size=40))
    dwg.save()

    # Generate metadata
    metadata = {
        "name": f"NFT {nft_id}",
        "description": f"A unique NFT with ID {nft_id}",
        "image": f"https://your-app.com/nft/{nft_id}.svg"
    }
    with open(f"../nft_images/{nft_id}.json", "w") as f:
        json.dump(metadata, f)

    return nft_id

if __name__ == "__main__":
    generate_nft()