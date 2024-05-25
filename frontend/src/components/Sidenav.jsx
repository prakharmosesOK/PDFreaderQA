// Importing modules
import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { MdOutlineChat } from 'react-icons/md';
import { FaUserCircle, FaListUl } from 'react-icons/fa';
import { BsPlusCircle } from "react-icons/bs";

// Importing styles
import '../styles/Sidenav.css';

const Sidenav = ({ children }) => {
    const [isOpen, setIsOpen] = useState(true);

    const toggleNav = () => {
        setIsOpen(!isOpen);
    };

    return (
        <nav className={`Sidenav ${isOpen ? 'active' : ''}`}>
            <div className="nav-header">
                <button onClick={toggleNav}><FaListUl className='customIcon' /></button>
            </div>
            <nav className={ isOpen ? 'active' : 'hidden' }>
                <ul>
                    <li>
                        <Link to="#" className='newChat'>
                            <BsPlusCircle className='customIcon' />
                            <span className='chatRoom'>New Chat</span>
                        </Link>
                    </li>
                    <li>
                        <Link to="#">
                            <MdOutlineChat />
                            Chats
                        </Link>
                    </li>
                    <li>
                        <Link to="#">
                            <FaUserCircle />
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