import React from "react";
import Draggable from "react-draggable";
import "../Card.css";

interface CardOneProps {
  title?: string;
  subtitle?: string;
  mainValue?: string;
  secondaryValue?: string;
  trendValue?: string;
  chartData?: number[];
  colorScheme?: {
    background: string;
    text: string;
    trend: string;
  };
}

const CardOne: React.FC<CardOneProps> = ({
  title,
  subtitle,
  mainValue,
  secondaryValue,
  trendValue,
  chartData,
  colorScheme,
}) => {
  return (
    <Draggable>
      <div
        className="card"
        style={{
          backgroundColor: colorScheme?.background || "#FFFFFF",
          color: colorScheme?.text || "#000000",
        }}
      >
        <h3>{title || "Title Placeholder"}</h3>
        <p className="card-subtitle">{subtitle || "Subtitle Placeholder"}</p>
        <div className="card-values">
          <h1 className="card-main-value">{mainValue || "Main Value"}</h1>
          <span className="card-secondary-value">
            / {secondaryValue || "Secondary Value"}
          </span>
        </div>
        <div
          className="card-trend"
          style={{
            backgroundColor: colorScheme?.trend || "#B2FEF7",
          }}
        >
          {trendValue || "Trend Placeholder"}
        </div>
        <div className="card-chart">
          <svg width="100%" height="100" style={{ overflow: "visible" }}>
            <polyline
              fill="lightgray"
              stroke="gray"
              strokeWidth="2"
              points={chartData
                ?.map((val, idx) => `${idx * 50},${100 - val}`)
                .join(" ")}
            />
            {chartData?.map((val, idx) => (
              <circle
                key={idx}
                cx={idx * 50}
                cy={100 - val}
                r="5"
                fill="white"
                stroke="black"
              />
            ))}
          </svg>
        </div>
      </div>
    </Draggable>
  );
};

export default CardOne;
