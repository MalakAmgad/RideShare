
# 🚕 Taxi Fare Prediction Web Application

This project is a web application that predicts the fare of a taxi ride based on user-inputted pickup and dropoff coordinates, passenger count, time, and other details. The app leverages Django as the backend framework, a Google Maps API integration for location selection, and a Jupyter notebook for data processing and model training.

## 📋 Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Data and Model](#data-and-model)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Acknowledgments](#acknowledgments)

## 🚀 Features

- **Fare Prediction**: Input pickup and dropoff locations, time, and passenger count, and receive an estimated fare.
- **Interactive Map Integration**: Select pickup and dropoff locations directly from the map using Google Maps API.
- **Distance & Bearing Calculation**: Computes the distance and direction between pickup and dropoff, integrating other nearby airports.
- **Dynamic UI**: A responsive, user-friendly design with live fare prediction output.

## 🛠 Tech Stack

- **Backend**: Django 5.0.6
- **Frontend**: HTML, CSS, JavaScript, Google Maps API
- **Machine Learning**: Jupyter Notebook for model training and evaluation
- **Language**: Python 3.11.3

## 📊 Data and Model

The model uses a dataset loaded and preprocessed in a Jupyter Notebook. The notebook includes data processing steps, exploratory data analysis (EDA), and training of the model used to predict taxi fares.

### Key Steps in the Notebook:
1. **Data Preprocessing**: Cleans and preprocesses input data for better model accuracy.
2. **Feature Engineering**: Calculates time and location-based features.
3. **Model Training**: Uses a supervised learning algorithm (e.g., Random Forest) to predict the fare based on training data.
4. **Evaluation**: Analyzes model performance and fine-tunes for optimal predictions.

## ⚙️ Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/taxi-fare-prediction.git
   cd taxi-fare-prediction
   ```

2. **Install the Dependencies**:
   Ensure you have Python 3.11.3 or above installed.
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Django Settings**:
   Update the settings in `settings.py` for static files, and add your Google Maps API key in the HTML file:
   ```html
   <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY"></script>
   ```

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the Server**:
   ```bash
   python manage.py runserver
   ```

6. **Launch Jupyter Notebook**:
   Open the provided Jupyter notebook to review and adjust the data and model training as needed.

## 🖱️ Usage

1. **Open the Web App**:
   Access the application at `http://127.0.0.1:8000`.

2. **Enter Ride Details**:
   - Input the latitude and longitude of the pickup and dropoff locations.
   - Select the passenger count, date, and time of the trip.
   - Click on **Select Pickup/Dropoff** to open the map for easy selection.

3. **Get Prediction**:
   The app will calculate the fare based on your inputs, displaying both the distance and bearing between locations, including proximity to nearby airports (JFK, EWR, LGA, Solberg-Hunterdon).

## 📂 Project Structure

```plaintext
taxi-fare-prediction/
├── DjangoApp/                    # Django application folder
│   ├── templates/                # HTML templates
│   ├── static/                   # CSS and JavaScript files
│   ├── views.py                  # View logic for the app
│   ├── urls.py                   # URL routing for the app
│   └── models.py                 # Database models
├── Notebook6.ipynb               # Jupyter notebook with data processing and model training
├── requirements.txt              # Required dependencies
└── README.md                     # Project documentation
```

## 📸 Screenshots

| Feature                  | Screenshot |
|--------------------------|------------|
| **Home Page**            | ![Home Page](https://github.com/MalakAmgad/RideShare/blob/main/Screenshot%20(843).png) |
| **Map Selection**        | ![Map Popup](https://github.com/MalakAmgad/RideShare/blob/main/Screenshot%20(842).png) |
| **Prediction Output**    | ![Prediction Output](https://github.com/MalakAmgad/RideShare/blob/main/Screenshot%20(6122).png) |

## 🙏 Acknowledgments

- **Django Documentation**: For guiding the structure and setup.
- **Google Maps API**: For the seamless map integration.
- **Machine Learning Community**: For inspiration on model design and data preprocessing.
