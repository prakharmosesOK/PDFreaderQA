// Importing modules
import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { FaListUl } from 'react-icons/fa';
import { BsPlusCircle } from "react-icons/bs";
import { FaRegMessage } from "react-icons/fa6";

// Importing styles
import '../styles/Sidenav.css';

const Sidenav = ({ children }) => {
    const location = useLocation();
    const [isOpen, setIsOpen] = useState(true);

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
                    <li>
                        <Link to="/963852" className={activeClass('/963852')}>
                            <FaRegMessage />
                            Chats
                        </Link>
                    </li>
                    <li>
                        <Link to="/785369" className={activeClass('/785369')}>
                            <FaRegMessage />
                            Profile
                        </Link>
                    </li>
                </ul>
            </nav>
            {children}
        </nav>
    );
};

export default Sidenav;