import React, { useState } from "react";
import Header from "./components/Header";
import Footer from "./components/Footer";
import RenderTable from "./components/RenderTable";
import AboutPage from "./components/about/AboutPage";

const App = () => {
  const [currentPage, setCurrentPage] = useState("about");

  const handlePageChange = (page) => {
    setCurrentPage(page);
  };

  return (
    <div className="bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 h-full">
      <Header onPageChange={handlePageChange} />
      {currentPage === "viewData" ? <RenderTable /> : <AboutPage />}
      <Footer />
    </div>
  );
};

export default App;
