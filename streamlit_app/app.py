import streamlit as st
from card_component import (
    render_cards_1,
    render_cards_2,
    render_cards_3,
    render_cards_4,
    render_cards_5,
)

if __name__ == "__main__":
    st.set_page_config(page_title="Show Us The Cards", page_icon="📈", layout="wide")
    st.title(
        "Example Cards 🃏",
    )

    st.caption(
        "Information About the Cards",
        unsafe_allow_html=False,
        help="There are a few different types of cards and they each take different \
            fields. They can connect dirrectly to a data source too.",
    )

    with st.expander("Code example"):

        code = """
        # pip install streamlit-analytics-cards
        import streamlit-analytics-cards as stac
        data = {
            "template": "CardOne",
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
        stac.card(data=data)"""
        st.code(code, language="python")

    st.subheader("Example usage", divider=True)

    render_cards_1()
    st.caption("Template: CardOne")

    render_cards_2()
    st.caption("Template: CardTwo")

    render_cards_3()
    st.caption("Template: CardThree")

    render_cards_4()
    st.caption("Template: CardFour")

    render_cards_5()
    st.caption("Template: CardFive")
