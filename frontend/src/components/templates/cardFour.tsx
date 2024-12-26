import React from "react";
import Draggable from "react-draggable";
import "../Card.css";

interface BarChartData {
  label: string;
  value: number;
}

interface CardFourProps {
  title?: string;
  mainValue?: string;
  subtitle?: string;
  bars: BarChartData[];
  colorScheme?: {
    background: string;
    text: string;
    bar: string;
    marker?: string;
  };
  marker?: number;
  markerLabel?: string;
}

const CardFour: React.FC<CardFourProps> = ({
  title,
  mainValue,
  subtitle,
  bars,
  colorScheme,
  marker,
  markerLabel,
}) => {
  const maxValue = Math.max(...bars.map((bar) => bar.value));

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
        <h3
          style={{
            marginBottom: subtitle ? "8px" : "16px",
            fontWeight: "bold",
          }}
        >
          {title || "Title Placeholder"}
        </h3>

        {subtitle && (
          <p style={{ marginBottom: "16px", color: "#888" }}>{subtitle}</p>
        )}

        {mainValue && (
          <div
            style={{
              marginBottom: "16px",
              fontSize: "32px",
              fontWeight: "bold",
            }}
          >
            {mainValue}
          </div>
        )}

        <div
          style={{
            display: "flex",
            flexDirection: "column",
            justifyContent: subtitle ? "flex-start" : "center",
            height: subtitle ? "auto" : "100%",
          }}
        >
          {bars.map((bar, idx) => (
            <div
              key={idx}
              style={{
                display: "flex",
                alignItems: "center",
                marginBottom: "8px",
              }}
            >
              <span
                style={{
                  width: "100px",
                  marginRight: "8px",
                  textAlign: "right",
                  whiteSpace: "nowrap",
                }}
              >
                {bar.label}
              </span>

              <div
                style={{
                  flex: 1,
                  height: "8px",
                  backgroundColor: colorScheme?.bar || "#E0E0E0",
                  position: "relative",
                }}
              >
                <div
                  style={{
                    width: `${(bar.value / maxValue) * 100}%`,
                    height: "100%",
                    backgroundColor: colorScheme?.text || "#000000",
                  }}
                ></div>
              </div>
            </div>
          ))}

          {marker !== undefined && (
            <div
              style={{
                position: "absolute",
                top: `${106 + bars.length * 8}px`,
                height: `${bars.length * 26}px`,
                left: `${marker}%`,
                borderLeft: `2px dashed ${colorScheme?.marker || "#FF0000"}`,
                pointerEvents: "none",
              }}
            >
              {markerLabel && (
                <div
                  style={{
                    position: "absolute",
                    top: "-40px",
                    left: "-20px",
                    color: colorScheme?.marker || "#FF0000",
                    fontSize: "12px",
                  }}
                >
                  {markerLabel}
                </div>
              )}
            </div>
          )}
        </div>
      </div>
    </Draggable>
  );
};

export default CardFour;
