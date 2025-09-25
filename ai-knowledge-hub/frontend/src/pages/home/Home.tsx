import React, { useState } from "react";
import "./Home.css";

const Home: React.FC = () => {
  const [messages, setMessages] = useState<
    Array<{ text: string; isUser: boolean }>
  >([]);
  const [input, setInput] = useState("");

  const handleSend = async () => {
    if (input.trim()) {
      setMessages([...messages, { text: input, isUser: true }]);
      setInput("");


      try {
        const response = await fetch(`http://127.0.0.1:8000/search?query=${encodeURIComponent(input)}`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        });

        const data = await response.json();
        setMessages((prev) => [
          ...prev,
          { text: data.answer, isUser: false },
        ]);
      } catch (error) {
        console.error("Error fetching AI response:", error);
      }
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
