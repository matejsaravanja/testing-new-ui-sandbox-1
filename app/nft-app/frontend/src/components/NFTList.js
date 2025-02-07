import React, { useEffect, useState } from 'react';
import NFTCard from './NFTCard';
import { useWallet } from '@solana/wallet-adapter-react';

const NFTList = () => {
    const [nfts, setNfts] = useState([]);
    const { publicKey } = useWallet();

    useEffect(() => {
        // Fetch available NFTs (mock data)
        setNfts([{ id: "1" }, { id: "2" }]);
    }, []);

    const purchaseNFT = async (nftId) => {
        if (!publicKey) return alert("Connect your wallet first!");
        const response = await fetch('http://localhost:5000/purchase-nft', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_wallet: publicKey.toBase58(), nft_id: nftId })
        });
        const data = await response.json();
        alert(`Purchased NFT ${data.nft_id}, Transaction ID: ${data.transaction_id}`);
    };

    return (
        <div>
            <h2>Available NFTs</h2>
            {nfts.map(nft => (
                <NFTCard key={nft.id} nft={nft} onPurchase={purchaseNFT} />
            ))}
        </div>
    );
};

export default NFTList;