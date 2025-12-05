"""
Brand Identity Discovery MCP Server - FULL VERSION

Complete brand identity generation using astrology, Human Design, and brand strategy.
Optimized for FastMCP Cloud deployment.
"""

from fastmcp import FastMCP
from datetime import datetime
import json

# Create FastMCP server
mcp = FastMCP("Brand Identity Discovery")

# ============================================================================
# DATA - All brand frameworks
# ============================================================================

ZODIAC_SIGNS = {
    "Aries": {
        "element": "Fire",
        "modality": "Cardinal",
        "keywords": ["pioneering", "bold", "energetic", "competitive", "direct"],
        "brand_traits": ["innovative", "dynamic", "courageous", "action-oriented"]
    },
    "Taurus": {
        "element": "Earth",
        "modality": "Fixed",
        "keywords": ["stable", "sensual", "reliable", "patient", "luxurious"],
        "brand_traits": ["trustworthy", "quality-focused", "grounded", "enduring"]
    },
    "Gemini": {
        "element": "Air",
        "modality": "Mutable",
        "keywords": ["communicative", "versatile", "curious", "witty", "social"],
        "brand_traits": ["adaptable", "engaging", "informative", "multi-faceted"]
    },
    "Cancer": {
        "element": "Water",
        "modality": "Cardinal",
        "keywords": ["nurturing", "intuitive", "protective", "emotional", "homey"],
        "brand_traits": ["caring", "supportive", "empathetic", "community-focused"]
    },
    "Leo": {
        "element": "Fire",
        "modality": "Fixed",
        "keywords": ["confident", "creative", "generous", "dramatic", "royal"],
        "brand_traits": ["bold", "charismatic", "premium", "expressive"]
    },
    "Virgo": {
        "element": "Earth",
        "modality": "Mutable",
        "keywords": ["analytical", "precise", "helpful", "practical", "refined"],
        "brand_traits": ["detail-oriented", "efficient", "service-focused", "expert"]
    },
    "Libra": {
        "element": "Air",
        "modality": "Cardinal",
        "keywords": ["harmonious", "diplomatic", "aesthetic", "balanced", "social"],
        "brand_traits": ["elegant", "fair", "collaborative", "refined"]
    },
    "Scorpio": {
        "element": "Water",
        "modality": "Fixed",
        "keywords": ["intense", "transformative", "mysterious", "powerful", "deep"],
        "brand_traits": ["authentic", "transformative", "passionate", "profound"]
    },
    "Sagittarius": {
        "element": "Fire",
        "modality": "Mutable",
        "keywords": ["adventurous", "philosophical", "optimistic", "free", "expansive"],
        "brand_traits": ["visionary", "adventurous", "inspiring", "global"]
    },
    "Capricorn": {
        "element": "Earth",
        "modality": "Cardinal",
        "keywords": ["ambitious", "disciplined", "traditional", "authoritative", "responsible"],
        "brand_traits": ["professional", "reliable", "ambitious", "structured"]
    },
    "Aquarius": {
        "element": "Air",
        "modality": "Fixed",
        "keywords": ["innovative", "humanitarian", "unconventional", "intellectual", "independent"],
        "brand_traits": ["progressive", "unique", "humanitarian", "innovative"]
    },
    "Pisces": {
        "element": "Water",
        "modality": "Mutable",
        "keywords": ["compassionate", "artistic", "intuitive", "dreamy", "spiritual"],
        "brand_traits": ["imaginative", "empathetic", "creative", "spiritual"]
    }
}

HUMAN_DESIGN_TYPES = {
    "Manifestor": {
        "strategy": "Inform before acting",
        "percentage": "9%",
        "brand_strength": "Initiating, pioneering, independent action",
        "brand_approach": "Bold launches, trend-setting, disruptive innovation"
    },
    "Generator": {
        "strategy": "Wait to respond",
        "percentage": "37%",
        "brand_strength": "Sustainable energy, mastery, satisfaction",
        "brand_approach": "Responsive service, building momentum, sustainable growth"
    },
    "Manifesting Generator": {
        "strategy": "Wait to respond, then inform",
        "percentage": "33%",
        "brand_strength": "Multi-passionate, efficient, fast-paced",
        "brand_approach": "Quick pivots, multi-faceted offerings, dynamic evolution"
    },
    "Projector": {
        "strategy": "Wait for invitation",
        "percentage": "20%",
        "brand_strength": "Guidance, systems, recognition",
        "brand_approach": "Expert positioning, premium pricing, invitation-based marketing"
    },
    "Reflector": {
        "strategy": "Wait a lunar cycle",
        "percentage": "1%",
        "brand_strength": "Evaluation, reflection, community barometer",
        "brand_approach": "Unique perspective, community-focused, reflective content"
    }
}

HUMAN_DESIGN_AUTHORITIES = {
    "Emotional": "Wait for emotional clarity over time",
    "Sacral": "Trust gut responses in the moment",
    "Splenic": "Trust intuitive hits in the present",
    "Ego": "Trust willpower and heart desires",
    "Self-Projected": "Trust what you hear yourself say",
    "Environmental": "Trust wisdom from your environment",
    "Lunar": "Wait through a full moon cycle"
}

HUMAN_DESIGN_PROFILES = {
    "1/3": {"name": "Investigator/Martyr", "essence": "Research-based experimentation"},
    "1/4": {"name": "Investigator/Opportunist", "essence": "Expert networking"},
    "2/4": {"name": "Hermit/Opportunist", "essence": "Natural talent meets networking"},
    "2/5": {"name": "Hermit/Heretic", "essence": "Called forth genius"},
    "3/5": {"name": "Martyr/Heretic", "essence": "Trial and error problem-solving"},
    "3/6": {"name": "Martyr/Role Model", "essence": "Experiential wisdom"},
    "4/6": {"name": "Opportunist/Role Model", "essence": "Network-based leadership"},
    "4/1": {"name": "Opportunist/Investigator", "essence": "Networking meets research"},
    "5/1": {"name": "Heretic/Investigator", "essence": "Practical solutions"},
    "5/2": {"name": "Heretic/Hermit", "essence": "Universal problem-solver"},
    "6/2": {"name": "Role Model/Hermit", "essence": "Wisdom through experience"},
    "6/3": {"name": "Role Model/Martyr", "essence": "Authentic living example"}
}

BRAND_ARCHETYPES = {
    "Innocent": {"desire": "Safety and happiness"},
    "Sage": {"desire": "Truth and knowledge"},
    "Explorer": {"desire": "Freedom and discovery"},
    "Outlaw": {"desire": "Revolution and change"},
    "Magician": {"desire": "Transformation"},
    "Hero": {"desire": "Mastery and courage"},
    "Lover": {"desire": "Intimacy and beauty"},
    "Jester": {"desire": "Joy and fun"},
    "Everyperson": {"desire": "Belonging and connection"},
    "Caregiver": {"desire": "Service and care"},
    "Ruler": {"desire": "Control and order"},
    "Creator": {"desire": "Innovation and expression"}
}

ARCHETYPE_COLORS = {
    "Innocent": {"primary": "#FFE5E5", "secondary": "#B8E6FF", "accent": "#FFF8DC"},
    "Sage": {"primary": "#2C3E50", "secondary": "#95A5A6", "accent": "#F39C12"},
    "Explorer": {"primary": "#8B4513", "secondary": "#556B2F", "accent": "#CD853F"},
    "Outlaw": {"primary": "#000000", "secondary": "#8B0000", "accent": "#4B0082"},
    "Magician": {"primary": "#4B0082", "secondary": "#483D8B", "accent": "#C0C0C0"},
    "Hero": {"primary": "#DC143C", "secondary": "#00008B", "accent": "#FFD700"},
    "Lover": {"primary": "#8B0000", "secondary": "#FF69B4", "accent": "#FFD700"},
    "Jester": {"primary": "#FF6347", "secondary": "#FFD700", "accent": "#32CD32"},
    "Everyperson": {"primary": "#8B7355", "secondary": "#CD853F", "accent": "#F5DEB3"},
    "Caregiver": {"primary": "#87CEEB", "secondary": "#98FB98", "accent": "#F5DEB3"},
    "Ruler": {"primary": "#00008B", "secondary": "#800080", "accent": "#FFD700"},
    "Creator": {"primary": "#FF4500", "secondary": "#9370DB", "accent": "#FFD700"}
}

ARCHETYPE_FONTS = {
    "Innocent": {"heading": "Quicksand, Nunito, or Poppins", "body": "Open Sans or Lato", "style": "Friendly, rounded, approachable"},
    "Sage": {"heading": "Merriweather, Playfair Display, or Georgia", "body": "Source Sans Pro or Roboto", "style": "Classic, authoritative, readable"},
    "Explorer": {"heading": "Montserrat Bold or Bebas Neue", "body": "Raleway or Lato", "style": "Bold, adventurous, rugged"},
    "Outlaw": {"heading": "Oswald, Bebas Neue, or Impact", "body": "Roboto or Open Sans", "style": "Bold, edgy, rebellious"},
    "Magician": {"heading": "Cinzel, Philosopher, or Cormorant Garamond", "body": "Lora or Crimson Text", "style": "Mystical, elegant, transformative"},
    "Hero": {"heading": "Montserrat Black or Oswald", "body": "Open Sans or Roboto", "style": "Strong, confident, powerful"},
    "Lover": {"heading": "Playfair Display or Cormorant Garamond", "body": "Crimson Text or Lora", "style": "Elegant, romantic, sophisticated"},
    "Jester": {"heading": "Fredoka One or Baloo", "body": "Quicksand or Nunito", "style": "Playful, energetic, fun"},
    "Everyperson": {"heading": "Open Sans or Lato", "body": "Roboto or PT Sans", "style": "Friendly, accessible, comfortable"},
    "Caregiver": {"heading": "Nunito or Quicksand", "body": "Open Sans or Lato", "style": "Warm, soft, nurturing"},
    "Ruler": {"heading": "Playfair Display or Cinzel", "body": "Lora or Crimson Text", "style": "Refined, authoritative, elegant"},
    "Creator": {"heading": "Montserrat or Raleway", "body": "Open Sans or Lato", "style": "Modern, creative, versatile"}
}

ARCHETYPE_VOICE = {
    "Innocent": {"personality": "Optimistic, simple, honest, pure", "tone": "Friendly, encouraging, positive"},
    "Sage": {"personality": "Intelligent, analytical, thoughtful, guiding", "tone": "Authoritative, informative, thoughtful"},
    "Explorer": {"personality": "Adventurous, authentic, brave, free", "tone": "Bold, inspiring, authentic"},
    "Outlaw": {"personality": "Rebellious, disruptive, provocative, raw", "tone": "Bold, direct, challenging"},
    "Magician": {"personality": "Visionary, inspirational, transformative, magical", "tone": "Inspiring, mystical, transformative"},
    "Hero": {"personality": "Courageous, inspiring, determined, triumphant", "tone": "Motivating, confident, strong"},
    "Lover": {"personality": "Passionate, intimate, sensual, devoted", "tone": "Warm, intimate, elegant"},
    "Jester": {"personality": "Fun, playful, irreverent, joyful", "tone": "Playful, humorous, lighthearted"},
    "Everyperson": {"personality": "Friendly, down-to-earth, reliable, genuine", "tone": "Conversational, warm, authentic"},
    "Caregiver": {"personality": "Compassionate, nurturing, supportive, warm", "tone": "Caring, gentle, supportive"},
    "Ruler": {"personality": "Authoritative, confident, refined, prestigious", "tone": "Sophisticated, authoritative, refined"},
    "Creator": {"personality": "Innovative, imaginative, artistic, original", "tone": "Creative, inspiring, original"}
}

VISUAL_STYLES = {
    "Innocent": {"aesthetic": "Soft, light, optimistic, simple", "imagery": "Bright, happy, uplifting images"},
    "Sage": {"aesthetic": "Clean, authoritative, informative, trustworthy", "imagery": "Professional, educational, thoughtful"},
    "Explorer": {"aesthetic": "Rugged, natural, adventurous, authentic", "imagery": "Nature, adventure, discovery, journeys"},
    "Outlaw": {"aesthetic": "Bold, edgy, disruptive, unconventional", "imagery": "Urban, raw, rebellious, provocative"},
    "Magician": {"aesthetic": "Mystical, transformative, visionary, enchanting", "imagery": "Transformative, magical, inspiring, cosmic"},
    "Hero": {"aesthetic": "Strong, confident, triumphant, powerful", "imagery": "Achievement, strength, victory, courage"},
    "Lover": {"aesthetic": "Elegant, sensual, intimate, beautiful", "imagery": "Beauty, romance, luxury, intimacy"},
    "Jester": {"aesthetic": "Fun, playful, energetic, joyful", "imagery": "Playful, humorous, colorful, lively"},
    "Everyperson": {"aesthetic": "Friendly, relatable, comfortable, genuine", "imagery": "Real people, everyday life, authenticity"},
    "Caregiver": {"aesthetic": "Warm, nurturing, supportive, gentle", "imagery": "Care, support, comfort, warmth"},
    "Ruler": {"aesthetic": "Refined, prestigious, authoritative, luxurious", "imagery": "Premium, sophisticated, powerful, prestigious"},
    "Creator": {"aesthetic": "Innovative, artistic, unique, expressive", "imagery": "Creative, original, artistic, imaginative"}
}

# ============================================================================
# CALCULATION FUNCTIONS
# ============================================================================

def calculate_zodiac_sign(day: int, month: int) -> str:
    """Calculate zodiac sign from day and month"""
    if (month == 3 and day >= 21) or (month == 4 and day <= 19): return "Aries"
    if (month == 4 and day >= 20) or (month == 5 and day <= 20): return "Taurus"
    if (month == 5 and day >= 21) or (month == 6 and day <= 20): return "Gemini"
    if (month == 6 and day >= 21) or (month == 7 and day <= 22): return "Cancer"
    if (month == 7 and day >= 23) or (month == 8 and day <= 22): return "Leo"
    if (month == 8 and day >= 23) or (month == 9 and day <= 22): return "Virgo"
    if (month == 9 and day >= 23) or (month == 10 and day <= 22): return "Libra"
    if (month == 10 and day >= 23) or (month == 11 and day <= 21): return "Scorpio"
    if (month == 11 and day >= 22) or (month == 12 and day <= 21): return "Sagittarius"
    if (month == 12 and day >= 22) or (month == 1 and day <= 19): return "Capricorn"
    if (month == 1 and day >= 20) or (month == 2 and day <= 18): return "Aquarius"
    return "Pisces"

def calculate_rising_sign(birth_hour: int, birth_minute: int) -> str:
    """Calculate rising sign from birth time (simplified)"""
    total_minutes = birth_hour * 60 + birth_minute
    sign_index = (total_minutes // 120) % 12
    signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
             "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
    return signs[sign_index]

def calculate_moon_sign(day: int, month: int, year: int) -> str:
    """Calculate moon sign (simplified lunar calculation)"""
    days_since_epoch = (year - 2000) * 365.25 + month * 30.44 + day
    lunar_position = (days_since_epoch * 13.176) % 360
    sign_index = int(lunar_position // 30)
    signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
             "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
    return signs[sign_index]

def calculate_human_design_type(day: int, month: int, hour: int) -> str:
    """Calculate Human Design type (simplified)"""
    value = (day + month * 3 + hour * 5) % 100
    if value < 9: return "Manifestor"
    if value < 46: return "Generator"
    if value < 79: return "Manifesting Generator"
    if value < 99: return "Projector"
    return "Reflector"

def calculate_human_design_authority(hd_type: str, day: int) -> str:
    """Calculate Human Design authority"""
    if hd_type == "Manifestor":
        return "Splenic" if day % 2 == 0 else "Emotional"
    elif hd_type in ["Generator", "Manifesting Generator"]:
        return "Sacral" if day % 3 == 0 else "Emotional"
    elif hd_type == "Projector":
        authorities = ["Splenic", "Ego", "Self-Projected", "Environmental", "Emotional"]
        return authorities[day % len(authorities)]
    return "Lunar"

def calculate_human_design_profile(day: int, month: int) -> str:
    """Calculate Human Design profile"""
    profiles = ["1/3", "1/4", "2/4", "2/5", "3/5", "3/6", "4/6", "4/1", "5/1", "5/2", "6/2", "6/3"]
    return profiles[(day + month) % len(profiles)]

def determine_brand_archetype(sun_sign: str, moon_sign: str, rising_sign: str, hd_type: str) -> str:
    """Determine primary brand archetype"""
    mapping = {
        "Aries": "Hero", "Taurus": "Everyperson", "Gemini": "Jester",
        "Cancer": "Caregiver", "Leo": "Ruler", "Virgo": "Sage",
        "Libra": "Lover", "Scorpio": "Magician", "Sagittarius": "Explorer",
        "Capricorn": "Ruler", "Aquarius": "Creator", "Pisces": "Innocent"
    }
    
    hd_archetypes = {
        "Manifestor": "Outlaw", "Generator": "Everyperson",
        "Manifesting Generator": "Creator", "Projector": "Sage", "Reflector": "Magician"
    }
    
    primary = mapping.get(sun_sign, "Sage")
    
    if hd_type in hd_archetypes:
        hd_influence = hd_archetypes[hd_type]
        if hd_influence != primary and hash(sun_sign + hd_type) % 10 < 3:
            return hd_influence
    
    return primary

def hex_to_rgb(hex_color: str) -> str:
    """Convert hex to RGB"""
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return f"{r}, {g}, {b}"

# ============================================================================
# MCP TOOLS
# ============================================================================

@mcp.tool()
def generate_brand_identity(
    birth_date: str,
    birth_time: str,
    birth_location: str,
    business_name: str = None
) -> dict:
    """
    Generate complete brand identity guidelines based on birth data.
    
    Args:
        birth_date: Birth date in YYYY-MM-DD format (e.g., "1987-10-28")
        birth_time: Birth time in HH:MM format, 24-hour (e.g., "14:30")
        birth_location: Birth location (e.g., "Buenos Aires, Argentina")
        business_name: Optional business name
    
    Returns:
        Complete Canva-style brand guidelines
    
    Example:
        generate_brand_identity("1987-10-28", "14:30", "Buenos Aires, Argentina")
    """
    try:
        # Parse date and time
        date_obj = datetime.strptime(birth_date, "%Y-%m-%d")
        time_obj = datetime.strptime(birth_time, "%H:%M")
        
        day, month, year = date_obj.day, date_obj.month, date_obj.year
        hour, minute = time_obj.hour, time_obj.minute
        
        # Calculate astrology
        sun_sign = calculate_zodiac_sign(day, month)
        moon_sign = calculate_moon_sign(day, month, year)
        rising_sign = calculate_rising_sign(hour, minute)
        
        # Calculate Human Design
        hd_type = calculate_human_design_type(day, month, hour)
        hd_authority = calculate_human_design_authority(hd_type, day)
        hd_profile = calculate_human_design_profile(day, month)
        
        # Determine archetype
        archetype = determine_brand_archetype(sun_sign, moon_sign, rising_sign, hd_type)
        
        # Get brand elements
        colors = ARCHETYPE_COLORS[archetype]
        fonts = ARCHETYPE_FONTS[archetype]
        voice = ARCHETYPE_VOICE[archetype]
        visual = VISUAL_STYLES[archetype]
        
        # Format guidelines
        guidelines = f"""# BRAND IDENTITY GUIDELINES

**Generated for:** {birth_date} at {birth_time} in {birth_location}

---

## Core Brand Identity

**Primary Archetype:** {archetype}
**Astrological Foundation:** {sun_sign} Sun • {moon_sign} Moon • {rising_sign} Rising
**Human Design:** {hd_type} • {hd_authority} Authority • {hd_profile} Profile

{BRAND_ARCHETYPES[archetype]['desire']} is at the heart of this brand.
This core identity shapes every visual and verbal element of your brand presence.

---

## Color Palette

**Primary Brand Color**
Primary Color • {colors['primary']} • RGB {hex_to_rgb(colors['primary'])}
Use for: Main brand elements, headers, key CTAs

**Secondary Color**
Secondary Color • {colors['secondary']} • RGB {hex_to_rgb(colors['secondary'])}
Use for: Supporting elements, subheadings, backgrounds

**Accent Color**
Accent Color • {colors['accent']} • RGB {hex_to_rgb(colors['accent'])}
Use for: Highlights, buttons, important details

**Neutral Colors**
Dark Neutral • #2C3E50 • RGB 44, 62, 80
Medium Neutral • #95A5A6 • RGB 149, 165, 166
Light Neutral • #ECF0F1 • RGB 236, 240, 241

---

## Typography

**Heading Font:** {fonts['heading']}
Use for: Main headlines, section headers, hero text
Sizes: H1 48-60px, H2 36-42px, H3 24-30px

**Body Font:** {fonts['body']}
Use for: Paragraphs, descriptions, general content
Sizes: Body 16-18px, Caption 14px

**Font Style:** {fonts['style']}
Line height: 1.5-1.8
Letter spacing: Normal (0) for body, tight (-0.5px) for headings

---

## Logo Guidelines

**Style:** {archetype} brand aesthetic

**Primary Logo**
Font: Primary heading font
Color: Primary brand color
Format: Full color on white background

**Required Variations**
• Full color
• Single color (black)
• Single color (white)
• Horizontal version
• Stacked version
• Icon only

**Sizing & Spacing**
Minimum size: 24px height for digital, 0.5 inch for print
Clear space: Equal to height of logo on all sides
Formats: SVG, PNG, PDF

---

## Visual Style

**Overall Aesthetic:** {visual['aesthetic']}

**Imagery Style:** {visual['imagery']}

**Photography Direction**
Style: Images should feel {visual['aesthetic']}
Subjects: {visual['imagery']}

---

## Brand Voice

**Personality:** {voice['personality']}
**Tone:** {voice['tone']}

**Communication Style**
Speak with {voice['tone']} to connect authentically with your audience.
Embody {voice['personality']} in every message.

---

## Quick Reference

**One-Line Brand Essence:** {archetype} brand with {sun_sign} energy, {hd_type} approach

**Color Snapshot:** {colors['primary']} • {colors['secondary']} • {colors['accent']}

**Font Pairing:** {fonts['heading']} + {fonts['body']}

**Visual Mood:** {visual['aesthetic']}

**Voice:** {voice['personality']}

---

*These guidelines provide a complete foundation for your brand identity. Use them to maintain consistency across all brand touchpoints, from website to social media to print materials.*
"""
        
        return {
            "status": "success",
            "birth_data": {
                "date": birth_date,
                "time": birth_time,
                "location": birth_location
            },
            "astrology": {
                "sun_sign": sun_sign,
                "moon_sign": moon_sign,
                "rising_sign": rising_sign
            },
            "human_design": {
                "type": hd_type,
                "authority": hd_authority,
                "profile": hd_profile
            },
            "archetype": archetype,
            "guidelines": guidelines
        }
        
    except Exception as e:
        return {"status": "error", "error": str(e)}


@mcp.tool()
def get_color_palette_only(
    birth_date: str,
    birth_time: str,
    birth_location: str
) -> dict:
    """
    Generate only the color palette based on birth data.
    
    Args:
        birth_date: Birth date in YYYY-MM-DD format
        birth_time: Birth time in HH:MM format
        birth_location: Birth location
    
    Returns:
        Color palette with hex codes
    
    Example:
        get_color_palette_only("1987-10-28", "14:30", "Buenos Aires, Argentina")
    """
    try:
        date_obj = datetime.strptime(birth_date, "%Y-%m-%d")
        time_obj = datetime.strptime(birth_time, "%H:%M")
        
        day, month, year = date_obj.day, date_obj.month, date_obj.year
        hour = time_obj.hour
        
        sun_sign = calculate_zodiac_sign(day, month)
        moon_sign = calculate_moon_sign(day, month, year)
        rising_sign = calculate_rising_sign(hour, time_obj.minute)
        hd_type = calculate_human_design_type(day, month, hour)
        
        archetype = determine_brand_archetype(sun_sign, moon_sign, rising_sign, hd_type)
        colors = ARCHETYPE_COLORS[archetype]
        
        return {
            "status": "success",
            "archetype": archetype,
            "colors": {
                "primary": {"hex": colors['primary'], "rgb": hex_to_rgb(colors['primary'])},
                "secondary": {"hex": colors['secondary'], "rgb": hex_to_rgb(colors['secondary'])},
                "accent": {"hex": colors['accent'], "rgb": hex_to_rgb(colors['accent'])}
            }
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


@mcp.tool()
def get_typography_only(
    birth_date: str,
    birth_time: str,
    birth_location: str
) -> dict:
    """
    Generate only typography recommendations based on birth data.
    
    Args:
        birth_date: Birth date in YYYY-MM-DD format
        birth_time: Birth time in HH:MM format
        birth_location: Birth location
    
    Returns:
        Typography recommendations
    
    Example:
        get_typography_only("1987-10-28", "14:30", "Buenos Aires, Argentina")
    """
    try:
        date_obj = datetime.strptime(birth_date, "%Y-%m-%d")
        time_obj = datetime.strptime(birth_time, "%H:%M")
        
        day, month, year = date_obj.day, date_obj.month, date_obj.year
        hour = time_obj.hour
        
        sun_sign = calculate_zodiac_sign(day, month)
        moon_sign = calculate_moon_sign(day, month, year)
        rising_sign = calculate_rising_sign(hour, time_obj.minute)
        hd_type = calculate_human_design_type(day, month, hour)
        
        archetype = determine_brand_archetype(sun_sign, moon_sign, rising_sign, hd_type)
        fonts = ARCHETYPE_FONTS[archetype]
        
        return {
            "status": "success",
            "archetype": archetype,
            "typography": fonts
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


@mcp.tool()
def calculate_birth_chart(
    birth_date: str,
    birth_time: str,
    birth_location: str
) -> dict:
    """
    Calculate astrological birth chart (Sun, Moon, Rising signs).
    
    Args:
        birth_date: Birth date in YYYY-MM-DD format
        birth_time: Birth time in HH:MM format
        birth_location: Birth location
    
    Returns:
        Birth chart with all three signs
    
    Example:
        calculate_birth_chart("1987-10-28", "14:30", "Buenos Aires, Argentina")
    """
    try:
        date_obj = datetime.strptime(birth_date, "%Y-%m-%d")
        time_obj = datetime.strptime(birth_time, "%H:%M")
        
        day, month, year = date_obj.day, date_obj.month, date_obj.year
        hour, minute = time_obj.hour, time_obj.minute
        
        sun_sign = calculate_zodiac_sign(day, month)
        moon_sign = calculate_moon_sign(day, month, year)
        rising_sign = calculate_rising_sign(hour, minute)
        
        return {
            "status": "success",
            "birth_chart": {
                "sun_sign": sun_sign,
                "sun_traits": ZODIAC_SIGNS[sun_sign],
                "moon_sign": moon_sign,
                "moon_traits": ZODIAC_SIGNS[moon_sign],
                "rising_sign": rising_sign,
                "rising_traits": ZODIAC_SIGNS[rising_sign]
            }
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


@mcp.tool()
def calculate_human_design(
    birth_date: str,
    birth_time: str,
    birth_location: str
) -> dict:
    """
    Calculate Human Design chart (Type, Authority, Profile).
    
    Args:
        birth_date: Birth date in YYYY-MM-DD format
        birth_time: Birth time in HH:MM format
        birth_location: Birth location
    
    Returns:
        Human Design chart
    
    Example:
        calculate_human_design("1987-10-28", "14:30", "Buenos Aires, Argentina")
    """
    try:
        date_obj = datetime.strptime(birth_date, "%Y-%m-%d")
        time_obj = datetime.strptime(birth_time, "%H:%M")
        
        day, month = date_obj.day, date_obj.month
        hour = time_obj.hour
        
        hd_type = calculate_human_design_type(day, month, hour)
        hd_authority = calculate_human_design_authority(hd_type, day)
        hd_profile = calculate_human_design_profile(day, month)
        
        return {
            "status": "success",
            "human_design": {
                "type": hd_type,
                "type_details": HUMAN_DESIGN_TYPES[hd_type],
                "authority": hd_authority,
                "authority_description": HUMAN_DESIGN_AUTHORITIES[hd_authority],
                "profile": hd_profile,
                "profile_details": HUMAN_DESIGN_PROFILES[hd_profile]
            }
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


# FastMCP Cloud will automatically run this server!

