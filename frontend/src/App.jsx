// Importing modules
import React, { useState } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

// Importing components
import Taskbar from './components/Taskbar';
import Sidenav from './components/Sidenav';
import ChatWindow from './components/ChatWindow';

// Importing context
import { TriggerContext } from './context/TriggerContext';

// Importing styles
import './App.css';

function App() {
  const [triggerResponse, setTriggerResponse] = useState([]);

  return (
    <div className="App">
      <TriggerContext.Provider value={{triggerResponse, setTriggerResponse}}>
        <BrowserRouter>
          <Taskbar />
          <div className="mainWrapper">
            <Sidenav />
            <Routes>
              <Route path='/:pdfchat' element={<ChatWindow />} />
            </Routes>
          </div>
        </BrowserRouter>
      </TriggerContext.Provider>
    </div>
  );
}

export default App;
