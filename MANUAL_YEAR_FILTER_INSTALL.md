# Year Filter Dropdown - Manual Installation Guide

I apologize for the technical difficulties with automated editing. The file keeps getting corrupted when I try to modify it programmatically.

## Simple Manual Solution

Here's how to add the year filter dropdown yourself in **2 simple steps**:

### Step 1: Add the Script Tag

1. Open `templates/analytics.html` in your text editor
2. Scroll to the very bottom of the file (around line 757-760)
3. Find this line:
   ```html
   </script>
</body>
   ```

4. Change it to:
   ```html
   </script>
   <script src="/static/js/year-filter.js"></script>
</body>
   ```

That's it! Just add ONE line: `<script src="/static/js/year-filter.js"></script>`

### Step 2: Refresh Your Browser

1. Save the file
2. Go to http://127.0.0.1:5000/analytics
3. Press `Ctrl + Shift + R` to hard refresh

### What This Does

The `year-filter.js` file I created will:
- Automatically find the "Monthly Statistics" section
- Inject a dropdown on the right side
- Populate it with years from your data
- Add filtering functionality

### The JavaScript File

I've already created `static/js/year-filter.js` with all the necessary code. It will:
1. Wait for the page to load
2. Find the Monthly Statistics card
3. Add a dropdown next to the title
4. Auto-populate with available years
5. Filter the table when you select a year

### If You Prefer, Here's the Exact Location

In `templates/analytics.html`, look for line 757-758:
```html
    </script>
</body>
```

Add the script tag between them:
```html
    </script>
    <script src="/static/js/year-filter.js"></script>
</body>
```

That's literally all you need to do!

---

## Alternative: I Can Create a Patch File

If you'd prefer, I can create a `.patch` file that you can apply with `git apply`, which might be more reliable than manual editing.

Let me know if you'd like me to create that instead!
