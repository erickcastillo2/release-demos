import streamlit as st
import altair as alt
import inspect
from vega_datasets import data

@st.experimental_memo
def get_chart_35124(use_container_width: bool):
    import altair as alt
    from vega_datasets import data
    
    source = data.iowa_electricity()
    
    chart = alt.Chart(source, title="Iowa's renewable energy boom").mark_area().encode(
        x=alt.X(
            "year:T",
            title="Year"
        ),
        y=alt.Y(
            "net_generation:Q",
            stack="normalize",
            title="Share of net generation",
            axis=alt.Axis(format=".0%"),
        ),
        color=alt.Color(
            "source:N",
            legend=alt.Legend(title="Electricity source"),
        )
    )
    
    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])
    
    with tab1:
        st.altair_chart(chart, theme="streamlit", use_container_width=True)
    with tab2:
        st.altair_chart(chart, theme=None, use_container_width=True)

try:
    st.expander("See code").code(inspect.getsource(get_chart_35124))
    get_chart_35124(use_container_width=True)
except Exception as e:
    st.exception(e)

