# Manual Instructions: Add Offer Details Table to Analytics Page

## Problem
The automated edits keep corrupting the analytics.html file. This guide will help you manually add the "Offer Details" table.

## Step 1: Open the File
Open: `d:\jagadeesh\hr portal project\29-11\RecurimentPortal\templates\analytics.html`

## Step 2: Find the Location
Search for this text (around line 289-291):
```html
        <!-- ============================================= -->
        <!-- POSITION STATISTICS TABLE ENDS HERE          -->
        <!-- ============================================= -->

    </div>
```

## Step 3: Add the Offer Details Table
**REPLACE** the above section with this:

```html
        <!-- ============================================= -->
        <!-- POSITION STATISTICS TABLE ENDS HERE          -->
        <!-- ============================================= -->

        <!-- ============================================= -->
        <!-- OFFER DETAILS TABLE STARTS HERE              -->
        <!-- ============================================= -->
        <div class="row justify-content-center mt-4">
            <div class="col-md-8">
                <div class="card mb-3">
                    <div class="card-body p-3">
                        <h5 class="card-title mb-3">Offer Details</h5>
                        <div class="table-responsive">
                            <table class="table table-bordered table-hover mb-0">
                                <thead>
                                    <tr>
                                        <th>Name</th>
                                        <th>Offered CTC</th>
                                        <th>Joining Date</th>
                                    </tr>
                                </thead>
                                <tbody id="offerDetailsBody">
                                    <tr>
                                        <td colspan="3" class="text-center text-muted">Loading offer details...</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- ============================================= -->
        <!-- OFFER DETAILS TABLE ENDS HERE                -->
        <!-- ============================================= -->

    </div>
```

## Step 4: Save the File

## Step 5: Refresh the Browser
1. Go to http://127.0.0.1:5000/analytics
2. Press `Ctrl + Shift + R` to hard refresh
3. Scroll down - you should see the "Offer Details" table after "Position Statistics"

## Note:
- The backend code has already been updated to provide the offer details data
- The JavaScript to populate the table is already in place
- The table will show candidates who have an "Offered CTC" value in the Excel file

## If You See "No offer details available":
This means either:
1. There are no candidates with "Offered CTC" values in your data
2. The server needs to be restarted to pick up the backend changes

To restart the server:
1. Stop the running `python app.py` command (Ctrl+C)
2. Run `python app.py` again
3. Refresh the analytics page

---

**That's it! The table should now appear on your analytics page.**
