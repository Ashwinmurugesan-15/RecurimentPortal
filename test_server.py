from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route('/test-analytics')
def test_analytics():
    # Read the analytics.html file directly
    with open('templates/analytics.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if filters are in the content
    has_year_filter = 'id="yearFilter"' in content
    has_position_filter = 'id="positionFilter"' in content
    
    # Get file modification time
    mtime = os.path.getmtime('templates/analytics.html')
    
    return f"""
    <html>
    <head><title>Analytics File Test</title></head>
    <body style="font-family: Arial; padding: 20px;">
        <h1>Analytics.html File Status</h1>
        <p><strong>File path:</strong> templates/analytics.html</p>
        <p><strong>File size:</strong> {len(content)} bytes</p>
        <p><strong>Last modified:</strong> {mtime}</p>
        <p><strong>Year filter present:</strong> <span style="color: {'green' if has_year_filter else 'red'}; font-weight: bold;">{'YES ✓' if has_year_filter else 'NO ✗'}</span></p>
        <p><strong>Position filter present:</strong> <span style="color: {'green' if has_position_filter else 'red'}; font-weight: bold;">{'YES ✓' if has_position_filter else 'NO ✗'}</span></p>
        
        <hr>
        <h2>Filter HTML Preview:</h2>
        <pre style="background: #f5f5f5; padding: 10px; overflow-x: auto;">
{content[content.find('id="yearFilter"')-200:content.find('id="yearFilter"')+500] if has_year_filter else 'NOT FOUND'}
        </pre>
        
        <hr>
        <p><a href="/analytics">Go to actual Analytics page</a></p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, port=5001)
