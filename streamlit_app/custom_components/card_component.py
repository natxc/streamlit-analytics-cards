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


# Functions to render the cards
def render_cards_1():
    my_component(data_1, key="card_1")
    my_component(data_2, key="card_2")


def render_cards_2():
    my_component(data_3, key="card_3")
    my_component(data_4, key="card_4")


def render_cards_3():
    my_component(data_5, key="card_5")
    my_component(data_6, key="card_6")


def render_cards_4():
    my_component(data_7, key="card_7")
    my_component(data_8, key="card_8")
    my_component(data_projects, key="card_9")
    my_component(data_sales, key="card_10")
