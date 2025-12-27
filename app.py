import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# Change Name & Logo
st.set_page_config(
    page_title="Smart Health AI Assistant", 
    page_icon="⚕️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    /* Main styling */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #2c3e50 0%, #3498db 100%);
    }
    
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
        color: white;
    }
    
    /* Card styling */
    .prediction-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
    }
    
    /* Title styling */
    .main-title {
        color: white;
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .sub-title {
        color: white;
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    /* Input field styling */
    .stTextInput > label, .stNumberInput > label, .stSelectbox > label {
        color: #2c3e50 !important;
        font-weight: 600;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        border-radius: 10px;
        width: 100%;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    
    /* Success/Error message styling */
    .success-box {
        background-color: #d4edda;
        border: 2px solid #28a745;
        border-radius: 10px;
        padding: 1rem;
        color: #155724;
        font-size: 1.2rem;
        font-weight: 600;
        text-align: center;
        margin: 1rem 0;
    }
    
    .warning-box {
        background-color: #fff3cd;
        border: 2px solid #ffc107;
        border-radius: 10px;
        padding: 1rem;
        color: #856404;
        font-size: 1.2rem;
        font-weight: 600;
        text-align: center;
        margin: 1rem 0;
    }
    
    /* Hiding Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Load the saved models with error handling
@st.cache_resource
def load_models():
    try:
        models = {
            'diabetes': pickle.load(open('Models/diabetes_model.sav', 'rb')),
            'heart_disease': pickle.load(open('Models/heart_disease_model.sav', 'rb')),
            'parkinsons': pickle.load(open('Models/parkinsons_model.sav', 'rb')),
            'lung_cancer': pickle.load(open('Models/lungs_disease_model.sav', 'rb')),
            'thyroid': pickle.load(open('Models/Thyroid_model.sav', 'rb'))
        }
        return models
    except Exception as e:
        st.error(f"Error loading models: {str(e)}")
        return None

models = load_models()

# Sidebar navigation with icons
with st.sidebar:
    st.markdown("## 🏥 Navigation")
    selected = option_menu(
        menu_title=None,
        options=['Home', 'Diabetes Prediction', 'Heart Disease Prediction', 
                'Parkinsons Prediction', 'Lung Cancer Prediction', 'Hypo-Thyroid Prediction'],
        icons=['house-fill', 'droplet-fill', 'heart-fill', 'activity', 'lungs-fill', 'thermometer-half'],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "transparent"},
            "icon": {"color": "white", "font-size": "20px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "0px",
                "color": "white",
                "--hover-color": "#667eea",
            },
            "nav-link-selected": {"background-color": "#667eea"},
        }
    )
    
    st.markdown("---")
    st.markdown("""
        <div style='color: white; text-align: center;'>
            <p><b>Smart Health AI Assistant</b></p>
            <p style='font-size: 0.9rem;'>AI-powered disease prediction system</p>
        </div>
    """, unsafe_allow_html=True)

# Home Page
if selected == 'Home':
    st.markdown("<h1 class='main-title'>🏥 Smart Health AI Assistant</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Advanced AI-powered disease prediction system for early detection and prevention</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='prediction-card'>
            <h3 style='color: #667eea; text-align: center;'>🎯 Accurate Predictions</h3>
            <p style='text-align: center;'>Machine learning models trained on extensive medical datasets for reliable predictions.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='prediction-card'>
            <h3 style='color: #667eea; text-align: center;'>⚡ Fast Results</h3>
            <p style='text-align: center;'>Get instant predictions within seconds of entering your health parameters.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='prediction-card'>
            <h3 style='color: #667eea; text-align: center;'>🔒 Secure & Private</h3>
            <p style='text-align: center;'>Your health data is processed locally and never stored or shared.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='prediction-card'>
        <h2 style='color: #2c3e50; margin-bottom: 1rem;'>📋 Available Predictions</h2>
        <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;'>
            <div style='padding: 1rem; background: #f8f9fa; border-radius: 10px;'>
                <h4 style='color: #667eea;'>💉 Diabetes</h4>
                <p>Predict diabetes risk based on glucose levels, BMI, and other health indicators.</p>
            </div>
            <div style='padding: 1rem; background: #f8f9fa; border-radius: 10px;'>
                <h4 style='color: #667eea;'>❤️ Heart Disease</h4>
                <p>Assess heart disease risk using cardiovascular health parameters.</p>
            </div>
            <div style='padding: 1rem; background: #f8f9fa; border-radius: 10px;'>
                <h4 style='color: #667eea;'>🧠 Parkinson's Disease</h4>
                <p>Detect Parkinson's disease using voice frequency analysis parameters.</p>
            </div>
            <div style='padding: 1rem; background: #f8f9fa; border-radius: 10px;'>
                <h4 style='color: #667eea;'>🫁 Lung Cancer</h4>
                <p>Evaluate lung cancer risk based on lifestyle and symptom indicators.</p>
            </div>
            <div style='padding: 1rem; background: #f8f9fa; border-radius: 10px;'>
                <h4 style='color: #667eea;'>🦋 Hypo-Thyroid</h4>
                <p>Check for thyroid disorders using thyroid hormone levels and related metrics.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='prediction-card'>
        <h2 style='color: #2c3e50; margin-bottom: 1rem;'>ℹ️ How to Use</h2>
        <ol style='font-size: 1.1rem; line-height: 2;'>
            <li>Select a disease prediction from the sidebar menu</li>
            <li>Fill in the required health parameters accurately</li>
            <li>Click the prediction button to get instant results</li>
            <li>Review the prediction and consult a healthcare professional if needed</li>
        </ol>
        <div style='background: #fff3cd; padding: 1rem; border-radius: 10px; margin-top: 1rem;'>
            <p style='color: #856404; margin: 0;'><b>⚠️ Important Disclaimer:</b> This tool is for informational purposes only and should not replace professional medical advice. Always consult with a qualified healthcare provider for diagnosis and treatment.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Diabetes Prediction Page
elif selected == 'Diabetes Prediction':
    st.markdown("<h1 class='main-title'>💉 Diabetes Prediction</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Predict diabetes risk based on health parameters</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='prediction-card'>", unsafe_allow_html=True)
    
    st.info("💡 **Tip:** Enter accurate values for the best prediction. Hover over field labels for more information.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Basic Information")
        Pregnancies = st.number_input(
            'Number of Pregnancies', 
            min_value=0, max_value=20, value=0,
            help='Number of times pregnant'
        )
        Age = st.number_input(
            'Age', 
            min_value=1, max_value=120, value=25,
            help='Age of the person in years'
        )
        BMI = st.number_input(
            'BMI (Body Mass Index)', 
            min_value=0.0, max_value=70.0, value=25.0, step=0.1,
            help='Weight in kg divided by height in meters squared'
        )
        DiabetesPedigreeFunction = st.number_input(
            'Diabetes Pedigree Function', 
            min_value=0.0, max_value=3.0, value=0.5, step=0.01,
            help='Function that represents the likelihood of diabetes based on family history'
        )
    
    with col2:
        st.markdown("#### Medical Measurements")
        Glucose = st.number_input(
            'Glucose Level (mg/dL)', 
            min_value=0, max_value=300, value=100,
            help='Plasma glucose concentration after 2 hours in an oral glucose tolerance test'
        )
        BloodPressure = st.number_input(
            'Blood Pressure (mm Hg)', 
            min_value=0, max_value=200, value=70,
            help='Diastolic blood pressure'
        )
        SkinThickness = st.number_input(
            'Skin Thickness (mm)', 
            min_value=0, max_value=100, value=20,
            help='Triceps skin fold thickness'
        )
        Insulin = st.number_input(
            'Insulin Level (mu U/ml)', 
            min_value=0, max_value=900, value=80,
            help='2-Hour serum insulin'
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button('🔍 Predict Diabetes Risk', use_container_width=True):
        if models:
            try:
                diab_prediction = models['diabetes'].predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
                if diab_prediction[0] == 1:
                    st.markdown("<div class='warning-box'>⚠️ High Risk: The person is likely to be diabetic. Please consult a healthcare professional.</div>", unsafe_allow_html=True)
                else:
                    st.markdown("<div class='success-box'>✅ Low Risk: The person is not likely to be diabetic. Maintain a healthy lifestyle!</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error during prediction: {str(e)}")
        else:
            st.error("Models not loaded properly. Please check the Models directory.")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Heart Disease Prediction Page
elif selected == 'Heart Disease Prediction':
    st.markdown("<h1 class='main-title'>❤️ Heart Disease Prediction</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Assess cardiovascular health risk</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='prediction-card'>", unsafe_allow_html=True)
    
    st.info("💡 **Tip:** Medical test results provide the most accurate predictions. Consult your recent health checkup reports.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### Personal Info")
        age = st.number_input('Age', min_value=1, max_value=120, value=50, help='Age in years')
        sex = st.selectbox('Sex', options=[0, 1], format_func=lambda x: 'Female' if x == 0 else 'Male', help='Biological sex')
        
        st.markdown("#### Blood Metrics")
        trestbps = st.number_input('Resting Blood Pressure (mm Hg)', min_value=0, max_value=300, value=120, help='Resting blood pressure on admission to the hospital')
        chol = st.number_input('Serum Cholesterol (mg/dl)', min_value=0, max_value=600, value=200, help='Serum cholesterol in mg/dl')
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes', help='Fasting blood sugar > 120 mg/dl')
    
    with col2:
        st.markdown("#### Chest Pain Type")
        cp = st.selectbox(
            'Chest Pain Type',
            options=[0, 1, 2, 3],
            format_func=lambda x: ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'][x],
            help='Type of chest pain experienced'
        )
        
        st.markdown("#### ECG Results")
        restecg = st.selectbox(
            'Resting ECG Results',
            options=[0, 1, 2],
            format_func=lambda x: ['Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy'][x],
            help='Resting electrocardiographic results'
        )
        thalach = st.number_input('Maximum Heart Rate', min_value=0, max_value=250, value=150, help='Maximum heart rate achieved')
        exang = st.selectbox('Exercise Induced Angina', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes', help='Exercise induced angina')
    
    with col3:
        st.markdown("#### Exercise Test")
        oldpeak = st.number_input('ST Depression', min_value=0.0, max_value=10.0, value=1.0, step=0.1, help='ST depression induced by exercise relative to rest')
        slope = st.selectbox(
            'ST Segment Slope',
            options=[0, 1, 2],
            format_func=lambda x: ['Upsloping', 'Flat', 'Downsloping'][x],
            help='The slope of the peak exercise ST segment'
        )
        
        st.markdown("#### Fluoroscopy")
        ca = st.selectbox('Number of Major Vessels', options=[0, 1, 2, 3], help='Number of major vessels colored by fluoroscopy')
        thal = st.selectbox(
            'Thalassemia',
            options=[0, 1, 2],
            format_func=lambda x: ['Normal', 'Fixed Defect', 'Reversible Defect'][x],
            help='Thalassemia blood disorder'
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button('🔍 Predict Heart Disease Risk', use_container_width=True):
        if models:
            try:
                heart_prediction = models['heart_disease'].predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
                if heart_prediction[0] == 1:
                    st.markdown("<div class='warning-box'>⚠️ High Risk: The person has a high risk of heart disease. Immediate medical consultation recommended.</div>", unsafe_allow_html=True)
                else:
                    st.markdown("<div class='success-box'>✅ Low Risk: The person does not have significant heart disease indicators. Continue healthy habits!</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error during prediction: {str(e)}")
        else:
            st.error("Models not loaded properly. Please check the Models directory.")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Parkinson's Prediction Page
elif selected == "Parkinsons Prediction":
    st.markdown("<h1 class='main-title'>🧠 Parkinson's Disease Prediction</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Detect Parkinson's disease using voice analysis parameters</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='prediction-card'>", unsafe_allow_html=True)
    
    st.info("💡 **Tip:** These parameters are derived from voice frequency analysis. Typically obtained from specialized medical equipment.")
    
    with st.expander("📊 Frequency Parameters", expanded=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            fo = st.number_input('MDVP:Fo(Hz)', min_value=0.0, value=150.0, step=0.1, help='Average vocal fundamental frequency')
        with col2:
            fhi = st.number_input('MDVP:Fhi(Hz)', min_value=0.0, value=200.0, step=0.1, help='Maximum vocal fundamental frequency')
        with col3:
            flo = st.number_input('MDVP:Flo(Hz)', min_value=0.0, value=100.0, step=0.1, help='Minimum vocal fundamental frequency')
    
    with st.expander("🔊 Jitter Parameters"):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            Jitter_percent = st.number_input('MDVP:Jitter(%)', min_value=0.0, value=0.005, step=0.001, format="%.5f", help='Jitter as a percentage')
        with col2:
            Jitter_Abs = st.number_input('MDVP:Jitter(Abs)', min_value=0.0, value=0.00003, step=0.00001, format="%.5f", help='Absolute jitter')
        with col3:
            RAP = st.number_input('MDVP:RAP', min_value=0.0, value=0.003, step=0.001, format="%.5f", help='Relative amplitude perturbation')
        with col4:
            PPQ = st.number_input('MDVP:PPQ', min_value=0.0, value=0.003, step=0.001, format="%.5f", help='Five-point period perturbation quotient')
        
        DDP = st.number_input('Jitter:DDP', min_value=0.0, value=0.009, step=0.001, format="%.5f", help='Average absolute difference of differences between jitter cycles')
    
    with st.expander("📈 Shimmer Parameters"):
        col1, col2, col3 = st.columns(3)
        with col1:
            Shimmer = st.number_input('MDVP:Shimmer', min_value=0.0, value=0.03, step=0.001, format="%.5f", help='Shimmer')
            Shimmer_dB = st.number_input('MDVP:Shimmer(dB)', min_value=0.0, value=0.3, step=0.01, help='Shimmer in dB')
        with col2:
            APQ3 = st.number_input('Shimmer:APQ3', min_value=0.0, value=0.015, step=0.001, format="%.5f", help='Three-point amplitude perturbation quotient')
            APQ5 = st.number_input('Shimmer:APQ5', min_value=0.0, value=0.02, step=0.001, format="%.5f", help='Five-point amplitude perturbation quotient')
        with col3:
            APQ = st.number_input('MDVP:APQ', min_value=0.0, value=0.02, step=0.001, format="%.5f", help='Amplitude perturbation quotient')
            DDA = st.number_input('Shimmer:DDA', min_value=0.0, value=0.045, step=0.001, format="%.5f", help='Average absolute difference between consecutive differences')
    
    with st.expander("🎵 Harmonic Parameters"):
        col1, col2 = st.columns(2)
        with col1:
            NHR = st.number_input('NHR', min_value=0.0, value=0.02, step=0.001, format="%.5f", help='Noise-to-harmonics ratio')
            HNR = st.number_input('HNR', min_value=0.0, value=22.0, step=0.1, help='Harmonics-to-noise ratio')
        with col2:
            RPDE = st.number_input('RPDE', min_value=0.0, value=0.5, step=0.01, help='Recurrence period density entropy')
            DFA = st.number_input('DFA', min_value=0.0, value=0.7, step=0.01, help='Detrended fluctuation analysis')
    
    with st.expander("📉 Spread & Complexity Parameters"):
        col1, col2, col3 = st.columns(3)
        with col1:
            spread1 = st.number_input('Spread1', value=-5.0, step=0.1, help='Nonlinear measure of fundamental frequency variation')
        with col2:
            spread2 = st.number_input('Spread2', value=0.2, step=0.01, help='Nonlinear measure of fundamental frequency variation')
        with col3:
            D2 = st.number_input('D2', min_value=0.0, value=2.5, step=0.1, help='Correlation dimension')
        
        PPE = st.number_input('PPE', min_value=0.0, value=0.2, step=0.01, help='Pitch period entropy')
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("🔍 Predict Parkinson's Risk", use_container_width=True):
        if models:
            try:
                parkinsons_prediction = models['parkinsons'].predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
                if parkinsons_prediction[0] == 1:
                    st.markdown("<div class='warning-box'>⚠️ High Risk: The voice analysis indicates potential Parkinson's disease. Consult a neurologist.</div>", unsafe_allow_html=True)
                else:
                    st.markdown("<div class='success-box'>✅ Low Risk: No significant Parkinson's disease indicators detected.</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error during prediction: {str(e)}")
        else:
            st.error("Models not loaded properly. Please check the Models directory.")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Lung Cancer Prediction Page
elif selected == "Lung Cancer Prediction":
    st.markdown("<h1 class='main-title'>🫁 Lung Cancer Prediction</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Assess lung cancer risk based on lifestyle and symptoms</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='prediction-card'>", unsafe_allow_html=True)
    
    st.info("💡 **Tip:** Answer all questions accurately. This assessment is based on risk factors and symptoms.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Personal Information")
        GENDER = st.selectbox('Gender', options=[0, 1], format_func=lambda x: 'Female' if x == 0 else 'Male', help='Biological sex')
        AGE = st.number_input('Age', min_value=1, max_value=120, value=50, help='Age in years')
        
        st.markdown("#### Lifestyle Factors")
        SMOKING = st.selectbox('Smoking', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes', help='Do you smoke?')
        ALCOHOL_CONSUMING = st.selectbox('Alcohol Consumption', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes', help='Do you consume alcohol regularly?')
        PEER_PRESSURE = st.selectbox('Peer Pressure', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes', help='Experience peer pressure?')
        
        st.markdown("#### Physical Indicators")
        YELLOW_FINGERS = st.selectbox('Yellow Fingers', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes', help='Do you have yellow staining on fingers?')
        CHRONIC_DISEASE = st.selectbox('Chronic Disease', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes', help='Do you have any chronic disease?')
        ALLERGY = st.selectbox('Allergy', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes', help='Do you have allergies?')
    
    with col2:
        st.markdown("#### Symptoms")
        ANXIETY = st.selectbox('Anxiety', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes', help='Do you experience anxiety?')
        FATIGUE = st.selectbox('Fatigue', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes', help='Do you experience chronic fatigue?')
        WHEEZING = st.selectbox('Wheezing', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes', help='Do you experience wheezing?')
        COUGHING = st.selectbox('Coughing', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes', help='Do you have persistent cough?')
        SHORTNESS_OF_BREATH = st.selectbox('Shortness of Breath', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes', help='Do you experience shortness of breath?')
        SWALLOWING_DIFFICULTY = st.selectbox('Swallowing Difficulty', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes', help='Do you have difficulty swallowing?')
        CHEST_PAIN = st.selectbox('Chest Pain', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes', help='Do you experience chest pain?')
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("🔍 Predict Lung Cancer Risk", use_container_width=True):
        if models:
            try:
                lungs_prediction = models['lung_cancer'].predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])
                if lungs_prediction[0] == 1:
                    st.markdown("<div class='warning-box'>⚠️ High Risk: Multiple risk factors detected. Schedule a comprehensive medical examination immediately.</div>", unsafe_allow_html=True)
                else:
                    st.markdown("<div class='success-box'>✅ Low Risk: No significant lung cancer risk factors detected. Continue healthy lifestyle choices!</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error during prediction: {str(e)}")
        else:
            st.error("Models not loaded properly. Please check the Models directory.")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Hypo-Thyroid Prediction Page
elif selected == "Hypo-Thyroid Prediction":
    st.markdown("<h1 class='main-title'>🦋 Hypo-Thyroid Prediction</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Detect thyroid disorders based on hormone levels</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='prediction-card'>", unsafe_allow_html=True)
    
    st.info("💡 **Tip:** These values come from blood tests. Check your recent thyroid function test results.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Basic Information")
        age = st.number_input('Age', min_value=1, max_value=120, value=40, help='Age in years')
        sex = st.selectbox('Sex', options=[0, 1], format_func=lambda x: 'Female' if x == 0 else 'Male', help='Biological sex')
        on_thyroxine = st.selectbox('On Thyroxine Medication', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes', help='Are you currently taking thyroxine?')
    
    with col2:
        st.markdown("#### Thyroid Hormone Levels")
        tsh = st.number_input('TSH Level (mU/L)', min_value=0.0, value=2.0, step=0.1, help='Thyroid Stimulating Hormone level')
        t3_measured = st.selectbox('T3 Measured', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes', help='Was T3 measured in the test?')
        t3 = st.number_input('T3 Level (ng/dL)', min_value=0.0, value=1.5, step=0.1, help='Triiodothyronine level')
        tt4 = st.number_input('TT4 Level (μg/dL)', min_value=0.0, value=100.0, step=1.0, help='Total Thyroxine level')
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background: #e7f3ff; padding: 1rem; border-radius: 10px; border-left: 4px solid #2196F3;'>
        <h4 style='color: #1976D2; margin-top: 0;'>📖 Reference Ranges:</h4>
        <ul style='color: #1565C0;'>
            <li><b>TSH:</b> Normal range is 0.4-4.0 mU/L</li>
            <li><b>T3:</b> Normal range is 0.8-2.0 ng/dL</li>
            <li><b>TT4:</b> Normal range is 60-120 μg/dL</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("🔍 Predict Thyroid Status", use_container_width=True):
        if models:
            try:
                thyroid_prediction = models['thyroid'].predict([[age, sex, on_thyroxine, tsh, t3_measured, t3, tt4]])
                if thyroid_prediction[0] == 1:
                    st.markdown("<div class='warning-box'>⚠️ Abnormal: Thyroid function test indicates potential hypothyroidism. Consult an endocrinologist.</div>", unsafe_allow_html=True)
                else:
                    st.markdown("<div class='success-box'>✅ Normal: Thyroid function appears to be within normal range.</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error during prediction: {str(e)}")
        else:
            st.error("Models not loaded properly. Please check the Models directory.")
    
    st.markdown("</div>", unsafe_allow_html=True)
