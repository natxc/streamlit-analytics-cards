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


# Functions to render the cards
def render_cards():
    my_component(data_1, key="card_1")
    my_component(data_2, key="card_2")
