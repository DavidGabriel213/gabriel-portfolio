import os
import smtplib

from flask import Flask, render_template, request, redirect, url_for, flash
from email.message import EmailMessage
@app.route("/contact", methods=["POST"])
def contact():

    name = request.form.get("name")
    email = request.form.get("email")
    subject = request.form.get("subject")
    message = request.form.get("message")

    msg = EmailMessage()

    msg["Subject"] = f"Portfolio Contact: {subject}"
    msg["From"] = os.environ.get("MAIL_USERNAME")
    msg["To"] = "gdkimati@gmail.com"
    msg["Reply-To"] = email

    msg.set_content(
        f"""
You received a new message from your portfolio.

Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}
"""
    )

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(
                os.environ.get("MAIL_USERNAME"),
                os.environ.get("MAIL_PASSWORD")
            )
            smtp.send_message(msg)

        return """
        <script>
            alert("Message sent successfully!");
            window.history.back();
        </script>
        """

    except Exception as e:
        print("Email error:", e)

        return """
        <script>
            alert("Sorry, the message could not be sent.");
            window.history.back();
        </script>
        """, 500
