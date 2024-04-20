import React, { useState, useEffect } from "react";
import Table from "./Table";
import ImageModal from "./ImageModal"; // Import the modal component

const RenderTable = () => {
  const [carData, setCarData] = useState([]);
  const [modalImageUrl, setModalImageUrl] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/data/all")
      .then((response) => response.json())
      .then((data) => setCarData(data))
      .catch((error) => console.error("Error fetching data:", error));
  }, []);

    const handleShowImage = (imageUrl) => {
    setModalImageUrl(imageUrl);
  };

  const handleCloseModal = () => {
    setModalImageUrl(null);
  };

  return (
    <div className="flex flex-col items-center justify-center h-full">
      <h1 class="text-3xl p-4 text-center font-bold text-black">
        Logged Vehicle Data
      </h1>

      <Table data={carData} handleShowImage={handleShowImage} />
      {modalImageUrl && (
        <ImageModal imageUrl={modalImageUrl} onClose={handleCloseModal} />
      )}
    </div>
  );
};

export default RenderTable;
