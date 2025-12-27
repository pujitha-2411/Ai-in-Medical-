# 🏥 Smart Health AI Assistant

An advanced AI-powered disease prediction system built with Streamlit that helps assess health risks for multiple diseases using machine learning models.

## 🌟 Features

- **5 Disease Predictions:**
  - 💉 Diabetes Prediction
  - ❤️ Heart Disease Prediction
  - 🧠 Parkinson's Disease Detection
  - 🫁 Lung Cancer Risk Assessment
  - 🦋 Hypo-Thyroid Detection

- **Modern UI/UX:**
  - Clean and intuitive interface
  - Responsive design with gradient backgrounds
  - Sidebar navigation with icons
  - Organized input fields with helpful tooltips
  - Color-coded prediction results
  - Expandable sections for complex inputs

- **User-Friendly Features:**
  - Interactive dropdowns for categorical inputs
  - Input validation and default values
  - Detailed descriptions and reference ranges
  - Professional styling with custom CSS
  - Fast prediction results

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/pujitha-2411/Ai-in-Medical-.git
   cd Ai-in-Medical-
   ```

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify Models directory:**
   Ensure the `Models` folder contains all required `.sav` files:
   - diabetes_model.sav
   - heart_disease_model.sav
   - parkinsons_model.sav
   - lungs_disease_model.sav
   - Thyroid_model.sav

## 💻 Usage

1. **Run the Streamlit application:**
   ```bash
   streamlit run app.py
   ```

2. **Access the application:**
   - The app will automatically open in your default web browser
   - If not, navigate to `http://localhost:8501`

3. **Using the application:**
   - Select a disease prediction from the sidebar menu
   - Fill in the required health parameters
   - Click the prediction button to get instant results
   - Review the prediction and consult a healthcare professional if needed

## 📊 Disease Prediction Details

### 💉 Diabetes Prediction
Assesses diabetes risk based on:
- Pregnancies, Glucose levels, Blood Pressure
- Skin Thickness, Insulin levels, BMI
- Diabetes Pedigree Function, Age

### ❤️ Heart Disease Prediction
Evaluates cardiovascular health using:
- Age, Sex, Chest Pain Type
- Blood Pressure, Cholesterol levels
- ECG results, Heart Rate
- Exercise-induced parameters

### 🧠 Parkinson's Disease Detection
Analyzes voice frequency parameters:
- Fundamental frequency measures
- Jitter and Shimmer parameters
- Harmonic ratios
- Nonlinear complexity measures

### 🫁 Lung Cancer Risk Assessment
Evaluates risk factors and symptoms:
- Demographic information
- Lifestyle factors (smoking, alcohol)
- Physical indicators
- Respiratory symptoms

### 🦋 Hypo-Thyroid Detection
Checks thyroid function based on:
- Age, Sex
- Thyroid medication status
- TSH, T3, and TT4 hormone levels

## ⚠️ Important Disclaimer

This tool is designed for informational and educational purposes only. It should **NOT** be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare providers for:

- Accurate medical diagnosis
- Treatment recommendations
- Health concerns or symptoms
- Medical decisions

The predictions are based on machine learning models and may not be 100% accurate.

## 🛠️ Technical Stack

- **Framework:** Streamlit
- **Machine Learning:** Scikit-learn
- **Data Processing:** Pandas, NumPy
- **UI Components:** streamlit-option-menu
- **Language:** Python 3.8+

## 📁 Project Structure

```
Ai-in-Medical-/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── Models/                         # Pre-trained ML models
│   ├── diabetes_model.sav
│   ├── heart_disease_model.sav
│   ├── parkinsons_model.sav
│   ├── lungs_disease_model.sav
│   └── Thyroid_model.sav
├── *.csv                          # Training datasets
└── *.ipynb                        # Jupyter notebooks for model training
```

## 🎨 UI Features

- **Gradient Background:** Modern purple gradient design
- **Sidebar Navigation:** Easy access to all prediction modules
- **Card-based Layout:** Clean, organized information display
- **Responsive Design:** Works on desktop and mobile devices
- **Color-coded Results:** Green for low risk, orange for high risk
- **Tooltips & Help Text:** Guidance for every input field
- **Expandable Sections:** Organized complex inputs into logical groups

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available for educational purposes.

## 👥 Authors

- Initial development by pujitha-2411
- UI/UX revamp with Streamlit enhancement

## 🔮 Future Enhancements

- Add more disease prediction models
- Implement user authentication
- Store prediction history
- Add data visualization charts
- Multi-language support
- Export prediction reports
- Integration with wearable health devices

## 📞 Support

For issues, questions, or suggestions, please open an issue on the GitHub repository.

---

**Made with ❤️ using Streamlit**
