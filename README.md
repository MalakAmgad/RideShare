

# 🚕 Taxi Fare Prediction Web Application

This project is a web application that accurately predicts the fare of a taxi ride based on pickup and dropoff locations, passenger count, and trip time details. The app is built using Django as the backend framework, with Google Maps API integration for an interactive user experience. A Jupyter notebook supports data processing and model training.

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

- **Fare Prediction**: Input pickup/dropoff locations, time, and passenger count, and receive an estimated fare.
- **Interactive Map Integration**: Allows map-based selection of locations via Google Maps API.
- **Automatic Distance & Bearing Calculation**: Dynamically computes the distance and bearing between pickup and dropoff points, and between them and nearby airports.
- **Time-Based Feature Engineering**: Automatically incorporates trip time, enhancing prediction accuracy.
- **Dynamic UI**: A responsive, user-friendly design with real-time fare prediction output.

## 🛠 Tech Stack

- **Backend**: Django 5.0.6
- **Frontend**: HTML, CSS, JavaScript, Google Maps API
- **Machine Learning**: Jupyter Notebook for data analysis, model training, and evaluation
- **Language**: Python 3.11.3

## 📊 Data and Model

The model is trained on a dataset with real-world taxi fare data, loaded and processed in a Jupyter Notebook. The notebook includes data preprocessing steps, Exploratory Data Analysis (EDA), and model training.

### Key Steps in the Notebook:
1. **Data Preprocessing**:
   - **Data Cleaning**: Handled missing values, outliers, and irrelevant data for a cleaner dataset.
   - **Feature Scaling**: Scaled numeric features to enhance model convergence.
   - **Time Feature Engineering**: Extracted day, month, hour, and weekday from timestamp data to capture temporal trends.
   
2. **Distance and Bearing Calculation**:
   - **Haversine Distance**: Calculated the great-circle distance between pickup and dropoff locations using their latitude and longitude coordinates.
   - **Bearing Calculation**: Computed bearing angles to show direction (e.g., north, south) of travel.
   - **Airport Proximity Analysis**: Included the distance between pickup/dropoff points and nearby airports (JFK, EWR, LGA, Solberg-Hunterdon) to account for fare adjustments.

3. **Exploratory Data Analysis (EDA)**:
   - Visualized relationships between fare amounts, distance, time, and other key variables.
   - Analyzed patterns related to peak times, location-based fare trends, and seasonal factors to enhance feature engineering.

4. **Model Training**:
   - **Model Selection**: Chose a Random Forest Regressor for robust and accurate fare predictions, leveraging its ability to handle complex interactions.
   - **Hyperparameter Tuning**: Fine-tuned model parameters for optimal results.
   - **Model Evaluation**: Achieved a Mean Absolute Error (MAE) of $2.90 on the test data.

## ⚙️ Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/taxi-fare-prediction.git
   cd taxi-fare-prediction
   ```

2. **Install Dependencies**:
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
   Open `Notebook6.ipynb` to review data preprocessing, model training, and adjust configurations as needed.

## 🖱️ Usage

1. **Open the Web App**:
   Access the application at `http://127.0.0.1:8000`.

2. **Enter Ride Details**:
   - Input pickup/dropoff latitude and longitude coordinates.
   - Select the passenger count, date, and time of the trip.
   - Click on **Select Pickup/Dropoff** to open an interactive map for easier selection.

3. **Get Prediction**:
   The app calculates and displays:
   - Predicted fare based on your inputs.
   - Distance and bearing between locations, including proximity to nearby airports (JFK, EWR, LGA, Solberg-Hunterdon).

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
| **Prediction Output**    | ![Prediction Output](https://github.com/MalakAmgad/RideShare/blob/main/screenshot(6122).png) |

## 🙏 Acknowledgments

- **Django Documentation**: For guiding the structure and setup.
- **Google Maps API**: For seamless map integration.
- **Machine Learning Community**: For inspiration on model design and data preprocessing.
