"""
Brand Identity Discovery MCP Server
Fixed for FastMCP Cloud asyncio compatibility
"""

from datetime import datetime
from typing import Optional
import json

# Import FastMCP without running any async code at module level
from mcp.server.fastmcp import FastMCP

# Create server instance (but don't run it)
mcp = FastMCP("Brand Identity Discovery")

# ============================================================================
# DATA & FUNCTIONS
# ============================================================================

ZODIAC_SIGNS = {
    "Aries": {"element": "Fire", "brand_traits": ["innovative", "dynamic", "courageous"]},
    "Taurus": {"element": "Earth", "brand_traits": ["trustworthy", "quality-focused", "grounded"]},
    "Gemini": {"element": "Air", "brand_traits": ["adaptable", "engaging", "informative"]},
    "Cancer": {"element": "Water", "brand_traits": ["caring", "supportive", "empathetic"]},
    "Leo": {"element": "Fire", "brand_traits": ["bold", "charismatic", "premium"]},
    "Virgo": {"element": "Earth", "brand_traits": ["detail-oriented", "efficient", "expert"]},
    "Libra": {"element": "Air", "brand_traits": ["elegant", "fair", "collaborative"]},
    "Scorpio": {"element": "Water", "brand_traits": ["authentic", "transformative", "passionate"]},
    "Sagittarius": {"element": "Fire", "brand_traits": ["visionary", "adventurous", "inspiring"]},
    "Capricorn": {"element": "Earth", "brand_traits": ["professional", "reliable", "ambitious"]},
    "Aquarius": {"element": "Air", "brand_traits": ["progressive", "unique", "innovative"]},
    "Pisces": {"element": "Water", "brand_traits": ["imaginative", "empathetic", "creative"]}
}

BRAND_ARCHETYPES = {
    "Innocent": {"colors": ["#FFE5E5", "#B8E6FF", "#FFF8DC"]},
    "Sage": {"colors": ["#2C3E50", "#95A5A6", "#F39C12"]},
    "Explorer": {"colors": ["#8B4513", "#556B2F", "#CD853F"]},
    "Outlaw": {"colors": ["#000000", "#8B0000", "#4B0082"]},
    "Magician": {"colors": ["#4B0082", "#483D8B", "#C0C0C0"]},
    "Hero": {"colors": ["#DC143C", "#00008B", "#FFD700"]},
    "Lover": {"colors": ["#8B0000", "#FF69B4", "#FFD700"]},
    "Jester": {"colors": ["#FF6347", "#FFD700", "#32CD32"]},
    "Everyperson": {"colors": ["#8B7355", "#CD853F", "#F5DEB3"]},
    "Caregiver": {"colors": ["#87CEEB", "#98FB98", "#F5DEB3"]},
    "Ruler": {"colors": ["#00008B", "#800080", "#FFD700"]},
    "Creator": {"colors": ["#FF4500", "#9370DB", "#FFD700"]}
}

def calculate_zodiac_sign(day: int, month: int) -> str:
    """Calculate zodiac sign"""
    dates = [(3,21,"Aries"),(4,20,"Taurus"),(5,21,"Gemini"),(6,21,"Cancer"),
             (7,23,"Leo"),(8,23,"Virgo"),(9,23,"Libra"),(10,23,"Scorpio"),
             (11,22,"Sagittarius"),(12,22,"Capricorn"),(1,20,"Aquarius"),(2,19,"Pisces")]
    
    for i, (sm, sd, sign) in enumerate(dates):
        ni = (i + 1) % 12
        em, ed, _ = dates[ni]
        if (month == sm and day >= sd) or (month == em and day < ed):
            return sign
    return "Capricorn"

def determine_archetype(sun_sign: str) -> str:
    """Simple archetype mapping"""
    mapping = {"Aries":"Hero","Taurus":"Everyperson","Gemini":"Jester","Cancer":"Caregiver",
               "Leo":"Ruler","Virgo":"Sage","Libra":"Lover","Scorpio":"Magician",
               "Sagittarius":"Explorer","Capricorn":"Ruler","Aquarius":"Creator","Pisces":"Innocent"}
    return mapping.get(sun_sign, "Sage")

# ============================================================================
# MCP TOOLS
# ============================================================================

@mcp.tool()
def generate_brand_identity(birth_date: str, birth_time: str, birth_location: str) -> str:
    """
    Generate complete brand identity guidelines.
    
    Args:
        birth_date: Birth date in YYYY-MM-DD format (e.g., "1987-10-28")
        birth_time: Birth time in HH:MM format (e.g., "14:30")
        birth_location: Birth location (e.g., "Buenos Aires, Argentina")
        
    Returns:
        Complete brand guidelines in Canva style
    """
    
    try:
        # Parse date
        date_obj = datetime.strptime(birth_date, "%Y-%m-%d")
        day, month = date_obj.day, date_obj.month
        
        # Calculate
        sun_sign = calculate_zodiac_sign(day, month)
        archetype = determine_archetype(sun_sign)
        colors = BRAND_ARCHETYPES[archetype]["colors"]
        
        # Generate guidelines
        guidelines = f"""# BRAND IDENTITY GUIDELINES

Generated for: {birth_date} at {birth_time} in {birth_location}

## Core Brand Identity
**Primary Archetype:** {archetype}
**Sun Sign:** {sun_sign}
**Element:** {ZODIAC_SIGNS[sun_sign]['element']}

## Color Palette
**Primary Color:** {colors[0]}
**Secondary Color:** {colors[1]}
**Accent Color:** {colors[2]}

## Brand Traits
{', '.join(ZODIAC_SIGNS[sun_sign]['brand_traits'])}

## Quick Reference
**Brand Essence:** {archetype} brand with {sun_sign} energy
**Color Snapshot:** {colors[0]} • {colors[1]} • {colors[2]}

---
*Complete brand identity guidelines generated successfully!*
"""
        return guidelines
        
    except Exception as e:
        return json.dumps({"error": str(e)}, indent=2)

@mcp.tool()
def get_color_palette(birth_date: str) -> str:
    """
    Get just the color palette.
    
    Args:
        birth_date: Birth date in YYYY-MM-DD format
        
    Returns:
        JSON with color palette
    """
    try:
        date_obj = datetime.strptime(birth_date, "%Y-%m-%d")
        sun_sign = calculate_zodiac_sign(date_obj.day, date_obj.month)
        archetype = determine_archetype(sun_sign)
        colors = BRAND_ARCHETYPES[archetype]["colors"]
        
        return json.dumps({
            "archetype": archetype,
            "primary": colors[0],
            "secondary": colors[1],
            "accent": colors[2]
        }, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)}, indent=2)

@mcp.tool()
def calculate_sun_sign(birth_date: str) -> str:
    """
    Calculate sun sign from birth date.
    
    Args:
        birth_date: Birth date in YYYY-MM-DD format
        
    Returns:
        JSON with sun sign and traits
    """
    try:
        date_obj = datetime.strptime(birth_date, "%Y-%m-%d")
        sun_sign = calculate_zodiac_sign(date_obj.day, date_obj.month)
        
        return json.dumps({
            "sun_sign": sun_sign,
            "element": ZODIAC_SIGNS[sun_sign]["element"],
            "brand_traits": ZODIAC_SIGNS[sun_sign]["brand_traits"]
        }, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)}, indent=2)

# Note: No mcp.run() call here - FastMCP Cloud handles that

