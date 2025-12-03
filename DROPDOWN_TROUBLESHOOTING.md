# Year Filter Dropdown - Troubleshooting

## The dropdown IS in the code!

I've verified that the year filter dropdown has been successfully added to the HTML at line 215-217 of `templates/analytics.html`.

## Why you can't see it:

The issue is **browser caching**. Your browser is showing you the old version of the page.

## How to fix it:

### Option 1: Hard Refresh (RECOMMENDED)
1. Go to the Analytics page
2. Press **Ctrl + Shift + R** (Windows) or **Cmd + Shift + R** (Mac)
3. This forces the browser to reload everything from the server

### Option 2: Clear Browser Cache
1. Press **Ctrl + Shift + Delete**
2. Select "Cached images and files"
3. Click "Clear data"
4. Refresh the page

### Option 3: Open in Incognito/Private Window
1. Press **Ctrl + Shift + N** (Chrome) or **Ctrl + Shift + P** (Firefox)
2. Navigate to http://127.0.0.1:5000/analytics
3. Login and check

## What you should see:

```
Monthly Statistics                    [All Years ▼]
```

The dropdown will be on the right side of "Monthly Statistics" with:
- Width: 150-200px
- Font size: 0.875rem (smaller than normal)
- Options: "All Years", then any years found in your data

## If it's STILL not visible after hard refresh:

1. Open browser Developer Tools (F12)
2. Go to the "Elements" or "Inspector" tab
3. Press Ctrl+F to search
4. Search for: `id="yearFilter"`
5. If you find it, the dropdown is there but might have CSS issues
6. Check the "Styles" panel to see if it's being hidden

## The dropdown HTML code:

```html
<select id="yearFilter" class="form-select" style="width: auto; min-width: 150px; max-width: 200px; font-size: 0.875rem;">
    <option value="all">All Years</option>
</select>
```

---

**TRY: Ctrl + Shift + R first!** This solves 99% of caching issues.
