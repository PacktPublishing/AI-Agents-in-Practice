# server.py
from mcp.server.fastmcp import FastMCP
import yfinance as yf

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()


def get_stock_price(ticker: str) -> float:
    """Fetch the latest stock price for a given ticker symbol from Yahoo Finance"""
    stock = yf.Ticker(ticker)
    return stock.history(period="1d")["Close"].iloc[-1]

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')

