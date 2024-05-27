// Importing modules
import React, { useContext, useState, useEffect } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import { FaListUl } from 'react-icons/fa';
import { BsPlusCircle } from "react-icons/bs";
import { FaRegMessage } from "react-icons/fa6";
import { MdDelete } from "react-icons/md";
import axios from 'axios';

// Importing Context
import { TriggerContext } from '../context/TriggerContext';

// Importing styles
import '../styles/Sidenav.css';

const Sidenav = ({ children }) => {
    const location = useLocation();
    const navigate = useNavigate();
    const [isOpen, setIsOpen] = useState(true);
    const [chatRooms, setChatRooms] = useState([]);
    const [error, setError] = useState(null);
    const { triggerResponse } = useContext(TriggerContext);

    const toggleNav = () => {
        setIsOpen(!isOpen);
    };

    const activeClass = (pathname) => {
        if (pathname === location.pathname.toString()) {
            return 'activated';
        } else {
            return 'deactivated';
        }
    }

    const handleDelete = async (event) => {
        event.preventDefault();
        try {
            const route = location.pathname.toString().split('/')[1];
            const response = await axios.delete(`http://127.0.0.1:8000/delete_chat/${route}`);

            if (response.status === 200) {
                navigate('/');
                setChatRooms(chatRooms.filter((chatRoom) => Number(chatRoom[1]) !== Number(route)));
            } else {
                setError('Failed to delete chat');
            }
        } catch (error) {
            setError(error.message);
        }
    }

    useEffect(() => {
        let chats = [];
        if (triggerResponse) {
            triggerResponse.forEach((chat) => {
                chats.push([chat[1], chat[0]]);
            })
        }
        setChatRooms(chats);
    }, [triggerResponse]);

    return (
        <nav className={`Sidenav ${isOpen ? 'active' : ''}`}>
            <div className="nav-header">
                <button onClick={toggleNav}><FaListUl className='customIcon' /></button>
            </div>
            <nav className={isOpen ? 'active' : 'hidden'}>
                <ul>
                    <li>
                        <Link to="/" className={`newChat ${activeClass('/')}`}>
                            <BsPlusCircle className='customIcon' />
                            <span className='chatRoom'>New Chat</span>
                        </Link>
                    </li>
                    {chatRooms.map((chatRoom, index) => {
                        return (
                            <li key={index} className={activeClass('/' + chatRoom[1])}>
                                <Link to={`/${chatRoom[1]}`} className='chatBoxContainer'>
                                    <FaRegMessage />
                                    <span className='chatRooms'>{chatRoom[0]}</span>
                                </Link>
                                <button onClick={handleDelete}><MdDelete /></button>
                            </li>
                        );
                    })}
                </ul>

                {error && <p>{error}</p>}
            </nav>
            {children}
        </nav>
    );
};

export default Sidenav;