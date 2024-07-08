import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load data using Pandas
df = pd.read_csv('input_data/crypto_prices.csv')

# Create candlestick trace
candlestick = go.Candlestick(
    x=df.index,
    open=df['Open'],
    high=df['High'],
    low=df['Low'], 
    close=df['Close'],
    name='Candlestick'
)

# Create Bollinger Bands trace
sma = df['Close'].rolling(20).mean()
std = df['Close'].rolling(20).std()
bb_upper = sma + 2 * std
bb_lower = sma - 2 * std

bollinger = go.Scatter(
    x=df.index,
    y=bb_upper,
    line=dict(color='gray', width=1),
    name='BB Upper'
)

# Create figure with subplots
fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.03)

# Add traces to figure
fig.add_trace(candlestick, row=1, col=1)
fig.add_trace(bollinger, row=1, col=1)

# Customize layout
fig.update_layout(
    title='Cryptocurrency Price Analysis',
    xaxis_title='Date',
    yaxis_title='Price (USD)',
    xaxis_rangeslider_visible=False
)

# Save report as HTML
fig.write_html('output_data/crypto_report.html')
