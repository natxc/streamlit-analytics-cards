from streamlit_analytics_cards import card as stac

data_3 = {
    "template": "CardTwo",
    "title": "Attrition Risk Factors",
    "subtitle": "Employee attrition prediction model",
    "insights": [
        {
            "text": "Tenure 2-4 years",
            "value": "3.2x more likely to leave - 768 employees",
        },
        {
            "text": "Prior year salary increase less than 3.5%",
            "value": "2.7x more likely to leave - 328 employees",
        },
        {
            "text": "Year in same role between 1.5 - 5 years",
            "value": "1.9x more likely to leave - 124 employees",
        },
    ],
    "colorScheme": {
        "background": "#FFFFFF",
        "text": "#000000",
    },
}

data_4 = {
    "template": "CardTwo",
    "title": "Top Revenue-Generating Destinations",
    "subtitle": "Tourism hotspots by annual revenue",
    "insights": [
        {"text": "Las Vegas, USA", "value": "$19.5B annual revenue - 42M visitors"},
        {"text": "Paris, France", "value": "$17.4B annual revenue - 38M visitors"},
        {"text": "Bangkok, Thailand", "value": "$16.2B annual revenue - 36M visitors"},
    ],
    "colorScheme": {
        "background": "#FFFFFF",
        "text": "#000000",
    },
}

tableData = [
    {"employee": "Lazy Sue", "date": "8/1/2024"},
    {"employee": "Sleepy Sam", "date": "9/7/2024"},
    {"employee": "Awesome Ann", "date": "7/8/2024", "key": "Y"},
    {"employee": "GPT Greg", "date": "10/1/2024"},
]

data_5 = {
    "template": "CardThree",
    "title": "Future Exits",
    "mainValue": "12",
    "subtitle": "in next 60 days",
    "tableData": tableData,
    "colorScheme": {
        "background": "#FFFFFF",
        "text": "#000000",
    },
}

tableData2 = [
    {
        "project": "Website Redesign",
        "deadline": "8/15/2024",
        "status": "On Track",
        "priority": "High",
    },
    {
        "project": "Marketing Campaign",
        "deadline": "9/1/2024",
        "status": "At Risk",
        "priority": "Medium",
    },
    {
        "project": "Product Launch",
        "deadline": "10/20/2024",
        "status": "Delayed",
        "priority": "High",
    },
    {
        "project": "Data Migration",
        "deadline": "11/5/2024",
        "status": "On Track",
        "priority": "Low",
    },
    {
        "project": "Q4 Sales Plan",
        "deadline": "9/25/2024",
        "status": "On Track",
        "priority": "Medium",
    },
    {
        "project": "Mobile App Update",
        "deadline": "10/10/2024",
        "status": "Delayed",
        "priority": "High",
    },
    {
        "project": "Customer Support Overhaul",
        "deadline": "12/15/2024",
        "status": "On Track",
        "priority": "Low",
    },
    {
        "project": "Cloud Infrastructure",
        "deadline": "8/30/2024",
        "status": "At Risk",
        "priority": "High",
    },
    {
        "project": "SEO Optimization",
        "deadline": "7/30/2024",
        "status": "On Track",
        "priority": "Medium",
    },
    {
        "project": "New Feature Development",
        "deadline": "11/20/2024",
        "status": "Delayed",
        "priority": "High",
    },
]

data_6 = {
    "template": "CardThree",
    "title": "Project Deadlines",
    "mainValue": "4",
    "subtitle": "Upcoming Projects",
    "tableData": tableData2,
    "colorScheme": {
        "background": "#FFFFFF",
        "text": "#000000",
    },
}

tableData3 = [
    {"label": "AI/ML", "value": 70},
    {"label": "IS&T", "value": 50},
    {"label": "HW TECH", "value": 90},
    {"label": "Services", "value": 100},
]

data_7 = {
    "template": "CardFour",
    "title": "Transfers Out",
    "mainValue": "125",
    "subtitle": "Exits to another organization",
    "bars": tableData3,
    "colorScheme": {
        "background": "#FFFFFF",
        "text": "#000000",
        "bar": "#E0E0E0",
    },
}

tableData4 = [
    {"label": "Apple", "value": 90},
    {"label": "R&D Orgs", "value": 50},
    {"label": "USA", "value": 70},
    {"label": "International", "value": 100},
]

data_8 = {
    "template": "CardFour",
    "title": "Attrition Comparisons",
    "bars": tableData4,
    "marker": 38,
    "markerLabel": "Software 3.8%",
    "colorScheme": {
        "background": "#FFFFFF",
        "text": "#000000",
        "bar": "#E0E0E0",
        "marker": "#FF0000",
    },
}

tableDataProjects = [
    {"label": "On Track", "value": 85},
    {"label": "At Risk", "value": 45},
    {"label": "Delayed", "value": 25},
    {"label": "Completed", "value": 120},
]

data_projects = {
    "template": "CardFour",
    "title": "Project Status",
    "mainValue": "275",
    "subtitle": "Total Tasks Across Projects",
    "bars": tableDataProjects,
    "colorScheme": {
        "background": "#F8F9FA",
        "text": "#212529",
        "bar": "#17A2B8",
    },
}

tableDataSales = [
    {"label": "Q1", "value": 200000},
    {"label": "Q2", "value": 180000},
    {"label": "Q3", "value": 220000},
    {"label": "Q4", "value": 240000},
]

data_sales = {
    "template": "CardFour",
    "title": "Quarterly Sales",
    "bars": tableDataSales,
    "marker": 90,
    "markerLabel": "Avg. Sales",
    "colorScheme": {
        "background": "#FFFFFF",
        "text": "#333333",
        "bar": "#FFC107",
    },
}

tableData5 = [
    {"label": "Headcount", "value": "4,228"},
    {"label": "Directs", "value": "9"},
    {"label": "Org Depth", "value": "8"},
]

tableData6 = [
    {"label": "Height", "value": "6'3\"", "percentile": 50, "color": "#FF4500"},
    {"label": "Weight", "value": "190", "percentile": 50, "color": "#FF4500"},
    {"label": "Draft position", "value": "7", "percentile": 90, "color": "#1E90FF"},
]


# Functions to render the cards
def render_cards_1():
    import pandas as pd
    import streamlit as st

    df = pd.DataFrame({"Number of Exits": [10, 20, 15, 30, 25, 10, 20, 15, 0, 7]})

    # Optional
    col1, col2 = st.columns(2)

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
            color_scheme={
                "background": "#F3F4F6",
                "text": "#1F2937",
                "trend": "#B2FEF7",
            },
            key="card_2",
        )


# def render_cards_2():
#     card(data_3, key="card_3")
#     card(data_4, key="card_4")


# def render_cards_3():
#     card(data_5, key="card_5")
#     card(data_6, key="card_6")


# def render_cards_4():
#     card(data_7, key="card_7")
#     card(data_8, key="card_8")
#     card(data_projects, key="card_9")
#     card(data_sales, key="card_10")

dotPlots5 = [
    {
        "title": "Percentile Corporate Leaders",
        "subtitle": "50TH",
        "percentiles": [{"value": 50, "label": "50TH"}],
        "dots": [{"row": 1, "col": 2, "color": "#0000FF"}],
    },
    {
        "title": "Percentile Operations LOB Leaders",
        "subtitle": "50TH",
        "percentiles": [{"value": 50, "label": "50TH"}],
        "dots": [{"row": 2, "col": 3, "color": "#0000FF"}],
    },
    {
        "title": "Percentile SF Bay Area Leaders",
        "subtitle": "50TH",
        "percentiles": [{"value": 50, "label": "50TH"}],
        "dots": [{"row": 2, "col": 3, "color": "#0000FF"}],
    },
]

dotPlots6 = [
    {
        "title": "Vitals",
        "subtitle": "Height, Weight, Draft Position",
        "percentiles": [
            {"value": 50, "label": "50TH"},  # Example percentile marker
            {"value": 90, "label": "90TH"},
        ],
        "dots": [
            {"row": 1, "col": 2, "color": "#FF4500"},  # Height percentile dot
            {"row": 2, "col": 2, "color": "#FF4500"},  # Weight percentile dot
            {"row": 3, "col": 4, "color": "#1E90FF"},  # Draft position percentile dot
        ],
    },
    {
        "title": "Scoring",
        "subtitle": "True Shooting %, Free Throw %, Usage %",
        "percentiles": [
            {"value": 70, "label": "70TH"},
            {"value": 95, "label": "95TH"},
            {"value": 80, "label": "80TH"},
        ],
        "dots": [
            {"row": 1, "col": 3, "color": "#1E90FF"},  # True shooting %
            {"row": 2, "col": 5, "color": "#1E90FF"},  # Free throw %
            {"row": 3, "col": 4, "color": "#1E90FF"},  # Usage %
        ],
    },
    {
        "title": "Tendencies",
        "subtitle": "3 pt. Frequency, FT Frequency",
        "percentiles": [
            {"value": 60, "label": "60TH"},
            {"value": 50, "label": "50TH"},
        ],
        "dots": [
            {"row": 1, "col": 3, "color": "#1E90FF"},  # 3 pt. frequency
            {"row": 2, "col": 2, "color": "#FFFFFF"},  # FT frequency
        ],
    },
]


def render_cards_5():
    stac(
        template="CardFive",
        title="Organization Data",
        table_data=tableData5,
        dot_plots=dotPlots5,
        color_scheme={"background": "#FFFFFF", "text": "#000000", "dot": "#0000FF"},
        key="card_11",
    )

    stac(
        template="CardFive",
        title="Player Stats Last Three Seasons",
        table_data=tableData6,
        dot_plots=dotPlots6,
        color_scheme={"background": "#FFFFFF", "text": "#000000", "dot": "#1E90FF"},
        key="card_12",
    )
