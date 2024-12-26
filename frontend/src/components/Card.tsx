import React from "react";
import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib";
import CardOne from "./templates/cardOne";
import CardTwo from "./templates/cardTwo";
import CardThree from "./templates/cardThree";

interface CardProps {
  template: "CardOne";
  colorScheme?: {
    background: string;
    text: string;
    trend: string;
  };
}

class Card extends StreamlitComponentBase<CardProps> {
  public render() {
    const { data } = this.props.args;
    const { template } = data || {};

    switch (template) {
      case "CardOne":
        return (
          <CardOne
            title={data?.title}
            subtitle={data?.subtitle}
            mainValue={data?.mainValue}
            secondaryValue={data?.secondaryValue}
            trendValue={data?.trendValue}
            chartData={data?.chartData}
            colorScheme={data?.colorScheme}
          />
        );
      case "CardTwo":
        return (
          <CardTwo
            title={data?.title}
            subtitle={data?.subtitle}
            insights={data?.insights}
            colorScheme={data?.colorScheme}
          />
        );
      case "CardThree":
        return (
          <CardThree
            title={data?.title}
            mainValue={data?.mainValue}
            subtitle={data?.subtitle}
            tableData={data?.tableData}
            colorScheme={data?.colorScheme}
          />
        );
      default:
        console.error("Invalid template:", template);
        return <div>Invalid template</div>;
    }
  }
}

export default withStreamlitConnection(Card);
