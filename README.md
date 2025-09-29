# Rainfall-predictor
🌧️ Rainfall Predictor

Predict whether it will rain based on weather conditions like pressure, dew point, humidity, cloud cover, sunshine, wind direction, and wind speed.

This project combines machine learning (Random Forest & Logistic Regression) with a Streamlit web app to make predictions in real time.

🚀 Why this project?

Accurate weather prediction can be critical for farmers, disaster management, and daily planning but if the model is good enough hahah i hust tried this one for practiced below i explained how this could be improved.
Instead of building a black-box model, I explored:

How different models (Random Forest vs Logistic Regression) perform.

The effect of data imbalance & feature scaling.

How to make predictions accessible via a simple web interface.

⚙️ How it Works

Data preprocessing

Cleaned weather dataset (pressure, dewpoint, humidity, etc.)

Handled skewed distributions (tested scaling, didn’t scale Random Forest).

Split into train/test sets.

Model training

Tuned Random Forest hyperparameters with RandomizedSearchCV.

Tuned Logistic Regression with penalty types (l1, elasticnet) + solver (saga).

Evaluated using cross-validation, confusion matrix, and classification report.

Web app

Built in Streamlit.

User inputs weather features.

App predicts if it will rain (1) or not rain (0).

📊 Results

Random Forest generally achieved higher accuracy and recall than Logistic Regression.

Logistic Regression required careful scaling; Random Forest handled raw features better.

Cross-validation showed consistent scores across folds, confirming stability.

Example (LogReg tuned):

Accuracy: 68%  
Precision (Rain): 65%  
Recall (Rain): 74%  


Random Forest was typically more robust in recall (catching rainy days).

🖥️ Running the Project
1️⃣ Clone the repo
git clone https://github.com/YOUR-USERNAME/rainfall-predictor.git
cd rainfall-predictor

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit app
streamlit run app.py


The app will launch in your browser at http://localhost:8501.

📂 Project Structure
rainfall-predictor/
│── app.py                  # Streamlit frontend
│── training.ipynb          # Colab notebook (model training + tuning)
│── requirements.txt        # Dependencies
│── README.md               # Documentation
│── .gitignore              # Ignore model files, cache, checkpoints

🔮 Next Steps

the dataset was a bit small so the accuracy was not great i tried diffrent models here but randomforest here which was better than the others
- next possible step could be to gather huge dataset from hugging face and use deeplearning models
- also you can get weather data from nasa or whatever publicaly availble dataset and train a domain specfic model on that or you can use RAG application

Deploy to Streamlit Cloud so others can use the app online.





👉 This README shows:

Motivation behind the project.

Exact workflow.

Results and what they mean.

Future improvements.

How someone can run your project.
