
import React from "react";

const ProjectDetails = () => {
  return (
    <div className="mb-8">
      <h2 className="text-3xl font-bold mb-4">Abstract</h2>
      <p className="w-auto text-justify text-xl">
        This project presents an <i>integrated surveillance system</i>{" "}
        leveraging <i>Advanced License Plate Recognition (ALPR)</i> technology.
        The primary objective is to develop a robust platform capable of
        efficiently identifying and tracking vehicles based on their license
        plates, thereby enhancing surveillance capabilities in various contexts.
        The system utilizes{" "}
        <a
          href="https://www.raspberrypi.com/products/raspberry-pi-5/"
          className="italic hover:text-blue-800"
        >
          Raspberry Pi 5
        </a>{" "}
        as its core computing platform, running PyTorch for deep learning-based
        object detection and recognition tasks. Specifically, the{" "}
        <a href="https://yolov8.com/" className="italic hover:text-blue-800">
          YOLOv8
        </a>{" "}
        model based on <i>Convolutional Neural Networks</i> is employed for
        initial object detection, followed by fine-tuning through transfer
        learning to specialize in license plate recognition. An{" "}
        <i>Optical Character Recognition (OCR)</i> model is then applied to
        extract alphanumeric characters from the identified plates. The
        collected data, along with corresponding timestamps and location, is
        stored in a database for organized retrieval and analysis. Additionally,
        a web interface is developed using React and Flask/Django, facilitating
        monitoring of surveillance data. This integrated system offers promising
        applications in security enforcement, access control, providing valuable
        insights and actionable information for surveillance operations. The
        utilization of PyTorch on Raspberry Pi 5 provides a portable and
        efficient platform for running complex deep learning models in
        resource-constrained environments.
      </p>
    </div>
  );
};

export default ProjectDetails;
