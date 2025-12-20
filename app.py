import streamlit as st
import pandas as pd

# ============================================================================
# PAGE CONFIG
# ============================================================================

st.set_page_config(
    page_title="MovieLens Analytics Dashboard",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CUSTOM CSS - NETFLIX THEME
# ============================================================================

st.markdown("""
<style>
    /* Netflix Dark Theme */
    .stApp {
        background-color: #141414;
    }
    
    /* Main content area */
    .main {
        background-color: #141414;
    }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #000000;
        border-right: 2px solid #E50914;
    }
    
    section[data-testid="stSidebar"] .css-1d391kg {
        background-color: #000000;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #FFFFFF !important;
        font-family: 'Helvetica Neue', Arial, sans-serif;
    }
    
    h1 {
        color: #E50914 !important;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    /* Text */
    p, li, span, div {
        color: #FFFFFF !important;
    }
    
    /* Metrics */
    [data-testid="stMetricValue"] {
        color: #E50914 !important;
        font-size: 2rem !important;
        font-weight: 700 !important;
    }
    
    [data-testid="stMetricLabel"] {
        color: #FFFFFF !important;
    }
    
    /* Buttons */
    .stButton button {
        background-color: #E50914;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 10px 24px;
        font-weight: 600;
        transition: all 0.3s;
    }
    
    .stButton button:hover {
        background-color: #F40612;
        transform: scale(1.05);
    }
    
    /* Cards */
    .css-1r6slb0 {
        background-color: #1a1a1a;
        border: 1px solid #333;
        border-radius: 8px;
        padding: 20px;
    }
    
    /* Dividers */
    hr {
        border-color: #E50914 !important;
        opacity: 0.3;
    }
    
    /* Links */
    a {
        color: #E50914 !important;
        text-decoration: none;
    }
    
    a:hover {
        color: #F40612 !important;
        text-decoration: underline;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: #1a1a1a;
        color: white !important;
        border: 1px solid #333;
    }
    
    .streamlit-expanderContent {
        background-color: #141414;
        border: 1px solid #333;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# LOAD PLATFORM STATISTICS
# ============================================================================

@st.cache_data
def load_platform_stats():
    try:
        stats = pd.read_csv('assets/data/summary/platform_stats.csv')
        return stats.iloc[0]
    except:
        # Fallback if file not found
        return {
            'total_ratings': '33.8M',
            'total_users': '331K',
            'total_movies': '86K',
            'avg_rating': 3.53
        }

platform_stats = load_platform_stats()

# ============================================================================
# HEADER
# ============================================================================

st.markdown("""
<div style='text-align: center; padding: 2rem 0;'>
    <h1 style='font-size: 3.5rem; margin-bottom: 0.5rem;'>
        🎬 MOVIELENS ANALYTICS DASHBOARD
    </h1>
    <p style='font-size: 1.2rem; color: #999; margin-top: 0;'>
        Powered by 33M+ Ratings | Machine Learning Final Project
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ============================================================================
# KEY METRICS
# ============================================================================

st.markdown("<h2 style='text-align: center; margin-top: 2rem;'>📊 PLATFORM OVERVIEW</h2>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Total Ratings",
        value=platform_stats['total_ratings'],
        delta="33.8M analyzed"
    )

with col2:
    st.metric(
        label="Active Users",
        value=platform_stats['total_users'],
        delta="331K profiles"
    )

with col3:
    st.metric(
        label="Movies Analyzed",
        value=platform_stats['total_movies'],
        delta="86K titles"
    )

with col4:
    st.metric(
        label="Avg Rating",
        value=f"{platform_stats['avg_rating']:.2f}★",
        delta="Quality content"
    )

st.markdown("<hr>", unsafe_allow_html=True)

# ============================================================================
# PROJECT OVERVIEW
# ============================================================================

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("<h2>🎯 PROJECT OVERVIEW</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background-color: #1a1a1a; padding: 2rem; border-radius: 8px; border: 1px solid #333;'>
        <h3>Business Context</h3>
        <p style='font-size: 1.1rem; line-height: 1.8;'>
        As Data Scientists for a leading streaming platform, we analyzed <strong>33.8 million ratings</strong> 
        from <strong>331,000 users</strong> across <strong>86,000 movies</strong> to extract actionable insights 
        for content strategy, user engagement, and personalized recommendations.
        </p>       
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("<h2>🗂️ NAVIGATION</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background-color: #1a1a1a; padding: 2rem; border-radius: 8px; border: 1px solid #333;'>
        <h3>Dashboard Sections</h3>
        <ul style='font-size: 1.1rem; line-height: 2;'>
            <li>👥 <strong>User Behavior</strong>
                <ul style='font-size: 0.95rem; margin-left: 1.5rem;'>
                    <li>Rating patterns</li>
                    <li>Temporal trends</li>
                    <li>User retention</li>
                </ul>
            </li>
            <li>🎬 <strong>Content Performance</strong>
                <ul style='font-size: 0.95rem; margin-left: 1.5rem;'>
                    <li>Genre analysis</li>
                    <li>Tag sentiment</li>
                    <li>Release year impact</li>
                </ul>
            </li>
            <li>💎 <strong>Hidden Gems</strong>
                <ul style='font-size: 0.95rem; margin-left: 1.5rem;'>
                    <li>Underrated movies</li>
                    <li>Quality vs popularity</li>
                </ul>
            </li>
            <li>🎭 <strong>User Personas</strong>
                <ul style='font-size: 0.95rem; margin-left: 1.5rem;'>
                    <li>Genre preferences</li>
                    <li>Clustering analysis</li>
                </ul>
            </li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ============================================================================
# KEY INSIGHTS PREVIEW
# ============================================================================

st.markdown("<h2 style='text-align: center;'>🔍 KEY INSIGHTS</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style='background-color: #1a1a1a; padding: 1.5rem; border-radius: 8px; border-left: 4px solid #E50914; height: 200px;'>
        <h3>👥 User Behavior</h3>
        <p>• 3 distinct user segments identified</p>
        <p>• Peak activity: 8-10 PM weekdays</p>
        <p>• 28-year rating history analyzed</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='background-color: #1a1a1a; padding: 1.5rem; border-radius: 8px; border-left: 4px solid #E50914; height: 200px;'>
        <h3>🎬 Content Insights</h3>
        <p>• Film-Noir highest rated genre (4.0★)</p>
        <p>• 1940s golden age of cinema</p>
        <p>• 194 hidden gems discovered</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style='background-color: #1a1a1a; padding: 1.5rem; border-radius: 8px; border-left: 4px solid #E50914; height: 200px;'>
        <h3>🎯 Recommendations</h3>
        <p>• 5 user personas identified</p>
        <p>• ML models: 66% Precision@10</p>
        <p>• Personalization opportunities</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ============================================================================
# CALL TO ACTION
# ============================================================================

st.markdown("<h2 style='text-align: center;'>🚀 EXPLORE THE DASHBOARD</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("""
    <div style='text-align: center; padding: 2rem;'>
        <p style='font-size: 1.2rem; margin-bottom: 1.5rem;'>
        Navigate to <strong style='color: #E50914;'>Business Insights</strong> in the sidebar to explore comprehensive visualizations and analytics.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("📊 GO TO BUSINESS INSIGHTS", use_container_width=True):
        st.switch_page("pages/business_insights.py")

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; padding: 2rem; color: #666;'>
    <p>Machine Learning Final Assessment | MovieLens 33M Dataset</p>
    <p>Built with Streamlit • Plotly • Pandas • Scikit-learn</p>
    <p style='font-size: 0.9rem; margin-top: 1rem;'>
        Data Source: <a href='https://grouplens.org/datasets/movielens/'>GroupLens Research</a>
    </p>
</div>
""", unsafe_allow_html=True)