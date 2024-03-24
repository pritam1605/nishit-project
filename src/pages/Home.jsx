import React from "react";
import "./static/home.css";
// import { Link } from "react-router-dom";

export default function Home() {
  const currentUser = JSON.parse(localStorage.getItem("user"));
  console.log(currentUser);

  

//   const logout = () => {
//     localStorage.clear();
//   };

  return (
    <div className="topic">
      <div class="bgimg">
        <div class="abcd">
            <nav>
                <a href="/" class="efgh">Website</a>
                <ul>
                    <li class="subs"><a href="#quiz-container">Features</a></li>
                    <li class="subs" id="scroll-to"><a href="#about">About</a></li>
                    <li class="subs"><a href="/">Login</a></li>
                </ul>
            </nav> 
        </div>  
        <div class="navigation"></div>
        <div class="background">
            <div class="header">
                <div class="header-content">
                    <h1 class="h1">AI project</h1>
                    <p class="paragraph">Bohra website of recommendation engine</p>
                    <a href="#quiz-container" class="button w-button" id="scroll-to">Get Started</a>
                </div>
            </div>
        </div>
      </div>

      <div class="quiz-container" id="quiz-container">
        <div class="quiz-content">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Modi rem doloremque odio fugiat perspiciatis pariatur at ex. Iste eum, explicabo ipsa minus id nesciunt architecto dicta nisi quia itaque fugit!
        </div>
        <div class="quiz-start">
            <div class="quiz-buttons">
                <button class="ai">Artificial Intelligence</button>
                <button class="ds">Data Science</button>
                <button class="webdev">Web Development</button>
                <button class="ml"> Machine Learning</button>
            </div>
        </div>
      </div>



      <div class="about" id="about">
        <div class="container cc-center">
            <div class="h2-container cc-center">
                <h2 class="h2 cc-center">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci, iusto quaerat quas suscipit quibusdam temporibus? Nemo, fugit, itaque harum ratione quidem debitis autem voluptatem placeat est, quam accusamus voluptates! Architecto?</h2>
                <a href="/about" class="link">More About Us</a>
            </div>
        </div>
      </div>
    </div>
    
  );
}