# Reject Mail Sent Automation - Feature Documentation

## Overview
The "Reject Mail Sent" field is now **automatically updated** when a candidate's Application Status is changed to "Rejected".

## How It Works

### Automatic Behavior
1. When a user changes the **Application Status** dropdown to **"Rejected"**
2. The system automatically:
   - Sets **"Reject Mail Sent"** to **"Yes"**
   - Updates the database
   - Shows a notification: "Reject Mail Sent automatically set to Yes"
   - Updates the UI immediately

### Manual Override
- Users can still manually change the "Reject Mail Sent" field if needed
- The automation only triggers when:
  - Application Status is changed to "Rejected"
  - "Reject Mail Sent" is not already set to "Yes"

## Benefits
✅ **Saves Time**: No need to manually update two fields
✅ **Reduces Errors**: Ensures rejected candidates are always marked
✅ **Consistent Data**: Maintains data integrity across the system
✅ **User-Friendly**: Works seamlessly in the background

## Future Enhancements (Optional)
You could further enhance this feature by:

1. **Email Integration**: Actually send rejection emails automatically
   - Integrate with SMTP server (Gmail, SendGrid, etc.)
   - Use email templates for professional rejection messages
   - Track email delivery status

2. **Bulk Operations**: Add a button to send rejection emails to all rejected candidates at once

3. **Email Templates**: Create customizable email templates for different rejection scenarios

4. **Audit Trail**: Log when rejection emails are sent and by whom

## Testing the Feature
1. Navigate to the Candidate Management page
2. Find any candidate
3. Change their "Application Status" to "Rejected"
4. Watch as "Reject Mail Sent" automatically changes to "Yes"
5. You'll see a notification confirming the automation

## Code Location
- **File**: `static/js/app.js`
- **Lines**: 1151-1171 (approximately)
- **Function**: Event listener for Application Status dropdown change

## Notes
- The automation is non-intrusive and doesn't prevent manual changes
- It only affects the "Reject Mail Sent" field when status becomes "Rejected"
- The feature works for both admin and non-admin users
