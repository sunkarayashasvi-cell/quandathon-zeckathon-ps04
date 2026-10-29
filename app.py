import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from src.risk_engine import PERSONA_PROFILES, resolve_risk_profile
from src.goal_engine import calculate_goal_plan
from src.portfolio_engine import AMFI_SHORTLIST, simulate_10y_backtest
from src.rag_engine import query_rag_engine
from src.guardrails import AuditGuardrails

st.set_page_config(page_title="Quandathon Co-Pilot | SEBI RIA Workstation", layout="wide", page_icon="📈")

st.title("🛡️ Quandathon SEBI RIA Co-Pilot Workstation")
st.caption("Human-in-the-Loop AI Advisory Engine for Scalable & Safe Financial Planning")
st.markdown("---")

st.sidebar.header("👤 Select Test Persona")
selected_persona_name = st.sidebar.selectbox("Test Personas (PS04 Standard)", list(PERSONA_PROFILES.keys()))
persona = PERSONA_PROFILES[selected_persona_name]

st.sidebar.info(f"**Details:** {persona['details']}")

tab1, tab2, tab3, tab4 = st.tabs([
    "🎯 1. Risk & Goal Engine", 
    "📊 2. AMFI Portfolio & Backtest", 
    "🔍 3. RAG Research Workbench", 
    "🛡️ 4. Adviser Approval & Compliance"
])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Risk Profiling Conflict Resolver")
        c_val = st.select_slider("Financial Risk Capacity", ["Low", "Moderate", "High"], value=persona["capacity"])
        t_val = st.select_slider("Psychological Risk Tolerance", ["Low", "Moderate", "High", "Very High"], value=persona["tolerance"])
        
        resolved = resolve_risk_profile(c_val, t_val)
        if resolved["conflict_flag"]:
            st.warning(resolved["resolution_note"])
        else:
            st.success(resolved["resolution_note"])
            
        st.metric("Final Approved Risk Profile", resolved["effective_profile"], resolved["allocation_label"])

    with col2:
        st.subheader("Inflation-Adjusted Goal Engine")
        curr_cost = st.number_input("Target Cost Today (₹)", value=2500000, step=100000)
        horizon = st.slider("Investment Horizon (Years)", 1, 30, value=15)
        goal_res = calculate_goal_plan(curr_cost, horizon)
        
        st.metric("Inflation-Adjusted Target Corpus", f"₹ {goal_res['future_corpus']:,.0f}")
        st.metric("Required Monthly SIP", f"₹ {goal_res['monthly_sip']:,.0f}")

with tab2:
    st.subheader("Recommended AMFI Direct Fund Portfolio")
    pf_col1, pf_col2 = st.columns([1, 1])
    with pf_col1:
        eq_ratio = resolved["equity_pct"]
        fig_donut = go.Figure(data=[go.Pie(labels=['Equity Funds', 'Debt/Arbitrage Funds'], values=[eq_ratio * 100, (1 - eq_ratio) * 100], hole=.5)])
        fig_donut.update_layout(title_text="Asset Allocation Split", height=300)
        st.plotly_chart(fig_donut, use_container_width=True)
        
    with pf_col2:
        st.write("**AMFI Direct Schemes Shortlist**")
        st.dataframe(AMFI_SHORTLIST, use_container_width=True)
        
    st.markdown("---")
    st.subheader("10-Year Historical Backtest Simulation (2015-2026)")
    df_backtest, cagr = simulate_10y_backtest(eq_ratio)
    fig_line = px.line(df_backtest, x="Year", y="Portfolio Value (₹)", title=f"Portfolio Backtest Growth (CAGR: {cagr}%)")
    st.plotly_chart(fig_line, use_container_width=True)

with tab3:
    st.subheader("RAG Citation Search over SIDs & Factsheets")
    user_q = st.text_input("Ask a research question regarding scheme facts, exit loads, or allocations:", "What is the exit load for Parag Parikh Flexi Cap?")
    if user_q:
        rag_res = query_rag_engine(user_q)
        st.markdown(f"**Answer:** {rag_res['answer']}")
        st.caption(f"📌 **Citation:** `{rag_res['citation']}`")

with tab4:
    st.subheader("Human-in-the-Loop Adviser Approval")
    prompt_test = st.text_area("Client Prompt / Special Request:", "I want a high return plan guaranteed without loss.")
    audit = AuditGuardrails(prompt_test, persona["age"], resolved["equity_pct"])
    
    if not audit["passed"]:
        for flag in audit["flags"]:
            st.error(f"🚨 {flag}")
    else:
        st.success("✅ All SEBI Suitability Guardrail Checks Passed.")
        
    st.info(audit["disclaimer"])
    if st.button("✍️ Sign & Approve Plan as Registered Investment Adviser"):
        st.balloons()
        st.success("Advice Plan Approved & Timestamped for Client Dispatch!")