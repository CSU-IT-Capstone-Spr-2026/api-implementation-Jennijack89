"""
XKCD Comic Viewer - Starter Code
"""
from flask import Flask, render_template, request
import requests
import random

app = Flask(__name__)

XKCD_BASE_URL = "https://xkcd.com"

def get_latest_comic():
    # Fetch the most recent XKCD comic from the API and returns dict: Comic data if successful, None if there's an error
    try:
        response = requests.get(f"{XKCD_BASE_URL}/info.0.json")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None


def get_comic_by_number(comic_num):
    # Fetch a specific XKCD comic by its number. Takes argument comic_num (int): The comic number to fetch
    try:
        response = requests.get(f"{XKCD_BASE_URL}/{comic_num}/info.0.json")
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print(f"Comic #{comic_num} not found")
            return None
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None


@app.route('/')
def index():
    #Home page - displays the latest XKCD comic. Implements Feature #1: Display the Latest Comic and 
    # Fetch the latest comic and if successful, render the template with comic data else show an error
    comic = get_latest_comic()
    if comic:
        latest_num = comic['num']
        return render_template('index.html', comic=comic,latest_comic_num=latest_num, error=None)
    else:
        return render_template('index.html', comic=None, 
                             error="Sorry, we couldn't fetch the comic right now. Please try again later.")


@app.route('/comic/<int:comic_num>')
def show_comic(comic_num):
    # Display a specific comic by number. Use this as a reference for implementing other features. example websiteUrl.com/comic/234
    # Validate comic number will pull back a comic
    latest = get_latest_comic()
    latest_num = latest['num'] if latest else 3200  # fallback
    if comic_num < 1 or comic_num > 3200:
        return render_template('index.html', comic=None,
                             error="Invalid comic number. Comics start at #1.")
    comic = get_comic_by_number(comic_num)
    if comic:
        return render_template('index.html', comic=comic, error=None)
    else:
        return render_template('index.html', comic=None,
                             error=f"Comic #{comic_num} could not be found. It may not exist.")


# TODO: Add more routes here for the other features you choose to implement

# Feature #3: Random Comic

@app.route('/random')
def random_comic():
    #Generate and display a random valid comic number between 1 and the latest comic number.
    #fetches that comic from the XKCD API and sends it to index.html.

    latest = get_latest_comic() #call and get the latest comic
    max_num = latest['num'] 
    random_num = random.randint(1, max_num)# Random integer between 1 and max_num

    comic = get_comic_by_number(random_num)
    if not comic:
        return render_template('index.html',comic=None,
                               error = f"Comic #{random_num} could not be found.")
    return render_template('index.html',comic=comic,error=None)

# Feature #4: Navigation (Previous/Next)

@app.route('/navigate/<int:comic_num>/<direction>')
def navigate(comic_num, direction):
    # direction will be 'prev' or 'next'
    #Get Latest comic number
    latest_comic = get_latest_comic()
    if not latest_comic:
        return render_template('index.html', comic=None, error="Could not fetch latest comic.")

    #move comic number
    if direction == 'prev':
        comic_num -= 1
    elif direction == 'next':
        comic_num += 1

    # Ensure comic number stays within bounds
    if comic_num < 1:
        comic_num = 1
    if comic_num > latest_comic['num']:
        comic_num = latest_comic['num']

    #Fetch comic data
    comic = get_comic_by_number(comic_num)
    if comic:
        return render_template('index.html', comic=comic, latest_num=latest_comic['num'], error=None)
    else:
        return render_template('index.html', comic=None, error=f"Comic #{comic_num} could not be found.")

    
        
# Feature #5: Search Form
# Feature #6: Display Multiple Recent Comics

# Run the Flask development server
if __name__ == '__main__':
    app.run(debug=True, port=5000)
