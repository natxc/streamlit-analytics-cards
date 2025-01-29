import React from "react";
import "../Card.css";

interface CardOneProps {
  title?: string;
  subtitle?: string;
  colorScheme?: {
    background: string;
    text: string;
  };
}

const CardOne: React.FC<CardOneProps> = ({ title, subtitle, colorScheme }) => {
  return (
    <div
      className="card"
      style={{
        backgroundColor: colorScheme?.background || "#FFFFFF",
        color: colorScheme?.text || "#000000",
      }}
    >
      <h3>{title}</h3>
      <p className="card-subtitle">{subtitle}</p>
    </div>
  );
};

export default CardOne;
