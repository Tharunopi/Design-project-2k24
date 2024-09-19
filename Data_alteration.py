import streamlit as st
import pandas as pd


options = st.multiselect(
    "Select dataset visualize",
    ["Dataset 1", "Dataset 2"],
)

def dataset1():
    st.title("Dataset 1")
    df = pd.read_csv(r"E:\Dataset\crop yield data sheet.csv")
    df = df.dropna()

    
    edited_df = st.data_editor(df,
                          column_config={
        "Yeild (Q/acre)": st.column_config.ProgressColumn(
            "Yield (Q/acre)",
            width="medium",
            format="%f",
            help="Total amount of yield",
            min_value=0,
            max_value=22,
         ),
        },
        hide_index=True,)

    st.divider()

    col1, col2 = st.columns(2)
    col1.subheader("Vega Lite Chart")
    col1.vega_lite_chart(df, {
        "mark": {"type": "circle", "tooltip": True},
        "encoding": {
        "x": {"field": "Rain Fall (mm)", "type": "quantitative"},
        "y": {"field": "Yeild (Q/acre)", "type": "quantitative"},
        "size": {"field": "Fertilizer", "type": "quantitative"},
        "color": {"field": "Temperatue", "type": "quantitative"},
        "tooltip": [
            {"field": "Rain Fall (mm)", "type": "quantitative"},
            {"field": "Fertilizer", "type": "quantitative"},
            {"field": "Temperatue", "type": "quantitative"},
            {"field": "Yeild (Q/acre)", "type": "quantitative"},
        ]
        }
    })

    col2.subheader("Area chart")
    col2.area_chart(df[["Fertilizer", "Yeild (Q/acre)"]])

    st.subheader("About dataset 1")
    tab1, tab2, tab3 = st.tabs(["Overview", "Features", "Potential Uses"])
    with tab1:
        st.markdown('''The dataset appears to contain agricultural data related to crop yield. It includes various features that might affect the yield of crops. The dataset is likely used for analyzing the relationship between these features and the crop yield.''')

    with tab2:
        st.markdown('''Rain Fall (mm): The amount of rainfall in millimeters. This represents the total precipitation received during the growing period of the crops. Rainfall is a critical factor in crop production, influencing plant growth and yield.

Fertilizer: The amount of fertilizer applied. Fertilizers are essential for providing nutrients that plants need to grow. The dataset records this in kilograms per hectare or another unit, depending on the data source.

Temperatue: The temperature during the growing period. Temperature affects plant metabolism, growth, and yield. It is important for determining the optimal conditions for crop production.

Nitrogen (N): The amount of nitrogen applied or present in the soil. Nitrogen is a crucial nutrient for plant growth and is often a significant factor in determining crop yield.

Phosphorus (P): The amount of phosphorus applied or present in the soil. Phosphorus supports root development and energy transfer within plants, impacting crop yield.

Potassium (K): The amount of potassium applied or present in the soil. Potassium is vital for plant health, affecting water regulation and enzyme activation, which in turn influences crop yield.

Yeild (Q/acre): The crop yield measured in quintals per acre. This is the target variable, representing the quantity of crops harvested per unit area.''')

    with tab3:
        st.markdown('''Analysis: The dataset can be used to analyze how different factors like rainfall, fertilizer application, and temperature affect crop yield.
Modeling: It can be utilized to build predictive models to forecast crop yield based on the provided features.
Optimization: Farmers and agricultural experts can use the insights gained from this dataset to optimize their farming practices, including adjusting fertilizer amounts, managing water resources, and controlling temperature conditions.''')

def dataset2():
    st.title("Dataset 2")
    df = pd.read_csv(r"E:\Dataset\ICRISAT-District Level Data.csv")
    df = df.dropna()

    
    edited_df = st.data_editor(df,
                          column_config={
        "RICE YIELD (Kg per ha)": st.column_config.ProgressColumn(
            "RICE YIELD (Kg per ha)",
            width="medium",
            format="%f",
            help="Yield kg/ha",
            min_value=0,
            max_value=2000,
         ),
        },
        hide_index=True,)

    st.divider()

    col1, col2 = st.columns(2)
    col1.subheader("Vega Lite Chart")
    col1.vega_lite_chart(df, {
        "mark": {"type": "circle", "tooltip": True},
        "encoding": {
        "x": {"field": "RICE AREA (1000 ha)", "type": "quantitative"},
        "y": {"field": "RICE YIELD (Kg per ha)", "type": "quantitative"},
        "size": {"field": "Year", "type": "quantitative"},
        "color": {"field": "State Code", "type": "quantitative"},
        "tooltip": [
            {"field": "RICE AREA (1000 ha)", "type": "quantitative"},
            {"field": "RICE YIELD (Kg per ha)", "type": "quantitative"},
            {"field": "Year", "type": "quantitative"},
            {"field": "State Code", "type": "quantitative"},
        ]
        }
    })

    col2.subheader("Area chart")
    col2.area_chart(df[["RICE AREA (1000 ha)", "RICE YIELD (Kg per ha)"]])

    st.subheader("About dataset 2")
    tab1, tab2, tab3 = st.tabs(["Overview", "Features", "Potential Uses"])

    with tab1:
        st.markdown('''The dataset appears to be related to rice production in different districts of a state, possibly within India. It includes information on rice cultivation area and yield over multiple years. This dataset is useful for analyzing trends in rice production and understanding regional variations in yield.''')

    with tab2:
        st.markdown('''Dist Code: District code. This is a numerical identifier for the district where the data was collected.

Year: The year in which the data was recorded. This allows for temporal analysis and trend identification.

State Code: Code representing the state in which the district is located. This numerical code helps in categorizing data by state.

State Name: Name of the state where the district is located. This provides a more readable format for identifying the geographical location of the data.

Dist Name: District name. This is the name of the district within the state where the data was collected.

RICE AREA (1000 ha): The area under rice cultivation, measured in thousands of hectares. This indicates the scale of rice farming in each district.

RICE YIELD (Kg per ha): The yield of rice per hectare, measured in kilograms. This is the amount of rice produced per unit area and serves as the target variable for analyzing productivity.''')

    with tab3:
        st.markdown('''Trend Analysis: Analyze how rice production area and yield have changed over the years in different districts and states.
        
Regional Comparison: Compare rice yield and cultivation area between different districts and states to identify high and low-performing regions.

Predictive Modeling: Build models to predict future rice yields based on historical data and area under cultivation.

Policy Making: Assist policymakers in understanding regional rice production trends and making informed decisions on resource allocation and support.''')
    
if "Dataset 1" in options:
    dataset1()

if "Dataset 2" in options:
    dataset2()