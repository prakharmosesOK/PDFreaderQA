// Imporring necessary modules
import React, { useRef, useState } from 'react';
import { BsPlusCircle } from "react-icons/bs";

// Importing styles
import '../styles/Taskbar.css';

function Taskbar() {
    const inputFileRef = useRef(null);
    const [pdfLink, setPdfLink] = useState('');

    const handleButtonClick = () => {
        inputFileRef.current.click();
    };

    const handleFileChange = (event) => {
        const selectedFile = event.target.files[0];
        if (selectedFile && selectedFile.type === 'application/pdf') {
            // Handle the selected PDF file here (e.g., upload or process it)
            console.log('Selected PDF file:', selectedFile.name);
        } else {
            console.log('Please select a valid PDF file.');
        }
    };

    const handlePdfLink = (event) => {
        event.preventDefault();

        console.log(`PDF link: ${pdfLink}`)
    }

    return (
        <header className="Taskbar">
            <img src="./aiplanetLogoFull.png" alt="AI Planet" />

            <div className="inputParams">
                <form onSubmit={handlePdfLink}>
                    <input
                        type="text"
                        placeholder='Enter the PDF link here'
                        value={pdfLink}
                        onChange={(event) => setPdfLink(event.target.value)}
                    />
                </form>
                <button onClick={handleButtonClick}>
                    <BsPlusCircle className='custom-icon' />
                    Upload PDF
                </button>
            </div>
            <input
                type="file"
                id="fileInput"
                ref={inputFileRef}
                className='hidden'
                accept=".pdf"
                onChange={handleFileChange}
            />
        </header>
    )
}

export default Taskbar;