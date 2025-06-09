# First definition – standard function
def convert_celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32


# Tool definition – for use in agent frameworks
from some_tool_framework import tool  # Replace with the actual import

@tool
def convert_celsius_to_fahrenheit(celsius: float) -> float:
    """Tool to convert temperature from Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32
