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
    fetch('/api/data', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ selectedOptions })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); // Handle the response data
    })
    .catch(error => {
      console.error('Error:', error);
    });
  };

  return (
    <div className="app">
      <h1>This or That!</h1>
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