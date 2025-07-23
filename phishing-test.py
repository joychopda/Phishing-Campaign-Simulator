import smtplib
from email.mime.text import MIMEText
from flask import Flask, request, redirect, url_for, render_template_string
import uuid
import datetime
import json

# --- Flask Application Setup ---
app = Flask(__name__)
# Configure SERVER_NAME for generating external URLs outside of a request context
app.config['SERVER_NAME'] = '127.0.0.1:5000'
# --- IMPORTANT: REPLACE THIS WITH YOUR ACTUAL PUBLISHED FAKE LANDING PAGE URL ---
app.config['EXTERNAL_FAKE_LANDING_PAGE_URL'] = 'https://sites.google.com/view/chopda-enterprise-test/home'

# In-memory storage for campaign data (for demonstration purposes)
campaign_results = {}
users = {
    "alice@example.com": "Alice",
    "bob@example.com": "Bob",
    "charlie@example.com": "Charlie"
}

# --- Email Simulation Function ---
def send_phishing_email(recipient_email, recipient_name, unique_link):
    """
    Simulates sending a phishing email.
    In a real scenario, you would configure an SMTP server here.
    """
    sender_email = "support@yourcompany.com" # This would be spoofed in a real attack
    subject = "Urgent: Action Required Regarding Your Employee Benefits"
    body = f"""
    Dear {recipient_name},

    We have detected unusual activity on your employee benefits portal.
    To secure your account and avoid suspension, please click on the link below to verify your details immediately:

    {unique_link}

    Failure to do so within 24 hours may result in the permanent suspension of your benefits access.

    Sincerely,

    Benefits Department
    Your Company HR
    """

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    print(f"\n--- Simulating Email to {recipient_email} ---")
    print(f"Subject: {subject}")
    print(f"From: {sender_email}")
    print(f"To: {recipient_email}")
    print(f"Body:\n{body}")
    print("--- End Email Simulation ---\n")

    # In a real scenario, you'd use smtplib like this:
    # try:
    #     with smtplib.SMTP_SSL('smtp.your-email-provider.com', 465) as smtp:
    #         smtp.login('your_smtp_username', 'your_smtp_password')
    #         smtp.send_message(msg)
    #     print(f"Email successfully 'sent' to {recipient_email}")
    # except Exception as e:
    #     print(f"Failed to 'send' email to {recipient_email}: {e}")

# --- Flask Routes ---

@app.route('/')
def home():
    """Simple home page for the Flask app."""
    return """
    <h1 style="font-family: Arial, sans-serif;">Phishing Campaign Simulator</h1>
    <p style="font-family: Arial, sans-serif;">
        This is a demonstration of a simple phishing campaign setup.
        <br>
        To start, run the `send_campaign_emails()` function in your Python environment.
        <br>
        Then, navigate to the generated links or check the dashboard.
    </p>
    <p style="font-family: Arial, sans-serif;">
        <a href="/dashboard" style="font-family: Arial, sans-serif;">View Campaign Dashboard</a>
    </p>
    """

@app.route('/phish/<user_id>')
def phishing_landing_page(user_id):
    """
    The 'phishing' landing page. Logs details and redirects to the external fake page.
    """
    ip_address = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    timestamp = datetime.datetime.now().isoformat()

    # Log the click immediately upon access
    campaign_results[user_id] = {
        'clicked': True,
        'ip': ip_address,
        'user_agent': user_agent,
        'timestamp': timestamp
    }
    print(f"Phishing link clicked by user_id: {user_id}")
    print(f"  IP: {ip_address}")
    print(f"  User-Agent: {user_agent}")
    print(f"  Timestamp: {timestamp}")

    # Redirect to your external fake landing page
    return redirect(app.config['EXTERNAL_FAKE_LANDING_PAGE_URL'])

@app.route('/awareness')
def awareness_page():
    """
    The awareness module page, explaining red flags.
    """
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>You've Been Phished! (But It's a Test!)</title>
        <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family: 'Inter', sans-serif; }
        </style>
    </head>
    <body class="bg-gray-100 flex items-center justify-center min-h-screen p-4">
        <div class="bg-white rounded-lg shadow-xl p-8 max-w-2xl w-full text-center">
            <h1 class="text-3xl font-bold text-red-600 mb-4">Oops! You Clicked a Phishing Link!</h1>
            <p class="text-gray-700 mb-6">
                Don't worry, this was a **simulated phishing test** designed to help you recognize malicious emails.
                You're not in trouble, but this is a great learning opportunity!
            </p>

            <h2 class="text-2xl font-semibold text-gray-800 mb-4">Here's What You Might Have Missed:</h2>
            <ul class="list-disc list-inside text-left text-gray-700 space-y-2 mb-6">
                <li><strong class="text-blue-600">Suspicious Sender:</strong> Did the email address look exactly right? Often, phishers use slight misspellings or unusual domains.</li>
                <li><strong class="text-blue-600">Urgent or Threatening Language:</strong> Phishing emails often create a sense of panic or urgency ("Act now or your account will be suspended!").</li>
                <li><strong class="text-blue-600">Generic Greetings:</strong> Did it address you by "Dear Customer" instead of your name?</li>
                <li><strong class="text-blue-600">Unusual Requests:</strong> Were you asked to click a link to "verify" details, send money, or provide sensitive information?</li>
                <li><strong class="text-blue-600">Grammar/Spelling Errors:</strong> While AI makes this less common, glaring mistakes are still a red flag.</li>
                <li><strong class="text-blue-600">Hover Over Links:</strong> Did you hover over the link before clicking? The actual URL might not match the text.</li>
            </ul>

            <p class="text-gray-700 mb-6">
                **AI-generated phishing emails are getting very sophisticated.** They can be grammatically perfect and sound incredibly convincing. Always apply the "context is king" rule: Is this request normal for this sender? Is the timing suspicious? When in doubt, verify through a *separate*, known channel (e.g., call the person, use an internal chat, or log in directly to the official website).
            </p>

            <p class="text-gray-700 font-semibold">
                Thanks for participating in this exercise! Your vigilance helps keep us all safe.
            </p>
            <a href="/" class="inline-block mt-8 px-6 py-3 bg-blue-600 text-white font-bold rounded-full hover:bg-blue-700 transition duration-300">
                Back to Home
            </a>
        </div>
    </body>
    </html>
    """)

@app.route('/dashboard')
def dashboard():
    """
    Displays the campaign results (who clicked).
    """
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Phishing Campaign Dashboard</title>
        <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family: 'Inter', sans-serif; }
        </style>
    </head>
    <body class="bg-gray-100 p-8">
        <div class="bg-white rounded-lg shadow-xl p-8 max-w-4xl mx-auto">
            <h1 class="text-3xl font-bold text-gray-800 mb-6 text-center">Phishing Campaign Results</h1>

            <div class="mb-8">
                <h2 class="text-2xl font-semibold text-gray-700 mb-4">Summary</h2>
                <p class="text-gray-600">Total Users: <span class="font-bold">{{ total_users }}</span></p>
                <p class="text-gray-600">Users Clicked: <span class="font-bold text-red-500">{{ clicked_users }}</span></p>
                <p class="text-gray-600">Click Rate: <span class="font-bold text-green-600">{{ '{:.2f}'.format(click_rate) }}%</span></p>
            </div>

            <h2 class="text-2xl font-semibold text-gray-700 mb-4">Detailed Clicks</h2>
            {% if clicked_users > 0 %}
            <div class="overflow-x-auto">
                <table class="min-w-full bg-white border border-gray-200 rounded-lg shadow-sm">
                    <thead>
                        <tr class="bg-gray-100 text-left text-gray-600 uppercase text-sm leading-normal">
                            <th class="py-3 px-6 border-b border-gray-200">User Email</th>
                            <th class="py-3 px-6 border-b border-gray-200">Status</th>
                            <th class="py-3 px-6 border-b border-gray-200">IP Address</th>
                            <th class="py-3 px-6 border-b border-gray-200">Timestamp</th>
                            <th class="py-3 px-6 border-b border-gray-200">User Agent</th>
                        </tr>
                    </thead>
                    <tbody class="text-gray-700 text-sm font-light">
                        {% for user_email, user_name in users.items() %}
                        <tr class="border-b border-gray-200 hover:bg-gray-50">
                            <td class="py-3 px-6 text-left whitespace-nowrap">{{ user_email }}</td>
                            <td class="py-3 px-6 text-left">
                                {% if campaign_results.get(user_email, {}).get('clicked') %}
                                    <span class="bg-red-200 text-red-600 py-1 px-3 rounded-full text-xs font-bold">CLICKED</span>
                                {% else %}
                                    <span class="bg-green-200 text-green-600 py-1 px-3 rounded-full text-xs font-bold">NOT CLICKED</span>
                                {% endif %}
                            </td>
                            <td class="py-3 px-6 text-left">{{ campaign_results.get(user_email, {}).get('ip', 'N/A') }}</td>
                            <td class="py-3 px-6 text-left">{{ campaign_results.get(user_email, {}).get('timestamp', 'N/A') }}</td>
                            <td class="py-3 px-6 text-left break-all">{{ campaign_results.get(user_email, {}).get('user_agent', 'N/A') }}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
            {% else %}
            <p class="text-gray-600 text-center">No clicks recorded yet. Send out the emails!</p>
            {% endif %}
            <div class="text-center mt-8">
                <a href="/" class="inline-block px-6 py-3 bg-blue-600 text-white font-bold rounded-full hover:bg-blue-700 transition duration-300">
                    Back to Home
                </a>
            </div>
        </div>
    </body>
    </html>
    """
    total_users = len(users)
    clicked_users = sum(1 for user_id in users if campaign_results.get(user_id, {}).get('clicked'))
    click_rate = (clicked_users / total_users * 100) if total_users > 0 else 0

    return render_template_string(
        html_content,
        total_users=total_users,
        clicked_users=clicked_users,
        click_rate=click_rate,
        users=users,
        campaign_results=campaign_results
    )

# --- Campaign Execution Function ---
def send_campaign_emails():
    """
    Prepares and 'sends' phishing emails to all defined users.
    """
    print("--- Initiating Phishing Campaign Email Dispatch ---")
    for email, name in users.items():
        # Initialize campaign_results for all users, even if not clicked yet
        if email not in campaign_results:
            campaign_results[email] = {'clicked': False, 'ip': 'N/A', 'user_agent': 'N/A', 'timestamp': 'N/A'}

        # Generate a unique link for each user
        unique_user_id = email
        with app.app_context():
            phishing_link = url_for('phishing_landing_page', user_id=unique_user_id, _external=True)

        send_phishing_email(email, name, phishing_link)
    print("--- Phishing Campaign Email Dispatch Complete (Simulated) ---")
    print("Now, open the generated links in a browser to see the fake landing page and then the awareness page.")
    print("Then, navigate to http://127.0.0.1:5000/dashboard to see the results.")


# --- Main execution block ---
if __name__ == '__main__':
    send_campaign_emails()

    print("\nStarting Flask web server...")
    print("Access the home page at: http://127.0.0.1:5000/")
    print("Access the dashboard at: http://127.0.0.1:5000/dashboard")
    app.run(debug=True)
