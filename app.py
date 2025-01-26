import streamlit as st
from card_component import (
    render_cards_1,
    # render_cards_2,
    # render_cards_3,
    # render_cards_4,
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
        from streamlit_analytics_cards import card as stac
        import pandas as pd
        import streamlit as st

        # The data
        df = pd.DataFrame({"Number of Exits": [10, 20, 15, 30, 25, 10, 20, 15, 0, 7]})

        # Optional - cards will be full-wdith or determined by how many columns are present
        col1, col2 = st.columns(2)

        # Render the components
        with col1:
            stac(
                template="CardOne",
                title="Attrition Diversity",
                subtitle="Female Attrition",
                main_value="4.7%",
                secondary_value="52",
                delta="Y/Y 5.1%, -0.4%",
                chart_data=df["Number of Exits"].tolist(),
                x_axis_label=df.columns[0],
                color_scheme={"background": "#FFFFFF", "text": "#000000"},
                key="card_1",
            )

        with col2:
            stac(
                template="CardOne",
                title="Revenue Growth",
                subtitle="Quarterly Performance",
                main_value="$1.2M",
                secondary_value="35% Increase",
                delta="Y/Y +10%",
                chart_data=[15, 25, 20, 40, 35],
                color_scheme={"background": "#F3F4F6", "text": "#1F2937", "trend": "#B2FEF7"},
                key="card_2",
            )"""
        st.code(code, language="python")

    st.subheader("Example usage", divider=True)

    render_cards_1()
    st.caption("Template: CardOne")

    # render_cards_2()
    # st.caption("Template: CardTwo")

    # render_cards_3()
    # st.caption("Template: CardThree")

    # render_cards_4()
    # st.caption("Template: CardFour")

    render_cards_5()
    st.caption("Template: CardFive")
