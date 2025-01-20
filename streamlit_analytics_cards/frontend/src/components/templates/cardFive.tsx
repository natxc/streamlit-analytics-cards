import React from "react";
import Draggable from "react-draggable";
import "../Card.css";

interface TableRow {
  label: string;
  value: string | number;
}

interface DotPlotData {
  title: string;
  subtitle: string;
  percentiles: { value: number; label: string }[];
  dots: { row: number; col: number; color: string }[];
}

interface CardFiveProps {
  title?: string;
  tableData: TableRow[];
  dotPlots: DotPlotData[];
  colorScheme?: {
    background: string;
    text: string;
    dot: string;
  };
}

const CardFive: React.FC<CardFiveProps> = ({
  title,
  tableData,
  dotPlots,
  colorScheme,
}) => {
  return (
    <Draggable>
      <div
        className="app-container"
        style={{
          display: "flex", // Side-by-side layout
          flexDirection: "row",
          alignItems: "flex-start",
          backgroundColor: colorScheme?.background || "#ffffff",
          color: colorScheme?.text || "#000000",
        }}
      >
        {/* Table Section */}
        <div style={{ flex: 1, marginRight: "16px" }}>
          <table>
            <thead>
              <tr>
                <th>Organization</th>
                <th>Value</th>
              </tr>
            </thead>
            <tbody>
              {tableData.map((row, idx) => (
                <tr key={idx}>
                  <td>{row.label}</td>
                  <td style={{ textAlign: "right" }}>{row.value}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {/* Dot Plot Section */}
        <div
          style={{
            flex: 2,
            display: "flex",
            justifyContent: "space-between",
            gap: "16px",
          }}
        >
          {dotPlots.map((plot, idx) => (
            <div
              key={idx}
              className="dot-plot"
              style={{
                textAlign: "center",
                border: "1px solid #ddd",
                borderRadius: "4px",
                padding: "8px",
                flex: 1,
              }}
            >
              <h4
                style={{
                  fontSize: "14px",
                  fontStyle: "italic",
                  marginBottom: "4px",
                }}
              >
                {plot.title}
              </h4>
              <h5 style={{ fontSize: "12px", marginBottom: "8px" }}>
                {plot.subtitle}
              </h5>
              <div
                style={{
                  display: "grid",
                  gridTemplateColumns: `repeat(${plot.percentiles.length}, 1fr)`,
                  gap: "4px",
                }}
              >
                {plot.percentiles.map((percentile, idx) => (
                  <div
                    key={idx}
                    style={{ fontSize: "10px", textAlign: "center" }}
                  >
                    {percentile.label}
                  </div>
                ))}
                {plot.dots.map((dot, idx) => (
                  <div
                    key={idx}
                    className="dot"
                    style={{
                      gridColumn: dot.col,
                      gridRow: dot.row,
                      backgroundColor: dot.color || "#0000ff",
                      borderRadius: "50%",
                      width: "10px",
                      height: "10px",
                      margin: "auto",
                    }}
                  />
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>
    </Draggable>
  );
};

export default CardFive;
