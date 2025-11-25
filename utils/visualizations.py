"""
Data Visualization Utilities
Creates charts, graphs, and visual analytics for resume analysis
"""
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st
import io
import numpy as np


def create_match_gauge(percentage, title="ATS Match Score"):
    """
    Create a gauge chart for match percentage
    
    Args:
        percentage: Match percentage (0-100)
        title: Chart title
        
    Returns:
        plotly figure
    """
    # Determine color based on percentage
    if percentage >= 80:
        color = "#00C853"  # Green
    elif percentage >= 60:
        color = "#FFB300"  # Amber
    else:
        color = "#FF5252"  # Red
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=percentage,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': title, 'font': {'size': 24, 'color': '#1f1f1f'}},
        number={'suffix': "%", 'font': {'size': 40}},
        gauge={
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkgray"},
            'bar': {'color': color},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 40], 'color': '#FFEBEE'},
                {'range': [40, 70], 'color': '#FFF9C4'},
                {'range': [70, 100], 'color': '#E8F5E9'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ))
    
    fig.update_layout(
        height=300,
        margin=dict(l=20, r=20, t=60, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        font={'family': "Arial, sans-serif"}
    )
    
    return fig


def create_category_bars(categories_dict):
    """
    Create horizontal bar chart for category-wise scores
    
    Args:
        categories_dict: Dictionary with category names as keys and scores as values
        
    Returns:
        plotly figure
    """
    categories = list(categories_dict.keys())
    scores = list(categories_dict.values())
    
    # Color code based on score
    colors = ['#00C853' if s >= 70 else '#FFB300' if s >= 50 else '#FF5252' for s in scores]
    
    fig = go.Figure(go.Bar(
        x=scores,
        y=categories,
        orientation='h',
        marker=dict(
            color=colors,
            line=dict(color='rgba(0,0,0,0.3)', width=1)
        ),
        text=[f"{s}%" for s in scores],
        textposition='auto',
    ))
    
    fig.update_layout(
        title="Category-wise Match Analysis",
        xaxis_title="Match Percentage",
        yaxis_title="",
        height=400,
        margin=dict(l=20, r=20, t=60, b=40),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={'family': "Arial, sans-serif", 'size': 12},
        xaxis=dict(range=[0, 100], gridcolor='lightgray'),
        yaxis=dict(gridcolor='lightgray')
    )
    
    return fig


def create_skills_radar(skills_dict):
    """
    Create radar chart for skills assessment
    
    Args:
        skills_dict: Dictionary with skill names as keys and proficiency (0-10) as values
        
    Returns:
        plotly figure
    """
    categories = list(skills_dict.keys())
    values = list(skills_dict.values())
    
    # Close the radar chart
    categories_closed = categories + [categories[0]]
    values_closed = values + [values[0]]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values_closed,
        theta=categories_closed,
        fill='toself',
        fillcolor='rgba(0, 200, 83, 0.3)',
        line=dict(color='#00C853', width=2),
        name='Current Level'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10],
                tickmode='linear',
                tick0=0,
                dtick=2,
                gridcolor='lightgray'
            ),
            angularaxis=dict(gridcolor='lightgray')
        ),
        showlegend=False,
        title="Skills Assessment Radar",
        height=500,
        margin=dict(l=80, r=80, t=80, b=80),
        paper_bgcolor="rgba(0,0,0,0)",
        font={'family': "Arial, sans-serif"}
    )
    
    return fig


def create_wordcloud(text, title="Keywords"):
    """
    Create word cloud from text
    
    Args:
        text: Input text or list of keywords
        title: Chart title
        
    Returns:
        matplotlib figure
    """
    if isinstance(text, list):
        text = ' '.join(text)
    
    # Create word cloud
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        colormap='viridis',
        max_words=50,
        relative_scaling=0.5,
        min_font_size=10
    ).generate(text)
    
    # Create matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
    
    plt.tight_layout(pad=0)
    
    return fig


def create_comparison_table(resume1_scores, resume2_scores, categories):
    """
    Create comparison table for two resumes
    
    Args:
        resume1_scores: List of scores for resume 1
        resume2_scores: List of scores for resume 2
        categories: List of category names
        
    Returns:
        plotly figure
    """
    winners = []
    for s1, s2 in zip(resume1_scores, resume2_scores):
        if s1 > s2:
            winners.append("Resume 1")
        elif s2 > s1:
            winners.append("Resume 2")
        else:
            winners.append("Tie")
    
    fig = go.Figure(data=[go.Table(
        header=dict(
            values=['<b>Category</b>', '<b>Resume 1</b>', '<b>Resume 2</b>', '<b>Winner</b>'],
            fill_color='#00C853',
            align='center',
            font=dict(color='white', size=14, family='Arial')
        ),
        cells=dict(
            values=[
                categories,
                [f"{s}/10" for s in resume1_scores],
                [f"{s}/10" for s in resume2_scores],
                winners
            ],
            fill_color=[['#f0f0f0', 'white'] * len(categories)],
            align='center',
            font=dict(color='#1f1f1f', size=12, family='Arial'),
            height=30
        )
    )])
    
    fig.update_layout(
        title="Side-by-Side Comparison",
        height=400,
        margin=dict(l=20, r=20, t=60, b=20),
        paper_bgcolor="rgba(0,0,0,0)"
    )
    
    return fig


def create_progress_bar(percentage, label="Progress"):
    """
    Create a simple progress bar using Streamlit
    
    Args:
        percentage: Progress percentage (0-100)
        label: Label for the progress bar
    """
    # Determine color
    if percentage >= 80:
        color = "🟢"
    elif percentage >= 60:
        color = "🟡"
    else:
        color = "🔴"
    
    st.markdown(f"**{label}** {color}")
    st.progress(percentage / 100)
    st.markdown(f"**{percentage}%**")


def display_metric_cards(metrics_dict):
    """
    Display metrics in card format
    
    Args:
        metrics_dict: Dictionary with metric names and values
    """
    cols = st.columns(len(metrics_dict))
    
    for col, (label, value) in zip(cols, metrics_dict.items()):
        with col:
            st.metric(label=label, value=value)
