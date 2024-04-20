import React, { useState } from "react";

const Header = ({ onPageChange }) => {
  const [currentPage, setCurrentPage] = useState("about");

  const handlePageChange = (page) => {
    setCurrentPage(page);
    onPageChange(page);
  };

  return (
    <header className="bg-gray-800 py-4">
      <div className="container mx-auto px-4 flex justify-between items-center">
        <h1 className="text-4xl font-bold text-white">
          Integrated Surveillance System Using Machine Vison
        </h1>
        <div className="sm:flex-row flex-col">
          <button
            className={`mb-4 xl:mb-0 mx-2 px-4 py-2 bg-white text-gray-800 rounded-md focus:outline-none ${
              currentPage === "about" ? "font-bold" : ""
            }`}
            onClick={() => handlePageChange("about")}
          >
            About
          </button>
          <button
            className={`mx-2 px-4 py-2 bg-white text-gray-800 rounded-md focus:outline-none ${
              currentPage === "viewData" ? "font-bold" : ""
            }`}
            onClick={() => handlePageChange("viewData")}
          >
            View Data
          </button>
        </div>
      </div>
    </header>
  );
};

export default Header;
