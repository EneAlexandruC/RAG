import React, { useState, useRef } from "react";
import "./Upload.css";

const Upload: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [status, setStatus] = useState<string>("");
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      setFile(e.target.files[0]);
    }
  };

  const handleUpload = async () => {
    if (!file) {
      setStatus("Please select a file.");
      return;
    }
    setStatus("Uploading...");
    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://127.0.0.1:8000/upload", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        setStatus("Upload successful!");
      } else {
        const errorText = await response.text();
        setStatus(`Upload failed: ${errorText}`);
      }
    } catch (error: any) {
      setStatus(`Upload failed: ${error.message}`);
    }
  };

  return (
    <div className="upload-container">
      <div className="upload-header pb-12">
        <h2 className="upload-title">Upload a file</h2>
      </div>
      <div className="upload-input">
        <input
          ref={fileInputRef}
          className="upload-file-input"
          type="file"
          onChange={handleFileChange}
          id="file-upload"
          style={{ display: "none" }}
        />
        <label htmlFor="file-upload" className="custom-file-label">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
            <path
              d="M12 16V4m0 0l-4 4m4-4l4 4M4 20h16"
              stroke="#4f8cff"
              strokeWidth="2"
              strokeLinecap="round"
            />
          </svg>
          {file ? file.name : "Choose File"}
        </label>
      </div>
      <button className="upload-btn" onClick={handleUpload} disabled={!file}>
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" style={{marginRight: "0.5rem"}}>
          <path
            d="M12 16V4m0 0l-4 4m4-4l4 4M4 20h16"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
          />
        </svg>
        Upload
      </button>
      <div className="upload-status">{status}</div>
    </div>
  );
};

export default Upload;