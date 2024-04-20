import React from "react";
import ProjectDetails from "./ProjectDetails";
import Objective from "./Objective";
import ProposedSystem from "./ProposedSystem";
import Novelty from "./Novelty";

const AboutPage = () => {
  return (
    <div className="container mx-auto px-4 py-8 mb-16">
      <ProjectDetails />
      <Objective />
      <ProposedSystem />
      <Novelty />
    </div>
  );
};

export default AboutPage;
