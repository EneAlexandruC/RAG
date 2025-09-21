import React, { useState } from "react";
import "./Home.css";

const Home: React.FC = () => {
  const [messages, setMessages] = useState<
    Array<{ text: string; isUser: boolean }>
  >([]);
  const [input, setInput] = useState("");

  const handleSend = () => {
    if (input.trim()) {
      setMessages([...messages, { text: input, isUser: true }]);
      setInput("");

      // Simulate AI response
      setTimeout(() => {
        setMessages((prev) => [
          ...prev,
          { text: "I'm a simple chatbot. How can I help you?", isUser: false },
        ]);
      }, 1000);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === "Enter") {
      handleSend();
    }
  };

  return (
    <div className="home-container">
      <div className="chat-container">
        <div className="chat-header">
          <h1>AI Knowledge Hub</h1>
        </div>

        <div className="messages-container">
          {messages.length === 0 && (
            <div className="welcome-message">
              <h2>How can I help you today?</h2>
            </div>
          )}

          {messages.map((message, index) => (
            <div
              key={index}
              className={`message ${message.isUser ? "user" : "ai"}`}
            >
              <div className="message-content">{message.text}</div>
            </div>
          ))}
        </div>

        <div className="input-container">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Message AI Knowledge Hub..."
            className="chat-input"
          />
          <button onClick={handleSend} className="send-button">
            Send
          </button>
        </div>
      </div>
    </div>
  );
};

export default Home;
