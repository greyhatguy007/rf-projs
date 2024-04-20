import React from "react";

const ProposedSystem = () => {
  return (
    <div className="mb-8">
      <h2 className="text-3xl font-bold mb-4">Proposed System</h2>
      <p className="w-auto text-justify text-xl">
        The proposed system integrates Raspberry Pi 5 and a webcam for video
        capture, utilizing PyTorch with YOLOv8 model for object detection,
        specifically targeting license plate recognition. The model is trained
        based on transfer-learning to identify license plates. With the
        inclusion of an OCR model, alphanumeric characters are extracted from
        recognized plates and stored along with timestamps in a SQL database.
        Real-time alerts are sent upon on-demand specific vehicle detection, and
        a user-friendly web interface facilitates monitoring and configuration.
      </p>
      <div className="pt-5 pb-2 rounded-lg flex justify-center">
        <img
          src="architecture.png"
          alt="system"
          className="max-w-full h-auto rounded-xl"
          style={{ maxWidth: "99%", width: "auto" }} 
        />
      </div>
    </div>
  );
};

export default ProposedSystem;
