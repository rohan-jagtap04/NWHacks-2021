import React from "react";
import './App.css';
import NavBar from './NavBar';
import Intro from './Intro';
import About from './About';
import webApp from './webApp';

function App() {
  return (
    <div>
      <NavBar />
      <Intro />
      <About />
      <webApp />
    </div>
  );
}

export default App;
