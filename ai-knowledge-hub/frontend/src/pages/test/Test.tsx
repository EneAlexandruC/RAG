import axios from "axios";
import { useEffect, useState } from "react";
import "./Test.css";

interface HealthResponse {
  message: string;
}

const Test = () => {
  const [data, setData] = useState<HealthResponse | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null as string | null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/health");
        setData(response.data);
      } catch (err) {
        setError("Error fetching data");
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return (
      <div className="test-container loading">
        <div className="spinner"></div>
        <p>Loading...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="test-container error">
        <div className="error-icon">⚠️</div>
        <h2>Oops! Something went wrong</h2>
        <p>{error}</p>
        <button onClick={() => window.location.reload()} className="retry-btn">
          Try Again
        </button>
      </div>
    );
  }

  return (
    <div className="test-container success">
      <div className="success-icon">✅</div>
      <h1>Health Check</h1>
      <div className="message-card">
        <p className="message">{data?.message}</p>
      </div>
      <div className="status-badge">Connected</div>
    </div>
  );
};

export default Test;
