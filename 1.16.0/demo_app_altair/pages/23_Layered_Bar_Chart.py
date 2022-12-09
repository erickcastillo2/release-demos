import streamlit as st
import altair as alt
import inspect
from vega_datasets import data

@st.experimental_memo
def get_chart_41714(use_container_width: bool):
    import altair as alt
    from vega_datasets import data
    
    source = data.iowa_electricity()
    
    chart = alt.Chart(source).mark_bar(opacity=0.7).encode(
        x='year:O',
        y=alt.Y('net_generation:Q', stack=None),
        color="source",
    )
    
    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])
    
    with tab1:
        st.altair_chart(chart, theme="streamlit", use_container_width=True)
    with tab2:
        st.altair_chart(chart, theme=None, use_container_width=True)

try:
    st.expander("See code").code(inspect.getsource(get_chart_41714))
    get_chart_41714(use_container_width=True)
except Exception as e:
    st.exception(e)

