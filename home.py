from streamlit_extras.let_it_rain import rain
import streamlit as st
from streamlit_extras.buy_me_a_coffee import button
from streamlit_extras.card import card
from streamlit_image_coordinates import streamlit_image_coordinates
from streamlit_extras.mention import mention
from streamlit_extras.stodo import to_do
import pandas as pd
import streamlit as st

value = streamlit_image_coordinates("ai wheat.jpg")

st.write(value)

card(
        title="Hello World!",
        text="Some description",
        image="http://placekitten.com/300/250",
        url="https://www.google.com",
    )
rain(
        emoji="🎈",
        font_size=54,
        falling_speed=5,
        animation_length=1,
    )
button(username="fake-username", floating=False, width=221)

mention(
        label="powerd by",
        icon="github",  # Some icons are available... like Streamlit!
        url="https://extras.streamlitapp.com",
)

to_do(
        [(st.write, "☕ Take my coffee")],
        "coffee",
)
to_do(
        [(st.write, "🥞 Have a nice breakfast")],
        "pancakes",
)
to_do(
        [(st.write, ":train: Go to work!")],
        "work",
)

from annotated_text import annotated_text

annotated_text(
    "This ",
    ("is", "verb"),
    " some ",
    ("annotated", "adj"),
    ("text", "noun"),
    " for those of ",
    ("you", "pronoun"),
    " who ",
    ("like", "verb"),
    " this sort of ",
    ("thing", "noun"),
    "."
)
