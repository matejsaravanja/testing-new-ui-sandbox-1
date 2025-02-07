import React from 'react';

const NFTCard = ({ nft, onPurchase }) => {
  return (
    <div className="nft-card">
      <div className="nft-image-placeholder"></div>
      <h3>NFT #{nft.id}</h3>
      <button onClick={() => onPurchase(nft.id)}>Purchase for 100 CRAFT</button>
    </div>
  );
};

export default NFTCard;