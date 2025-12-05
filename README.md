# Brand Identity Discovery MCP Server

A Model Context Protocol (MCP) server that generates personalized brand identity guidelines by combining astrology, Human Design, and brand strategy frameworks.

## Overview

This MCP server takes birth data (date, time, location) and generates comprehensive brand guidelines in a clean, Canva-style format. The output includes:

- **Color Palette** - Primary, secondary, accent colors with hex codes
- **Typography** - Heading and body font recommendations
- **Logo Guidelines** - Style specifications and requirements
- **Visual Style** - Photography direction and design principles
- **Brand Voice** - Personality, tone, and messaging guidelines

## Features

- 🎨 **Astrological Foundation** - Sun, Moon, and Rising sign calculations
- 🔮 **Human Design Integration** - Type, Authority, and Profile mapping
- 🎯 **Brand Archetype System** - 12 core archetypes (Hero, Sage, Creator, etc.)
- 🌈 **Color Psychology** - Element and archetype-based palette generation
- ✍️ **Typography Matching** - Font recommendations aligned with brand personality
- 📋 **Clean Output Format** - ~500 word brand guidelines ready for designers

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Install via pip

```bash
pip install mcp
```

Or install from source:

```bash
git clone https://github.com/YOUR_USERNAME/brand-identity-mcp.git
cd brand-identity-mcp
pip install -r requirements.txt
```

## Usage

### As MCP Server

Add to your MCP client configuration (e.g., Claude Desktop):

```json
{
  "mcpServers": {
    "brand-identity": {
      "command": "python",
      "args": ["/path/to/brand_identity_mcp_server.py"]
    }
  }
}
```

### Available Tools

#### 1. `generate_brand_identity`

Generate complete brand identity guidelines.

**Parameters:**
- `birth_date` (string, required): Birth date in YYYY-MM-DD format
- `birth_time` (string, required): Birth time in HH:MM format (24-hour)
- `birth_location` (string, required): Birth location (city, country)
- `business_name` (string, optional): Business name for personalization

**Example:**
```python
generate_brand_identity(
    birth_date="1987-10-28",
    birth_time="14:30",
    birth_location="Buenos Aires, Argentina"
)
```

#### 2. `get_color_palette_only`

Generate only the color palette.

#### 3. `get_typography_only`

Generate only typography recommendations.

#### 4. `calculate_birth_chart`

Calculate astrological birth chart only.

#### 5. `calculate_human_design`

Calculate Human Design chart only.

## Example Output

```markdown
# BRAND IDENTITY GUIDELINES

## Core Brand Identity

**Primary Archetype:** Magician
**Astrological Foundation:** Scorpio Sun • Cancer Moon • Virgo Rising
**Human Design:** Projector • Emotional Authority • 5/1 Profile

Transformation is at the heart of this brand.

## Color Palette

**Primary Brand Color**
Primary Brand Color • #4B0082 • RGB 75, 0, 130
Use for: Main brand elements, headers, key CTAs

[... continues with full guidelines ...]
```

## How It Works

### 1. Astrological Calculation
- Calculates Sun, Moon, and Rising signs from birth data
- Maps zodiac signs to elemental energies (Fire, Earth, Air, Water)

### 2. Human Design Analysis
- Determines Type, Authority, and Profile

### 3. Brand Archetype Mapping
- Synthesizes astrology + Human Design into brand archetypes

### 4. Visual Identity Generation
- Colors, typography, logo specs, imagery direction

### 5. Brand Voice Development
- Personality, tone, messaging guidelines

## License

MIT License

## Contact

For questions or suggestions, please open an issue on GitHub.

---

**Built with ❤️ for brand creators seeking alignment between identity and expression.**
