"""
Script to add Year and Position filters to the Monthly Statistics section
"""

# Read the current analytics.html file
with open('templates/analytics.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the Monthly Statistics header section and add filters
old_header = '''                <div class="d-flex justify-content-between align-items-center mb-2">
                    <h5 class="card-title mb-0" style="font-size: 1rem;">Monthly Statistics</h5>
                </div>'''

new_header = '''                <div class="d-flex justify-content-between align-items-center mb-2">
                    <h5 class="card-title mb-0" style="font-size: 1rem;">Monthly Statistics</h5>
                    <div class="d-flex align-items-center gap-2">
                        <label for="yearFilter" class="mb-0" style="font-size: 0.875rem; font-weight: 500;">Year:</label>
                        <select id="yearFilter" class="form-select form-select-sm" style="width: auto;">
                            <option value="" selected>All Time</option>
                            <option value="2024">2024</option>
                            <option value="2025">2025</option>
                            <option value="2026">2026</option>
                        </select>
                        
                        <label for="positionFilter" class="mb-0 ms-2" style="font-size: 0.875rem; font-weight: 500;">Position:</label>
                        <select id="positionFilter" class="form-select form-select-sm" style="width: auto; max-width: 180px;">
                            <option value="" selected>All Positions</option>
                        </select>
                    </div>
                </div>'''

# Replace the header
if old_header in content:
    content = content.replace(old_header, new_header)
    print("✓ Added filter dropdowns to Monthly Statistics header")
else:
    print("✗ Could not find the Monthly Statistics header section")
    exit(1)

# Add JavaScript for the filters in the initializeDropdown function
old_init = '''        // Function to initialize the dropdown
        function initializeDropdown() {
            const viewTypeSelect = document.getElementById('viewType');
            console.log('viewTypeSelect element:', viewTypeSelect);
            if (viewTypeSelect) {'''

new_init = '''        // Function to initialize the dropdown
        function initializeDropdown() {
            const viewTypeSelect = document.getElementById('viewType');
            const yearFilterSelect = document.getElementById('yearFilter');
            const positionFilterSelect = document.getElementById('positionFilter');
            
            console.log('viewTypeSelect element:', viewTypeSelect);
            if (viewTypeSelect) {'''

if old_init in content:
    content = content.replace(old_init, new_init)
    print("✓ Updated initializeDropdown function")
else:
    print("✗ Could not find initializeDropdown function")
    exit(1)

# Add event listeners for the new filters
old_end_init = '''                console.log('Dropdown initialized and enabled');
            } else {
                console.error('Error: Dropdown element with ID "viewType" not found.');
            }
        }'''

new_end_init = '''                console.log('Dropdown initialized and enabled');
            } else {
                console.error('Error: Dropdown element with ID "viewType" not found.');
            }
            
            // Initialize year filter
            if (yearFilterSelect) {
                console.log('Initializing year filter');
                yearFilterSelect.addEventListener('change', function() {
                    console.log('Year filter changed to:', this.value);
                    fetchAnalyticsData();
                });
            }
            
            // Initialize position filter
            if (positionFilterSelect) {
                console.log('Initializing position filter');
                positionFilterSelect.addEventListener('change', function() {
                    console.log('Position filter changed to:', this.value);
                    fetchAnalyticsData();
                });
            }
        }'''

if old_end_init in content:
    content = content.replace(old_end_init, new_end_init)
    print("✓ Added event listeners for filters")
else:
    print("✗ Could not find end of initializeDropdown function")
    exit(1)

# Update fetchAnalyticsData to include filters
old_fetch = '''        // Function to fetch analytics data
        function fetchAnalyticsData() {
            console.log('Fetching analytics data');

            // Construct URL without year parameter
            let url = '/api/analytics?t=' + new Date().getTime(); // Cache busting
            console.log('API URL:', url);'''

new_fetch = '''        // Function to fetch analytics data
        function fetchAnalyticsData() {
            console.log('Fetching analytics data');

            // Construct URL with filters
            let url = '/api/analytics?t=' + new Date().getTime(); // Cache busting
            
            const yearFilter = document.getElementById('yearFilter');
            if (yearFilter && yearFilter.value) {
                url += '&year=' + yearFilter.value;
            }
            
            const positionFilter = document.getElementById('positionFilter');
            if (positionFilter && positionFilter.value) {
                url += '&position=' + encodeURIComponent(positionFilter.value);
            }
            
            console.log('API URL:', url);'''

if old_fetch in content:
    content = content.replace(old_fetch, new_fetch)
    print("✓ Updated fetchAnalyticsData to include filters")
else:
    print("✗ Could not find fetchAnalyticsData function")
    exit(1)

# Add logic to populate position dropdown
old_position_stats = '''                    // POSITION STATISTICS
                    const positionStatisticsBody = document.getElementById('positionStatisticsBody');

                    if (positionStatisticsBody) {'''

new_position_stats = '''                    // Populate position filter dropdown
                    const positionFilter = document.getElementById('positionFilter');
                    if (positionFilter && data.position_statistics) {
                        const currentSelection = positionFilter.value;
                        // Keep the "All Positions" option
                        positionFilter.innerHTML = '<option value="">All Positions</option>';
                        
                        data.position_statistics.forEach(pos => {
                            if (pos.position) {
                                const option = document.createElement('option');
                                option.value = pos.position;
                                option.textContent = pos.position;
                                if (pos.position === currentSelection) {
                                    option.selected = true;
                                }
                                positionFilter.appendChild(option);
                            }
                        });
                    }

                    // POSITION STATISTICS
                    const positionStatisticsBody = document.getElementById('positionStatisticsBody');

                    if (positionStatisticsBody) {'''

if old_position_stats in content:
    content = content.replace(old_position_stats, new_position_stats)
    print("✓ Added position dropdown population logic")
else:
    print("✗ Could not find position statistics section")
    exit(1)

# Write the updated content back
with open('templates/analytics.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✅ Successfully added Year and Position filters to analytics.html!")
print("Please refresh your browser to see the changes.")
