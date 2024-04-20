import React from "react";

const Footer = () => {
  return (
    <footer className="bg-gray-800 py-4 fixed bottom-0 w-full">
      <div className="container mx-auto px-4 flex-row md:flex md:justify-between">
        <p className="text-center text-white text-xs">
          &copy; {new Date().getFullYear()} Integrated Surveillance System Using
          Machine Vision
        </p>
        <div className="flex-col md:flex-row md:gap-3">
          <div className="text-center text-xs pt-2 pb-1 md:pt-0 md:text-sm font-bold text-white">
            Contributors
          </div>
          <div className="flex gap-5 justify-center">
            <p className="text-white text-sm hover:text-cyan-400 hover:font-bold hover:scale-x-125 transition ease-in-out">
              Ritvik
            </p>
            <p className="text-white text-sm">|</p>
            <p className="text-white text-sm hover:text-rose-500 hover:font-bold hover:scale-x-125 transition ease-in-out">
              Nitya
            </p>
            <p className="text-white text-sm">|</p>
            <p className="text-white text-sm hover:text-yellow-400 hover:font-bold hover:scale-x-125 transition ease-in-out">
              Tharun
            </p>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
