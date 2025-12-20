# MovieLens Analytics Dashboard

A comprehensive data analytics dashboard built with Streamlit that analyzes **33.8 million ratings** from **331,000 users** across **86,000 movies** from the MovieLens dataset. This project provides actionable business insights for content strategy, user engagement, and personalized recommendations.

## Overview

This dashboard displayed extracted meaningful insights from one of the largest movie rating datasets available. The application features a Netflix-inspired dark theme and provides interactive visualizations across multiple analytical dimensions.

### Key Statistics

- **Total Ratings**: 33.8M
- **Active Users**: 331K
- **Movies Analyzed**: 86K
- **Average Rating**: 3.53★
- **Time Period**: 1995-2023 (28 years)

## Features

### Main Dashboard

- **Platform Overview**: Key metrics and statistics at a glance
- **Project Overview**: Business context and navigation guide
- **Key Insights Preview**: Quick summary of major findings
- **Interactive Navigation**: Seamless transition to detailed analytics

### Business Insights Page

#### 👥 User Behavior Analysis

- Rating distribution patterns
- Temporal trends (1995-2023)
- User retention analysis
- Monthly and hourly activity patterns
- User segmentation (Harsh, Neutral, Generous raters)

#### 🎬 Content Performance

- Genre performance analysis (Film-Noir highest at 4.0★)
- Tag sentiment analysis
- Release year impact (1940s golden era)
- Movie polarization analysis
- Premium format effects (IMAX: +1.9% rating boost)

#### 💎 Hidden Gems Discovery

- High-quality movies (≥4.0★) with low visibility
- Quality vs. popularity analysis
- Curated recommendations for promotion

#### 🎭 User Personas & Segmentation

- K-Means clustering analysis
- 5 distinct user personas identified:
  - Drama Enthusiasts (27.0%)
  - Art House Lovers (28.4%)
  - Mainstream Viewers (25.1%)
  - Family Oriented (9.5%)
  - Sci-Fi Fans (10.0%)

#### 📥 Data Export

- Download summary datasets in CSV format
- Platform statistics, user segments, yearly trends
- Genre stats, hidden gems, top movies

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup Steps

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd movielens-dashboard
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**

   ```bash
   streamlit run app.py
   ```

4. **Access the dashboard**
   - The application will automatically open in your default web browser
   - Default URL: `http://localhost:8501`

   Or Checkout thedeployed dashboard:

   - https://github.com/C-Ronny/movielens-dashboard

## Project Structure

```
movielens-dashboard/
├── app.py                          # Main dashboard application
├── pages/
│   └── business_insights.py        # Detailed analytics page
├── assets/
│   ├── data/
│   │   └── summary/                # Processed summary datasets
│   │       ├── platform_stats.csv
│   │       ├── user_segments.csv
│   │       ├── yearly_trends.csv
│   │       ├── genre_stats.csv
│   │       ├── hidden_gems.csv
│   │       └── top_movies.csv
│   └── visualizations/             # Interactive HTML visualizations
│       ├── user_behavior/
│       ├── content_performance/
│       ├── hidden_gems/
│       └── user_personas/
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## Technologies Used

- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive visualizations
- **Pillow (PIL)**: Image processing
- **Matplotlib**: Additional plotting capabilities

## Key Insights

### User Behavior

- **3 distinct user segments** identified based on rating patterns
- **Peak activity**: 8-10 PM on weekdays
- **28-year rating history** analyzed (1995-2023)
- Steady growth with peak activity in 2016-2018

### Content Performance

- **Film-Noir** is the highest-rated genre (4.0★)
- **1940s** represents the golden age of cinema
- **IMAX format** provides a statistically significant 1.9% rating boost
- **194 hidden gems** discovered (high quality, low visibility)

### Recommendations

- **5 user personas** identified for personalized experiences
- ML models achieve **66% Precision@10** for recommendations
- Persona-specific homepage experiences could increase engagement by 15-25%


## Usage

1. **Main Dashboard**: Start here for an overview of platform statistics and key insights
2. **Business Insights**: Navigate via sidebar to explore detailed analytics
3. **Interactive Tabs**: Switch between different analysis sections
4. **Data Export**: Download processed datasets for further analysis

## Analysis Sections

### User Behavior

- Understand rating patterns and temporal trends
- Analyze user retention and engagement
- Identify peak activity times

### Content Performance

- Evaluate genre performance
- Analyze tag sentiment
- Study release year impact
- Discover polarization patterns

### Hidden Gems

- Find high-quality underrated movies
- Identify promotion opportunities
- Balance quality vs. popularity

### User Personas

- Explore user segmentation
- Understand genre preferences
- Enable personalized recommendations

