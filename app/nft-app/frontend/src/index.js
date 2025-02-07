import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import { WalletProvider, WalletAdapterNetwork } from '@solana/wallet-adapter-react';
import { PhantomWalletAdapter } from '@solana/wallet-adapter-wallets';
import { ConnectionProvider } from '@solana/wallet-adapter-react';

const network = WalletAdapterNetwork.Mainnet;
const wallets = [new PhantomWalletAdapter()];

ReactDOM.render(
  <React.StrictMode>
    <ConnectionProvider endpoint="https://api.mainnet-beta.solana.com">
      <WalletProvider wallets={wallets} autoConnect>
        <App />
      </WalletProvider>
    </ConnectionProvider>
  </React.StrictMode>,
  document.getElementById('root')
);