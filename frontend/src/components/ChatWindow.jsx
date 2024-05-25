import React, { useState, useRef } from 'react';
import { LuSendHorizonal } from "react-icons/lu";

// Importing styles
import '../styles/ChatWindow.css';

const ChatWindow = ({ pdfId = () => { }, onMessageSend = () => { } }) => {
    const [messages, setMessages] = useState([]); // Stores conversation history for this PDF
    const userInputRef = useRef(null); // Ref for user input field

    const handleUserInput = (event) => {
        const message = event.target.value;
        setMessages([...messages, { user: true, text: message }]); // Add user message
        userInputRef.current.value = ''; // Clear input field
        onMessageSend(pdfId, message); // Send message with PDF ID
    };

    // const handleAIResponse = (response) => {
    //     setMessages([...messages, { user: false, text: response }]); // Add AI response
    // };

    return (
        <div className={`ChatWindow chat-window-${pdfId}`}>
            <ul>
                {messages.map((message, index) => (
                    <li key={index} className={message.user ? 'user-message' : 'ai-message'}>
                        {message.text}
                    </li>
                ))}
            </ul>
            
            <form onSubmit={handleUserInput}>
                <input
                    ref={userInputRef}
                    type="text"
                    placeholder="Send a message..."
                />
                <button>
                    <LuSendHorizonal />
                </button>
            </form>
        </div>
    );
};

export default ChatWindow;
