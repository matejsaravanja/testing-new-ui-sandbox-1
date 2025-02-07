from flask import Flask, request, jsonify
from flask_cors import CORS
from solana_integration import process_payment
import sqlite3
import models

app = Flask(__name__)
CORS(app)
models.init_db()

@app.route("/purchase-nft", methods=["POST"])
def purchase_nft():
    data = request.json
    user_wallet = data["user_wallet"]
    nft_id = data["nft_id"]

    # Process payment of 100 CRAFT
    transaction_id = process_payment(user_wallet, "YOUR_WALLET_ADDRESS", 100)
    
    # Save NFT ownership to database
    conn = sqlite3.connect("nft_database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO nfts (user_wallet, nft_id) VALUES (?, ?)", (user_wallet, nft_id))
    conn.commit()
    conn.close()

    return jsonify({"transaction_id": transaction_id, "nft_id": nft_id})

@app.route("/get-nft", methods=["GET"])
def get_nft():
    nft_id = request.args.get("nft_id")
    conn = sqlite3.connect("nft_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM nfts WHERE nft_id = ?", (nft_id,))
    nft = cursor.fetchone()
    conn.close()
    if nft:
        return jsonify({
            "nft_id": nft[2],
            "web": f"https://your-app.com/nft/{nft[2]}",
            "email": f"nft-{nft[2]}@your-app.com",
            "svg": f"https://your-app.com/nft/{nft[2]}.svg"
        })
    else:
        return jsonify({"error": "NFT not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)