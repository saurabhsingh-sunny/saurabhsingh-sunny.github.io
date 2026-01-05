# Icon Options for Tech Stack Cube

## Option 1: Use Devicon CDN (Recommended - Easy)

Add this to the `<head>` section of your Quarto site (in `_quarto.yml` or directly in HTML):

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css">
```

Then use in your cube like this:
```html
<div class="icon">
  <i class="devicon-python-plain colored"></i>
</div>
<div class="icon">
  <i class="devicon-tableau-plain colored"></i>
</div>
<div class="icon">
  <i class="devicon-azuresqldatabase-plain colored"></i>
</div>
<div class="icon">
  <i class="devicon-github-original"></i>
</div>
```

Browse available icons at: https://devicon.dev/

---

## Option 2: Download and Use Local SVG Images

### Step 1: Download Official Logos

Download SVG files from these sources:
- **Python**: https://www.python.org/community/logos/
- **Tableau**: https://www.tableau.com/about/media-kit
- **SQL/Database**: https://simpleicons.org/ (search for PostgreSQL, MySQL, etc.)
- **GitHub**: https://github.com/logos

### Step 2: Save to Images Folder

Save downloaded SVGs to: `/images/icons/`
- python.svg
- tableau.svg
- database.svg
- github.svg

### Step 3: Reference in index.qmd

```html
<div class="icon">
  <img src="images/icons/python.svg" alt="Python">
</div>
<div class="icon">
  <img src="images/icons/tableau.svg" alt="Tableau">
</div>
<div class="icon">
  <img src="images/icons/database.svg" alt="SQL">
</div>
<div class="icon">
  <img src="images/icons/github.svg" alt="GitHub">
</div>
```

---

## Option 3: Use Simple Icons CDN

Add unpkg CDN for Simple Icons:

```html
<!-- In your HTML -->
<div class="icon">
  <img src="https://cdn.simpleicons.org/python/3776AB" alt="Python">
</div>
<div class="icon">
  <img src="https://cdn.simpleicons.org/tableau/E97627" alt="Tableau">
</div>
<div class="icon">
  <img src="https://cdn.simpleicons.org/mysql/4479A1" alt="SQL">
</div>
<div class="icon">
  <img src="https://cdn.simpleicons.org/github/FFFFFF" alt="GitHub">
</div>
```

Note: The hex color at the end sets the icon color.

---

## Recommended Approach

**Use Devicon (Option 1)** for the easiest implementation with official, colored icons that are already optimized for web use.
