import React from "react";
import Draggable from "react-draggable";
import "../Card.css";

interface TableRow {
  [key: string]: string | undefined;
}

interface CardThreeProps {
  title?: string;
  mainValue?: string;
  subtitle?: string;
  tableData: TableRow[];
  colorScheme?: {
    background: string;
    text: string;
  };
}

const CardThree: React.FC<CardThreeProps> = ({
  title,
  mainValue,
  subtitle,
  tableData,
  colorScheme,
}) => {
  const columnHeaders =
    tableData.length > 0
      ? Array.from(new Set(tableData.flatMap((row) => Object.keys(row))))
      : [];

  return (
    <Draggable>
      <div
        className="card"
        style={{
          backgroundColor: colorScheme?.background || "#FFFFFF",
          color: colorScheme?.text || "#000000",
          borderRadius: "8px",
          padding: "16px",
          maxWidth: "400px",
          boxShadow: "0 2px 4px rgba(0,0,0,0.1)",
          overflow: "hidden",
        }}
      >
        <h3 style={{ marginBottom: "8px", fontWeight: "bold" }}>
          {title || "Title Placeholder"}
        </h3>
        <div className="card-values" style={{ marginBottom: "16px" }}>
          <h1 className="card-main-value">
            {mainValue || "Value Placeholder"}
          </h1>
          <span style={{ marginLeft: "8px", color: "#888" }}>
            {subtitle || "Subtitle Placeholder"}
          </span>
        </div>
        <div style={{ maxHeight: "200px", overflow: "auto" }}>
          <table style={{ width: "100%", borderCollapse: "collapse" }}>
            <thead>
              <tr style={{ borderBottom: "1px solid #eee", textAlign: "left" }}>
                {columnHeaders.map((header, idx) => (
                  <th
                    key={idx}
                    style={{ padding: "8px 0", textTransform: "capitalize" }}
                  >
                    {header.replace(/_/g, " ")}
                    {}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {tableData.map((row, rowIndex) => (
                <tr key={rowIndex} style={{ borderBottom: "1px solid #eee" }}>
                  {columnHeaders.map((header, colIndex) => (
                    <td
                      key={colIndex}
                      style={{ padding: "8px 0", textAlign: "left" }}
                    >
                      {row[header] || ""} {}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </Draggable>
  );
};

export default CardThree;
