import React from "react";
import { createRoot } from "react-dom/client";
import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib";
import Draggable from "react-draggable";

interface State {
  data: {
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
    genderFilter?: string;
  };
}

class MyComponent extends StreamlitComponentBase<State> {
  constructor(props: any) {
    super(props);
    this.state = {
      data: this.props.args["data"] || {
        title: "Attrition Diversity",
        subtitle: "Female Attrition",
        mainValue: "4.7%",
        secondaryValue: "52",
        trendValue: "Y/Y 5.1%, -0.4%",
        chartData: [10, 20, 15, 30, 25],
        colorScheme: {
          background: "#FFFFFF",
          text: "#000000",
          trend: "#B2FEF7",
        },
        genderFilter: "Male",
      },
    };
  }

  handleColorChange = (gender: string) => {
    const newColorScheme = {
      background: gender === "Male" ? "#000000" : "#FFFFFF",
      text: gender === "Male" ? "#FFFFFF" : "#000000",
      trend: "#B2FEF7",
    };

    this.setState((prevState) => ({
      data: {
        ...prevState.data,
        colorScheme: newColorScheme,
        genderFilter: gender,
      },
    }));

    Streamlit.setComponentValue(newColorScheme);
  };

  public render() {
    const { data } = this.state;
    const {
      title,
      subtitle,
      mainValue,
      secondaryValue,
      trendValue,
      chartData,
      colorScheme,
      genderFilter,
    } = data;

    return (
      <Draggable>
        <div
          style={{
            border: "1px solid #ccc",
            borderRadius: "8px",
            padding: "16px",
            maxWidth: "300px",
            backgroundColor: colorScheme?.background,
            color: colorScheme?.text,
          }}
        >
          <h3>{title}</h3>
          <p style={{ color: "#888" }}>{subtitle}</p>
          <div style={{ display: "flex", alignItems: "baseline" }}>
            <h1 style={{ margin: "0" }}>{mainValue}</h1>
            <span style={{ fontSize: "24px", marginLeft: "8px" }}>
              / {secondaryValue}
            </span>
          </div>
          <div
            style={{
              backgroundColor: colorScheme?.trend,
              borderRadius: "4px",
              padding: "8px",
              marginTop: "8px",
            }}
          >
            {trendValue}
          </div>
          <div style={{ marginTop: "16px" }}>
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
          <div style={{ marginTop: "8px" }}>
            <strong>Gender Filter:</strong>
            <button
              style={{
                backgroundColor:
                  genderFilter === "Male" ? "#000000" : "transparent",
                color: genderFilter === "Male" ? "#FFFFFF" : "#000000",
                border: "1px solid #000",
                borderRadius: "8px",
                padding: "4px 8px",
                marginLeft: "8px",
              }}
              onClick={() => this.handleColorChange("Male")}
            >
              Male
            </button>
            <button
              style={{
                backgroundColor:
                  genderFilter === "Female" ? "#000000" : "transparent",
                color: genderFilter === "Female" ? "#FFFFFF" : "#000000",
                border: "1px solid #000",
                borderRadius: "8px",
                padding: "4px 8px",
                marginLeft: "8px",
              }}
              onClick={() => this.handleColorChange("Female")}
            >
              Female
            </button>
          </div>
        </div>
      </Draggable>
    );
  }
}

export default withStreamlitConnection(MyComponent);
