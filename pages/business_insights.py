import streamlit as st
import pandas as pd
import os
from pathlib import Path

# ============================================================================
# PAGE CONFIG
# ============================================================================

st.set_page_config(
    page_title="Business Insights | MovieLens Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CUSTOM CSS - NETFLIX THEME (Same as app.py)
# ============================================================================

st.markdown("""
<style>
    .stApp { background-color: #141414; }
    .main { background-color: #141414; }
    section[data-testid="stSidebar"] {
        background-color: #000000;
        border-right: 2px solid #E50914;
    }
    h1, h2, h3 { color: #FFFFFF !important; font-family: 'Helvetica Neue', Arial, sans-serif; }
    h1 { color: #E50914 !important; font-weight: 700; }
    p, li, span, div { color: #FFFFFF !important; }
    [data-testid="stMetricValue"] { color: #E50914 !important; font-size: 1.5rem !important; }
    .stButton button {
        background-color: #E50914;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 10px 24px;
        font-weight: 600;
    }
    .stButton button:hover { background-color: #F40612; }
    hr { border-color: #E50914 !important; opacity: 0.3; }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #1a1a1a;
        border-radius: 8px 8px 0 0;
    }
    
    .stTabs [data-baseweb="tab"] {
        color: #999 !important;
        background-color: transparent;
        border: none;
        padding: 1rem 2rem;
        font-weight: 600;
    }
    
    .stTabs [aria-selected="true"] {
        color: #E50914 !important;
        border-bottom: 3px solid #E50914;
    }
    
    .stTabs [data-baseweb="tab-panel"] {
        background-color: #141414;
        padding: 2rem 1rem;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# DATA LOADING
# ============================================================================

@st.cache_data
def load_summary_data():
    """Load all summary CSV files"""
    try:
        return {
            'platform_stats': pd.read_csv('assets/data/summary/platform_stats.csv'),
            'user_segments': pd.read_csv('assets/data/summary/user_segments.csv'),
            'yearly_trends': pd.read_csv('assets/data/summary/yearly_trends.csv'),
            'genre_stats': pd.read_csv('assets/data/summary/genre_stats.csv'),
            'hidden_gems': pd.read_csv('assets/data/summary/hidden_gems.csv'),
            'top_movies': pd.read_csv('assets/data/summary/top_movies.csv')
        }
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

def load_html_viz(filepath):
    """Load and display HTML visualization"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html_content = f.read()
        return html_content
    except Exception as e:
        st.error(f"Could not load visualization: {filepath}")
        st.error(f"Error: {e}")
        return None

# Load data
data = load_summary_data()

# ============================================================================
# HEADER
# ============================================================================

st.markdown("""
<div style='text-align: center; padding: 1.5rem 0;'>
    <h1 style='font-size: 3rem;'>📊 BUSINESS INSIGHTS & ANALYTICS</h1>
    <p style='font-size: 1.1rem; color: #999;'>
        Comprehensive Analysis of 33.8M Ratings | 331K Users | 86K Movies
    </p>
</div>
<hr>
""", unsafe_allow_html=True)

# ============================================================================
# SUMMARY METRICS
# ============================================================================

if data:
    col1, col2, col3, col4, col5 = st.columns(5)
    
    platform_stats = data['platform_stats'].iloc[0]
    
    with col1:
        st.metric("Total Ratings", platform_stats['total_ratings'])
    with col2:
        st.metric("Active Users", platform_stats['total_users'])
    with col3:
        st.metric("Movies", platform_stats['total_movies'])
    with col4:
        st.metric("Avg Rating", f"{platform_stats['avg_rating']:.2f}★")
    with col5:
        st.metric("Hidden Gems", f"{len(data['hidden_gems'])}")

st.markdown("<hr>", unsafe_allow_html=True)

# ============================================================================
# TABBED INTERFACE
# ============================================================================

tabs = st.tabs([
    "👥 User Behavior", 
    "🎬 Content Performance", 
    "💎 Hidden Gems",
    "🎭 User Personas",
    "📥 Export Data"
])

# ============================================================================
# TAB 1: USER BEHAVIOR
# ============================================================================

with tabs[0]:
    st.markdown("<h2>👥 User Behavior Analysis</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background-color: #1a1a1a; padding: 1rem; border-radius: 8px; margin-bottom: 2rem;'>
        <p style='font-size: 1.05rem;'>
        Understanding user rating patterns, temporal trends, and engagement behaviors across our platform.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # User Behavior Overview
    st.markdown("### 📊 User Rating Distribution")
    html_content = load_html_viz('assets/visualizations/user_behavior/overview.html')
    if html_content:
        st.components.v1.html(html_content, height=550, scrolling=False)
    
    st.markdown("<hr style='margin: 2rem 0;'>", unsafe_allow_html=True)
    
    # Temporal Trends
    st.markdown("### 📈 Rating Trends Over Time (1995-2023)")
    html_content = load_html_viz('assets/visualizations/user_behavior/temporal_trends.html')
    if html_content:
        st.components.v1.html(html_content, height=850, scrolling=False)
    
    st.markdown("<hr style='margin: 2rem 0;'>", unsafe_allow_html=True)
    
    # User Retention
    st.markdown("### 🔄 User Retention Analysis")
    html_content = load_html_viz('assets/visualizations/user_behavior/retention.html')
    if html_content:
        st.components.v1.html(html_content, height=550, scrolling=False)
    
    st.markdown("<hr style='margin: 2rem 0;'>", unsafe_allow_html=True)
    
    # Activity Patterns
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📅 Monthly Activity Patterns")
        html_content = load_html_viz('assets/visualizations/user_behavior/monthly_patterns.html')
        if html_content:
            st.components.v1.html(html_content, height=550, scrolling=False)
    
    with col2:
        st.markdown("### 🕐 Hourly Activity Patterns")
        html_content = load_html_viz('assets/visualizations/user_behavior/hourly_patterns.html')
        if html_content:
            st.components.v1.html(html_content, height=550, scrolling=False)
    
    # Key Insights
    st.markdown("<hr style='margin: 2rem 0;'>", unsafe_allow_html=True)
    st.markdown("### 🎯 Key Insights")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style='background-color: #1a1a1a; padding: 1.5rem; border-radius: 8px; border-left: 4px solid #E50914;'>
            <h4>User Segments</h4>
            <p>• Harsh Raters: <strong>8.5%</strong></p>
            <p>• Neutral Raters: <strong>73.2%</strong></p>
            <p>• Generous Raters: <strong>18.3%</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background-color: #1a1a1a; padding: 1.5rem; border-radius: 8px; border-left: 4px solid #E50914;'>
            <h4>Peak Activity</h4>
            <p>• Time: <strong>8-10 PM</strong></p>
            <p>• Day: <strong>Weekdays</strong></p>
            <p>• Month: <strong>October</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='background-color: #1a1a1a; padding: 1.5rem; border-radius: 8px; border-left: 4px solid #E50914;'>
            <h4>Trends</h4>
            <p>• 28-year history</p>
            <p>• Steady growth since 1995</p>
            <p>• Peak: 2016-2018</p>
        </div>
        """, unsafe_allow_html=True)

# ============================================================================
# TAB 2: CONTENT PERFORMANCE
# ============================================================================

with tabs[1]:
    st.markdown("<h2>🎬 Content Performance & Tag Analysis</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background-color: #1a1a1a; padding: 1rem; border-radius: 8px; margin-bottom: 2rem;'>
        <p style='font-size: 1.05rem;'>
        Analyzing genre performance, user-generated tags, and release year impact on ratings.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Genre Performance
    st.markdown("### 🎭 Genre Performance Analysis")
    html_content = load_html_viz('assets/visualizations/content_performance/genre_performance.html')
    if html_content:
        st.components.v1.html(html_content, height=700, scrolling=False)
    else:
        st.warning("Genre performance visualization not found. Check file path.")
    
    st.markdown("<hr style='margin: 2rem 0;'>", unsafe_allow_html=True)
    
    # Tag Analysis
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 🏷️ Tag Sentiment Analysis")
        html_content = load_html_viz('assets/visualizations/content_performance/tag_sentiment.html')
        if html_content:
            st.components.v1.html(html_content, height=550, scrolling=False)
    
    with col2:
        st.markdown("### ☁️ Popular Movie Tags")
        try:
            st.image('assets/visualizations/content_performance/tag_wordcloud.png', use_container_width=True)
        except:
            st.warning("Word cloud image not found.")
    
    st.markdown("<hr style='margin: 2rem 0;'>", unsafe_allow_html=True)
    
    # Release Year Impact
    st.markdown("### 📅 Release Year Impact Analysis")
    html_content = load_html_viz('assets/visualizations/content_performance/release_year_impact.html')
    if html_content:
        st.components.v1.html(html_content, height=900, scrolling=False)
    
    st.markdown("<hr style='margin: 2rem 0;'>", unsafe_allow_html=True)
    
    # Polarization Analysis
    st.markdown("### 📊 Movie Polarization Analysis")
    html_content = load_html_viz('assets/visualizations/content_performance/polarization.html')
    if html_content:
        st.components.v1.html(html_content, height=650, scrolling=False)
    
    # Key Insights
    st.markdown("<hr style='margin: 2rem 0;'>", unsafe_allow_html=True)
    st.markdown("### 🎯 Key Insights")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style='background-color: #1a1a1a; padding: 1.5rem; border-radius: 8px; border-left: 4px solid #E50914;'>
            <h4>Top Genres</h4>
            <p>• Film-Noir: <strong>4.00★</strong></p>
            <p>• Documentary: <strong>3.95★</strong></p>
            <p>• War: <strong>3.93★</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background-color: #1a1a1a; padding: 1.5rem; border-radius: 8px; border-left: 4px solid #E50914;'>
            <h4>Golden Era</h4>
            <p>• Best decade: <strong>1940s</strong></p>
            <p>• Peak rating: <strong>3.85★</strong></p>
            <p>• Classic cinema dominance</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='background-color: #1a1a1a; padding: 1.5rem; border-radius: 8px; border-left: 4px solid #E50914;'>
            <h4>Tag Insights</h4>
            <p>• Positive tags: <strong>2.2%</strong></p>
            <p>• Neutral tags: <strong>96.5%</strong></p>
            <p>• Negative tags: <strong>1.3%</strong></p>
        </div>
        """, unsafe_allow_html=True)

# ============================================================================
# TAB 3: HIDDEN GEMS
# ============================================================================

with tabs[2]:
    st.markdown("<h2>💎 Hidden Gems Discovery</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background-color: #1a1a1a; padding: 1rem; border-radius: 8px; margin-bottom: 2rem;'>
        <p style='font-size: 1.05rem;'>
        High-quality movies (≥4.0★) with low visibility (10-100 ratings) - perfect for curation and promotion.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Hidden Gems Visualization
    st.markdown("### 🏆 Top Hidden Gems")
    html_content = load_html_viz('assets/visualizations/hidden_gems/gems_analysis.html')
    if html_content:
        st.components.v1.html(html_content, height=800, scrolling=False)
    
    st.markdown("<hr style='margin: 2rem 0;'>", unsafe_allow_html=True)
    
    # Hidden Gems Table
    if data and 'hidden_gems' in data:
        st.markdown("### 📋 Hidden Gems Database")
        
        hidden_gems_df = data['hidden_gems'].head(50)
        
        st.dataframe(
            hidden_gems_df[['title', 'genres', 'release_year', 'avg_rating', 'num_ratings']],
            use_container_width=True,
            height=400
        )
        
        st.markdown("<hr style='margin: 2rem 0;'>", unsafe_allow_html=True)
        
        # Statistics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Hidden Gems", len(data['hidden_gems']))
        with col2:
            st.metric("Avg Rating", f"{data['hidden_gems']['avg_rating'].mean():.2f}★")
        with col3:
            st.metric("Avg Reviews", f"{data['hidden_gems']['num_ratings'].mean():.0f}")
        with col4:
            top_genre = data['hidden_gems']['genres'].str.split('|').explode().value_counts().index[0]
            st.metric("Top Genre", top_genre)

# ============================================================================
# TAB 4: USER PERSONAS
# ============================================================================

with tabs[3]:
    st.markdown("<h2>🎭 User Personas & Segmentation</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background-color: #1a1a1a; padding: 1rem; border-radius: 8px; margin-bottom: 2rem;'>
        <p style='font-size: 1.05rem;'>
        K-Means clustering analysis revealing distinct user segments based on genre preferences.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # User Personas Visualization
    st.markdown("### 🎨 User Persona Distribution")
    html_content = load_html_viz('assets/visualizations/user_personas/persona_clusters.html')
    if html_content:
        st.components.v1.html(html_content, height=800, scrolling=False)
    
    st.markdown("<hr style='margin: 2rem 0;'>", unsafe_allow_html=True)
    
    # Persona Descriptions
    st.markdown("### 📊 Persona Profiles")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style='background-color: #1a1a1a; padding: 1.5rem; border-radius: 8px; margin-bottom: 1rem;'>
            <h4>🎭 Drama Enthusiasts (27.0%)</h4>
            <p>Prefers: Drama, Romance, Thriller</p>
            <p>Characteristics: Emotional, character-driven stories</p>
        </div>
        
        <div style='background-color: #1a1a1a; padding: 1.5rem; border-radius: 8px; margin-bottom: 1rem;'>
            <h4>🎬 Mainstream Viewers (25.1%)</h4>
            <p>Prefers: Comedy, Drama, Action</p>
            <p>Characteristics: Popular, accessible content</p>
        </div>
        
        <div style='background-color: #1a1a1a; padding: 1.5rem; border-radius: 8px;'>
            <h4>🚀 Sci-Fi Fans (10.0%)</h4>
            <p>Prefers: Sci-Fi, Action, Fantasy</p>
            <p>Characteristics: Speculative, futuristic themes</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background-color: #1a1a1a; padding: 1.5rem; border-radius: 8px; margin-bottom: 1rem;'>
            <h4>🎨 Art House Lovers (28.4%)</h4>
            <p>Prefers: Documentary, Film-Noir, Independent</p>
            <p>Characteristics: Intellectual, artistic films</p>
        </div>
        
        <div style='background-color: #1a1a1a; padding: 1.5rem; border-radius: 8px; margin-bottom: 1rem;'>
            <h4>👨‍👩‍👧‍👦 Family Oriented (9.5%)</h4>
            <p>Prefers: Animation, Children, Comedy</p>
            <p>Characteristics: All-ages, wholesome content</p>
        </div>
        
        <div style='background-color: #1a1a1a; padding: 1.5rem; border-radius: 8px;'>
            <h4>💡 Strategic Value</h4>
            <p>Enable persona-specific homepage experiences</p>
            <p>Expected impact: 15-25% engagement increase</p>
        </div>
        """, unsafe_allow_html=True)

# ============================================================================
# TAB 5: EXPORT DATA
# ============================================================================

with tabs[4]:
    st.markdown("<h2>📥 Export & Download Data</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background-color: #1a1a1a; padding: 1rem; border-radius: 8px; margin-bottom: 2rem;'>
        <p style='font-size: 1.05rem;'>
        Download summary data and insights for further analysis or reporting.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if data:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📊 Available Datasets")
            
            st.download_button(
                label="📈 Platform Statistics",
                data=data['platform_stats'].to_csv(index=False),
                file_name="platform_stats.csv",
                mime="text/csv"
            )
            
            st.download_button(
                label="👥 User Segments",
                data=data['user_segments'].to_csv(index=False),
                file_name="user_segments.csv",
                mime="text/csv"
            )
            
            st.download_button(
                label="📅 Yearly Trends",
                data=data['yearly_trends'].to_csv(index=False),
                file_name="yearly_trends.csv",
                mime="text/csv"
            )
        
        with col2:
            st.markdown("### 🎬 Content Data")
            
            st.download_button(
                label="🎭 Genre Statistics",
                data=data['genre_stats'].to_csv(index=False),
                file_name="genre_stats.csv",
                mime="text/csv"
            )
            
            st.download_button(
                label="💎 Hidden Gems",
                data=data['hidden_gems'].to_csv(index=False),
                file_name="hidden_gems.csv",
                mime="text/csv"
            )
            
            st.download_button(
                label="🏆 Top Movies",
                data=data['top_movies'].to_csv(index=False),
                file_name="top_movies.csv",
                mime="text/csv"
            )

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; padding: 2rem; color: #666;'>
    <p>Business Insights Dashboard | MovieLens 33M Dataset Analysis</p>
    <p>Machine Learning Final Project | 2024</p>
</div>
""", unsafe_allow_html=True)