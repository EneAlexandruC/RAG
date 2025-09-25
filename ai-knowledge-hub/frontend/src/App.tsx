import { Route, BrowserRouter, Routes } from "react-router-dom";
import Nav from "./components/navbar/Navbar";
import Home from "./pages/home/Home";
import Test from "./pages/test/Test";
import Upload from "./components/upload/Upload";
import "./App.css";

function App() {
  return (
    <div className="App">
      <Nav />
      <BrowserRouter>
        <Routes>
          <Route path="/upload" element={<Upload />} />
          <Route path="/test" element={<Test />} />
          <Route path="/" element={<Home />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
