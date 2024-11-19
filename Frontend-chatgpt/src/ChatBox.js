// src/ChatBox.js
import React from "react";
import './Chat.css';

const ChatBox = ({ messages }) => {
  return (
    <div className="chat-box">
      {messages.map((msg, index) => (
        <div key={index} className="message-wrapper">
          {/* Show avatars for user and bot */}
          {msg.sender === "user" ? (
            <div className="avatar user-avatar">U</div>
          ) : (
            <div className="avatar bot-avatar">B</div>
          )}
          <div
            className={`message ${msg.sender === "user" ? "user-message" : "bot-message"}`}
          >
            {msg.text}
          </div>
        </div>
      ))}
    </div>
  );
};

export default ChatBox;
