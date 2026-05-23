"""
Job Market Intelligence Platform - Streamlit Frontend
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import warnings
import plotly.express as px
import plotly.graph_objects as go
from typing import Tuple
from trial_new import JobMarketIntelligence


warnings.filterwarnings('ignore')

# ==================== KONFIGURASI ====================

st.set_page_config(
    page_title="Job Market Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== CSS STYLING ====================
def load_css():
    st.markdown("""
    <style>

    /* =========================
       GLOBAL
    ========================== */

    :root {
        --primary-color: #FF6B35;
        --secondary-color: #FF8C42;
        --accent-color: #FFD166;
        --border-color: rgba(255,107,53,0.45);
    }

    /* =========================
       MAIN APP
    ========================== */

    .stApp {
        background: var(--background-color);
        color: var(--text-color);
    }

    /* =========================
       MAIN HEADER
    ========================== */

    .main-header {
        font-size: clamp(1.1rem, 4vw, 1.5rem);
        text-align: center;
        margin-bottom: 1rem;
        font-weight: bold;
    }

    .main-header .gradient-text {
        background: linear-gradient(
            135deg,
            #FF6B35 0%,
            #FF8C42 50%,
            #FFD166 100%
        );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* =========================
       SECTION HEADER
    ========================== */

    .section-header {
        font-size: 1.3rem;
        color: var(--text-color) !important;
        margin-bottom: 0.8rem;
        font-weight: bold;
        text-align: center;
    }

    /* =========================
       INFO BOX
    ========================== */

    .info-box {
        background-color: #FF8C42;
        padding: 1rem;
        border-radius: 12px;
        margin: 0.8rem 0;
        color: white !important;
        border-left: 5px solid #FF6B35;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    }

    .info-box * {
        color: white !important;
    }

    /* =========================
       INSIGHT BOX
    ========================== */

    .insight-box {
        background-color: var(--secondary-background-color);
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;

        color: var(--text-color) !important;

        border-left: 5px solid #E9C46A;
        border: 1px solid var(--border-color);
    }

    .insight-box * {
        color: var(--text-color) !important;
    }

    /* =========================
       SKILL CARD
    ========================== */

    .skill-card {
        background-color: var(--secondary-background-color);

        padding: 1rem;

        border-radius: 12px;

        margin-bottom: 18px !important;

        border-left: 4px solid #FF6B35;

        border: 1px solid var(--border-color);

        box-shadow: 0 2px 4px rgba(0,0,0,0.15);

        color: var(--text-color) !important;

        overflow: hidden !important;
        position: relative !important;
    }

    .skill-card * {
        color: var(--text-color) !important;
    }

    /* =========================
       HIGHLIGHT CARD
    ========================== */

    .highlight-card {
        background: linear-gradient(
            135deg,
            #FF6B35 0%,
            #FF8C42 100%
        );

        padding: 1rem;

        border-radius: 12px;

        margin: 1rem 0;

        color: white !important;

        box-shadow: 0 4px 15px rgba(255,107,53,0.25);
    }

    .highlight-card * {
        color: white !important;
    }

    /* =========================
       SIDEBAR
    ========================== */

    [data-testid="stSidebar"] {
        background: linear-gradient(
            135deg,
            #FF6B35 0%,
            #FF8C42 50%,
            #FFD166 100%
        );
    }

    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* =========================
       HR LINE
    ========================== */

    hr {
        margin: 0.5rem 0;
        border: none;
        height: 1px;
        background-color: rgba(120,120,120,0.2);
    }

    /* =========================
       TEXT INPUT FIX
    ========================= */
    
    .stTextInput > div > div {
        background-color: transparent !important;
    }
    
    .stTextInput input {
        background-color: #212121 !important;
    
        color: #212121 !important;
    
        border: 1px solid rgba(255,107,53,0.45) !important;
    
        border-radius: 8px !important;
    
        box-shadow: none !important;
    }
    
    /* PLACEHOLDER */
    
    .stTextInput input::placeholder {
        color: rgba(255,255,255,0.5) !important;
    }

    /* =========================
       SELECTBOX
    ========================== */

    .stSelectbox > div > div {
        background-color: transparent !important;
        border-radius: 8px !important;
    }

    .stSelectbox div[data-baseweb="select"] {
        background-color: var(--secondary-background-color) !important;

        color: var(--text-color) !important;

        border: 1px solid var(--border-color) !important;

        border-radius: 8px !important;
    }

    .stSelectbox div[data-baseweb="select"] * {
        color: var(--text-color) !important;
    }

    /* =========================
       DROPDOWN
    ========================== */

    div[role="listbox"] {
        background-color: var(--secondary-background-color) !important;
        border: 1px solid var(--border-color) !important;
    }

    div[role="option"] {
        color: var(--text-color) !important;
        background-color: var(--secondary-background-color) !important;
    }

    div[role="option"]:hover {
        background-color: rgba(255,107,53,0.15) !important;
    }

    /* =========================
       LABELS
    ========================== */

    .stTextInput label,
    .stSelectbox label,
    .stMarkdown,
    p,
    span,
    li,
    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {
        color: var(--text-color) !important;
    }

    /* =========================
       BUTTON
    ========================== */

    .stButton button {
        background-color: #FF6B35 !important;

        color: white !important;

        border-radius: 8px !important;

        border: none !important;

        padding: 0.5rem 1rem !important;

        font-weight: bold !important;

        transition: 0.3s ease;
    }

    .stButton button:hover {
        background-color: #E85D04 !important;
    }

    /* =========================
       SIDEBAR SELECTBOX
    ========================== */

    [data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] {
        background-color: rgba(0,0,0,0.25) !important;

        border: 1px solid rgba(255,255,255,0.3) !important;

        border-radius: 8px !important;
    }

    [data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] div {
        color: white !important;
    }

    /* =========================
       RADIO
    ========================== */

    [data-testid="stSidebar"] .stRadio label {
        color: white !important;
    }

    [data-testid="stSidebar"] .stRadio label:hover {
        color: #FFD166 !important;
    }

    /* =========================
       SUBHEADER
    ========================== */

    [data-testid="stSidebar"] .stSubheader {
        color: #FFD166 !important;
        font-weight: bold !important;
    }

    /* =========================
       FORM SPACING
    ========================== */

    div[data-testid="stForm"] {
        margin-bottom: 1.5rem !important;
    }

    /* =========================
       RECOMMENDATION SPACING
    ========================== */

    div[data-testid="stVerticalBlock"] > div {
        margin-bottom: 0.8rem;
    }

    /* ===================================
       LIGHT MODE FIX
    ==================================== */

    [data-theme="light"] .skill-card,
    [data-theme="light"] .insight-box {
        background-color: #FFFFFF !important;
    }

    /* ALL TEXT INSIDE LIGHT MODE */

    [data-theme="light"] .skill-card *,
    [data-theme="light"] .insight-box *,
    [data-theme="light"] .section-header,
    [data-theme="light"] .stMarkdown,
    [data-theme="light"] .stMarkdown *,
    [data-theme="light"] .element-container,
    [data-theme="light"] .element-container *,
    [data-theme="light"] p,
    [data-theme="light"] span,
    [data-theme="light"] li,
    [data-theme="light"] div,
    [data-theme="light"] label,
    [data-theme="light"] h1,
    [data-theme="light"] h2,
    [data-theme="light"] h3,
    [data-theme="light"] h4,
    [data-theme="light"] h5,
    [data-theme="light"] h6 {
        color: #212121 !important;
    }

    /* =====================================
       TEXT INPUT AUTO LIGHT/DARK
    ===================================== */
    
    /* WRAPPER */
    
    .stTextInput div[data-baseweb="input"] {
        background-color: var(--secondary-background-color) !important;
    
        border: 1px solid var(--border-color) !important;
    
        border-radius: 8px !important;
    }
    
    /* INPUT */
    
    .stTextInput input {
        background-color: transparent !important;
    
        color: var(--text-color) !important;
    
        caret-color: var(--text-color) !important;
    }
    
    /* PLACEHOLDER */
    
    .stTextInput input::placeholder {
        color: rgba(120,120,120,0.8) !important;
    }

    /* SELECTBOX */

    [data-theme="light"] .stSelectbox div[data-baseweb="select"] {
        background-color: white !important;
        color: #1A1A1A !important;
    }

    [data-theme="light"] .stSelectbox div[data-baseweb="select"] * {
        color: #1A1A1A !important;
    }

    /* DROPDOWN OPTIONS */

    [data-theme="light"] div[role="option"] {
        background-color: white !important;
        color: #1A1A1A !important;
    }

    /* SVG ICON */

    [data-theme="light"] .stSelectbox svg {
        fill: #1A1A1A !important;
    }
    /* =========================================
   LIGHT MODE TEXT FIX (SAFE)
    ========================================= */
    
    html[data-theme="light"] .main-header,
    html[data-theme="light"] .section-header,
    html[data-theme="light"] p,
    html[data-theme="light"] span,
    html[data-theme="light"] label,
    html[data-theme="light"] li,
    html[data-theme="light"] h1,
    html[data-theme="light"] h2,
    html[data-theme="light"] h3,
    html[data-theme="light"] h4,
    html[data-theme="light"] h5,
    html[data-theme="light"] h6 {
        color: #212121 !important;
    }
    
    /* KEEP SIDEBAR WHITE */
    
    html[data-theme="light"] [data-testid="stSidebar"] *,
    html[data-theme="dark"] [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* KEEP ORANGE CARDS WHITE */
    
    html[data-theme="light"] .info-box *,
    html[data-theme="light"] .highlight-card * {
        color: white !important;
    }
    /* =========================
       CHART CONTAINER
    ========================= */
    
    div[data-testid="stPlotlyChart"] {
        background-color: var(--secondary-background-color) !important;
    
        border: 1px solid var(--border-color) !important;
    
        border-radius: 16px !important;
    
        padding: 0.8rem !important;
    
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    
        overflow: hidden !important;
    }
    
    /* BIAR HEIGHT PAS */
    
    div[data-testid="stPlotlyChart"] > div {
        border-radius: 12px !important;
    }
    
    /* LIGHT MODE */
    
    html[data-theme="light"] div[data-testid="stPlotlyChart"] {
        background-color: #FFFFFF !important;
    
        border: 1px solid rgba(0,0,0,0.08) !important;
    }
    
    /* DARK MODE */
    
    html[data-theme="dark"] div[data-testid="stPlotlyChart"] {
        background-color: #262730 !important;
    }
        </style>
        """, unsafe_allow_html=True)

# ==================== BOX RENDERERS ====================

def render_title_box(title: str):
    st.markdown(f"""
    <div class="info-box">
        <div class="section-header">{title}</div>
    </div>
    """, unsafe_allow_html=True)

def render_insight_box(insight: str):
    st.markdown(f"""
    <div class="insight-box">
        💡 <strong>Insight:</strong> {insight}
    </div>
    """, unsafe_allow_html=True)

# ==================== GRAFIK FUNCTIONS (DETEKSI MODE OTOMATIS) ====================

def get_text_color_and_background():
    try:
        background = st.get_option("theme.backgroundColor")

        # LIGHT MODE
        if background and background.lower() in ["#ffffff", "white"]:
            return "#1A1A1A", "#FFFFFF"

        # DARK MODE
        else:
            return "#ECECEC", "#2F2F2F"

    except:
        return "#ECECEC", "#2F2F2F"

def plot_horizontal_job_titles(titles_df: pd.Series):

    colors = ['#FF6B35', '#FF8C42', '#F4A261', '#E9C46A', '#6A9C89']

    fig = px.bar(
        x=titles_df.values,
        y=titles_df.index,
        orientation='h',
        text=titles_df.values,
        color=titles_df.index,
        color_discrete_sequence=colors
    )

    fig.update_layout(
        title="Top Job Titles",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color="white"),
        showlegend=False,
        height=520,
        margin=dict(l=20, r=20, t=60, b=20)
    )

    fig.update_traces(textposition='outside')

    fig.update_yaxes(autorange="reversed")

    return fig

def plot_skill_gaps(gaps_df: pd.DataFrame, skill_type: str):

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=gaps_df['skill'],
        y=gaps_df['have_count'],
        name='Have (Current Users)',
        marker_color='#E9C46A'
    ))

    fig.add_trace(go.Bar(
        x=gaps_df['skill'],
        y=gaps_df['want_count'],
        name='Want (Learners)',
        marker_color='#FF6B35'
    ))

    fig.update_layout(
        title=f"Top Skill Gaps - {skill_type.title()}",
        barmode='group',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color="white"),
        height=400,
        margin = dict(l=20, r=20, t=60, b=20)
    )

    return fig


def plot_hiring_priorities(priorities: pd.Series) -> go.Figure:
    """Donut chart dengan persentase di dalam"""
    plt.style.use('default')

    labels = priorities.index.tolist()
    values = priorities.values.tolist()
    colors = ['#FF6B35', '#FF8C42', '#F4A261', '#E9C46A', '#6A9C89', '#A0C4E2']

    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.4,
        domain=dict(x=[0, 0.72]),
        marker=dict(colors=colors[:len(labels)]),
        textinfo='percent',
        textposition='inside',
        textfont=dict(size=12),
        hoverinfo='label+value+percent',
        pull=[0.05 if i == 0 else 0 for i in range(len(labels))]
    )])

    fig.update_layout(
        title=dict(
            text='Hiring Priorities',
            x=0.1,
            font=dict(size=16)
        ),
        height=400,  # tinggi chart
        width=550,  # lebar chart lebih besar supaya legend muat
        margin=dict(
            t=50,  # jarak atas
            l=10,  # jarak kiri
            r=50,  # jarak kanan lebih kecil supaya legend deket donut
            b=40  # jarak bawah
        ),
        legend=dict(
            x=0.70,
            y=0.5,
            xanchor='left',
            yanchor='middle',
            font=dict(size=10),
            bgcolor='rgba(0,0,0,0)'
        )
    )
    return fig


def plot_emerging_skill(selected_skill: str,
                         demand_ratio: float,
                         want_count: int,
                         have_count: int):

    fig = go.Figure(data=[
        go.Bar(
            x=['Have (Current Users)', 'Want (Learners)'],
            y=[have_count, want_count],
            marker_color=['#F4A261', '#FF6B35'],
            text=[have_count, want_count],
            textposition='outside'
        )
    ])

    fig.update_layout(
        title=f"{selected_skill} - Demand Ratio: {demand_ratio}x",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color="white"),
        height=400,
        margin = dict(l=20, r=20, t=60, b=20)
    )

    return fig

# ==================== DATA LOADER ====================

@st.cache_resource
def load_data(csv_path: str = "cleaned_data.csv") -> JobMarketIntelligence:
    return JobMarketIntelligence(csv_path)

# ==================== SIDEBAR ====================

def render_sidebar(jmi: JobMarketIntelligence) -> Tuple[str, str, str]:
    with st.sidebar:
        st.image("download-removebg-preview.png", width=225)
        st.title("🎯 Navigation")
        page = st.radio(
            "Choose a section:",
            ["💡 Personal Recommendations", "🏠 Dashboard", "📈 Skill Analysis", "🎯 Skill Gaps",
             "🚀 Emerging Skills", "⭐ Hiring Priorities"]
        )
        st.divider()
        st.subheader("🔍 Filters")
        countries = ['All'] + sorted(jmi.df['country'].dropna().unique().tolist())
        selected_country = st.selectbox("Country", countries)
        skill_types = ['languages', 'frameworks', 'databases', 'platforms']
        selected_skill_type = st.selectbox("Skill Type", skill_types)
    return page, selected_country, selected_skill_type

# ==================== DASHBOARD PAGE ====================

def render_dashboard_page(jmi: JobMarketIntelligence, selected_country: str, selected_skill_type: str):
    st.markdown('<h1 class="main-header">📊 <span class="gradient-text">Job Market Intelligence Dashboard</span></h1>', unsafe_allow_html=True)

    # KEY METRICS
    st.markdown("""
    <div style="text-align: center; margin-bottom: 1rem;">
        <div class="section-header">📈 Key Metrics</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4, gap="medium")
    with col1:
        st.markdown(f"""
        <div style="background: var(--secondary-background-color); padding: 1.2rem; border-radius: 16px; text-align: center; border-left: 4px solid #FF6B35;">
            <div style="font-size: 2.2rem;">👥</div>
            <div style="font-size: 1.8rem; font-weight: 700; color: var(--text-color);">{len(jmi.df):,}</div>
            <div style="font-size: 0.85rem; color: var(--text-color);">Total Developers</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div style="background: var(--secondary-background-color);; padding: 1.2rem; border-radius: 16px; text-align: center; border-left: 4px solid #06D6A0;">
            <div style="font-size: 2.2rem;">🌍</div>
            <div style="font-size: 1.8rem; font-weight: 700; color: var(--text-color);">{jmi.df['country'].nunique()}</div>
            <div style="font-size: 0.85rem; color: var(--text-color);">Countries</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        top_lang = jmi.get_top_skills('languages', 1).index[0]
        st.markdown(f"""
        <div style="background: var(--secondary-background-color); padding: 1.2rem; border-radius: 16px; text-align: center; border-left: 4px solid #4361EE;">
            <div style="font-size: 2.2rem;">🏆</div>
            <div style="font-size: 1.5rem; font-weight: 700; color: var(--text-color);">{top_lang}</div>
            <div style="font-size: 0.85rem; color: var(--text-color);">Most Popular Language</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        total_skills = jmi.df['skills_languages'].dropna().str.split(';').explode().nunique()
        st.markdown(f"""
        <div style="background: var(--secondary-background-color); padding: 1.2rem; border-radius: 16px; text-align: center; border-left: 4px solid #F72585;">
            <div style="font-size: 2.2rem;">💻</div>
            <div style="font-size: 1.8rem; font-weight: 700; color: var(--text-color);">{total_skills}</div>
            <div style="font-size: 0.85rem; color: var(--text-color);">Unique Skills</div>
        </div>
        """, unsafe_allow_html=True)

    # TOP JOB TITLES
    top_titles = jmi.get_top_job_titles(10)

    fig = plot_horizontal_job_titles(top_titles)

    st.plotly_chart(fig, use_container_width=True)


    # SKILL GAPS & HIRING PRIORITIES - SEJAJAR KANAN KIRI (TANPA JUDUL)
    col1, col2 = st.columns(2)

    with col1:
        gaps = jmi.get_skill_gap(selected_skill_type, 8)
        if len(gaps) > 0:
            fig = plot_skill_gaps(gaps, selected_skill_type)

            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No skill gaps found for this category")

    with col2:
        country_for_hiring = selected_country if selected_country != 'All' else None
        priorities = jmi.get_hiring_priorities(country_for_hiring)
        if not priorities.empty:
            fig = plot_hiring_priorities(priorities)
            st.plotly_chart(fig, use_container_width=True)  # ← Pakai st.plotly_chart
        else:
            st.warning("No hiring priority data available")
# ==================== SKILL ANALYSIS PAGE ====================

def render_skill_analysis_page(jmi: JobMarketIntelligence, selected_country: str, selected_skill_type: str):
    st.markdown('<h1 class="main-header">📈 <span class="gradient-text">Skill Analysis</span></h1>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        render_title_box("✅ Most Used Languages")
        if selected_country == 'All':
            skills = jmi.get_top_skills(selected_skill_type, 15)
        else:
            skills = jmi.get_skills_by_country(selected_country, selected_skill_type, 15)
        for i, (skill, count) in enumerate(skills.items(), 1):
            st.markdown(f'<div class="skill-card">{i}. {skill} — {count:,} developers</div>', unsafe_allow_html=True)
    with col2:
        render_title_box("🎯 Most Wanted Languages")
        if selected_country == 'All':
            want_skills = jmi.get_wanted_skills(selected_skill_type, 15)
        else:
            col_map = {'languages': 'wanted_languages', 'frameworks': 'wanted_frameworks', 'databases': 'wanted_databases', 'platforms': 'wanted_platforms'}
            country_data = jmi.df[jmi.df['country'] == selected_country]
            want_skills = (country_data[col_map[selected_skill_type]].dropna().str.split(';').explode().str.strip().str.title().value_counts().head(15))
        for i, (skill, count) in enumerate(want_skills.items(), 1):
            st.markdown(f'<div class="skill-card">{i}. {skill} — wanted by {count:,} developers</div>', unsafe_allow_html=True)

# ==================== SKILL GAPS PAGE ====================

def render_skill_gaps_page(jmi: JobMarketIntelligence, selected_country: str, selected_skill_type: str):
    st.markdown('<h1 class="main-header">🎯 <span class="gradient-text">Skill Gap Analysis</span></h1>', unsafe_allow_html=True)
    st.markdown('<div style="color: var(--text-color);">*Skills that are in high demand but low supply*</div>', unsafe_allow_html=True)
    gaps = jmi.get_skill_gap(selected_skill_type, 15)
    if len(gaps) > 0:
        for _, row in gaps.iterrows():
            st.markdown(f"""
            <div class="skill-card">
                <strong>{row['skill']}</strong><br>
                📊 Want: {row['want_count']:,} | ✅ Have: {row['have_count']:,} | 
                <span style="color:#FF6B35; font-weight:bold;">⚠️ Gap: {row['gap']:,}</span>
            </div>
            """, unsafe_allow_html=True)
        top_skill = gaps.iloc[0]['skill']
        render_insight_box(f"**{top_skill}** has the biggest gap with {gaps.iloc[0]['gap']:,} more developers wanting to learn it!")
    else:
        st.info("No skill gaps found")

# ==================== EMERGING SKILLS PAGE ====================

def render_emerging_skills_page(jmi: JobMarketIntelligence, selected_country: str, selected_skill_type: str):
    st.markdown('<h1 class="main-header">🚀 <span class="gradient-text">Emerging Skills</span></h1>', unsafe_allow_html=True)
    st.markdown('<div style="color: var(--text-color);">*Skills with highest demand ratio - Select a skill to see the graph*</div>', unsafe_allow_html=True)
    emerging = jmi.get_emerging_skills(selected_skill_type, 15)
    if len(emerging) > 0:
        col1, col2 = st.columns([1, 1])
        with col1:
            render_title_box("📋 Select a Skill")
            skill_options = emerging['skill'].tolist()
            selected_skill = st.selectbox("Choose a skill:", skill_options, label_visibility="collapsed")
            st.markdown("---")
            st.markdown('<div style="color: var(--text-color); font-weight: bold;">🔥 All Emerging Skills:</div>', unsafe_allow_html=True)
            for _, row in emerging.iterrows():
                ratio = row['demand_ratio']
                emoji = "🚀" if ratio >= 5 else "📈" if ratio >= 3 else "⭐"
                if selected_skill == row['skill']:
                    st.markdown(f'<div style="color: #FF6B35; font-weight: bold;">👉 {emoji} {row["skill"]} — {ratio}x 👈</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div style="color: var(--text-color);">{emoji} {row["skill"]} — {ratio}x</div>', unsafe_allow_html=True)
        with col2:
            if selected_skill:
                skill_data = emerging[emerging['skill'] == selected_skill].iloc[0]
                fig = plot_emerging_skill(
                    selected_skill,
                    skill_data['demand_ratio'],
                    skill_data['want_count'],
                    skill_data['have_count']
                )

                st.plotly_chart(fig, use_container_width=True)
                st.markdown(f'<div class="insight-box">💡 <strong>Insight:</strong> {selected_skill} has <strong>{skill_data["demand_ratio"]}x</strong> more learners than users!</div>', unsafe_allow_html=True)
        top_skill = emerging.iloc[0]['skill']
        st.markdown(f'<div class="insight-box">🎯 <strong>Top Emerging Skill:</strong> {top_skill} has the highest demand ratio at {emerging.iloc[0]["demand_ratio"]}x!</div>', unsafe_allow_html=True)
    else:
        st.info("No emerging skills identified")

# ==================== HIRING PRIORITIES PAGE ====================

def render_hiring_priorities_page(jmi: JobMarketIntelligence, selected_country: str, selected_skill_type: str):
    st.markdown('<h1 class="main-header">⭐ <span class="gradient-text">Hiring Priorities</span></h1>', unsafe_allow_html=True)
    st.markdown('<div style="color: var(--text-color);">*What employers value most when hiring*</div>', unsafe_allow_html=True)
    country_for_hiring = selected_country if selected_country != 'All' else None
    priorities = jmi.get_hiring_priorities(country_for_hiring)
    if not priorities.empty:
        for name, pct in priorities.items():
            if name == list(priorities.keys())[0]:
                st.markdown(f'<div class="highlight-card"><h3 style="margin: 0;">⭐ {name}</h3><div style="font-size: 1.2rem;"><strong>{pct:.0f}%</strong> of recruiters find this important</div></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="skill-card"><strong>{name}</strong><br>{pct:.0f}% of recruiters find this important</div>', unsafe_allow_html=True)
        top_priority = list(priorities.keys())[0]
        render_insight_box(f"{top_priority} is what recruiters value most! ({priorities.iloc[0]:.0f}%)")
    else:
        st.warning("No hiring priority data available")

# ==================== PERSONAL RECOMMENDATIONS PAGE ====================
def render_personal_recommendations_page(jmi: JobMarketIntelligence, selected_country: str, selected_skill_type: str):
    st.markdown('<h1 class="main-header">💡 <span class="gradient-text">Personalized Skill Recommendations</span></h1>',
                unsafe_allow_html=True)
    countries = ['All'] + sorted(jmi.df['country'].dropna().unique().tolist())
    with st.form("user_profile"):
        col1, col2 = st.columns(2)
        with col1:
            current_skills = st.text_input("💻 Your current skills", placeholder="e.g., Python, SQL, JavaScript")
            career_goal = st.selectbox("🎯 Career goal",
                                       ["Data Scientist", "Web Developer", "DevOps Engineer", "Mobile Developer",
                                        "Machine Learning Engineer", "Other"])
        with col2:
            target_country = st.selectbox("🌍 Target country", countries[1:])
            if career_goal == "Other":
                career_goal = st.text_input("📝 Specify your target role")
        submitted = st.form_submit_button("🎯 Get Recommendations", use_container_width=True)

    if submitted and current_skills:
        skill_list = [s.strip() for s in current_skills.split(',')]
        with st.spinner("📊 Analyzing market data..."):
            try:
                recommendations = jmi.recommend_skills(skill_list, career_goal if career_goal != "Other" else None,
                                                       target_country if target_country != "All" else None, n=10)
                if len(recommendations) > 0:
                    for i, (_, row) in enumerate(recommendations.iterrows(), 1):
                        if i == 1:
                            st.markdown(
                                f'<div class="highlight-card"><h2>🏆 #{i}</h2><h1 style="font-size: 1.8rem; color: white;">{row["skill"]}</h1><div style="color: white;">💡 {row["reasons"]}</div></div>',
                                unsafe_allow_html=True)
                        elif i == 2:
                            st.markdown(
                                f'<div class="highlight-card" style="background: linear-gradient(135deg, #FF8C42 0%, #FFA559 100%);"><h3 style="color: white;">🥈 #{i}</h3><h2 style="font-size: 1.7rem; color: white;">{row["skill"]}</h2><div style="color: white;">💡 {row["reasons"]}</div></div>',
                                unsafe_allow_html=True)
                        elif i == 3:
                            st.markdown(
                                f'<div class="highlight-card" style="background: linear-gradient(135deg, #F4A261 0%, #F6B17A 100%);"><h3 style="color: white;">🥉 #{i}</h3><h2 style="font-size: 1.7rem; color: white;">{row["skill"]}</h2><div style="color: white;">💡 {row["reasons"]}</div></div>',
                                unsafe_allow_html=True)
                        else:
                            st.markdown(
                                f'<div class="skill-card"><strong>#{i} {row["skill"]}</strong><br>💡 {row["reasons"]}</div>',
                                unsafe_allow_html=True)
                    render_insight_box(
                        f"Start with {recommendations.iloc[0]['skill']} — it has the highest demand!")
                else:
                    st.info("📭 No recommendations found.")
            except AttributeError:
                st.error("❌ Method 'recommend_skills()' not found.")
            except Exception as e:
                st.error(f"❌ Error: {e}")
    elif submitted:
        st.warning("⚠️ Please enter your current skills first!")

# ==================== FOOTER ====================

def render_footer():
    st.divider()
    st.markdown(
        "<p style='text-align: center; color: var(--text-color);'>📊 Job Market Intelligence Platform | Powered by Stack Overflow Survey Data</p>",
        unsafe_allow_html=True
    )
# ==================== MAIN APP ====================

def main():
    load_css()
    try:
        jmi = load_data("cleaned_data.csv")
    except FileNotFoundError:
        st.error("❌ File 'cleaned_data.csv' tidak ditemukan!")
        st.stop()
    page, selected_country, selected_skill_type = render_sidebar(jmi)
    if page == "🏠 Dashboard":
        render_dashboard_page(jmi, selected_country, selected_skill_type)
    elif page == "📈 Skill Analysis":
        render_skill_analysis_page(jmi, selected_country, selected_skill_type)
    elif page == "🎯 Skill Gaps":
        render_skill_gaps_page(jmi, selected_country, selected_skill_type)
    elif page == "🚀 Emerging Skills":
        render_emerging_skills_page(jmi, selected_country, selected_skill_type)
    elif page == "⭐ Hiring Priorities":
        render_hiring_priorities_page(jmi, selected_country, selected_skill_type)
    elif page == "💡 Personal Recommendations":
        render_personal_recommendations_page(jmi, selected_country, selected_skill_type)
    render_footer()

if __name__ == "__main__":
    main()