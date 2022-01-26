import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [text, setText] = useState("Fetching...");

  useEffect(() => {
    // Update the document title using the browser API
    fetch(`/api/v1/example/`)
            .then((res) => res.json())
            .then((json) => {
                setText(json.text);
            })
  });

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          {text}
        </p>
      </header>
    </div>
  );
}

export default App;
