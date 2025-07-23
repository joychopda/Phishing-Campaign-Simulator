# Phishing Campaign Simulator

## 🚀 Overview

This project is a **Phishing Campaign Simulator & Awareness Platform** built with Python and Flask. It helps organizations assess user susceptibility to phishing attacks and delivers immediate educational feedback through a simulated, yet realistic, phishing experience.

The platform tracks user interactions and provides a dashboard for campaign analysis. A standout feature is its **humorous and informative awareness module**, which guides users who fall for the simulation on how to identify future phishing attempts.

## ✨ Features

- **Simulated Phishing Emails**: "Sends" personalized phishing emails to a predefined list of users with unique, trackable links.
- **Click Tracking**: Logs details (IP address, user agent, timestamp) of users who click the phishing links.
- **Humorous & Informative Awareness Module**: Redirects clickers to a fake Google Sites landing page that educates them on red flags with a humorous twist.
- **Real-time Dashboard**: Displays campaign results including total users, clicks, and click rate.
- **Customizable User List**: Easily edit the predefined user list for different campaigns.
- **Flask Web App**: Provides a simple interface for managing the campaign and viewing results.

## 🎯 How it Works

1. **Email Dispatch**  
   The `send_campaign_emails()` function generates unique phishing links for each user.
2. **Simulated Email Sending**  
   The `send_phishing_email()` function simulates sending. (SMTP integration can be added.)
3. **Phishing Endpoint**  
   When a user clicks the link, the `/phish/` route logs details and redirects to the awareness page.
4. **Awareness Page**  
   The user lands on a humorous Google Site:  
   [Chopda Enterprise Test](https://sites.google.com/view/chopda-enterprise-test/home)
5. **Dashboard**  
   The `/dashboard` route displays the campaign’s metrics and click stats.

## 🛠️ Installation & Setup

1. **Clone the Repo**
   ```bash
   git clone https://github.com/your-username/phishing-campaign-simulator.git
   cd phishing-campaign-simulator
   ```

2. **Install Dependencies**
   ```bash
   pip install Flask
   ```

3. **Configure Awareness Page URL**  
   In `phishing-test.py`, set the awareness page:
   ```python
   app.config['EXTERNAL_FAKE_LANDING_PAGE_URL'] = 'https://sites.google.com/view/chopda-enterprise-test/home'
   ```

4. **Run the App**
   ```bash
   python phishing-test.py
   ```

## 🏃 How to Use

1. **Start the App**  
   Run `python phishing-test.py` to simulate the phishing campaign and launch the Flask server.

2. **Check Console Output**  
   Unique phishing links for each user will be printed.

3. **Simulate a Click**  
   Paste a link (e.g., `http://127.0.0.1:5000/phish/alice@example.com`) into your browser.

4. **Redirect to Awareness Page**  
   You’ll be redirected to the humorous Google Site with awareness info.

5. **View the Dashboard**  
   Go to `http://127.0.0.1:5000/dashboard` to see click data.

## 📂 Project Structure

```
├── phishing-test.py      # Main Flask app and phishing logic
└── README.md             # This file
```

## 🤝 Contributing

Fork it, open issues, or submit pull requests — contributions are welcome!

## 📜 License

This project is open-source under the MIT License.
