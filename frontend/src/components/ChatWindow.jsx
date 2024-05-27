import React, { useState, useRef, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { LuSendHorizonal } from "react-icons/lu";
import axios from 'axios';

// Importing styles
import '../styles/ChatWindow.css';

// HumanMessage.jsx
const HumanMessage = ({ message }) => (
    <div className='oneChatRow'>
        <img src="./man.png" alt="Human" />
        {message.question}
    </div>
);

// AIMessage.jsx
const AIMessage = ({ message }) => (
    <div className='oneChatRow'>
        <img src="./aiplanetLogo.png" alt="AI" />
        {message.answer}
    </div>
);

const ChatWindow = () => {
    const { pdfchat } = useParams();
    const [messages, setMessages] = useState([]); // Stores conversation history for this PDF
    const [humanText, setHumanText] = useState('');
    const userInputRef = useRef(null); // Ref for user input field
    const [error, setError] = useState(null); // Error state
    const [loading, setLoading] = useState(false); // Loading state
    const chatListRef = useRef(null); // Ref for the chat list container

    const handleUserInput = async (event) => {
        event.preventDefault(); // Prevent default form submission behavior
        scrollToBottom(); // Scroll to the bottom
        setMessages([...messages, { question: humanText }])
        const humamMessage = humanText;
        setHumanText(''); // Clearing the input field

        try {
            setLoading(true);
            const response = await axios.post('http://127.0.0.1:8000/chat', {
                route: pdfchat,
                question: humanText
            });
            const aiResponse = response.data.output;
            setMessages([...messages, { question: humamMessage, answer: aiResponse }]);
        } catch (error) {
            setError(error.message);
        } finally {
            setLoading(false);
        }

        userInputRef.current.value = ''; // Clear input field
    };

    const scrollToBottom = () => {
        if (chatListRef.current) {
            chatListRef.current.scrollTop = chatListRef.current.scrollHeight; // Scroll to the bottom
        }
    };


    useEffect(() => {
        const fetchMessages = async () => {
            try {
                setLoading(true);
                const response = await axios.post('http://127.0.0.1:8000/chat_hist', {
                    route: pdfchat
                });
                const conversation = response.data.output;
                setMessages(conversation);
            } catch (error) {
                setError(error.message);
            } finally {
                setLoading(false);
            }
        }

        fetchMessages();
        scrollToBottom();
    }, [pdfchat])

    return (
        <div className={`ChatWindow`}>
            {error && <p>{error}</p>}

            <ul ref={chatListRef}> {/* Wrap the list in a ref */}
                {messages.map((message, idx) => (
                    message.answer ? (
                        <li>
                            <HumanMessage key={idx} message={message} />
                            <AIMessage key={message.id} message={message} />
                        </li>
                    ) : (
                        <li>
                            <HumanMessage key={message.id} message={message} />
                        </li>
                    )
                ))}
            </ul>

            {loading && <p className='loadingUI'>Loading...</p>}

            <form onSubmit={handleUserInput}>
                <input
                    ref={userInputRef}
                    type="text"
                    placeholder="Send a message..."
                    value={humanText}
                    onChange={(event) => setHumanText(event.target.value)}
                />
                <button>
                    <LuSendHorizonal />
                </button>
            </form>
        </div>
    );
};

export default ChatWindow;
