import React from "react";
import {
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib";
import CardOne from "./templates/cardOne";
import CardTwo from "./templates/cardTwo";
import CardThree from "./templates/cardThree";
import CardFour from "./templates/cardFour";
import CardFive from "./templates/cardFive";

interface CardProps {
  template: "CardOne" | "CardTwo" | "CardThree" | "CardFour" | "CardFive";
  title?: string;
  subtitle?: string;
  mainValue?: string;
  secondaryValue?: string;
  delta?: string;
  chartData?: number[];
  xAxisLabel?: string;
  insights?: string[];
  tableData?: any[];
  bars?: any[];
  marker?: any;
  markerLabel?: string;
  dotPlots?: any[];
  colorScheme?: {
    background: string;
    text: string;
    trend?: string;
  };
}

class Card extends StreamlitComponentBase<CardProps> {
  public render() {
    const {
      template,
      title,
      subtitle,
      mainValue,
      secondaryValue,
      delta,
      chartData,
      xAxisLabel,
      insights,
      tableData,
      bars,
      marker,
      markerLabel,
      dotPlots,
      colorScheme,
    } = this.props.args;

    const defaultGreen = "#34D399";
    const defaultRed = "rgb(241, 155, 145)";
    const trendColor =
      colorScheme?.trend || (delta?.includes("-") ? defaultRed : defaultGreen);

    switch (template) {
      case "CardOne":
        return (
          <CardOne
            title={title}
            subtitle={subtitle}
            mainValue={mainValue}
            secondaryValue={secondaryValue}
            delta={delta}
            chartData={chartData}
            xAxisLabel={xAxisLabel}
            colorScheme={{ ...colorScheme, trend: trendColor }}
          />
        );
      case "CardTwo":
        return (
          <CardTwo
            title={title}
            subtitle={subtitle}
            insights={insights}
            colorScheme={colorScheme}
          />
        );
      case "CardThree":
        return (
          <CardThree
            title={title}
            mainValue={mainValue}
            subtitle={subtitle}
            tableData={tableData}
            colorScheme={colorScheme}
          />
        );
      case "CardFour":
        return (
          <CardFour
            title={title}
            mainValue={mainValue}
            subtitle={subtitle}
            bars={bars}
            colorScheme={colorScheme}
            marker={marker}
            markerLabel={markerLabel}
          />
        );
      case "CardFive":
        return (
          <CardFive
            title={title}
            tableData={tableData}
            dotPlots={dotPlots}
            colorScheme={colorScheme}
          />
        );
      default:
        console.error("Invalid template:", template);
        return <div>Invalid template</div>;
    }
  }
}

export default withStreamlitConnection(Card);
