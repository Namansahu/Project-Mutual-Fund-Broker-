javascript
import React, { useState } from 'react';

function App() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [family, setFamily] = useState('');
    const [funds, setFunds] = useState([]);

    const register = async () => {
        const response = await fetch('http://localhost:8000/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password }),
        });
        const data = await response.json();
        console.log(data);
    };

    const fetchFunds = async () => {
        const response = await fetch('http://localhost:8000/funds', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ family }),
        });
        const data = await response.json();
        setFunds(data);
    }
    return (
        <div>
            <h1>Mutual Fund Broker</h1>
            <h2>Register</h2>
            <input type="email" onChange={(e) => setEmail(e.target.value)} placeholder="Email" />
            <input type="password" onChange={(e) => setPassword(e.target.value)} placeholder="Password" />
            <button onClick={register}>Register</button>

            <h2>Fetch Funds</h2>
            <input type="text" onChange={(e) => setFamily(e.target.value)} placeholder="Fund Family" />
            <button onClick={fetchFunds}>Fetch</button>

            <h3>Funds</h3>
            <ul>
                {funds.map((fund, index) => (
                    <li key={index}>{fund.scheme_name}</li>
                ))}
            </ul>
        </div>
    );
}






