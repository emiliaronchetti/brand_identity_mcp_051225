"""
Brand Identity Discovery MCP Server - Minimal Test Version
"""

from mcp.server.fastmcp import FastMCP

# Initialize server
mcp = FastMCP("Brand Identity Discovery")

@mcp.tool()
def test_tool(name: str = "World") -> str:
    """
    Simple test tool to verify server is working.
    
    Args:
        name: Name to greet
        
    Returns:
        A greeting message
    """
    return f"Hello {name}! Brand Identity MCP Server is working! 🎉"
