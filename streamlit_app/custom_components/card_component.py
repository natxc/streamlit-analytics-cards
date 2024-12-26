from custom_components import my_component

# Define data for the cards
data_1 = {
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

data_2 = {
    "template": "CardOne",
    "title": "Revenue Growth",
    "subtitle": "Quarterly Performance",
    "mainValue": "$1.2M",
    "secondaryValue": "35% Increase",
    "trendValue": "Y/Y +10%",
    "chartData": [15, 25, 20, 40, 35],
    "colorScheme": {
        "background": "#F3F4F6",
        "text": "#1F2937",
        "trend": "#34D399",
    },
}

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


# Functions to render the cards
def render_cards_1():
    my_component(data_1, key="card_1")
    my_component(data_2, key="card_2")


def render_cards_2():
    my_component(data_3, key="card_3")
    my_component(data_4, key="card_4")
