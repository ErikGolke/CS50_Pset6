from flask import Flask, redirect, render_template, request, url_for

import helpers
import os
import sys
from analyzer import Analyzer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name", "").lstrip("@")
    if not screen_name:
        return redirect(url_for("index"))

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name)

    # absolute paths to lists
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")

    # instantiate analyzer
    analyzer = Analyzer(positives, negatives)

    positive = 0.0
    negative = 0.0
    neutral = 0.0
    
    # If invalid twitter user, redirects to index page
    if tweets is None:
        return redirect(url_for("index"))
    
    # If user has less than 100 tweets, analyze all tweets    
    if len(tweets) < 100:
        for i in range(len(tweets)):
            score = analyzer.analyze(tweets[i])
        
            if score > 0.0:
                positive += 1.0
            elif score < 0.0:
                negative += 1.0
            else:
                neutral += 1.0  
                
    # If user has over 100 tweets, only analyze 100 
    else:    
        for i in range(100):
    
            score = analyzer.analyze(tweets[i])
        
            if score > 0.0:
                positive += 1.0
            elif score < 0.0:
                negative += 1.0
            else:
                neutral += 1.0  
        
            
    # generate chart
    chart = helpers.chart(positive, negative, neutral)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)
