// textbook/src/components/FloatingChatButton.js
import React, { useState } from 'react';
import ChatInterface from './ChatInterface';
import styles from './FloatingChatButton.module.css';

const FloatingChatButton = () => {
  const [isChatOpen, setIsChatOpen] = useState(false);

  const toggleChat = () => {
    setIsChatOpen(!isChatOpen);
  };

  return (
    <div className={styles['floating-chat-container']}>
      {isChatOpen && (
        <div className={styles['chat-window']}>
          <div className={styles['chat-header']}>
            <h3>Textbook Assistant</h3>
            <button 
              className={styles['close-button']} 
              onClick={toggleChat}
              aria-label="Close chat"
            >
              ×
            </button>
          </div>
          <div className={styles['chat-body']}>
            <ChatInterface />
          </div>
        </div>
      )}
      <button
        className={`${styles['floating-button']} ${isChatOpen ? styles['open'] : ''}`}
        onClick={toggleChat}
        aria-label={isChatOpen ? "Close chat" : "Open chat"}
      >
        {isChatOpen ? (
          <span className={styles['close-icon']}>×</span>
        ) : (
          <svg 
            xmlns="http://www.w3.org/2000/svg" 
            width="24" 
            height="24" 
            viewBox="0 0 24 24" 
            fill="none" 
            stroke="currentColor" 
            strokeWidth="2" 
            strokeLinecap="round" 
            strokeLinejoin="round"
            className={styles['chat-icon']}
          >
            <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
          </svg>
        )}
      </button>
    </div>
  );
};

export default FloatingChatButton;