import React, { useState, useEffect } from 'react';
import { useWallet } from '@solana/wallet-adapter-react';
import { Connection, PublicKey } from '@solana/web3.js';

const WalletConnection = () => {
    const { connect, disconnect, publicKey } = useWallet();
    const [balance, setBalance] = useState(null);
    const connection = new Connection("https://api.mainnet-beta.solana.com");

    const handleConnect = async () => {
        await connect();
        if (publicKey) {
            const balance = await connection.getBalance(publicKey);
            setBalance(balance);
        }
    };

    return (
        <div>
            {publicKey ? (
                <div>
                    <p>Wallet Address: {publicKey.toBase58()}</p>
                    <p>Balance: {balance} CRAFT</p>
                    <button onClick={disconnect}>Disconnect</button>
                </div>
            ) : (
                <button onClick={handleConnect}>Connect Wallet</button>
            )}
        </div>
    );
};

export default WalletConnection;