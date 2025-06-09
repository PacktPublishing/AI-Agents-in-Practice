import asyncio
from some_tool_framework import tool  # Replace with actual decorator source if needed

@tool
async def fetch_sales_report(region: str) -> str:
    """Fetches the weekly sales report for a given region."""
    await asyncio.sleep(2)  # Simulated network delay
    return f"{region} sales report: total sales $100k"

async def fetch_all_reports():
    regions = ["North", "South", "East", "West", "Central"]
    tasks = [fetch_sales_report(region) for region in regions]
    results = await asyncio.gather(*tasks)
    return "\n".join(results)

# To run it
# asyncio.run(fetch_all_reports())
