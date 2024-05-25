// Importing modules
import React from 'react';
// import { BrowserRouter, Routes, Route } from 'react-router-dom';

// Importing components
import Taskbar from './components/Taskbar';
// import Sidenav from './components/Sidenav';

// Importing styles
import './App.css';

function App() {
  return (
    <div className="App">
      <Taskbar />
      {/* <Sidenav /> */}
    </div>
  );
}

export default App;
