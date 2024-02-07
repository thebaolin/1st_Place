import React, { useState, useEffect } from 'react';
import './App.css';

function App() {


  const categories = ['Japanese', 'Korean', 'Fast Food', 'Italian', 'Mexican', 'Indian', 'Chinese'];
  const [selectedOptions, setSelectedOptions] = useState([]);

  const handleCategoryClick = (category) => {
    const formattedCategory = `${category.toLowerCase().replace(/\s+/g, '_')}_restaurant`;
    
    if (selectedOptions.includes(formattedCategory)) {
      setSelectedOptions(selectedOptions.filter(item => item !== formattedCategory));
    } else {
      setSelectedOptions([...selectedOptions, formattedCategory]);
    }
  };

  useEffect(() => {
    console.log(selectedOptions); // print the list of selected options
    const circles = document.querySelectorAll('.circle');

    circles.forEach((circle, index) => {
      const angle = (360 / circles.length) * index;
      const radius = 200;

      const x = Math.cos((angle * Math.PI) / 180) * radius;
      const y = Math.sin((angle * Math.PI) / 180) * radius;

      circle.style.left = `calc(50% + ${x}px)`;
      circle.style.top = `calc(50% + ${y}px)`;
    });
  }, [selectedOptions]);

  const handleSurpriseMeClick = () => {
    const randomIndex = Math.floor(Math.random() * categories.length);
    const randomCategory = categories[randomIndex];
    
    const formattedCategory = `${randomCategory.toLowerCase().replace(/\s+/g, '_')}_restaurant`;
    
    if (selectedOptions.length === 0) {
      setSelectedOptions([formattedCategory]);
    } else {
      setSelectedOptions([...selectedOptions, formattedCategory]);
    }
  };

  return (
    <div className="app">
      {/* render circles for each category */}
      {categories.map((category, index) => (
        <div
          key={index}
          className={`circle ${selectedOptions.includes(`${category.toLowerCase().replace(/\s+/g, '_')}_restaurant`) ? 'selected' : ''}`}
          onClick={() => handleCategoryClick(category)}
        >
          {category}
        </div>
      ))}
      
      {/* render the "Surprise Me" circle */}
      <div
        className="circle surprise-circle"
        onClick={handleSurpriseMeClick}
      >
        Surprise Me
      </div>
    </div>
  );
}

export default App;
