import React from "react";
import { Link } from "react-router-dom";
import "./Navbar.css";

interface NavbarProps {
  onNewChat?: () => void;
  onToggleSidebar?: () => void;
}

const Navbar: React.FC<NavbarProps> = ({ onNewChat, onToggleSidebar }) => {
  return (
    <nav className="navbar">
      <div className="navbar-left">
        <div className="user-menu">
          <button className="user-avatar">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path
                d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2M12 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8z"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
              />
            </svg>
          </button>
        </div>
      </div>

      <div className="navbar-left">
        <button className="upload-avatar" onClick={() => window.location.href = "/upload"}>
          <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
            <path
              d="M12 16V4m0 0l-4 4m4-4l4 4M4 20h16"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
            />
          </svg>
          <span style={{ marginLeft: "0.5rem" }}>Upload</span>
        </button>
      </div>

      <div className="navbar-right">
        <button className="new-chat-btn" onClick={onNewChat}>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
            <path
              d="M12 5v14m-7-7h14"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
            />
          </svg>
          New chat
        </button>
      </div>
    </nav>
  );
};

export default Navbar;
