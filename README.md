[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/zN2AskmG)
# XKCD Comic Viewer

A simple web application to view XKCD comics using the XKCD API.  
Users can view the latest comic, a specific comic by number, a random comic, and navigate with Previous/Next buttons.

## Features Implemented

Check off the features you implemented (must have at least 4 and 2 are implemeted for you already):

- [X] Feature #1: Display the Latest Comic
- [X] Feature #2: Display a Specific Comic by Number
- [X] Feature #3: Random Comic Button
- [X] Feature #4: Navigation (Previous/Next)
- [ ] Feature #5: Search by Comic Number Form
- [ ] Feature #6: Display Multiple Recent Comics

## Technologies Used

- Python 3.8+
- Flask 3.0.0
- Requests 2.31.0
- XKCD API

## Installation and Setup

### Prerequisites
- Python 3.8 or higher installed
- pip (Python package manager)

### Steps to Run

1. Clone or download this repository

2. Navigate to the project directory in your terminal:
   ```
   cd projectName
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python app.py
   ```

5. Open your web browser and go to:
   ```
   http://localhost:5000
   ```

## Usage

- **Latest Comic:** The home page automatically shows the most recent comic.  
- **Random Comic:** Click the "Random Comic" button to view a random comic.  
- **Navigation Buttons:**  
- **Previous:** Goes to the previous comic (will be disabled on the first comic).  
- **Next:** Go to the next comic (will be disabled on the latest comic).  

## Screenshots

[Add screenshots of your application here - you can drag and drop images into GitHub or use Markdown image syntax]

Example:
```
![Latest Comic View](screenshots/latest-comic.png)
![Search Feature](screenshots/search.png)
```

## API Endpoints Used

- `GET /info.0.json` - Fetches the latest comic
- `GET /{comic_number}/info.0.json` - Fetches a specific comic by number

## Challenges and Solutions

- The main Challenge I faced was learning to work with technologies I haven't used in a while. Git, Python, HTLM
- I've found I need a lot more practice and some refreshers
- It was also a challenge managing navigation buttons to avoid invalid comic numbers.  
- I learned a little about how API responses work and how flask acts as the go between
- I also learned about JSON parsing and basic error handling.  
- Solved issues by using Python functions to validate comic numbers and I'm still working on using the disable buttons correctly.

## Future Improvements

- I would add the search by comic number feature.  
- The display multiple recent comics on one page feature.  

## Author

Jennifer Jackson