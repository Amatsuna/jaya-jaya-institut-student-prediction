import streamlit as st
import pandas as pd
import joblib

# Memuat model
model = joblib.load("model_dropout.pkl")

# Konfigurasi halaman
st.set_page_config(
    page_title="Prediksi Status Mahasiswa",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Prediksi Status Mahasiswa")
st.write(
    "Aplikasi ini digunakan untuk memprediksi status mahasiswa "
    "berdasarkan karakteristik dan performa akademik semester pertama."
)

st.divider()

# Input data mahasiswa
st.header("Data Mahasiswa")

col1, col2, col3 = st.columns(3)

with col1:
    marital_status = st.number_input(
        "Marital Status",
        min_value=1,
        max_value=6,
        value=1
    )

    application_mode = st.number_input(
        "Application Mode",
        min_value=1,
        max_value=60,
        value=1
    )

    application_order = st.number_input(
        "Application Order",
        min_value=0,
        max_value=9,
        value=1
    )

    course = st.number_input(
        "Course",
        min_value=1,
        max_value=10000,
        value=9500
    )

    daytime_evening = st.number_input(
        "Daytime/Evening Attendance",
        min_value=0,
        max_value=1,
        value=1
    )

    previous_qualification = st.number_input(
        "Previous Qualification",
        min_value=1,
        max_value=50,
        value=1
    )

    previous_qualification_grade = st.number_input(
        "Previous Qualification Grade",
        min_value=0.0,
        max_value=200.0,
        value=130.0
    )

    nationality = st.number_input(
        "Nacionality",
        min_value=1,
        max_value=110,
        value=1
    )

    mothers_qualification = st.number_input(
        "Mother's Qualification",
        min_value=1,
        max_value=50,
        value=1
    )

    fathers_qualification = st.number_input(
        "Father's Qualification",
        min_value=1,
        max_value=50,
        value=1
    )

with col2:
    mothers_occupation = st.number_input(
        "Mother's Occupation",
        min_value=0,
        max_value=200,
        value=9
    )

    fathers_occupation = st.number_input(
        "Father's Occupation",
        min_value=0,
        max_value=200,
        value=9
    )

    admission_grade = st.number_input(
        "Admission Grade",
        min_value=0.0,
        max_value=200.0,
        value=130.0
    )

    displaced = st.number_input(
        "Displaced",
        min_value=0,
        max_value=1,
        value=1
    )

    educational_special_needs = st.number_input(
        "Educational Special Needs",
        min_value=0,
        max_value=1,
        value=0
    )

    debtor = st.number_input(
        "Debtor",
        min_value=0,
        max_value=1,
        value=0
    )

    tuition_fees_up_to_date = st.number_input(
        "Tuition Fees Up To Date",
        min_value=0,
        max_value=1,
        value=1
    )

    gender = st.number_input(
        "Gender",
        min_value=0,
        max_value=1,
        value=0
    )

    scholarship_holder = st.number_input(
        "Scholarship Holder",
        min_value=0,
        max_value=1,
        value=0
    )

    age_at_enrollment = st.number_input(
        "Age At Enrollment",
        min_value=15,
        max_value=100,
        value=19
    )

    international = st.number_input(
        "International",
        min_value=0,
        max_value=1,
        value=0
    )

with col3:
    curricular_units_1st_sem_credited = st.number_input(
        "1st Sem - Units Credited",
        min_value=0,
        max_value=30,
        value=0
    )

    curricular_units_1st_sem_enrolled = st.number_input(
        "1st Sem - Units Enrolled",
        min_value=0,
        max_value=30,
        value=6
    )

    curricular_units_1st_sem_evaluations = st.number_input(
        "1st Sem - Units Evaluated",
        min_value=0,
        max_value=30,
        value=6
    )

    curricular_units_1st_sem_approved = st.number_input(
        "1st Sem - Units Approved",
        min_value=0,
        max_value=30,
        value=5
    )

    curricular_units_1st_sem_grade = st.number_input(
        "1st Sem - Grade",
        min_value=0.0,
        max_value=20.0,
        value=12.0
    )

    curricular_units_1st_sem_without_evaluations = st.number_input(
        "1st Sem - Without Evaluations",
        min_value=0,
        max_value=30,
        value=0
    )

    unemployment_rate = st.number_input(
        "Unemployment Rate",
        min_value=-20.0,
        max_value=30.0,
        value=10.8
    )

    inflation_rate = st.number_input(
        "Inflation Rate",
        min_value=-20.0,
        max_value=20.0,
        value=1.4
    )

    gdp = st.number_input(
        "GDP",
        min_value=-20.0,
        max_value=20.0,
        value=1.7
    )

st.divider()

# Tombol prediksi
if st.button("🔍 Prediksi Status Mahasiswa", use_container_width=True):

    student_data = {
        "Marital_status": marital_status,
        "Application_mode": application_mode,
        "Application_order": application_order,
        "Course": course,
        "Daytime_evening_attendance": daytime_evening,
        "Previous_qualification": previous_qualification,
        "Previous_qualification_grade": previous_qualification_grade,
        "Nacionality": nationality,
        "Mothers_qualification": mothers_qualification,
        "Fathers_qualification": fathers_qualification,
        "Mothers_occupation": mothers_occupation,
        "Fathers_occupation": fathers_occupation,
        "Admission_grade": admission_grade,
        "Displaced": displaced,
        "Educational_special_needs": educational_special_needs,
        "Debtor": debtor,
        "Tuition_fees_up_to_date": tuition_fees_up_to_date,
        "Gender": gender,
        "Scholarship_holder": scholarship_holder,
        "Age_at_enrollment": age_at_enrollment,
        "International": international,
        "Curricular_units_1st_sem_credited": curricular_units_1st_sem_credited,
        "Curricular_units_1st_sem_enrolled": curricular_units_1st_sem_enrolled,
        "Curricular_units_1st_sem_evaluations": curricular_units_1st_sem_evaluations,
        "Curricular_units_1st_sem_approved": curricular_units_1st_sem_approved,
        "Curricular_units_1st_sem_grade": curricular_units_1st_sem_grade,
        "Curricular_units_1st_sem_without_evaluations": curricular_units_1st_sem_without_evaluations,
        "Unemployment_rate": unemployment_rate,
        "Inflation_rate": inflation_rate,
        "GDP": gdp
    }

    data = pd.DataFrame([student_data])

    prediction = model.predict(data)[0]
    probabilities = model.predict_proba(data)[0]
    classes = model.classes_

    probability_df = pd.DataFrame({
        "Status": classes,
        "Probabilitas": probabilities
    })

    st.subheader("Hasil Prediksi")

    if prediction == "Dropout":
        st.error(f"Prediksi Status: {prediction}")
    elif prediction == "Enrolled":
        st.warning(f"Prediksi Status: {prediction}")
    else:
        st.success(f"Prediksi Status: {prediction}")

    st.subheader("Probabilitas Prediksi")

    for status, probability in zip(classes, probabilities):
        st.write(f"**{status}**: {probability:.2%}")
        st.progress(float(probability))