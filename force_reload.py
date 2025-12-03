"""
Add a cache-busting comment to force browser reload
"""
import time

with open('templates/analytics.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add a timestamp comment at the top of the file to force reload
timestamp = f"<!-- Cache buster: {int(time.time())} -->\n"

if "<!-- Cache buster:" not in content:
    # Add after <!DOCTYPE html>
    content = content.replace('<!DOCTYPE html>', f'<!DOCTYPE html>\n{timestamp}', 1)
    print(f"✓ Added cache buster timestamp")
else:
    # Update existing timestamp
    import re
    content = re.sub(r'<!-- Cache buster: \d+ -->', f'<!-- Cache buster: {int(time.time())} -->', content)
    print(f"✓ Updated cache buster timestamp")

with open('templates/analytics.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ File updated. The browser should now reload the new version.")
print("\nPlease:")
print("1. Close ALL browser tabs with the analytics page")
print("2. Open a NEW tab")
print("3. Go to http://127.0.0.1:5000/analytics")
