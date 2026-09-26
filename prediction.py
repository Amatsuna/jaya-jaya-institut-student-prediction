import joblib
import pandas as pd


# Memuat final model
model = joblib.load("model_dropout.pkl")


def predict_student(student_data):
    """
    Melakukan prediksi status mahasiswa.

    Parameter:
        student_data (dict): Data karakteristik seorang mahasiswa.

    Return:
        str: Status mahasiswa hasil prediksi.
    """

    data = pd.DataFrame([student_data])

    prediction = model.predict(data)[0]

    # Probabilitas untuk masing-masing kelas
    probabilities = model.predict_proba(data)[0]
    classes = model.classes_

    probability = dict(zip(classes, probabilities))

    print(f"Prediksi Status: {prediction}")

    print("\nProbabilitas:")
    for status, prob in probability.items():
        print(f"- {status}: {prob:.2%}")

    return prediction


if __name__ == "__main__":

    student = {
        "Marital_status": 1,
        "Application_mode": 1,
        "Application_order": 1,
        "Course": 9500,
        "Daytime_evening_attendance": 1,
        "Previous_qualification": 1,
        "Previous_qualification_grade": 130.0,
        "Nacionality": 1,
        "Mothers_qualification": 1,
        "Fathers_qualification": 1,
        "Mothers_occupation": 9,
        "Fathers_occupation": 9,
        "Admission_grade": 130.0,
        "Displaced": 1,
        "Educational_special_needs": 0,
        "Debtor": 0,
        "Tuition_fees_up_to_date": 1,
        "Gender": 0,
        "Scholarship_holder": 0,
        "Age_at_enrollment": 19,
        "International": 0,
        "Curricular_units_1st_sem_credited": 0,
        "Curricular_units_1st_sem_enrolled": 6,
        "Curricular_units_1st_sem_evaluations": 6,
        "Curricular_units_1st_sem_approved": 5,
        "Curricular_units_1st_sem_grade": 12.0,
        "Curricular_units_1st_sem_without_evaluations": 0,
        "Unemployment_rate": 10.8,
        "Inflation_rate": 1.4,
        "GDP": 1.7
    }

    predict_student(student)