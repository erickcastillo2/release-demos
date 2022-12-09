import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import inspect

@st.experimental_memo
def get_chart_84517131():
    import plotly.express as px
    df = px.data.tips()
    fig = px.bar(df, x="total_bill", y="day", orientation='h')
    
    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_84517131))
    get_chart_84517131()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_34891977():
    import plotly.express as px
    df = px.data.tips()
    fig = px.bar(df, x="total_bill", y="sex", color='day', orientation='h',
                 hover_data=["tip", "size"],
                 height=400,
                 title='Restaurant bills')
    
    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_34891977))
    get_chart_34891977()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_48913275():
    import plotly.graph_objects as go
    
    fig = go.Figure(go.Bar(
                x=[20, 14, 23],
                y=['giraffes', 'orangutans', 'monkeys'],
                orientation='h'))
    
    
    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_48913275))
    get_chart_48913275()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_44789842():
    import plotly.graph_objects as go
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=['giraffes', 'orangutans', 'monkeys'],
        x=[20, 14, 23],
        name='SF Zoo',
        orientation='h',
        marker=dict(
            color='rgba(246, 78, 139, 0.6)',
            line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
        )
    ))
    fig.add_trace(go.Bar(
        y=['giraffes', 'orangutans', 'monkeys'],
        x=[12, 18, 29],
        name='LA Zoo',
        orientation='h',
        marker=dict(
            color='rgba(58, 71, 80, 0.6)',
            line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
        )
    ))
    
    fig.update_layout(barmode='stack')
    
    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_44789842))
    get_chart_44789842()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_46973499():
    import plotly.graph_objects as go
    
    top_labels = ['Strongly<br>agree', 'Agree', 'Neutral', 'Disagree',
                  'Strongly<br>disagree']
    
    colors = ['rgba(38, 24, 74, 0.8)', 'rgba(71, 58, 131, 0.8)',
              'rgba(122, 120, 168, 0.8)', 'rgba(164, 163, 204, 0.85)',
              'rgba(190, 192, 213, 1)']
    
    x_data = [[21, 30, 21, 16, 12],
              [24, 31, 19, 15, 11],
              [27, 26, 23, 11, 13],
              [29, 24, 15, 18, 14]]
    
    y_data = ['The course was effectively<br>organized',
              'The course developed my<br>abilities and skills ' +
              'for<br>the subject', 'The course developed ' +
              'my<br>ability to think critically about<br>the subject',
              'I would recommend this<br>course to a friend']
    
    fig = go.Figure()
    
    for i in range(0, len(x_data[0])):
        for xd, yd in zip(x_data, y_data):
            fig.add_trace(go.Bar(
                x=[xd[i]], y=[yd],
                orientation='h',
                marker=dict(
                    color=colors[i],
                    line=dict(color='rgb(248, 248, 249)', width=1)
                )
            ))
    
    fig.update_layout(
        xaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=False,
            zeroline=False,
            domain=[0.15, 1]
        ),
        yaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=False,
            zeroline=False,
        ),
        barmode='stack',
        paper_bgcolor='rgb(248, 248, 255)',
        plot_bgcolor='rgb(248, 248, 255)',
        margin=dict(l=120, r=10, t=140, b=80),
        showlegend=False,
    )
    
    annotations = []
    
    for yd, xd in zip(y_data, x_data):
        # labeling the y-axis
        annotations.append(dict(xref='paper', yref='y',
                                x=0.14, y=yd,
                                xanchor='right',
                                text=str(yd),
                                font=dict(family='Arial', size=14,
                                          color='rgb(67, 67, 67)'),
                                showarrow=False, align='right'))
        # labeling the first percentage of each bar (x_axis)
        annotations.append(dict(xref='x', yref='y',
                                x=xd[0] / 2, y=yd,
                                text=str(xd[0]) + '%',
                                font=dict(family='Arial', size=14,
                                          color='rgb(248, 248, 255)'),
                                showarrow=False))
        # labeling the first Likert scale (on the top)
        if yd == y_data[-1]:
            annotations.append(dict(xref='x', yref='paper',
                                    x=xd[0] / 2, y=1.1,
                                    text=top_labels[0],
                                    font=dict(family='Arial', size=14,
                                              color='rgb(67, 67, 67)'),
                                    showarrow=False))
        space = xd[0]
        for i in range(1, len(xd)):
                # labeling the rest of percentages for each bar (x_axis)
                annotations.append(dict(xref='x', yref='y',
                                        x=space + (xd[i]/2), y=yd,
                                        text=str(xd[i]) + '%',
                                        font=dict(family='Arial', size=14,
                                                  color='rgb(248, 248, 255)'),
                                        showarrow=False))
                # labeling the Likert scale
                if yd == y_data[-1]:
                    annotations.append(dict(xref='x', yref='paper',
                                            x=space + (xd[i]/2), y=1.1,
                                            text=top_labels[i],
                                            font=dict(family='Arial', size=14,
                                                      color='rgb(67, 67, 67)'),
                                            showarrow=False))
                space += xd[i]
    
    fig.update_layout(annotations=annotations)
    
    
    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_46973499))
    get_chart_46973499()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_53001787():
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    
    import numpy as np
    
    y_saving = [1.3586, 2.2623000000000002, 4.9821999999999997, 6.5096999999999996,
                7.4812000000000003, 7.5133000000000001, 15.2148, 17.520499999999998
                ]
    y_net_worth = [93453.919999999998, 81666.570000000007, 69889.619999999995,
                   78381.529999999999, 141395.29999999999, 92969.020000000004,
                   66090.179999999993, 122379.3]
    x = ['Japan', 'United Kingdom', 'Canada', 'Netherlands',
         'United States', 'Belgium', 'Sweden', 'Switzerland']
    
    
    # Creating two subplots
    fig = make_subplots(rows=1, cols=2, specs=[[{}, {}]], shared_xaxes=True,
                        shared_yaxes=False, vertical_spacing=0.001)
    
    fig.append_trace(go.Bar(
        x=y_saving,
        y=x,
        marker=dict(
            color='rgba(50, 171, 96, 0.6)',
            line=dict(
                color='rgba(50, 171, 96, 1.0)',
                width=1),
        ),
        name='Household savings, percentage of household disposable income',
        orientation='h',
    ), 1, 1)
    
    fig.append_trace(go.Scatter(
        x=y_net_worth, y=x,
        mode='lines+markers',
        line_color='rgb(128, 0, 128)',
        name='Household net worth, Million USD/capita',
    ), 1, 2)
    
    fig.update_layout(
        title='Household savings & net worth for eight OECD countries',
        yaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=True,
            domain=[0, 0.85],
        ),
        yaxis2=dict(
            showgrid=False,
            showline=True,
            showticklabels=False,
            linecolor='rgba(102, 102, 102, 0.8)',
            linewidth=2,
            domain=[0, 0.85],
        ),
        xaxis=dict(
            zeroline=False,
            showline=False,
            showticklabels=True,
            showgrid=True,
            domain=[0, 0.42],
        ),
        xaxis2=dict(
            zeroline=False,
            showline=False,
            showticklabels=True,
            showgrid=True,
            domain=[0.47, 1],
            side='top',
            dtick=25000,
        ),
        legend=dict(x=0.029, y=1.038, font_size=10),
        margin=dict(l=100, r=20, t=70, b=70),
        paper_bgcolor='rgb(248, 248, 255)',
        plot_bgcolor='rgb(248, 248, 255)',
    )
    
    annotations = []
    
    y_s = np.round(y_saving, decimals=2)
    y_nw = np.rint(y_net_worth)
    
    # Adding labels
    for ydn, yd, xd in zip(y_nw, y_s, x):
        # labeling the scatter savings
        annotations.append(dict(xref='x2', yref='y2',
                                y=xd, x=ydn - 20000,
                                text='{:,}'.format(ydn) + 'M',
                                font=dict(family='Arial', size=12,
                                          color='rgb(128, 0, 128)'),
                                showarrow=False))
        # labeling the bar net worth
        annotations.append(dict(xref='x1', yref='y1',
                                y=xd, x=yd + 3,
                                text=str(yd) + '%',
                                font=dict(family='Arial', size=12,
                                          color='rgb(50, 171, 96)'),
                                showarrow=False))
    # Source
    annotations.append(dict(xref='paper', yref='paper',
                            x=-0.2, y=-0.109,
                            text='OECD "' +
                                 '(2015), Household savings (indicator), ' +
                                 'Household net worth (indicator). doi: ' +
                                 '10.1787/cfc6f499-en (Accessed on 05 June 2015)',
                            font=dict(family='Arial', size=10, color='rgb(150,150,150)'),
                            showarrow=False))
    
    fig.update_layout(annotations=annotations)
    
    
    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_53001787))
    get_chart_53001787()
except Exception as e:
    st.exception(e)

