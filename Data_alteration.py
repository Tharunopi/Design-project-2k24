import streamlit as st
import pandas as pd


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