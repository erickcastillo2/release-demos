import numpy as np
import streamlit as st
from streamlit_extras.markdownlit import mdlit
from streamlit_extras.switch_page_button import switch_page

TITLE = "Streamlit theme for Altair charts!"
ICON = "🎨"

st.set_page_config(page_title=TITLE, page_icon=ICON)
st.title(ICON + " " + TITLE)
ALTAIR_ICON_URL = "https://avatars.githubusercontent.com/u/22396732?s=200&v=4"

mdlit(
    f"""Welcome! 👋

This is a demo app for the 1.16 release of Streamlit, focusing on showcasing the new Streamlit theme for Altair charts! We collected a bunch of example charts from @(Altair's docs)(https://altair-viz.github.io/gallery/index.html) to show you how the charts look with/without Streamlit theme. \n

👈 Check them out by browsing the pages in the sidebar!
"""
)

show = st.button("I'm lazy!")
if show:
    new_page = np.random.choice(
        [
            "Horizontal Stacked Bar Chart",
            "Bar Chart With Mean Line",
            "Layered Bar Chart",
            "Iowa Electricity",
            "Scatter Marginal Hist",
            "Simple Stacked Area Chart",
        ]
    )
    switch_page(new_page)

mdlit(
    """
Read more in the dedicated @(streamlit)(Streamlit blog post)(https://blog.streamlit.io/).

Oh and if you liked this demo, you might as well like our @(👯)(twin demo for Plotly)(https://plotly.streamlit.app)!\n
"""
)
