import React from "react";

const ImageModal = ({ imageUrl, onClose }) => {
  return (
    <div className="fixed top-0 left-0 w-full h-full flex items-center justify-center bg-black bg-opacity-50 z-50">
      <div className="max-w-md w-full bg-white p-6 rounded-lg flex flex-col items-center justify-center">
        <img
          src={`data:image/jpeg;base64,${imageUrl}`}
          alt="requested vehicle data"
          className="max-w-full h-auto"
        />
        <button
          onClick={onClose}
          className="mt-4 text-white font-extrabold bg-red-600 hover:bg-red-700 px-2 py-1 rounded-md"
        >
          Close
        </button>
      </div>
    </div>
  );
};

export default ImageModal;
