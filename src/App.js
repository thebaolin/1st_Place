// App.js

import React, { useState } from 'react';
import './App.css';

function App() {
  const [selectedOptions, setSelectedOptions] = useState([]);

  const handleOptionClick = (option) => {
    if (selectedOptions.includes(option)) {
      setSelectedOptions(selectedOptions.filter(item => item !== option));
    } else {
      setSelectedOptions([...selectedOptions, option]);
    }
  };

  const handleNextPage = () => {
    // Send selected options to the backend
    fetch('/current-location', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ selectedOptions })
    })
    .then(response => response.json())
    .then(data => {
      // Handle response from the backend, e.g., navigate to the next page
    })
    .catch(error => {
      console.error('Error:', error);
    });
  };

  return (
    <div className="app">
      <h1>Welcome to Restaurant This or That!</h1>
      <div className="options-container">
        <button className={`option ${selectedOptions.includes('Japanese') ? 'selected' : ''}`} onClick={() => handleOptionClick('Japanese')}>Japanese</button>
        <button className={`option ${selectedOptions.includes('Korean') ? 'selected' : ''}`} onClick={() => handleOptionClick('Korean')}>Korean</button>
        <button className={`option ${selectedOptions.includes('Fast Food') ? 'selected' : ''}`} onClick={() => handleOptionClick('Fast Food')}>Fast Food</button>
        {/* Add more options here */}
      </div>
      <button className="next-button" onClick={handleNextPage}>Next</button>
    </div>
  );
}

export default App;
