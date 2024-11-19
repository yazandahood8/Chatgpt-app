import React, { useState, useEffect } from "react";
import ChatBox from "./ChatBox";
import "./Chat.css";

function App() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);

  // Fetch chat history on component mount
  useEffect(() => {
    const fetchChatHistory = async () => {
      try {
        const response = await fetch("http://127.0.0.1:5000/history");
        if (!response.ok) {
          throw new Error(`Error fetching chat history: ${response.status}`);
        }
        const chatHistory = await response.json();
        // Update messages with history - treating each entry as two messages, one for question and one for answer
        const formattedMessages = chatHistory.flatMap((msg) => [
          { sender: "user", text: msg.question },
          { sender: "bot", text: msg.answer },
        ]);
        setMessages(formattedMessages);
      } catch (error) {
        console.error("Error loading chat history:", error);
      }
    };
    fetchChatHistory();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!question.trim()) return;

    // Add the user's question to the chat
    const newMessages = [...messages, { sender: "user", text: question }];
    setMessages(newMessages);
    setQuestion("");

    try {
      // Send the question to the backend
      const response = await fetch("http://127.0.0.1:5000/ask", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ question }),
      });

      if (!response.ok) {
        throw new Error(`Server error: ${response.status}`);
      }

      const data = await response.json();

      // Add the bot's answer to the chat
      setMessages([...newMessages, { sender: "bot", text: data.answer || "No answer available." }]);
    } catch (error) {
      console.error("Fetch error:", error);
      setMessages([...newMessages, { sender: "bot", text: "Error: Unable to reach the server." }]);
    }
  };

  return (
    <div className="chat-container">
<h1>AI BOT</h1>
<p>Your personal assistant for answering questions and providing information.</p>      <ChatBox messages={messages} />
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Type your question here..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          required
        />
        <button type="submit">Ask</button>
      </form>
    </div>
  );
}

export default App;
