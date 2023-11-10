# Car Price Prediction Project

## Overview

This Django-based web application predicts car prices based on user input. The app fetches data from the `bama.ir` website, processes it using a machine learning model built with Scikit-learn, and predicts the price of a car based on its brand, model, mileage, year, and body color.

## Features

- User-friendly web interface for inputting car details.
- Price prediction using Linear Regression model.
- Data fetching and processing from `bama.ir`.

## Requirements

- Python 3.x
- Django
- Scikit-learn
- Pandas
- Requests
- Googletrans

## Installation

1. Clone the repository:
2. Install the required packages:
```
pip install -r requirements.txt
```
3. Navigate to the project directory and run the Django server:
```
python manage.py runserver
```

## Usage

1. Open a web browser and navigate to `http://127.0.0.1:8000/`.
2. Enter the details of the car (brand, model, mileage, year, and body color).
3. Click on "Predict Price" to view the predicted price.
4. A loader animation will display while processing, followed by the predicted price.

## Project Structure

- `fetch_car_data_as_dataframe.py`: Module to fetch car data and convert it to a DataFrame.
- `predict_car_price.py`: Module containing the machine learning model for price prediction.
- `templates/`: Folder containing HTML templates for the web interface.
- `static/`: Folder containing static files (CSS, JS, etc.).

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

[Specify the license here or state that it's unlicensed]

---

For more information, contact the project maintainer at [Your Email/Contact Information].
