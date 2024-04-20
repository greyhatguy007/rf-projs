import React from "react";

const Novelty = () => {
  return (
    <div className="mb-8">
      <h2 className="text-3xl font-bold mb-4">
        Novelty In the Proposed System
      </h2>
      <p className="w-auto text-justify text-xl">
        The proposed system introduces a transfer learnt YOLOv8 architecture algorithm, which is
        the most fastest and effective in segmentation tasks and detection. This
        innovative approach enables real-time surveillance leveraging the quick
        response time of the algorithm. The project proposes a hybrid approach
        for license plate recognition, combining deep learning techniques with
        Optical Character Recognition. By cascading YOLOv8 for object detection
        and an OCR model for character extraction, the system achieves high
        accuracy in recognizing license plates, even in varying environmental
        conditions and with different plate formats.
      </p>
    </div>
  );
};

export default Novelty;
