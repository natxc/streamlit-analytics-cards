import React from "react";

// A little helper function to format a string with bold numbers
export const formatValueWithBoldNumbers = (
  value: string,
): (string | React.ReactNode)[] => {
  const parts = value.split(/(\$?\d+(?:\.\d+)?[MBx]?)/);
  return parts.map((part, idx) =>
    /\d/.test(part) ? React.createElement("strong", { key: idx }, part) : part,
  );
};
