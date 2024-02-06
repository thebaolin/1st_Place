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
    // Implement your logic to navigate to the next page (using Flask backend)
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
