import React from "react";

const Table = ({ data, handleShowImage }) => {
  return (
    <table className="table-auto mb-36">
      <thead className="bg-gray-800 text-white">
        <tr>
          <th className="px-4 py-2">ID</th>
          <th className="px-4 py-2">Timestamp</th>
          <th className="px-4 py-2">Predicted License Plate</th>
          <th className="px-4 py-2">Vehicle</th>
          <th className="px-4 py-2">License Plate</th>
        </tr>
      </thead>

      <tbody className="bg-gray-300 divide-y divide-gray-500 ">
        {data.map((item) => (
          <tr
            key={item.id}
            className="hover:bg-white"
          >
            <td className="px-6 py-4 whitespace-nowrap">{item.id}</td>
            <td className="px-6 py-4 whitespace-nowrap">{item.timestamp}</td>
            <td className="px-6 py-4 whitespace-nowrap">
              {item.license_plate_number}
            </td>
            <td className="px-6 py-4 whitespace-nowrap">
              <button
                className="text-white bg-blue-600 hover:bg-blue-800 font-bold px-2 py-1 rounded-lg text-sm"
                onClick={() => handleShowImage(item.car_cropped_image)}
              >
                View Image
              </button>
            </td>
            <td className="px-6 py-4 whitespace-nowrap">
              <button
                className="text-white bg-blue-600 hover:bg-blue-800 font-bold px-2 py-1 rounded-lg text-sm"
                onClick={() =>
                  handleShowImage(item.license_plate_cropped_image)
                }
              >
                View Image
              </button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default Table;
