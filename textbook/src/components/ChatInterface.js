import React, { useState, useRef, useEffect } from 'react';
import { useColorMode } from '@docusaurus/theme-common';
import styles from './ChatInterface.module.css';

// Define the ChatInterface component
const ChatInterface = ({ sessionId }) => {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [selectedText, setSelectedText] = useState('');
  const messagesEndRef = useRef(null);
  const textareaRef = useRef(null);
  
  const { colorMode } = useColorMode();
  
  // Scroll to bottom of messages
  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  // Get selected text when user selects text on the page
  useEffect(() => {
    const handleSelection = () => {
      const selectedText = window.getSelection().toString().trim();
      if (selectedText) {
        setSelectedText(selectedText);
      }
    };

    document.addEventListener('mouseup', handleSelection);
    return () => {
      document.removeEventListener('mouseup', handleSelection);
    };
  }, []);

  // Preload chat API endpoint to establish connection early
  useEffect(() => {
    // Simple preload to warm up the connection
    if (typeof window !== 'undefined') {
      const preloadController = new AbortController();

      // Use a minimal endpoint to preload the connection
      fetch('/api/v1/health', {
        signal: preloadController.signal,
        method: 'GET',
        cache: 'force-cache'
      }).catch((error) => {
        // Silently ignore preload errors
        console.debug('Connection preload failed (not critical):', error);
      });

      // Cleanup function
      return () => {
        preloadController.abort();
      };
    }
  }, []);
  
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!inputValue.trim() || isLoading) return;
    
    // Add user message to the chat
    const userMessage = {
      id: Date.now(),
      text: inputValue,
      sender: 'user',
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    };
    
    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);
    
    try {
      // Prepare context with selected text if available
      const context = selectedText ? { selectedText, chapterId: null } : null;
      
      // Call the backend API
      const response = await fetch('/api/v1/chat/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          question: inputValue,
          session_id: sessionId || 'default-session',
          context: context
        }),
      });
      
      if (!response.ok) {
        throw new Error(`Server error: ${response.status}`);
      }
      
      const data = await response.json();
      
      // Add AI response to the chat
      const aiMessage = {
        id: data.id,
        text: data.answer,
        sender: 'ai',
        sources: data.sources,
        confidence: data.confidence,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      };
      
      setMessages(prev => [...prev, aiMessage]);
    } catch (error) {
      console.error('Error sending message:', error);
      
      // Add error message to the chat
      const errorMessage = {
        id: Date.now(),
        text: 'Sorry, I encountered an error processing your question. Please try again.',
        sender: 'error',
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      };
      
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };
  
  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  };
  
  // Function to provide feedback on a response
  const submitFeedback = async (responseId, rating) => {
    try {
      await fetch('/api/v1/chat/feedback', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          responseId: responseId,
          rating: rating,
        }),
      });
    } catch (error) {
      console.error('Error submitting feedback:', error);
    }
  };
  
  // Render message with proper formatting
  const renderMessage = (message) => {
    if (message.sender === 'ai') {
      return (
        <div className={styles['ai-message-content']}>
          <div className={styles['ai-answer']}>{message.text}</div>

          {message.sources && message.sources.length > 0 && (
            <div className={styles['sources-section']}>
              <strong>Sources:</strong>
              <ul className={styles['sources-list']}>
                {message.sources.map((source, idx) => (
                  <li key={idx}>
                    <a href={source.url} target="_blank" rel="noopener noreferrer">
                      {source.chapter}
                    </a>
                  </li>
                ))}
              </ul>
            </div>
          )}

          <div className={styles['feedback-section']}>
            <small>Was this helpful?
              <button
                onClick={() => submitFeedback(message.id, 5)}
                className={`${styles['feedback-btn']} ${styles['positive']}`}
                title="Helpful"
              >
                👍
              </button>
              <button
                onClick={() => submitFeedback(message.id, 1)}
                className={`${styles['feedback-btn']} ${styles['negative']}`}
                title="Not helpful"
              >
                👎
              </button>
            </small>
          </div>
        </div>
      );
    } else if (message.sender === 'error') {
      return (
        <div className={styles['error-message']}>
          {message.text}
        </div>
      );
    } else {
      return <div className={styles['user-message-content']}>{message.text}</div>;
    }
  };
  
  return (
    <div className={`${styles['chat-interface']} ${styles[colorMode]}`}>
      <div className={styles['chat-header']}>
        <h3>Textbook Assistant</h3>
        <p>Ask questions about the Physical AI & Humanoid Robotics content</p>
      </div>

      <div className={styles['chat-messages']}>
        {messages.length === 0 ? (
          <div className={styles['welcome-message']}>
            <p>Hello! I'm your textbook assistant. Ask me anything about the Physical AI & Humanoid Robotics content.</p>
            {selectedText && (
              <p className={styles['selected-text-notice']}>
                I noticed you selected: <em>"{selectedText.substring(0, 60)}{selectedText.length > 60 ? '...' : ''}"</em>
              </p>
            )}
          </div>
        ) : (
          messages.map((message) => (
            <div
              key={message.id}
              className={`${styles['message']} ${styles[`${message.sender}-message`]}`}
            >
              <div className={styles['message-content']}>
                {renderMessage(message)}
              </div>
              <div className={styles['message-timestamp']}>{message.timestamp}</div>
            </div>
          ))
        )}
        {isLoading && (
          <div className={`${styles['message']} ${styles['ai-message']}`}>
            <div className={styles['message-content']}>
              <div className={styles['ai-message-content']}>
                Thinking...
              </div>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <form className={styles['chat-input-form']} onSubmit={handleSubmit}>
        {selectedText && (
          <div className={styles['selected-text-preview']}>
            <small>Context: "{selectedText.substring(0, 80)}{selectedText.length > 80 ? '...' : ''}"</small>
          </div>
        )}
        <div className={styles['input-area']}>
          <textarea
            ref={textareaRef}
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Ask a question about the textbook content..."
            rows="1"
            disabled={isLoading}
          />
          <button
            type="submit"
            disabled={!inputValue.trim() || isLoading}
            className={styles['send-button']}
          >
            {isLoading ? 'Sending...' : '→'}
          </button>
        </div>
      </form>
    </div>
  );
};

export default ChatInterface;