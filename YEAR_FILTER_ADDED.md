# Year Filter Added to Analytics

## Changes Made
1.  **Frontend (`templates/analytics.html`)**:
    -   Added a "Year" dropdown next to the "View Type" dropdown in the page header.
    -   Options include "All Time", "2024", "2025", "2026".
    -   Updated `initializeDropdown` to handle the new Year dropdown.
    -   Updated `fetchAnalyticsData` to include the selected `year` in the API request query parameters.

2.  **Backend (`app.py`)**:
    -   The `/api/analytics` endpoint was already set up to handle the `year` parameter, so no changes were needed there.

## How to Test
1.  Navigate to the **Analytics** page.
2.  You should see a **Year** dropdown next to "View Type".
3.  Select a year (e.g., 2024).
4.  The charts and tables (Monthly Statistics, etc.) should update to show data only for that year.
5.  Select "All Time" to see all data again.
