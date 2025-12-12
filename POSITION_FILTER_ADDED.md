# Position Filter Added to Analytics

## What Was Added

A **Position** filter dropdown has been added to the Monthly Statistics section on the Analytics page.

## Location

The filter appears in the **Monthly Statistics** card header, next to the Year filter:
- **Year** dropdown (existing)
- **Position** dropdown (NEW)

## How It Works

1. **Auto-Population**: The Position dropdown automatically populates with all unique positions from your candidate data
2. **Filtering**: Select a position to filter all analytics data for that specific role
3. **Combined Filters**: You can use both Year and Position filters together for more granular insights

## Changes Made

### Frontend (`templates/analytics.html`)
- Added Position dropdown HTML (lines 227-232)
- Added JavaScript event listener for position filter changes
- Updated `fetchAnalyticsData()` to include position parameter in API calls
- Auto-populates dropdown with available positions from data

### Backend (`app.py`)
- Added position filter logic (lines 580-584)
- Reads `position` query parameter from request
- Filters candidate data by "Interested Position" field

## How to Use

1. Navigate to **Analytics** page: http://127.0.0.1:5000/analytics
2. Look at the **Monthly Statistics** section
3. You'll see two dropdowns:
   - **Year**: All Time, 2024, 2025, 2026
   - **Position**: All Positions, [dynamically loaded positions]
4. Select a position to filter the data
5. The entire analytics dashboard updates based on your selection

## Troubleshooting

If you don't see the Position filter:
1. **Hard refresh** the page: Press `Ctrl + Shift + R` (Windows) or `Cmd + Shift + R` (Mac)
2. **Clear browser cache** and reload
3. **Check browser console** for any JavaScript errors (F12 → Console tab)
4. Verify you're logged in and on the Analytics page

## Technical Details

- **API Endpoint**: `/api/analytics?position=<position_name>`
- **Filter Field**: `Interested Position` from candidate data
- **Dropdown ID**: `positionFilter`
- **Default Value**: Empty string (shows all positions)
