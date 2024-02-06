import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const categories = ['Japanese', 'Korean', 'Fast Food', 'Italian', 'Mexican', 'Indian', 'Chinese'];
  const [selectedCategories, setSelectedCategories] = useState([]);

  const handleCategoryClick = (category) => {
    if (selectedCategories.includes(category)) {
      setSelectedCategories(selectedCategories.filter(item => item !== category));
    } else {
      setSelectedCategories([...selectedCategories, category]);
    }
  };

  useEffect(() => {
    const circles = document.querySelectorAll('.circle');

    circles.forEach((circle, index) => {
      const angle = (360 / circles.length) * index;
      const radius = 200;

      const x = Math.cos((angle * Math.PI) / 180) * radius;
      const y = Math.sin((angle * Math.PI) / 180) * radius;

      circle.style.left = `calc(50% + ${x}px)`;
      circle.style.top = `calc(50% + ${y}px)`;
    });
  }, [selectedCategories]);

  const handleSurpriseMeClick = () => {
    const randomIndex = Math.floor(Math.random() * categories.length);
    const randomCategory = categories[randomIndex];
    
    //if no category is selected, just select one randomly
    if (selectedCategories.length === 0) {
      setSelectedCategories([randomCategory]);
    } else {
      setSelectedCategories([...selectedCategories, randomCategory]);
    }
  };

  return (
    <div className="app">
      {/* render circles for each category */}
      {categories.map((category, index) => (
        <div
          key={index}
          className={`circle ${selectedCategories.includes(category) ? 'selected' : ''}`}
          onClick={() => handleCategoryClick(category)}
        >
          {category}
        </div>
      ))}
      
      {/*render surprise me circle */}
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
