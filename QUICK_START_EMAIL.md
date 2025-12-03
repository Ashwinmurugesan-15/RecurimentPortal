# 🚀 Quick Start: Email Automation

## What This Does
When you change a candidate's **Application Status** to **"Rejected"**, the system will:
1. ✉️ **Automatically send** a professional rejection email to the candidate
2. ✅ **Update** "Reject Mail Sent" to "Yes"
3. 📢 **Show** a success notification

## Setup (5 Minutes)

### Step 1: Get Gmail App Password (2 minutes)

1. Go to https://myaccount.google.com/security
2. Enable "2-Step Verification" if not already enabled
3. Go to https://myaccount.google.com/apppasswords
4. Select "Mail" and "Windows Computer"
5. Click "Generate"
6. **Copy the 16-character password** (looks like: `xxxx xxxx xxxx xxxx`)

### Step 2: Update app.py (2 minutes)

1. Open `app.py`
2. Add these imports at the top (after line 12):
```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
```

3. Add email configuration (after line 24, before `EXCEL_FILE`):
```python
# Email Configuration
EMAIL_CONFIG = {
    'SMTP_SERVER': 'smtp.gmail.com',
    'SMTP_PORT': 587,
    'SENDER_EMAIL': 'jagadeesh19ct11@gmail.com',  # ← PUT YOUR EMAIL HERE
    'SENDER_PASSWORD': 'lwda firu drjp ajiy',  # ← PUT YOUR APP PASSWORD HERE
    'SENDER_NAME': 'HR Recruitment Team'
}
```

4. Copy the entire content from `email_module.py` and paste it:
   - The `send_rejection_email()` function (after the `is_admin()` function, around line 305)
   - The `@app.route('/api/send-rejection-email')` endpoint (before `if __name__ == '__main__':`, around line 760)

### Step 3: Update app.js (1 minute)

1. Open `static/js/app.js`
2. Find the line with `} else if (newStatus === 'Rejected') {` (around line 1151)
3. Replace the automation code with the content from `email_automation.js`

### Step 4: Test It! (30 seconds)

1. **Restart** the Flask server (Ctrl+C, then `python app.py`)
2. **Refresh** your browser (Ctrl+Shift+R)
3. **Change** any candidate's status to "Rejected"
4. **Watch** the magic happen! ✨

## What You'll See

1. **Notification**: "Sending rejection email..."
2. **Email sent** to the candidate
3. **Notification**: "✅ Rejection email sent to [Name]"
4. **"Reject Mail Sent"** automatically changes to "Yes"

## Email Template Preview

The candidate will receive a professional email like this:

---

**Subject:** Application Update - Software Developer

Dear John Doe,

Thank you for your interest in the **Software Developer** position at our organization and for taking the time to go through our recruitment process.

After careful consideration of your application and qualifications, we regret to inform you that we have decided to move forward with other candidates whose experience and skills more closely match our current requirements.

We truly appreciate the time and effort you invested in applying for this position. Your credentials are impressive, and we encourage you to apply for future openings that match your qualifications.

We wish you all the best in your job search and future professional endeavors.

Best regards,  
**HR Recruitment Team**

---

## Troubleshooting

### ❌ "Authentication failed"
- Make sure you're using the **App Password**, not your regular Gmail password
- Verify 2-Step Verification is enabled

### ❌ "No valid email address found"
- Check that the candidate has an email address in the "Email ID" field
- Make sure the email contains an @ symbol

### ❌ Email not received
- Check the candidate's spam/junk folder
- Verify the email address is correct
- Check the Flask console for error messages

## Customization

### Change Email Template
Edit the `html_body` and `text_body` in the `send_rejection_email()` function in `app.py`

### Change Sender Name
Update `'SENDER_NAME': 'Your Company Name'` in `EMAIL_CONFIG`

### Add CC/BCC
Add these lines in the `send_rejection_email()` function:
```python
msg['Cc'] = 'hr@yourcompany.com'
msg['Bcc'] = 'archive@yourcompany.com'
```

## Security Tips

⚠️ **IMPORTANT:**
- Never share your App Password
- Don't commit passwords to Git
- Use environment variables for production
- Keep your App Password secure

## Need Help?

Check the detailed guide in `EMAIL_AUTOMATION_SETUP.md` for:
- Using other email providers (Outlook, Yahoo)
- Advanced customization
- Bulk email sending
- Email logging and tracking

---

**That's it! You're all set!** 🎉

Now when you reject a candidate, they'll automatically receive a professional email, and you'll never have to manually update "Reject Mail Sent" again!
