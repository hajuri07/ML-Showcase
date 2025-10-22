This project is a binary classification problem based on the popular Pima Indians Diabetes Dataset.
It uses Supervised Machine Learning algorithms (Logistic Regression, Random Forest, and XGBoost) to predict diabetes.
After evaluating all three models, I selected the best-performing one and built an interactive Streamlit web app that allows users to input their health details and get predictions instantly ⚡

🔥 Features

✅ End-to-end ML workflow (EDA → Model Training → Evaluation → Deployment)
✅ Multiple ML models trained and compared (Logistic Regression, Random Forest, XGBoost)
✅ Accuracy, Precision, Recall, F1-score comparison table
✅ Feature scaling using StandardScaler
✅ Model bundling using joblib for real-world reusability
✅ Interactive Streamlit web app with clean UI
✅ Instant diabetes risk prediction based on user input

🧩 Tech Stack
Category	Tools Used
Language	Python 🐍
ML Libraries	scikit-learn, XGBoost, NumPy, Pandas
Visualization	Matplotlib, Seaborn
Model Saving	joblib
Web App Framework	Streamlit
Environment	kaggle Notebook + VS Code (Anaconda)
📊 Model Development

1️⃣ Data Understanding & Cleaning

Used Pima Indians Diabetes Dataset from Kaggle

Checked null values, outliers, and feature distributions

Scaled features using StandardScaler

2️⃣ EDA (Exploratory Data Analysis)

Pairplots to visualize feature relationships

Observed that higher glucose and BMI correlated with diabetes

3️⃣ Model Training

Trained and compared:

Logistic Regression

Random Forest

XGBoost

4️⃣ Model Evaluation

Model	Accuracy	F1-Score	Precision	Recall
Logistic Regression	0.753	0.661	0.649	0.673
Random Forest	0.734	0.631	0.625	0.636
XGBoost	0.708	0.615	0.581	0.654

📈 Best Model: Logistic Regression ✅
(simple yet strong for this dataset)

5️⃣ Model Saving

Combined StandardScaler and best model into one bundle:

obj = {"scaler": scaler, "model": model}
joblib.dump(obj, "scaler_model_bundle.joblib")


6️⃣ Streamlit App
I have created a streamlit app for prediction 
you can check it online using :

🧮 Example Input

Feature	Example Value

Pregnancies	2

Glucose	130

Blood Pressure	70

Skin Thickness	25

Insulin	100

BMI	28.4

DiabetesPedigreeFunction	0.5

Age	35

Output:
✅ Non-Diabetic or ⚠️ Diabetic (with probability)


🧰 Future Improvements

🚧 Add more algorithms (like SVM, KNN)
🚧 Hyperparameter tuning with GridSearchCV
🚧 Add visual explanations (like SHAP for feature importance)
🚧 Deploy publicly using Streamlit Cloud or HuggingFace Spaces

🧑‍💻 Author

👤 Ibrahim Hajuri (Hajuri)
🎯 Aspiring Machine Learning Engineer | Data Science Enthusiast💬 LinkedIn
 • GitHub

⭐ Show Some Love
