"""
Brand Identity Discovery MCP Server
Integrated version combining astrology, Human Design, and brand strategy
Output format: Clean Canva-style brand guidelines
"""

from datetime import datetime
from typing import Optional
import json
import math

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    print("Warning: FastMCP not available. Install with: pip install fastmcp")
    FastMCP = None

# Initialize MCP server
if FastMCP:
    mcp = FastMCP("Brand Identity Discovery")

# ============================================================================
# VALIDATION
# ============================================================================

class ValidationError(Exception):
    """Custom validation error"""
    def __init__(self, message: str, field: str = None, valid_values: list = None):
        self.message = message
        self.field = field
        self.valid_values = valid_values
        super().__init__(self.message)

def validate_birth_data(date: str, time: str, location: str) -> dict:
    """Validate birth data inputs"""
    errors = []
    
    # Validate date format
    try:
        birth_date = datetime.strptime(date, "%Y-%m-%d")
        if birth_date > datetime.now():
            errors.append({"field": "date", "message": "Birth date cannot be in the future"})
    except ValueError:
        errors.append({"field": "date", "message": "Invalid date format. Use YYYY-MM-DD"})
    
    # Validate time format
    try:
        datetime.strptime(time, "%H:%M")
    except ValueError:
        errors.append({"field": "time", "message": "Invalid time format. Use HH:MM (24-hour)"})
    
    # Validate location
    if not location or len(location.strip()) < 2:
        errors.append({"field": "location", "message": "Location must be at least 2 characters"})
    
    if errors:
        return {"valid": False, "errors": errors}
    
    return {"valid": True, "errors": []}

# ============================================================================
# ASTROLOGY DATA
# ============================================================================

ZODIAC_SIGNS = {
    "Aries": {
        "element": "Fire",
        "quality": "Cardinal",
        "ruler": "Mars",
        "keywords": ["pioneering", "bold", "energetic", "competitive", "direct"],
        "brand_traits": ["innovative", "dynamic", "courageous", "action-oriented"]
    },
    "Taurus": {
        "element": "Earth",
        "quality": "Fixed",
        "ruler": "Venus",
        "keywords": ["stable", "sensual", "reliable", "patient", "luxurious"],
        "brand_traits": ["trustworthy", "quality-focused", "grounded", "enduring"]
    },
    "Gemini": {
        "element": "Air",
        "quality": "Mutable",
        "ruler": "Mercury",
        "keywords": ["communicative", "versatile", "curious", "witty", "social"],
        "brand_traits": ["adaptable", "engaging", "informative", "multi-faceted"]
    },
    "Cancer": {
        "element": "Water",
        "quality": "Cardinal",
        "ruler": "Moon",
        "keywords": ["nurturing", "intuitive", "protective", "emotional", "homey"],
        "brand_traits": ["caring", "supportive", "empathetic", "community-focused"]
    },
    "Leo": {
        "element": "Fire",
        "quality": "Fixed",
        "ruler": "Sun",
        "keywords": ["confident", "creative", "generous", "dramatic", "royal"],
        "brand_traits": ["bold", "charismatic", "premium", "expressive"]
    },
    "Virgo": {
        "element": "Earth",
        "quality": "Mutable",
        "ruler": "Mercury",
        "keywords": ["analytical", "precise", "helpful", "practical", "refined"],
        "brand_traits": ["detail-oriented", "efficient", "service-focused", "expert"]
    },
    "Libra": {
        "element": "Air",
        "quality": "Cardinal",
        "ruler": "Venus",
        "keywords": ["harmonious", "diplomatic", "aesthetic", "balanced", "social"],
        "brand_traits": ["elegant", "fair", "collaborative", "refined"]
    },
    "Scorpio": {
        "element": "Water",
        "quality": "Fixed",
        "ruler": "Pluto",
        "keywords": ["intense", "transformative", "mysterious", "powerful", "deep"],
        "brand_traits": ["authentic", "transformative", "passionate", "profound"]
    },
    "Sagittarius": {
        "element": "Fire",
        "quality": "Mutable",
        "ruler": "Jupiter",
        "keywords": ["adventurous", "philosophical", "optimistic", "free", "expansive"],
        "brand_traits": ["visionary", "adventurous", "inspiring", "global"]
    },
    "Capricorn": {
        "element": "Earth",
        "quality": "Cardinal",
        "ruler": "Saturn",
        "keywords": ["ambitious", "disciplined", "traditional", "authoritative", "responsible"],
        "brand_traits": ["professional", "reliable", "ambitious", "structured"]
    },
    "Aquarius": {
        "element": "Air",
        "quality": "Fixed",
        "ruler": "Uranus",
        "keywords": ["innovative", "humanitarian", "unconventional", "intellectual", "independent"],
        "brand_traits": ["progressive", "unique", "humanitarian", "innovative"]
    },
    "Pisces": {
        "element": "Water",
        "quality": "Mutable",
        "ruler": "Neptune",
        "keywords": ["compassionate", "artistic", "intuitive", "dreamy", "spiritual"],
        "brand_traits": ["imaginative", "empathetic", "creative", "spiritual"]
    }
}

PLANETS = {
    "Sun": {
        "represents": "Core identity, ego, life force",
        "brand_influence": "Overall brand personality and essence"
    },
    "Moon": {
        "represents": "Emotions, instincts, inner needs",
        "brand_influence": "Emotional connection and customer care"
    },
    "Mercury": {
        "represents": "Communication, thinking, information",
        "brand_influence": "Brand voice and messaging style"
    },
    "Venus": {
        "represents": "Beauty, values, attraction",
        "brand_influence": "Visual aesthetics and brand values"
    },
    "Mars": {
        "represents": "Action, drive, energy",
        "brand_influence": "Brand energy and competitive approach"
    },
    "Jupiter": {
        "represents": "Growth, expansion, abundance",
        "brand_influence": "Growth strategy and vision"
    },
    "Saturn": {
        "represents": "Structure, discipline, boundaries",
        "brand_influence": "Brand structure and professionalism"
    },
    "Uranus": {
        "represents": "Innovation, revolution, uniqueness",
        "brand_influence": "Innovation and differentiation"
    },
    "Neptune": {
        "represents": "Dreams, inspiration, spirituality",
        "brand_influence": "Brand mystique and inspiration"
    },
    "Pluto": {
        "represents": "Transformation, power, depth",
        "brand_influence": "Transformational impact"
    }
}

HOUSES = {
    1: {"area": "Self & Identity", "brand_aspect": "Brand personality"},
    2: {"area": "Values & Resources", "brand_aspect": "Brand values & pricing"},
    3: {"area": "Communication", "brand_aspect": "Messaging & content"},
    4: {"area": "Home & Roots", "brand_aspect": "Brand foundation"},
    5: {"area": "Creativity & Expression", "brand_aspect": "Creative expression"},
    6: {"area": "Service & Work", "brand_aspect": "Service delivery"},
    7: {"area": "Partnerships", "brand_aspect": "Collaborations"},
    8: {"area": "Transformation", "brand_aspect": "Deep impact"},
    9: {"area": "Philosophy & Travel", "brand_aspect": "Vision & expansion"},
    10: {"area": "Career & Public Image", "brand_aspect": "Public brand image"},
    11: {"area": "Community & Innovation", "brand_aspect": "Community building"},
    12: {"area": "Spirituality & Unconscious", "brand_aspect": "Deeper meaning"}
}

# ============================================================================
# HUMAN DESIGN DATA
# ============================================================================

HUMAN_DESIGN_TYPES = {
    "Manifestor": {
        "strategy": "Inform before acting",
        "aura": "Closed and repelling",
        "percentage": "9%",
        "brand_strength": "Initiating, pioneering, independent action",
        "brand_approach": "Bold launches, trend-setting, disruptive innovation"
    },
    "Generator": {
        "strategy": "Wait to respond",
        "aura": "Open and enveloping",
        "percentage": "37%",
        "brand_strength": "Sustainable energy, mastery, satisfaction",
        "brand_approach": "Responsive service, building momentum, sustainable growth"
    },
    "Manifesting Generator": {
        "strategy": "Wait to respond, then inform",
        "aura": "Open and enveloping",
        "percentage": "33%",
        "brand_strength": "Multi-passionate, efficient, fast-paced",
        "brand_approach": "Quick pivots, multi-faceted offerings, dynamic evolution"
    },
    "Projector": {
        "strategy": "Wait for invitation",
        "aura": "Focused and absorbing",
        "percentage": "20%",
        "brand_strength": "Guidance, systems, recognition",
        "brand_approach": "Expert positioning, premium pricing, invitation-based marketing"
    },
    "Reflector": {
        "strategy": "Wait a lunar cycle",
        "aura": "Resistant and sampling",
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
    "1/3": {"name": "Investigator/Martyr", "brand_essence": "Research-based experimentation"},
    "1/4": {"name": "Investigator/Opportunist", "brand_essence": "Expert networking"},
    "2/4": {"name": "Hermit/Opportunist", "brand_essence": "Natural talent meets networking"},
    "2/5": {"name": "Hermit/Heretic", "brand_essence": "Called forth genius"},
    "3/5": {"name": "Martyr/Heretic", "brand_essence": "Trial and error problem-solving"},
    "3/6": {"name": "Martyr/Role Model", "brand_essence": "Experiential wisdom"},
    "4/6": {"name": "Opportunist/Role Model", "brand_essence": "Network-based leadership"},
    "4/1": {"name": "Opportunist/Investigator", "brand_essence": "Networking meets research"},
    "5/1": {"name": "Heretic/Investigator", "brand_essence": "Practical solutions"},
    "5/2": {"name": "Heretic/Hermit", "brand_essence": "Universal problem-solver"},
    "6/2": {"name": "Role Model/Hermit", "brand_essence": "Wisdom through experience"},
    "6/3": {"name": "Role Model/Martyr", "brand_essence": "Authentic living example"}
}

# ============================================================================
# BRAND ARCHETYPES
# ============================================================================

BRAND_ARCHETYPES = {
    "Innocent": {
        "desire": "Safety and happiness",
        "colors": ["Soft pastels", "Light blues", "Gentle pinks", "Cream", "Pure white"],
        "fonts": "Friendly, rounded, approachable",
        "voice": "Optimistic, simple, honest, pure"
    },
    "Sage": {
        "desire": "Truth and knowledge",
        "colors": ["Deep blues", "Grays", "White", "Gold accents"],
        "fonts": "Classic serif, readable, authoritative",
        "voice": "Intelligent, analytical, thoughtful, guiding"
    },
    "Explorer": {
        "desire": "Freedom and discovery",
        "colors": ["Earth tones", "Forest green", "Rust", "Sky blue", "Warm neutrals"],
        "fonts": "Adventurous, bold, rugged",
        "voice": "Adventurous, authentic, brave, free"
    },
    "Outlaw": {
        "desire": "Revolution and change",
        "colors": ["Black", "Red", "Purple", "Dark metallics"],
        "fonts": "Bold, edgy, unconventional",
        "voice": "Rebellious, disruptive, provocative, raw"
    },
    "Magician": {
        "desire": "Transformation",
        "colors": ["Purple", "Deep blue", "Silver", "Mystical gradients"],
        "fonts": "Mystical, elegant, transformative",
        "voice": "Visionary, inspirational, transformative, magical"
    },
    "Hero": {
        "desire": "Mastery and courage",
        "colors": ["Bold red", "Strong blue", "Black", "Metallic gold"],
        "fonts": "Strong, bold, confident",
        "voice": "Courageous, inspiring, determined, triumphant"
    },
    "Lover": {
        "desire": "Intimacy and beauty",
        "colors": ["Deep red", "Rose", "Burgundy", "Gold", "Champagne"],
        "fonts": "Elegant, sensual, romantic",
        "voice": "Passionate, intimate, sensual, devoted"
    },
    "Jester": {
        "desire": "Joy and fun",
        "colors": ["Bright primary colors", "Rainbow", "Playful combinations"],
        "fonts": "Playful, fun, energetic",
        "voice": "Fun, playful, irreverent, joyful"
    },
    "Everyperson": {
        "desire": "Belonging and connection",
        "colors": ["Earthy tones", "Warm colors", "Accessible palette"],
        "fonts": "Friendly, approachable, comfortable",
        "voice": "Friendly, down-to-earth, reliable, genuine"
    },
    "Caregiver": {
        "desire": "Service and care",
        "colors": ["Soft blues", "Gentle greens", "Warm neutrals", "Comforting tones"],
        "fonts": "Warm, nurturing, soft",
        "voice": "Compassionate, nurturing, supportive, warm"
    },
    "Ruler": {
        "desire": "Control and order",
        "colors": ["Royal blue", "Purple", "Gold", "Black", "Rich tones"],
        "fonts": "Authoritative, elegant, refined",
        "voice": "Authoritative, confident, refined, prestigious"
    },
    "Creator": {
        "desire": "Innovation and expression",
        "colors": ["Bold combinations", "Artistic palettes", "Creative contrasts"],
        "fonts": "Unique, artistic, expressive",
        "voice": "Innovative, imaginative, artistic, original"
    }
}

# ============================================================================
# CALCULATION FUNCTIONS
# ============================================================================

def calculate_zodiac_sign(day: int, month: int) -> str:
    """Calculate zodiac sign from day and month"""
    dates = [
        (3, 21, "Aries"), (4, 20, "Taurus"), (5, 21, "Gemini"),
        (6, 21, "Cancer"), (7, 23, "Leo"), (8, 23, "Virgo"),
        (9, 23, "Libra"), (10, 23, "Scorpio"), (11, 22, "Sagittarius"),
        (12, 22, "Capricorn"), (1, 20, "Aquarius"), (2, 19, "Pisces")
    ]
    
    for i, (start_month, start_day, sign) in enumerate(dates):
        next_i = (i + 1) % 12
        end_month, end_day, _ = dates[next_i]
        
        if month == start_month and day >= start_day:
            return sign
        elif month == end_month and day < end_day:
            return sign
    
    return "Capricorn"  # Default

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
    if value < 9:
        return "Manifestor"
    elif value < 46:
        return "Generator"
    elif value < 79:
        return "Manifesting Generator"
    elif value < 99:
        return "Projector"
    else:
        return "Reflector"

def calculate_human_design_authority(hd_type: str, day: int) -> str:
    """Calculate Human Design authority based on type and birth data"""
    if hd_type == "Manifestor":
        return "Splenic" if day % 2 == 0 else "Emotional"
    elif hd_type in ["Generator", "Manifesting Generator"]:
        return "Sacral" if day % 3 == 0 else "Emotional"
    elif hd_type == "Projector":
        authorities = ["Splenic", "Ego", "Self-Projected", "Environmental", "Emotional"]
        return authorities[day % len(authorities)]
    else:  # Reflector
        return "Lunar"

def calculate_human_design_profile(day: int, month: int) -> str:
    """Calculate Human Design profile (simplified)"""
    profiles = ["1/3", "1/4", "2/4", "2/5", "3/5", "3/6", 
                "4/6", "4/1", "5/1", "5/2", "6/2", "6/3"]
    index = (day + month) % len(profiles)
    return profiles[index]

def determine_brand_archetype(sun_sign: str, moon_sign: str, rising_sign: str, 
                              hd_type: str) -> str:
    """Determine primary brand archetype"""
    
    # Mapping system (simplified but meaningful)
    archetype_mapping = {
        "Aries": "Hero",
        "Taurus": "Everyperson",
        "Gemini": "Jester",
        "Cancer": "Caregiver",
        "Leo": "Ruler",
        "Virgo": "Sage",
        "Libra": "Lover",
        "Scorpio": "Magician",
        "Sagittarius": "Explorer",
        "Capricorn": "Ruler",
        "Aquarius": "Creator",
        "Pisces": "Innocent"
    }
    
    hd_archetypes = {
        "Manifestor": "Outlaw",
        "Generator": "Everyperson",
        "Manifesting Generator": "Creator",
        "Projector": "Sage",
        "Reflector": "Magician"
    }
    
    # Weight sun sign most heavily
    primary = archetype_mapping.get(sun_sign, "Sage")
    
    # Consider HD type for modification
    if hd_type in hd_archetypes:
        hd_influence = hd_archetypes[hd_type]
        # If HD suggests different archetype, blend them
        if hd_influence != primary:
            # Return the HD-influenced archetype 30% of the time
            return hd_influence if hash(sun_sign + hd_type) % 10 < 3 else primary
    
    return primary

# ============================================================================
# COLOR PALETTE GENERATION
# ============================================================================

def generate_color_palette(archetype: str, sun_sign: str, moon_sign: str) -> dict:
    """Generate color palette based on archetype and astrology"""
    
    element_colors = {
        "Fire": {"base": "#FF5733", "accent": "#FFC300", "neutral": "#8B4513"},
        "Earth": {"base": "#8B7355", "accent": "#556B2F", "neutral": "#A0826D"},
        "Air": {"base": "#87CEEB", "accent": "#FFD700", "neutral": "#B0C4DE"},
        "Water": {"base": "#4682B4", "accent": "#20B2AA", "neutral": "#708090"}
    }
    
    archetype_colors = {
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
    
    base_palette = archetype_colors.get(archetype, archetype_colors["Sage"])
    
    return {
        "primary": {
            "name": "Primary Brand Color",
            "hex": base_palette["primary"],
            "rgb": hex_to_rgb(base_palette["primary"])
        },
        "secondary": {
            "name": "Secondary Color",
            "hex": base_palette["secondary"],
            "rgb": hex_to_rgb(base_palette["secondary"])
        },
        "accent": {
            "name": "Accent Color",
            "hex": base_palette["accent"],
            "rgb": hex_to_rgb(base_palette["accent"])
        },
        "neutrals": [
            {"name": "Dark Neutral", "hex": "#2C3E50", "rgb": "44, 62, 80"},
            {"name": "Medium Neutral", "hex": "#95A5A6", "rgb": "149, 165, 166"},
            {"name": "Light Neutral", "hex": "#ECF0F1", "rgb": "236, 240, 241"}
        ],
        "usage_guidelines": {
            "primary": "Main brand elements, headers, key CTAs",
            "secondary": "Supporting elements, subheadings, backgrounds",
            "accent": "Highlights, buttons, important details"
        }
    }

def hex_to_rgb(hex_color: str) -> str:
    """Convert hex color to RGB string"""
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return f"{r}, {g}, {b}"

# ============================================================================
# TYPOGRAPHY GENERATION
# ============================================================================

def generate_typography(archetype: str, sun_sign: str) -> dict:
    """Generate typography recommendations"""
    
    archetype_fonts = {
        "Innocent": {
            "heading": "Quicksand, Nunito, or Poppins",
            "body": "Open Sans or Lato",
            "style": "Friendly, rounded, approachable"
        },
        "Sage": {
            "heading": "Merriweather, Playfair Display, or Georgia",
            "body": "Source Sans Pro or Roboto",
            "style": "Classic, authoritative, readable"
        },
        "Explorer": {
            "heading": "Montserrat Bold or Bebas Neue",
            "body": "Raleway or Lato",
            "style": "Bold, adventurous, rugged"
        },
        "Outlaw": {
            "heading": "Oswald, Bebas Neue, or Impact",
            "body": "Roboto or Open Sans",
            "style": "Bold, edgy, rebellious"
        },
        "Magician": {
            "heading": "Cinzel, Philosopher, or Cormorant Garamond",
            "body": "Lora or Crimson Text",
            "style": "Mystical, elegant, transformative"
        },
        "Hero": {
            "heading": "Montserrat Black or Oswald",
            "body": "Open Sans or Roboto",
            "style": "Strong, confident, powerful"
        },
        "Lover": {
            "heading": "Playfair Display or Cormorant Garamond",
            "body": "Crimson Text or Lora",
            "style": "Elegant, romantic, sophisticated"
        },
        "Jester": {
            "heading": "Fredoka One or Baloo",
            "body": "Quicksand or Nunito",
            "style": "Playful, energetic, fun"
        },
        "Everyperson": {
            "heading": "Open Sans or Lato",
            "body": "Roboto or PT Sans",
            "style": "Friendly, accessible, comfortable"
        },
        "Caregiver": {
            "heading": "Nunito or Quicksand",
            "body": "Open Sans or Lato",
            "style": "Warm, soft, nurturing"
        },
        "Ruler": {
            "heading": "Playfair Display or Cinzel",
            "body": "Lora or Crimson Text",
            "style": "Refined, authoritative, elegant"
        },
        "Creator": {
            "heading": "Montserrat or Raleway",
            "body": "Open Sans or Lato",
            "style": "Modern, creative, versatile"
        }
    }
    
    fonts = archetype_fonts.get(archetype, archetype_fonts["Sage"])
    
    return {
        "heading_font": fonts["heading"],
        "body_font": fonts["body"],
        "style_description": fonts["style"],
        "sizes": {
            "h1": "48-60px",
            "h2": "36-42px",
            "h3": "24-30px",
            "body": "16-18px",
            "caption": "14px"
        },
        "spacing": {
            "line_height": "1.5-1.8",
            "letter_spacing": "Normal (0) for body, tight (-0.5px) for headings"
        }
    }

# ============================================================================
# LOGO & VISUAL GUIDELINES
# ============================================================================

def generate_logo_guidelines(archetype: str, sun_sign: str) -> dict:
    """Generate logo specifications"""
    
    logo_styles = {
        "Innocent": "Simple, clean wordmark or friendly icon",
        "Sage": "Classic emblem or sophisticated wordmark",
        "Explorer": "Bold mark with adventure symbolism",
        "Outlaw": "Edgy symbol or stark wordmark",
        "Magician": "Mystical symbol or transformative mark",
        "Hero": "Strong emblem or powerful symbol",
        "Lover": "Elegant script or romantic icon",
        "Jester": "Playful illustration or fun character",
        "Everyperson": "Friendly, approachable mark",
        "Caregiver": "Soft, nurturing symbol",
        "Ruler": "Regal emblem or refined mark",
        "Creator": "Unique, artistic expression"
    }
    
    return {
        "logo_style": logo_styles.get(archetype, "Clean, professional mark"),
        "primary_version": {
            "format": "Full color on white background",
            "font": "Primary heading font",
            "color": "Primary brand color"
        },
        "variations_needed": [
            "Full color",
            "Single color (black)",
            "Single color (white)",
            "Horizontal version",
            "Stacked version",
            "Icon only"
        ],
        "sizing_specifications": {
            "minimum_size": "24px height for digital, 0.5 inch for print",
            "clear_space": "Equal to height of logo on all sides",
            "file_formats": ["SVG", "PNG", "PDF"]
        }
    }

def generate_visual_style(archetype: str, element: str) -> dict:
    """Generate visual style guidelines"""
    
    visual_styles = {
        "Innocent": {
            "aesthetic": "Soft, light, optimistic, simple",
            "imagery": "Bright, happy, uplifting images",
            "principles": ["Simplicity", "Clarity", "Positivity", "Friendliness"]
        },
        "Sage": {
            "aesthetic": "Clean, authoritative, informative, trustworthy",
            "imagery": "Professional, educational, thoughtful",
            "principles": ["Clarity", "Authority", "Intelligence", "Trustworthiness"]
        },
        "Explorer": {
            "aesthetic": "Rugged, natural, adventurous, authentic",
            "imagery": "Nature, adventure, discovery, journeys",
            "principles": ["Authenticity", "Adventure", "Freedom", "Discovery"]
        },
        "Outlaw": {
            "aesthetic": "Bold, edgy, disruptive, unconventional",
            "imagery": "Urban, raw, rebellious, provocative",
            "principles": ["Disruption", "Authenticity", "Boldness", "Revolution"]
        },
        "Magician": {
            "aesthetic": "Mystical, transformative, visionary, enchanting",
            "imagery": "Transformative, magical, inspiring, cosmic",
            "principles": ["Transformation", "Vision", "Wonder", "Inspiration"]
        },
        "Hero": {
            "aesthetic": "Strong, confident, triumphant, powerful",
            "imagery": "Achievement, strength, victory, courage",
            "principles": ["Courage", "Excellence", "Achievement", "Strength"]
        },
        "Lover": {
            "aesthetic": "Elegant, sensual, intimate, beautiful",
            "imagery": "Beauty, romance, luxury, intimacy",
            "principles": ["Beauty", "Passion", "Intimacy", "Elegance"]
        },
        "Jester": {
            "aesthetic": "Fun, playful, energetic, joyful",
            "imagery": "Playful, humorous, colorful, lively",
            "principles": ["Fun", "Joy", "Energy", "Playfulness"]
        },
        "Everyperson": {
            "aesthetic": "Friendly, relatable, comfortable, genuine",
            "imagery": "Real people, everyday life, authenticity",
            "principles": ["Authenticity", "Connection", "Comfort", "Reliability"]
        },
        "Caregiver": {
            "aesthetic": "Warm, nurturing, supportive, gentle",
            "imagery": "Care, support, comfort, warmth",
            "principles": ["Compassion", "Support", "Warmth", "Care"]
        },
        "Ruler": {
            "aesthetic": "Refined, prestigious, authoritative, luxurious",
            "imagery": "Premium, sophisticated, powerful, prestigious",
            "principles": ["Excellence", "Authority", "Prestige", "Quality"]
        },
        "Creator": {
            "aesthetic": "Innovative, artistic, unique, expressive",
            "imagery": "Creative, original, artistic, imaginative",
            "principles": ["Innovation", "Creativity", "Originality", "Expression"]
        }
    }
    
    style = visual_styles.get(archetype, visual_styles["Sage"])
    
    return {
        "overall_aesthetic": style["aesthetic"],
        "imagery_style": style["imagery"],
        "design_principles": style["principles"],
        "photography_direction": {
            "style": f"Images should feel {style['aesthetic']}",
            "subjects": style["imagery"],
            "mood": style["aesthetic"].split(',')[0]
        },
        "graphic_elements": f"Use shapes and patterns that reinforce {style['aesthetic']} feeling"
    }

# ============================================================================
# BRAND VOICE
# ============================================================================

def generate_brand_voice(archetype: str, mercury_sign: str) -> dict:
    """Generate brand voice guidelines"""
    
    voice_profiles = {
        "Innocent": {
            "personality": "Optimistic, simple, honest, pure",
            "tone": "Friendly, encouraging, positive",
            "dos": ["Use simple language", "Be encouraging", "Focus on happiness"],
            "donts": ["Be cynical", "Use complex jargon", "Be negative"]
        },
        "Sage": {
            "personality": "Intelligent, analytical, thoughtful, guiding",
            "tone": "Authoritative, informative, thoughtful",
            "dos": ["Share knowledge", "Be clear and accurate", "Guide with wisdom"],
            "donts": ["Dumb down content", "Make unsubstantiated claims", "Be preachy"]
        },
        "Explorer": {
            "personality": "Adventurous, authentic, brave, free",
            "tone": "Bold, inspiring, authentic",
            "dos": ["Inspire adventure", "Be authentic", "Encourage discovery"],
            "donts": ["Be boring", "Focus on safety", "Be conventional"]
        },
        "Outlaw": {
            "personality": "Rebellious, disruptive, provocative, raw",
            "tone": "Bold, direct, challenging",
            "dos": ["Challenge norms", "Be provocative", "Speak truth"],
            "donts": ["Play it safe", "Follow trends", "Be corporate"]
        },
        "Magician": {
            "personality": "Visionary, inspirational, transformative, magical",
            "tone": "Inspiring, mystical, transformative",
            "dos": ["Inspire transformation", "Create wonder", "Be visionary"],
            "donts": ["Be mundane", "Focus on limitations", "Be skeptical"]
        },
        "Hero": {
            "personality": "Courageous, inspiring, determined, triumphant",
            "tone": "Motivating, confident, strong",
            "dos": ["Inspire courage", "Celebrate achievement", "Be empowering"],
            "donts": ["Be defeatist", "Focus on weakness", "Be passive"]
        },
        "Lover": {
            "personality": "Passionate, intimate, sensual, devoted",
            "tone": "Warm, intimate, elegant",
            "dos": ["Create intimacy", "Be sensual", "Celebrate beauty"],
            "donts": ["Be cold", "Be utilitarian", "Be impersonal"]
        },
        "Jester": {
            "personality": "Fun, playful, irreverent, joyful",
            "tone": "Playful, humorous, lighthearted",
            "dos": ["Have fun", "Use humor", "Be spontaneous"],
            "donts": ["Be serious", "Be boring", "Be corporate"]
        },
        "Everyperson": {
            "personality": "Friendly, down-to-earth, reliable, genuine",
            "tone": "Conversational, warm, authentic",
            "dos": ["Be relatable", "Keep it real", "Build connection"],
            "donts": ["Be pretentious", "Use jargon", "Be distant"]
        },
        "Caregiver": {
            "personality": "Compassionate, nurturing, supportive, warm",
            "tone": "Caring, gentle, supportive",
            "dos": ["Show empathy", "Offer support", "Be warm"],
            "donts": ["Be cold", "Be critical", "Be dismissive"]
        },
        "Ruler": {
            "personality": "Authoritative, confident, refined, prestigious",
            "tone": "Sophisticated, authoritative, refined",
            "dos": ["Demonstrate expertise", "Be confident", "Maintain quality"],
            "donts": ["Be casual", "Lower standards", "Be apologetic"]
        },
        "Creator": {
            "personality": "Innovative, imaginative, artistic, original",
            "tone": "Creative, inspiring, original",
            "dos": ["Be innovative", "Inspire creativity", "Be authentic"],
            "donts": ["Be conventional", "Copy others", "Be formulaic"]
        }
    }
    
    voice = voice_profiles.get(archetype, voice_profiles["Sage"])
    
    return {
        "personality": voice["personality"],
        "tone": voice["tone"],
        "dos": voice["dos"],
        "donts": voice["donts"]
    }

# ============================================================================
# MAIN BRAND GUIDELINES GENERATION
# ============================================================================

def format_brand_guidelines(birth_data: dict, astrology: dict, human_design: dict,
                           archetype: str, colors: dict, typography: dict,
                           logo: dict, visual: dict, voice: dict) -> str:
    """Format complete brand guidelines in Canva style"""
    
    guidelines = f"""# BRAND IDENTITY GUIDELINES

**Generated for:** {birth_data['date']} at {birth_data['time']} in {birth_data['location']}

---

## Core Brand Identity

**Primary Archetype:** {archetype}
**Astrological Foundation:** {astrology['sun_sign']} Sun • {astrology['moon_sign']} Moon • {astrology['rising_sign']} Rising
**Human Design:** {human_design['type']} • {human_design['authority']} Authority • {human_design['profile']} Profile

{BRAND_ARCHETYPES[archetype]['desire']} is at the heart of this brand. 
This core identity shapes every visual and verbal element of your brand presence.

---

## Color Palette

**Primary Brand Color**
{colors['primary']['name']} • {colors['primary']['hex']} • RGB {colors['primary']['rgb']}
Use for: {colors['usage_guidelines']['primary']}

**Secondary Color**
{colors['secondary']['name']} • {colors['secondary']['hex']} • RGB {colors['secondary']['rgb']}
Use for: {colors['usage_guidelines']['secondary']}

**Accent Color**
{colors['accent']['name']} • {colors['accent']['hex']} • RGB {colors['accent']['rgb']}
Use for: {colors['usage_guidelines']['accent']}

**Neutral Colors**
"""
    
    for neutral in colors['neutrals']:
        guidelines += f"{neutral['name']} • {neutral['hex']} • RGB {neutral['rgb']}\n"
    
    guidelines += f"""
---

## Typography

**Heading Font:** {typography['heading_font']}
Use for: Main headlines, section headers, hero text
Sizes: H1 {typography['sizes']['h1']}, H2 {typography['sizes']['h2']}, H3 {typography['sizes']['h3']}

**Body Font:** {typography['body_font']}
Use for: Paragraphs, descriptions, general content
Sizes: Body {typography['sizes']['body']}, Caption {typography['sizes']['caption']}

**Font Style:** {typography['style_description']}
Line height: {typography['spacing']['line_height']}
Letter spacing: {typography['spacing']['letter_spacing']}

---

## Logo Guidelines

**Style:** {logo['logo_style']}

**Primary Logo**
Font: {logo['primary_version']['font']}
Color: {logo['primary_version']['color']}
Format: {logo['primary_version']['format']}

**Required Variations**
"""
    
    for variation in logo['variations_needed']:
        guidelines += f"• {variation}\n"
    
    guidelines += f"""
**Sizing & Spacing**
Minimum size: {logo['sizing_specifications']['minimum_size']}
Clear space: {logo['sizing_specifications']['clear_space']}
Formats: {', '.join(logo['sizing_specifications']['file_formats'])}

---

## Visual Style

**Overall Aesthetic:** {visual['overall_aesthetic']}

**Imagery Style:** {visual['imagery_style']}

**Design Principles:**
"""
    
    for principle in visual['design_principles']:
        guidelines += f"• {principle}\n"
    
    guidelines += f"""
**Photography Direction**
Style: {visual['photography_direction']['style']}
Subjects: {visual['photography_direction']['subjects']}
Mood: {visual['photography_direction']['mood']}

**Graphic Elements**
{visual['graphic_elements']}

---

## Brand Voice

**Personality:** {voice['personality']}
**Tone:** {voice['tone']}

**Do's:**
"""
    
    for do in voice['dos']:
        guidelines += f"• {do}\n"
    
    guidelines += "\n**Don'ts:**\n"
    
    for dont in voice['donts']:
        guidelines += f"• {dont}\n"
    
    guidelines += f"""
---

## Quick Reference

**One-Line Brand Essence:** {archetype} brand with {astrology['sun_sign']} energy, {human_design['type']} approach

**Color Snapshot:** {colors['primary']['hex']} • {colors['secondary']['hex']} • {colors['accent']['hex']}

**Font Pairing:** {typography['heading_font']} + {typography['body_font']}

**Visual Mood:** {visual['overall_aesthetic']}

**Voice:** {voice['personality']}

---

*These guidelines provide a complete foundation for your brand identity. Use them to maintain consistency across all brand touchpoints, from website to social media to print materials.*
"""
    
    return guidelines

# ============================================================================
# MCP TOOLS
# ============================================================================

if FastMCP:
    @mcp.tool()
    def generate_brand_identity(
        birth_date: str,
        birth_time: str,
        birth_location: str,
        business_name: Optional[str] = None
    ) -> str:
        """
        Generate complete brand identity guidelines based on birth data.
        
        Args:
            birth_date: Birth date in YYYY-MM-DD format
            birth_time: Birth time in HH:MM format (24-hour)
            birth_location: Birth location (city, country)
            business_name: Optional business name for personalization
            
        Returns:
            Complete Canva-style brand guidelines
        """
        
        # Validate inputs
        validation = validate_birth_data(birth_date, birth_time, birth_location)
        if not validation["valid"]:
            return json.dumps({"error": "Validation failed", "details": validation["errors"]}, indent=2)
        
        # Parse birth data
        date_obj = datetime.strptime(birth_date, "%Y-%m-%d")
        time_obj = datetime.strptime(birth_time, "%H:%M")
        
        day = date_obj.day
        month = date_obj.month
        year = date_obj.year
        hour = time_obj.hour
        minute = time_obj.minute
        
        # Calculate astrology
        sun_sign = calculate_zodiac_sign(day, month)
        moon_sign = calculate_moon_sign(day, month, year)
        rising_sign = calculate_rising_sign(hour, minute)
        
        astrology = {
            "sun_sign": sun_sign,
            "moon_sign": moon_sign,
            "rising_sign": rising_sign,
            "sun_element": ZODIAC_SIGNS[sun_sign]["element"]
        }
        
        # Calculate Human Design
        hd_type = calculate_human_design_type(day, month, hour)
        hd_authority = calculate_human_design_authority(hd_type, day)
        hd_profile = calculate_human_design_profile(day, month)
        
        human_design = {
            "type": hd_type,
            "authority": hd_authority,
            "profile": hd_profile
        }
        
        # Determine brand archetype
        archetype = determine_brand_archetype(sun_sign, moon_sign, rising_sign, hd_type)
        
        # Generate all brand elements
        colors = generate_color_palette(archetype, sun_sign, moon_sign)
        typography = generate_typography(archetype, sun_sign)
        logo = generate_logo_guidelines(archetype, sun_sign)
        visual = generate_visual_style(archetype, astrology["sun_element"])
        voice = generate_brand_voice(archetype, sun_sign)
        
        # Format guidelines
        birth_data = {
            "date": birth_date,
            "time": birth_time,
            "location": birth_location
        }
        
        guidelines = format_brand_guidelines(
            birth_data, astrology, human_design, archetype,
            colors, typography, logo, visual, voice
        )
        
        return guidelines

    @mcp.tool()
    def get_color_palette_only(
        birth_date: str,
        birth_time: str,
        birth_location: str
    ) -> str:
        """
        Generate only the color palette based on birth data.
        
        Args:
            birth_date: Birth date in YYYY-MM-DD format
            birth_time: Birth time in HH:MM format (24-hour)
            birth_location: Birth location (city, country)
            
        Returns:
            Color palette with hex codes and usage guidelines
        """
        
        validation = validate_birth_data(birth_date, birth_time, birth_location)
        if not validation["valid"]:
            return json.dumps({"error": "Validation failed", "details": validation["errors"]}, indent=2)
        
        date_obj = datetime.strptime(birth_date, "%Y-%m-%d")
        day, month, year = date_obj.day, date_obj.month, date_obj.year
        
        sun_sign = calculate_zodiac_sign(day, month)
        moon_sign = calculate_moon_sign(day, month, year)
        
        time_obj = datetime.strptime(birth_time, "%H:%M")
        hour = time_obj.hour
        
        hd_type = calculate_human_design_type(day, month, hour)
        rising_sign = calculate_rising_sign(hour, time_obj.minute)
        
        archetype = determine_brand_archetype(sun_sign, moon_sign, rising_sign, hd_type)
        colors = generate_color_palette(archetype, sun_sign, moon_sign)
        
        return json.dumps(colors, indent=2)

    @mcp.tool()
    def get_typography_only(
        birth_date: str,
        birth_time: str,
        birth_location: str
    ) -> str:
        """
        Generate only typography recommendations based on birth data.
        
        Args:
            birth_date: Birth date in YYYY-MM-DD format
            birth_time: Birth time in HH:MM format (24-hour)
            birth_location: Birth location (city, country)
            
        Returns:
            Typography recommendations with fonts and sizing
        """
        
        validation = validate_birth_data(birth_date, birth_time, birth_location)
        if not validation["valid"]:
            return json.dumps({"error": "Validation failed", "details": validation["errors"]}, indent=2)
        
        date_obj = datetime.strptime(birth_date, "%Y-%m-%d")
        day, month, year = date_obj.day, date_obj.month, date_obj.year
        
        sun_sign = calculate_zodiac_sign(day, month)
        moon_sign = calculate_moon_sign(day, month, year)
        
        time_obj = datetime.strptime(birth_time, "%H:%M")
        hour = time_obj.hour
        
        hd_type = calculate_human_design_type(day, month, hour)
        rising_sign = calculate_rising_sign(hour, time_obj.minute)
        
        archetype = determine_brand_archetype(sun_sign, moon_sign, rising_sign, hd_type)
        typography = generate_typography(archetype, sun_sign)
        
        return json.dumps(typography, indent=2)

    @mcp.tool()
    def calculate_birth_chart(
        birth_date: str,
        birth_time: str,
        birth_location: str
    ) -> str:
        """
        Calculate astrological birth chart (Sun, Moon, Rising signs).
        
        Args:
            birth_date: Birth date in YYYY-MM-DD format
            birth_time: Birth time in HH:MM format (24-hour)
            birth_location: Birth location (city, country)
            
        Returns:
            Birth chart with Sun, Moon, and Rising signs
        """
        
        validation = validate_birth_data(birth_date, birth_time, birth_location)
        if not validation["valid"]:
            return json.dumps({"error": "Validation failed", "details": validation["errors"]}, indent=2)
        
        date_obj = datetime.strptime(birth_date, "%Y-%m-%d")
        time_obj = datetime.strptime(birth_time, "%H:%M")
        
        day, month, year = date_obj.day, date_obj.month, date_obj.year
        hour, minute = time_obj.hour, time_obj.minute
        
        sun_sign = calculate_zodiac_sign(day, month)
        moon_sign = calculate_moon_sign(day, month, year)
        rising_sign = calculate_rising_sign(hour, minute)
        
        chart = {
            "sun_sign": sun_sign,
            "sun_traits": ZODIAC_SIGNS[sun_sign],
            "moon_sign": moon_sign,
            "moon_traits": ZODIAC_SIGNS[moon_sign],
            "rising_sign": rising_sign,
            "rising_traits": ZODIAC_SIGNS[rising_sign]
        }
        
        return json.dumps(chart, indent=2)

    @mcp.tool()
    def calculate_human_design(
        birth_date: str,
        birth_time: str,
        birth_location: str
    ) -> str:
        """
        Calculate Human Design chart (Type, Authority, Profile).
        
        Args:
            birth_date: Birth date in YYYY-MM-DD format
            birth_time: Birth time in HH:MM format (24-hour)
            birth_location: Birth location (city, country)
            
        Returns:
            Human Design chart with Type, Authority, and Profile
        """
        
        validation = validate_birth_data(birth_date, birth_time, birth_location)
        if not validation["valid"]:
            return json.dumps({"error": "Validation failed", "details": validation["errors"]}, indent=2)
        
        date_obj = datetime.strptime(birth_date, "%Y-%m-%d")
        time_obj = datetime.strptime(birth_time, "%H:%M")
        
        day, month = date_obj.day, date_obj.month
        hour = time_obj.hour
        
        hd_type = calculate_human_design_type(day, month, hour)
        hd_authority = calculate_human_design_authority(hd_type, day)
        hd_profile = calculate_human_design_profile(day, month)
        
        chart = {
            "type": hd_type,
            "type_details": HUMAN_DESIGN_TYPES[hd_type],
            "authority": hd_authority,
            "authority_description": HUMAN_DESIGN_AUTHORITIES[hd_authority],
            "profile": hd_profile,
            "profile_details": HUMAN_DESIGN_PROFILES[hd_profile]
        }
        
        return json.dumps(chart, indent=2)

# ============================================================================
# MAIN - Auto-run for FastMCP Cloud
# ============================================================================

# For FastMCP Cloud deployment, the server needs to run automatically
if FastMCP:
    # This will be called by FastMCP Cloud when the module is imported
    pass
else:
    print("Warning: FastMCP not available. Install with: pip install fastmcp")

# If running locally as a script
if __name__ == "__main__":
    if FastMCP:
        mcp.run()
    else:
        print("For testing, you can import and use the functions directly.")
