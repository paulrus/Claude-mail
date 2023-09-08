# Flask app
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
   emails = get_classified_emails()
   return render_template('index.html', emails=emails)
   
@app.route('/classify', methods=['POST'])
def classify():
   # Classify email API
   return {'result': 'classified'}

# JavaScript code 

# Render classified emails
function renderEmails(emails) {
  // Loop through emails and add to DOM
}

# Handle classify button click
$('#classify').click(function() {

  // Call classification API
  $.post('/classify', {}, function(result) {
    // Handle result 
  });

});
