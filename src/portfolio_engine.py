"""
AMFI Direct Mutual Fund Selection & Backtest Engine
"""
import pandas as pd

AMFI_SHORTLIST = [
    {"name": "UTI Nifty 50 Index Fund Direct-Growth", "category": "Equity Large Cap", "ter": "0.18%", "cagr_10y": 13.5},
    {"name": "Parag Parikh Flexi Cap Fund Direct-Growth", "category": "Equity Flexi Cap", "ter": "0.62%", "cagr_10y": 17.2},
    {"name": "HDFC Short Term Debt Fund Direct-Growth", "category": "Debt Low Duration", "ter": "0.35%", "cagr_10y": 7.4},
    {"name": "ICICI Prudential Corporate Bond Direct-Growth", "category": "Debt Corporate", "ter": "0.28%", "cagr_10y": 7.8},
    {"name": "SBI Arbitrage Opportunities Fund Direct-Growth", "category": "Arbitrage", "ter": "0.41%", "cagr_10y": 6.1}
]

def simulate_10y_backtest(equity_ratio: float, initial_lump: float = 100000):
    years = list(range(2016, 2027))
    equity_returns = [0.03, 0.28, 0.04, 0.12, 0.15, 0.24, 0.04, 0.20, 0.16, 0.11, 0.12]
    debt_returns = [0.08, 0.07, 0.06, 0.08, 0.06, 0.05, 0.05, 0.07, 0.07, 0.07, 0.07]
    
    portfolio_values = [initial_lump]
    curr = initial_lump
    
    for eq_ret, dt_ret in zip(equity_returns, debt_returns):
        weighted_ret = (equity_ratio * eq_ret) + ((1 - equity_ratio) * dt_ret)
        curr *= (1 + weighted_ret)
        portfolio_values.append(round(curr, 2))
        
    df = pd.DataFrame({"Year": ["2015"] + [str(y) for y in years], "Portfolio Value (₹)": portfolio_values})
    cagr = ((portfolio_values[-1] / initial_lump) ** (1 / 11) - 1) * 100
    return df, round(cagr, 2)