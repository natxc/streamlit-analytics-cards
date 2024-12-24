import streamlit as st
from custom_components import my_component

if __name__ == "__main__":
    st.title("Merry Christmas 🎄")

    data = {
        "title": "Attrition Diversity",
        "subtitle": "Female Attrition",
        "mainValue": "4.7%",
        "secondaryValue": "52",
        "trendValue": "Y/Y 5.1%, -0.4%",
        "chartData": [10, 20, 15, 30, 25],
        "colorScheme": {
            "background": "#FFFFFF",
            "text": "#000000",
            "trend": "#B2FEF7",
        },
        "genderFilter": "Male",
    }

    # Render the component
    my_component(data=data)
