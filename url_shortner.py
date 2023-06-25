import hashlib
from flask import Flask, redirect, render_template, request

app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost:3116'  # Replace with your server name

# In-memory database to store mappings
urls = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form['url']
    short_url = hashlib.md5(long_url.encode()).hexdigest()[:8]
    urls[short_url] = long_url
    return render_template('shortened.html', short_url=short_url)

@app.route('/<short_url>')
def redirect_to_url(short_url):
    if short_url in urls:
        long_url = urls[short_url]
        return redirect(long_url, code=302)  # Add code=302 for explicit redirection
    else:
        return "URL not found."

if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for better error messages
