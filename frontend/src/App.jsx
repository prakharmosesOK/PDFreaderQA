// Importing modules
import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

// Importing components
import Taskbar from './components/Taskbar';
import Sidenav from './components/Sidenav';
import ChatWindow from './components/ChatWindow';

// Importing styles
import './App.css';

function App() {
  return (
    <div className="App">
      <Taskbar />
      <BrowserRouter>
        <div className="mainWrapper">
          <Sidenav />
          <Routes>
            <Route path='/:pdfchat' element={<ChatWindow />} />
          </Routes>
        </div>
      </BrowserRouter>
    </div>
  );
}

export default App;
