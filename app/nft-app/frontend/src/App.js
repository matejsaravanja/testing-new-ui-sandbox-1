import React from 'react';
import './App.css';
import NFTList from './components/NFTList';
import WalletConnection from './components/WalletConnection';

function App() {
  return (
    <div className="app">
      <div className="header">
        <h1>NFT Marketplace</h1>
        <WalletConnection />
      </div>
      <NFTList />
    </div>
  );
}

export default App;