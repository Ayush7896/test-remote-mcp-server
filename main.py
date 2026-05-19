from fastmcp import FastMCP
import random
import json


mcp = FastMCP("Simple calculator server")

# Tool: add two numbers

@mcp.tool
def add(a: int, b: int) -> int:
    """
    Add two numbers together

    Args:
        a: First number
        b: Second number

    Returns:
        The sum of a and b    
    """
    return a + b


if __name__ == "__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000)
