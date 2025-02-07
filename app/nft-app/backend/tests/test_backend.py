import unittest
import requests
import sqlite3

class TestBackend(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://localhost:5000"

    def test_purchase_nft(self):
        response = requests.post(f"{self.base_url}/purchase-nft", json={"user_wallet": "TEST_WALLET", "nft_id": "TEST_NFT"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("transaction_id", response.json())

    def tearDown(self):
        conn = sqlite3.connect("nft_database.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM nfts WHERE user_wallet = 'TEST_WALLET' AND nft_id = 'TEST_NFT'")
        conn.commit()
        conn.close()

if __name__ == "__main__":
    unittest.main()