# Email Automation Setup Guide

## Overview
This guide will help you set up automatic rejection email sending when a candidate's Application Status is changed to "Rejected".

## Step 1: Email Configuration

### Option A: Using Gmail (Recommended for Testing)

1. **Enable 2-Step Verification** on your Gmail account
   - Go to https://myaccount.google.com/security
   - Enable 2-Step Verification

2. **Create an App Password**
   - Go to https://myaccount.google.com/apppasswords
   - Select "Mail" and "Windows Computer"
   - Click "Generate"
   - Copy the 16-character password

3. **Update Email Configuration**
   - Open `app.py`
   - Find the `EMAIL_CONFIG` section (around line 20)
   - Update with your details:
   ```python
   EMAIL_CONFIG = {
       'SMTP_SERVER': 'smtp.gmail.com',
       'SMTP_PORT': 587,
       'SENDER_EMAIL': 'your-email@gmail.com',  # Your Gmail address
       'SENDER_PASSWORD': 'xxxx xxxx xxxx xxxx',  # Your App Password
       'SENDER_NAME': 'HR Recruitment Team'
   }
   ```

### Option B: Using Other Email Providers

**Outlook/Office365:**
```python
EMAIL_CONFIG = {
    'SMTP_SERVER': 'smtp.office365.com',
    'SMTP_PORT': 587,
    'SENDER_EMAIL': 'your-email@outlook.com',
    'SENDER_PASSWORD': 'your-password',
    'SENDER_NAME': 'HR Recruitment Team'
}
```

**Yahoo Mail:**
```python
EMAIL_CONFIG = {
    'SMTP_SERVER': 'smtp.mail.yahoo.com',
    'SMTP_PORT': 587,
    'SENDER_EMAIL': 'your-email@yahoo.com',
    'SENDER_PASSWORD': 'your-app-password',  # Generate from Yahoo
    'SENDER_NAME': 'HR Recruitment Team'
}
```

## Step 2: Add Required Code to app.py

### 2.1 Add Imports (at the top of app.py, after line 12)
```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
```

### 2.2 Add Email Configuration (after line 24)
```python
# Email Configuration
EMAIL_CONFIG = {
    'SMTP_SERVER': 'smtp.gmail.com',
    'SMTP_PORT': 587,
    'SENDER_EMAIL': 'your-email@gmail.com',
    'SENDER_PASSWORD': 'your-app-password',
    'SENDER_NAME': 'HR Recruitment Team'
}
```

### 2.3 Add Email Sending Function (after the `is_admin()` function, around line 305)
```python
def send_rejection_email(candidate_name, candidate_email, position):
    """Send a professional rejection email to the candidate"""
    try:
        # Create message
        msg = MIMEMultipart('alternative')
        msg['From'] = f"{EMAIL_CONFIG['SENDER_NAME']} <{EMAIL_CONFIG['SENDER_EMAIL']}>"
        msg['To'] = candidate_email
        msg['Subject'] = f"Application Update - {position}"
        
        # HTML email body
        html_body = f"""
        <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
                    <h2 style="color: #2c3e50;">Application Status Update</h2>
                    
                    <p>Dear {candidate_name},</p>
                    
                    <p>Thank you for your interest in the <strong>{position}</strong> position at our organization.</p>
                    
                    <p>After careful consideration, we regret to inform you that we have decided to move forward with other candidates whose experience more closely matches our current requirements.</p>
                    
                    <p>We appreciate the time you invested in applying. Your credentials are impressive, and we encourage you to apply for future openings.</p>
                    
                    <p>We wish you all the best in your job search.</p>
                    
                    <p>Best regards,<br>
                    <strong>{EMAIL_CONFIG['SENDER_NAME']}</strong></p>
                    
                    <hr style="border: none; border-top: 1px solid #eee; margin: 20px 0;">
                    <p style="font-size: 12px; color: #666;">
                        This is an automated message. Please do not reply to this email.
                    </p>
                </div>
            </body>
        </html>
        """
        
        # Plain text version
        text_body = f"""
Dear {candidate_name},

Thank you for your interest in the {position} position at our organization.

After careful consideration, we regret to inform you that we have decided to move forward with other candidates whose experience more closely matches our current requirements.

We appreciate the time you invested in applying. Your credentials are impressive, and we encourage you to apply for future openings.

We wish you all the best in your job search.

Best regards,
{EMAIL_CONFIG['SENDER_NAME']}

---
This is an automated message.
        """
        
        # Attach both versions
        part1 = MIMEText(text_body, 'plain')
        part2 = MIMEText(html_body, 'html')
        msg.attach(part1)
        msg.attach(part2)
        
        # Send email
        with smtplib.SMTP(EMAIL_CONFIG['SMTP_SERVER'], EMAIL_CONFIG['SMTP_PORT']) as server:
            server.starttls()
            server.login(EMAIL_CONFIG['SENDER_EMAIL'], EMAIL_CONFIG['SENDER_PASSWORD'])
            server.send_message(msg)
        
        return True, "Email sent successfully"
    
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False, str(e)
```

### 2.4 Add API Endpoint (before the `if __name__ == '__main__':` line, around line 760)
```python
@app.route('/api/send-rejection-email', methods=['POST'])
@login_required
def send_rejection_email_api():
    """API endpoint to send rejection email"""
    try:
        data = request.json
        candidate_name = data.get('name', 'Candidate')
        candidate_email = data.get('email')
        position = data.get('position', 'the position')
        
        if not candidate_email:
            return jsonify({
                "status": "error",
                "message": "Candidate email is required"
            }), 400
        
        # Send the email
        success, message = send_rejection_email(candidate_name, candidate_email, position)
        
        if success:
            return jsonify({
                "status": "success",
                "message": "Rejection email sent successfully"
            })
        else:
            return jsonify({
                "status": "error",
                "message": f"Failed to send email: {message}"
            }), 500
    
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
```

## Step 3: Update JavaScript (app.js)

Find the section where we added the automation (around line 1151) and update it to send emails:

```javascript
} else if (newStatus === 'Rejected') {
    select.classList.add('status-rejected');
    
    // AUTOMATION: Send rejection email and update "Reject Mail Sent"
    const rejectMailCell = rowElement.querySelector('td[data-column="Reject Mail Sent"]');
    if (rejectMailCell) {
        const rejectMailSelect = rejectMailCell.querySelector('select');
        if (rejectMailSelect && rejectMailSelect.value !== 'Yes') {
            // Get candidate details
            const candidateName = row['Name'] || 'Candidate';
            const candidateEmail = row['Email ID'];
            const position = row['Interested Position'] || 'the position';
            
            if (candidateEmail) {
                // Send rejection email
                fetch('/api/send-rejection-email', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        name: candidateName,
                        email: candidateEmail,
                        position: position
                    })
                })
                .then(response => response.json())
                .then(emailData => {
                    if (emailData.status === 'success') {
                        // Update "Reject Mail Sent" to "Yes"
                        rejectMailSelect.value = 'Yes';
                        updateRecordStatus(recordIndex, 'Reject Mail Sent', 'Yes', rowElement, rejectMailSelect.value, 'Reject Mail Sent');
                        row['Reject Mail Sent'] = 'Yes';
                        showNotification('Rejection email sent successfully!', 'success');
                    } else {
                        showNotification('Failed to send rejection email: ' + emailData.message, 'error');
                    }
                })
                .catch(error => {
                    console.error('Error sending rejection email:', error);
                    showNotification('Error sending rejection email', 'error');
                });
            } else {
                showNotification('No email address found for candidate', 'warning');
            }
        }
    }
}
```

## Step 4: Testing

1. **Test Email Configuration**
   - Restart the Flask server
   - Change a candidate's status to "Rejected"
   - Check if the email is sent
   - Verify "Reject Mail Sent" changes to "Yes"

2. **Check for Errors**
   - Monitor the Flask console for any error messages
   - Check the browser console for JavaScript errors

## Troubleshooting

### Common Issues:

1. **"Authentication failed"**
   - Make sure you're using an App Password, not your regular password
   - Verify 2-Step Verification is enabled

2. **"Connection refused"**
   - Check your firewall settings
   - Verify SMTP server and port are correct

3. **"Email not received"**
   - Check spam/junk folder
   - Verify the candidate's email address is correct
   - Check Flask console for error messages

4. **"Reject Mail Sent not updating"**
   - Check browser console for JavaScript errors
   - Verify the API endpoint is working

## Security Notes

⚠️ **IMPORTANT:**
- Never commit your email password to version control
- Consider using environment variables for sensitive data
- Use App Passwords instead of regular passwords
- Limit email sending to prevent spam

## Next Steps

Once email sending is working, you can:
- Customize the email template
- Add email templates for different scenarios
- Implement bulk email sending
- Add email delivery tracking
- Create email logs for audit purposes
