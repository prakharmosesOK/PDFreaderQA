// Imporring necessary modules
import React, { useRef, useState, useEffect, useContext } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { BsPlusCircle } from "react-icons/bs";
import { FaRegFile } from "react-icons/fa";
import axios from 'axios';

// Importing Context
import { TriggerContext } from '../context/TriggerContext';

// Importing styles
import '../styles/Taskbar.css';

function Taskbar() {
    const navigate = useNavigate();
    const location = useLocation();
    const { triggerResponse, setTriggerResponse } = useContext(TriggerContext);

    const inputFileRef = useRef(null);
    const [selectedFiles, setSelectedFiles] = useState([]);
    const [error, setError] = useState(null);
    const [pdfLink, setPdfLink] = useState('');
    const [loading, setLoading] = useState(false);
    const [uploadedFile, setUploadedFile] = useState(null);

    const handleButtonClick = () => {
        inputFileRef.current.click();
    };

    const handleFileChange = (event) => {
        setError(null);
        const newFiles = event.target.files;
        if (newFiles.length > 0) {
            const validFiles = [];
            for (const file of newFiles) {
                if (file.type === 'application/pdf') {
                    validFiles.push(file);
                }
            }
            setSelectedFiles(Array.from(validFiles));
            setError(null);
        } else {
            setSelectedFiles([]);
            setError('Please select PDF files only!')
        }
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        setError(null);
        setLoading(true);

        try {
            const formData = new FormData();
            if (selectedFiles.length > 0) {
                selectedFiles.forEach(file => {
                    formData.append('files', file);
                });
            }

            const response = await axios.post('http://127.0.0.1:8000/upload_pdf', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })

            if (response.status === 200 || response.status === 201) {
                const newChat = response.data.output;
                navigate(`/${newChat[1]}`)
            }
        } catch (error) {
            setError('Failed to upload PDF files');
        } finally {
            setLoading(false);
            setSelectedFiles([]);
            setPdfLink('');
        }
    }

    useEffect(() => {
        setError(null);
        if (location.pathname === '/') {
            setUploadedFile(null);
            const fetchInfoToUpdate = async () => {
                try {
                    const response = await axios.get('http://127.0.0.1:8000/chat_info');
                    const chats = response.data.output;
                    setTriggerResponse(chats);
                } catch (error) {
                    setError(`Failed to fetch chat info: ${error.message}`);
                }
            }
            
            fetchInfoToUpdate();
        } else {
            const fetchChatInfo = async () => {
                const route = location.pathname.toString().split('/')[1];
                try {
                    const response = await axios.get('http://127.0.0.1:8000/chat_info');
                    const chats = response.data.output;
                    const routeName = chats.find(chat => Number(chat[0]) === Number(route))[1];
                    setUploadedFile(routeName);
                    setTriggerResponse(chats);
                } catch (error) {
                    setError(`Failed to fetch chat info: ${error.message}`)
                }
            }
            fetchChatInfo();
        }
    }, [location.pathname, setTriggerResponse]);

    return (
        <header className="Taskbar">
            <img src="./aiplanetLogoFull.png" alt="AI Planet" />

            <div className="inputParams">
                {uploadedFile && <div className='uploaded-file'>
                    <FaRegFile />
                    <span>{uploadedFile}</span>
                </div>}
                <form onSubmit={handleSubmit}>
                    <input
                        type="text"
                        placeholder='Enter the PDF link here'
                        value={pdfLink}
                        multiple
                        onChange={(event) => setPdfLink(event.target.value)}
                        disabled={uploadedFile}
                    />
                </form>
                <button onClick={handleButtonClick} className={selectedFiles.length > 0 ? 'containPdf' : ''} disabled={uploadedFile}>
                    <BsPlusCircle className='custom-icon' />
                    Upload PDF
                </button>
                <input
                    type="file"
                    id="fileInput"
                    ref={inputFileRef}
                    className='hidden'
                    accept=".pdf"
                    multiple
                    onChange={handleFileChange}
                />
                <button
                    onClick={handleSubmit}
                    disabled={loading || uploadedFile}
                >{loading ? "Loading..." : "Submit"}</button>
            </div>

            {error && <p className='error'>{error}</p>}
        </header>
    )
}

export default Taskbar;