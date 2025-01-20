import React from "react";
import Draggable from "react-draggable";
import { formatValueWithBoldNumbers } from "../../utils/formatUtils";
import "../Card.css";

interface Insight {
  text: string;
  value: string;
}

interface CardTwoProps {
  title?: string;
  subtitle?: string;
  insights?: Insight[];
  colorScheme?: {
    background: string;
    text: string;
  };
}

const CardTwo: React.FC<CardTwoProps> = ({
  title,
  subtitle,
  insights,
  colorScheme,
}) => {
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
        }}
      >
        <h3 style={{ marginBottom: "8px", fontWeight: "bold" }}>
          {title || "Title Placeholder"}
        </h3>
        <p style={{ marginBottom: "16px", color: "#888" }}>
          {subtitle || "Subtitle Placeholder"}
        </p>
        <ul style={{ listStyleType: "none", padding: 0, margin: 0 }}>
          {insights?.map((insight, idx) => (
            <li
              key={idx}
              style={{
                marginBottom: "12px",
                display: "flex",
                justifyContent: "space-between",
                alignItems: "flex-start",
                borderBottom:
                  idx !== insights.length - 1 ? "1px solid #EEE" : "none",
                paddingBottom: idx !== insights.length - 1 ? "8px" : "0",
              }}
            >
              <span style={{ flex: 1, fontSize: "14px", lineHeight: "1.4" }}>
                {insight.text || "Insight Placeholder"}
              </span>
              <span
                style={{
                  fontWeight: "normal",
                  marginLeft: "8px",
                  whiteSpace: "nowrap",
                }}
              >
                {formatValueWithBoldNumbers(insight.value || "")}
              </span>
            </li>
          ))}
        </ul>
      </div>
    </Draggable>
  );
};

export default CardTwo;
