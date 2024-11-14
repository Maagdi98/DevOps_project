// frontend/src/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';  // Optional: If you have a CSS file to style the app
import App from './app';

ReactDOM.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>,
    document.getElementById('root')
);
