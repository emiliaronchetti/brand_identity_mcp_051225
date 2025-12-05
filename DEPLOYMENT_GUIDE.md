# Deployment Guide

Step-by-step instructions for deploying the Brand Identity Discovery MCP Server.

---

## 📦 GitHub Deployment

### 1. Create GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the "+" icon in the top right
3. Select "New repository"
4. Repository settings:
   - **Name**: `brand-identity-mcp` (or your preferred name)
   - **Description**: "MCP server for generating personalized brand identity guidelines"
   - **Visibility**: Public or Private (your choice)
   - **Initialize**: Leave unchecked (we have files already)
5. Click "Create repository"

### 2. Upload Files to GitHub

#### Option A: Using GitHub Web Interface

1. On your new repository page, click "uploading an existing file"
2. Drag and drop these files:
   - `brand_identity_mcp_server.py`
   - `README.md`
   - `requirements.txt`
   - `LICENSE`
   - `.gitignore`
   - `EXAMPLE_OUTPUT.md`
3. Add commit message: "Initial commit - Brand Identity Discovery MCP Server"
4. Click "Commit changes"

#### Option B: Using Git Command Line

```bash
# Navigate to where you saved the files
cd /path/to/your/files

# Initialize git repository
git init

# Add all files
git add .

# Commit files
git commit -m "Initial commit - Brand Identity Discovery MCP Server"

# Add remote repository (replace YOUR_USERNAME and REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/brand-identity-mcp.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### 3. Verify Deployment

1. Go to your repository URL: `https://github.com/YOUR_USERNAME/brand-identity-mcp`
2. Verify all files are present
3. Check that README.md displays properly on the main page

---

## ☁️ FastMCP Cloud Deployment

### 1. Access FastMCP Cloud

1. Go to [FastMCP Cloud](https://fastmcp.com) (or your MCP cloud provider)
2. Sign in or create an account

### 2. Create New MCP Server

1. Click "New Server" or "Create Server"
2. Server settings:
   - **Name**: `brand-identity-discovery`
   - **Description**: "Personalized brand identity guidelines generator"
   - **Runtime**: Python 3.9+

### 3. Upload Server File

1. Upload `brand_identity_mcp_server.py`
2. Upload `requirements.txt` (if supported)
3. Or paste the file contents directly into the code editor

### 4. Configure Dependencies

In the dependencies or requirements section, add:
```
fastmcp>=0.1.0
```

### 5. Deploy Server

1. Click "Deploy" or "Activate"
2. Wait for deployment to complete (usually 30-60 seconds)
3. Copy your server endpoint URL

### 6. Test Deployment

Use the testing interface or API to call:
```python
generate_brand_identity(
    birth_date="1987-10-28",
    birth_time="14:30",
    birth_location="Buenos Aires, Argentina"
)
```

Expected response: Complete brand guidelines in Canva style

---

## 🧪 Testing Your Deployment

### Local Testing

```bash
# Install dependencies
pip install fastmcp

# Run server
python brand_identity_mcp_server.py

# Server should start on default MCP port
# Use MCP client to connect and test tools
```

### Test Cases

#### Test 1: Complete Brand Identity
```python
Input:
  birth_date: "1990-05-15"
  birth_time: "09:30"
  birth_location: "New York, USA"

Expected: Full brand guidelines with all sections
```

#### Test 2: Color Palette Only
```python
Input:
  birth_date: "1985-12-03"
  birth_time: "18:45"
  birth_location: "London, UK"

Expected: JSON with color palette
```

#### Test 3: Birth Chart
```python
Input:
  birth_date: "1992-08-22"
  birth_time: "06:15"
  birth_location: "Tokyo, Japan"

Expected: Sun, Moon, Rising signs
```

#### Test 4: Invalid Input
```python
Input:
  birth_date: "2030-01-01"  # Future date
  birth_time: "14:30"
  birth_location: "Paris, France"

Expected: Validation error with helpful message
```

### Validation Checks

- ✅ Server starts without errors
- ✅ All 5 tools are accessible
- ✅ Valid inputs generate complete output
- ✅ Invalid inputs return clear error messages
- ✅ Output format matches Canva-style guidelines
- ✅ Color hex codes are properly formatted
- ✅ Typography recommendations are complete
- ✅ Brand voice guidelines are present

---

## 🔧 Troubleshooting

### Issue: "FastMCP not found"

**Solution**: Install FastMCP
```bash
pip install fastmcp
```

### Issue: "Invalid date format"

**Solution**: Ensure date is in YYYY-MM-DD format
- ✅ Correct: "1987-10-28"
- ❌ Wrong: "28-10-1987", "10/28/1987"

### Issue: "Server won't start"

**Solution**: Check Python version
```bash
python --version  # Should be 3.8 or higher
```

### Issue: "Missing dependencies"

**Solution**: Install from requirements.txt
```bash
pip install -r requirements.txt
```

---

## 📊 Monitoring

### GitHub
- Watch repository stars/forks
- Monitor issues and pull requests
- Check traffic analytics

### FastMCP Cloud
- Monitor API calls
- Check error rates
- Review response times
- Monitor usage limits

---

## 🚀 Next Steps

After successful deployment:

1. **Test thoroughly**: Run all test cases
2. **Share repository**: Share GitHub URL with collaborators
3. **Document usage**: Add examples to README if needed
4. **Monitor performance**: Watch for errors or issues
5. **Iterate**: Gather feedback and improve

---

## 📝 Deployment Checklist

### Pre-Deployment
- [ ] All files downloaded
- [ ] README.md reviewed
- [ ] Example output verified
- [ ] Dependencies confirmed

### GitHub Deployment
- [ ] Repository created
- [ ] All files uploaded
- [ ] README displays correctly
- [ ] Repository URL saved

### FastMCP Cloud Deployment
- [ ] Account created
- [ ] Server configured
- [ ] File uploaded
- [ ] Dependencies set
- [ ] Server deployed
- [ ] Endpoint URL saved

### Testing
- [ ] Local testing completed
- [ ] All tools tested
- [ ] Validation tested
- [ ] Output format verified
- [ ] Error handling confirmed

### Documentation
- [ ] README updated (if needed)
- [ ] Deployment guide reviewed
- [ ] Example output added
- [ ] Usage instructions clear

---

## 🎉 Success!

Your Brand Identity Discovery MCP Server is now deployed and ready to generate personalized brand guidelines!

**GitHub Repository**: `https://github.com/YOUR_USERNAME/brand-identity-mcp`
**FastMCP Cloud**: `https://fastmcp.com/YOUR_USERNAME/brand-identity-discovery`

Share your amazing work! 🌟
