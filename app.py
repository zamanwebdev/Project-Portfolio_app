from flask import Flask, render_template, request, flash, redirect
import smtplib

app = Flask(__name__)
app.secret_key = "secret123"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        send_email(name, email, message)
        flash("Message sent successfully!")
        return redirect('/contact')

    return render_template('contact.html')


def send_email(name, email, message):
    sender_email = "zamanwebdev@gmail.com"
    sender_password = "cfho rivf pgtu cmza"

    full_message = f"From: {name}\nEmail: {email}\n\nMessage:\n{message}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, sender_email, full_message)
    server.quit()


if __name__ == '__main__':
    app.run()
