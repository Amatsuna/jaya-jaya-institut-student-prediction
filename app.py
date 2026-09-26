import os

import streamlit as st
import pandas as pd
import joblib


# ==========================================================
# MEMUAT MODEL
# ==========================================================

model = joblib.load("model_dropout.pkl")


# ==========================================================
# KONFIGURASI HALAMAN
# ==========================================================

st.set_page_config(
    page_title="Prediksi Status Mahasiswa",
    page_icon="🎓",
    layout="wide"
)


# ==========================================================
# LOGO DAN JUDUL
# ==========================================================

logo_path = "logo_jaya_jaya_institut.png"

if os.path.exists(logo_path):
    st.image(logo_path, width=120)

st.title("🎓 Prediksi Status Mahasiswa")
st.write(
    "Aplikasi ini digunakan untuk memprediksi status mahasiswa "
    "berdasarkan karakteristik dan performa akademik semester pertama."
)

st.divider()


# ==========================================================
# MAPPING DATA KATEGORIK
# ==========================================================

marital_options = {
    "Single": 1,
    "Married": 2,
    "Widower": 3,
    "Divorced": 4,
    "Facto union": 5,
    "Legally separated": 6
}

application_mode_options = {
    "1st phase - general contingent": 1,
    "Ordinance No. 612/93": 2,
    "1st phase - special contingent (Azores Island)": 5,
    "Holders of other higher courses": 7,
    "Ordinance No. 854-B/99": 10,
    "International student (bachelor)": 15,
    "1st phase - special contingent (Madeira Island)": 16,
    "2nd phase - general contingent": 17,
    "3rd phase - general contingent": 18,
    "Ordinance No. 533-A/99, item b2) (Different Plan)": 26,
    "Ordinance No. 533-A/99, item b3) (Other Institution)": 27,
    "Over 23 years old": 39,
    "Transfer": 42,
    "Change of course": 43,
    "Technological specialization diploma holders": 44,
    "Change of institution/course": 51,
    "Short cycle diploma holders": 53,
    "Change of institution/course (International)": 57
}

application_order_options = {
    "First choice": 0,
    "Second choice": 1,
    "Third choice": 2,
    "Fourth choice": 3,
    "Fifth choice": 4,
    "Sixth choice": 5,
    "Seventh choice": 6,
    "Eighth choice": 7,
    "Ninth choice": 8,
    "Last choice": 9
}

course_options = {
    "Biofuel Production Technologies": 33,
    "Animation and Multimedia Design": 171,
    "Social Service (evening attendance)": 8014,
    "Agronomy": 9003,
    "Communication Design": 9070,
    "Veterinary Nursing": 9085,
    "Informatics Engineering": 9119,
    "Equinculture": 9130,
    "Management": 9147,
    "Social Service": 9238,
    "Tourism": 9254,
    "Nursing": 9500,
    "Oral Hygiene": 9556,
    "Advertising and Marketing Management": 9670,
    "Journalism and Communication": 9773,
    "Basic Education": 9853,
    "Management (evening attendance)": 9991
}

attendance_options = {
    "Daytime": 1,
    "Evening": 0
}

previous_qualification_options = {
    "Secondary education": 1,
    "Higher education - bachelor's degree": 2,
    "Higher education - degree": 3,
    "Higher education - master's": 4,
    "Higher education - doctorate": 5,
    "Frequency of higher education": 6,
    "12th year of schooling - not completed": 9,
    "11th year of schooling - not completed": 10,
    "Other - 11th year of schooling": 12,
    "10th year of schooling": 14,
    "10th year of schooling - not completed": 15,
    "Basic education 3rd cycle": 19,
    "Basic education 2nd cycle": 38,
    "Technological specialization course": 39,
    "Higher education - degree (1st cycle)": 40,
    "Professional higher technical course": 42,
    "Higher education - master (2nd cycle)": 43
}

nationality_options = {
    "Portuguese": 1,
    "German": 2,
    "Spanish": 6,
    "Italian": 11,
    "Dutch": 13,
    "English": 14,
    "Lithuanian": 17,
    "Angolan": 21,
    "Cape Verdean": 22,
    "Guinean": 24,
    "Mozambican": 25,
    "Santomean": 26,
    "Turkish": 32,
    "Brazilian": 41,
    "Romanian": 62,
    "Moldova (Republic of)": 100,
    "Mexican": 101,
    "Ukrainian": 103,
    "Russian": 105,
    "Cuban": 108,
    "Colombian": 109
}

education_level_options = {
    "Secondary education": 1,
    "Higher education - bachelor's degree": 2,
    "Higher education - degree": 3,
    "Higher education - master's": 4,
    "Higher education - doctorate": 5,
    "Frequency of higher education": 6,
    "12th year of schooling - not completed": 9,
    "11th year of schooling - not completed": 10,
    "Other - 11th year of schooling": 12,
    "10th year of schooling": 14,
    "10th year of schooling - not completed": 15,
    "Basic education 3rd cycle": 19,
    "Basic education 2nd cycle": 38,
    "Technological specialization course": 39,
    "Higher education - degree (1st cycle)": 40,
    "Professional higher technical course": 42,
    "Higher education - master (2nd cycle)": 43
}

occupation_options = {
    "Student": 0,
    "Representatives of legislative power, executive bodies and directors": 1,
    "Specialists in intellectual and scientific activities": 2,
    "Intermediate level technicians and professions": 3,
    "Administrative staff": 4,
    "Personal services, security and sales workers": 5,
    "Farmers and skilled agricultural, forestry and fishery workers": 6,
    "Skilled workers in industry, construction and crafts": 7,
    "Installation and machine operators and assembly workers": 8,
    "Unskilled workers": 9,
    "Armed forces professions": 10,
    "Other situation": 90,
    "Blank / unknown": 99,
    "Health professionals": 122,
    "Teachers": 123,
    "Information and communication technology specialists": 125,
    "Science and engineering technicians": 131,
    "Health associate professionals": 132,
    "Education technicians": 134,
    "Office workers and data processing operators": 141,
    "Accounting and financial service operators": 143,
    "Other administrative support staff": 144,
    "Personal service workers": 151,
    "Sellers": 152,
    "Personal care workers": 153,
    "Skilled construction workers": 171,
    "Skilled workers in printing, manufacturing and crafts": 173,
    "Electrical and electronic workers": 175,
    "Plant and machine operators and assemblers": 181,
    "Unskilled agricultural workers": 191,
    "Unskilled manufacturing and mining workers": 192,
    "Unskilled construction workers": 193,
    "Unskilled transport workers": 194,
    "Unskilled catering workers": 195
}

yes_no_options = {
    "No": 0,
    "Yes": 1
}

gender_options = {
    "Female": 0,
    "Male": 1
}


# ==========================================================
# DAFTAR FITUR MODEL
# ==========================================================

feature_columns = [
    "Marital_status",
    "Application_mode",
    "Application_order",
    "Course",
    "Daytime_evening_attendance",
    "Previous_qualification",
    "Previous_qualification_grade",
    "Nacionality",
    "Mothers_qualification",
    "Fathers_qualification",
    "Mothers_occupation",
    "Fathers_occupation",
    "Admission_grade",
    "Displaced",
    "Educational_special_needs",
    "Debtor",
    "Tuition_fees_up_to_date",
    "Gender",
    "Scholarship_holder",
    "Age_at_enrollment",
    "International",
    "Curricular_units_1st_sem_credited",
    "Curricular_units_1st_sem_enrolled",
    "Curricular_units_1st_sem_evaluations",
    "Curricular_units_1st_sem_approved",
    "Curricular_units_1st_sem_grade",
    "Curricular_units_1st_sem_without_evaluations",
    "Unemployment_rate",
    "Inflation_rate",
    "GDP"
]


# ==========================================================
# TAB APLIKASI
# ==========================================================

tab_individu, tab_batch, tab_panduan = st.tabs(
    [
        "👤 Prediksi Individu",
        "📂 Prediksi Batch",
        "ℹ️ Panduan"
    ]
)


# ==========================================================
# TAB 1 - PREDIKSI INDIVIDU
# ==========================================================

with tab_individu:

    st.header("Data Mahasiswa")

    col1, col2, col3 = st.columns(3)

    # ------------------------------------------------------
    # KOLOM 1
    # ------------------------------------------------------

    with col1:

        marital_status_label = st.selectbox(
            "Marital Status",
            options=list(marital_options.keys())
        )
        marital_status = marital_options[marital_status_label]

        application_mode_label = st.selectbox(
            "Application Mode",
            options=list(application_mode_options.keys())
        )
        application_mode = application_mode_options[
            application_mode_label
        ]

        application_order_label = st.selectbox(
            "Application Order",
            options=list(application_order_options.keys())
        )
        application_order = application_order_options[
            application_order_label
        ]

        course_label = st.selectbox(
            "Course",
            options=list(course_options.keys())
        )
        course = course_options[course_label]

        daytime_evening_label = st.selectbox(
            "Attendance",
            options=list(attendance_options.keys())
        )
        daytime_evening = attendance_options[
            daytime_evening_label
        ]

        previous_qualification_label = st.selectbox(
            "Previous Qualification",
            options=list(previous_qualification_options.keys())
        )
        previous_qualification = previous_qualification_options[
            previous_qualification_label
        ]

        previous_qualification_grade = st.number_input(
            "Previous Qualification Grade",
            min_value=0.0,
            max_value=200.0,
            value=130.0
        )

        nationality_label = st.selectbox(
            "Nacionality",
            options=list(nationality_options.keys())
        )
        nationality = nationality_options[nationality_label]

        mothers_qualification_label = st.selectbox(
            "Mother's Qualification",
            options=list(education_level_options.keys())
        )
        mothers_qualification = education_level_options[
            mothers_qualification_label
        ]

        fathers_qualification_label = st.selectbox(
            "Father's Qualification",
            options=list(education_level_options.keys())
        )
        fathers_qualification = education_level_options[
            fathers_qualification_label
        ]

    # ------------------------------------------------------
    # KOLOM 2
    # ------------------------------------------------------

    with col2:

        mothers_occupation_label = st.selectbox(
            "Mother's Occupation",
            options=list(occupation_options.keys())
        )
        mothers_occupation = occupation_options[
            mothers_occupation_label
        ]

        fathers_occupation_label = st.selectbox(
            "Father's Occupation",
            options=list(occupation_options.keys())
        )
        fathers_occupation = occupation_options[
            fathers_occupation_label
        ]

        admission_grade = st.number_input(
            "Admission Grade",
            min_value=0.0,
            max_value=200.0,
            value=130.0
        )

        displaced_label = st.selectbox(
            "Displaced",
            options=list(yes_no_options.keys())
        )
        displaced = yes_no_options[displaced_label]

        educational_special_needs_label = st.selectbox(
            "Educational Special Needs",
            options=list(yes_no_options.keys())
        )
        educational_special_needs = yes_no_options[
            educational_special_needs_label
        ]

        debtor_label = st.selectbox(
            "Debtor",
            options=list(yes_no_options.keys())
        )
        debtor = yes_no_options[debtor_label]

        tuition_fees_up_to_date_label = st.selectbox(
            "Tuition Fees Up To Date",
            options=list(yes_no_options.keys())
        )
        tuition_fees_up_to_date = yes_no_options[
            tuition_fees_up_to_date_label
        ]

        gender_label = st.selectbox(
            "Gender",
            options=list(gender_options.keys())
        )
        gender = gender_options[gender_label]

        scholarship_holder_label = st.selectbox(
            "Scholarship Holder",
            options=list(yes_no_options.keys())
        )
        scholarship_holder = yes_no_options[
            scholarship_holder_label
        ]

        age_at_enrollment = st.number_input(
            "Age At Enrollment",
            min_value=15,
            max_value=100,
            value=19
        )

        international_label = st.selectbox(
            "International Student",
            options=list(yes_no_options.keys())
        )
        international = yes_no_options[international_label]

    # ------------------------------------------------------
    # KOLOM 3
    # ------------------------------------------------------

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

    # ------------------------------------------------------
    # TOMBOL PREDIKSI
    # ------------------------------------------------------

    if st.button(
        "🔍 Prediksi Status Mahasiswa",
        use_container_width=True
    ):

        student_data = {
            "Marital_status": marital_status,
            "Application_mode": application_mode,
            "Application_order": application_order,
            "Course": course,
            "Daytime_evening_attendance": daytime_evening,
            "Previous_qualification": previous_qualification,
            "Previous_qualification_grade":
                previous_qualification_grade,
            "Nacionality": nationality,
            "Mothers_qualification": mothers_qualification,
            "Fathers_qualification": fathers_qualification,
            "Mothers_occupation": mothers_occupation,
            "Fathers_occupation": fathers_occupation,
            "Admission_grade": admission_grade,
            "Displaced": displaced,
            "Educational_special_needs":
                educational_special_needs,
            "Debtor": debtor,
            "Tuition_fees_up_to_date":
                tuition_fees_up_to_date,
            "Gender": gender,
            "Scholarship_holder": scholarship_holder,
            "Age_at_enrollment": age_at_enrollment,
            "International": international,
            "Curricular_units_1st_sem_credited":
                curricular_units_1st_sem_credited,
            "Curricular_units_1st_sem_enrolled":
                curricular_units_1st_sem_enrolled,
            "Curricular_units_1st_sem_evaluations":
                curricular_units_1st_sem_evaluations,
            "Curricular_units_1st_sem_approved":
                curricular_units_1st_sem_approved,
            "Curricular_units_1st_sem_grade":
                curricular_units_1st_sem_grade,
            "Curricular_units_1st_sem_without_evaluations":
                curricular_units_1st_sem_without_evaluations,
            "Unemployment_rate": unemployment_rate,
            "Inflation_rate": inflation_rate,
            "GDP": gdp
        }

        data = pd.DataFrame([student_data])

        prediction = model.predict(data)[0]
        probabilities = model.predict_proba(data)[0]
        classes = model.classes_

        st.subheader("Hasil Prediksi")

        if prediction == "Dropout":
            st.error(
                f"Prediksi Status: {prediction}"
            )
        elif prediction == "Enrolled":
            st.warning(
                f"Prediksi Status: {prediction}"
            )
        else:
            st.success(
                f"Prediksi Status: {prediction}"
            )

        st.subheader("Probabilitas Prediksi")

        for status, probability in zip(
            classes,
            probabilities
        ):
            st.write(
                f"**{status}**: {probability:.2%}"
            )
            st.progress(float(probability))


# ==========================================================
# TAB 2 - PREDIKSI BATCH
# ==========================================================

with tab_batch:

    st.header("📂 Prediksi Batch Mahasiswa")

    st.write(
        "Gunakan fitur ini untuk melakukan prediksi terhadap "
        "beberapa mahasiswa sekaligus menggunakan file CSV atau Excel."
    )

    st.info(
        "File harus berisi 30 kolom fitur yang digunakan oleh model. "
        "Satu baris mewakili satu mahasiswa."
    )

    # ------------------------------------------------------
    # TEMPLATE DATA
    # ------------------------------------------------------

    template_data = pd.DataFrame(columns=feature_columns)

    csv_template = template_data.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download Template CSV",
        data=csv_template,
        file_name="template_prediksi_mahasiswa.csv",
        mime="text/csv"
    )

    st.divider()

    uploaded_file = st.file_uploader(
        "Upload file CSV atau Excel",
        type=["csv", "xlsx"]
    )

    if uploaded_file is not None:

        try:

            file_extension = uploaded_file.name.lower()

            if file_extension.endswith(".csv"):
                batch_data = pd.read_csv(uploaded_file)

            elif file_extension.endswith(".xlsx"):
                batch_data = pd.read_excel(uploaded_file)

            else:
                st.error(
                    "Format file tidak didukung."
                )
                st.stop()

            # --------------------------------------------------
            # JIKA ADA KOLOM STATUS, HAPUS DARI INPUT
            # --------------------------------------------------

            if "Status" in batch_data.columns:
                batch_data = batch_data.drop(
                    columns=["Status"]
                )

            # --------------------------------------------------
            # VALIDASI KOLOM
            # --------------------------------------------------

            missing_columns = [
                column
                for column in feature_columns
                if column not in batch_data.columns
            ]

            extra_columns = [
                column
                for column in batch_data.columns
                if column not in feature_columns
            ]

            if missing_columns:

                st.error(
                    "File tidak dapat diproses karena "
                    "terdapat kolom yang belum tersedia."
                )

                st.write("Kolom yang belum tersedia:")

                for column in missing_columns:
                    st.write(f"- `{column}`")

            else:

                if extra_columns:

                    st.warning(
                        "Kolom tambahan akan diabaikan:"
                    )

                    for column in extra_columns:
                        st.write(f"- `{column}`")

                # --------------------------------------------------
                # URUTKAN KOLOM SESUAI MODEL
                # --------------------------------------------------

                prediction_data = batch_data[
                    feature_columns
                ].copy()

                # --------------------------------------------------
                # KONVERSI DATA NUMERIK
                # --------------------------------------------------

                for column in feature_columns:

                    prediction_data[column] = pd.to_numeric(
                        prediction_data[column],
                        errors="coerce"
                    )

                invalid_rows = prediction_data.isnull().any(
                    axis=1
                )

                if invalid_rows.any():

                    invalid_count = int(
                        invalid_rows.sum()
                    )

                    st.error(
                        f"Terdapat {invalid_count} baris "
                        "yang memiliki data kosong atau "
                        "tidak dapat dibaca sebagai angka."
                    )

                else:

                    # ----------------------------------------------
                    # PREDIKSI BATCH
                    # ----------------------------------------------

                    predictions = model.predict(
                        prediction_data
                    )

                    probabilities = model.predict_proba(
                        prediction_data
                    )

                    classes = list(model.classes_)

                    result_data = batch_data.copy()

                    result_data["Predicted_Status"] = (
                        predictions
                    )

                    for index, class_name in enumerate(
                        classes
                    ):

                        result_data[
                            f"Probability_{class_name}"
                        ] = probabilities[:, index]

                    # ----------------------------------------------
                    # HASIL
                    # ----------------------------------------------

                    st.success(
                        f"Berhasil memproses "
                        f"{len(result_data)} mahasiswa."
                    )

                    st.subheader(
                        "Hasil Prediksi"
                    )

                    st.dataframe(
                        result_data,
                        use_container_width=True
                    )

                    # ----------------------------------------------
                    # RINGKASAN
                    # ----------------------------------------------

                    st.subheader(
                        "Ringkasan Hasil"
                    )

                    status_counts = (
                        result_data[
                            "Predicted_Status"
                        ]
                        .value_counts()
                    )

                    summary_col1, summary_col2, summary_col3 = (
                        st.columns(3)
                    )

                    with summary_col1:
                        st.metric(
                            "Total Mahasiswa",
                            len(result_data)
                        )

                    with summary_col2:
                        st.metric(
                            "Prediksi Dropout",
                            int(
                                status_counts.get(
                                    "Dropout",
                                    0
                                )
                            )
                        )

                    with summary_col3:
                        st.metric(
                            "Prediksi Graduate",
                            int(
                                status_counts.get(
                                    "Graduate",
                                    0
                                )
                            )
                        )

                    # ----------------------------------------------
                    # DOWNLOAD HASIL
                    # ----------------------------------------------

                    result_csv = result_data.to_csv(
                        index=False
                    ).encode("utf-8")

                    st.download_button(
                        label="⬇️ Download Hasil Prediksi CSV",
                        data=result_csv,
                        file_name=(
                            "hasil_prediksi_mahasiswa.csv"
                        ),
                        mime="text/csv",
                        use_container_width=True
                    )

        except Exception as error:

            st.error(
                "Terjadi kesalahan saat membaca atau "
                "memproses file."
            )

            st.code(str(error))


# ==========================================================
# TAB 3 - PANDUAN
# ==========================================================

with tab_panduan:

    st.header("ℹ️ Panduan Penggunaan")

    st.subheader("1. Prediksi Individu")

    st.write(
        "Gunakan tab **Prediksi Individu** apabila ingin "
        "memprediksi status satu mahasiswa."
    )

    st.markdown(
        """
        **Langkah penggunaan:**

        1. Isi informasi karakteristik mahasiswa.
        2. Pilih kategori yang tersedia pada menu dropdown.
        3. Isi informasi akademik semester pertama.
        4. Klik **Prediksi Status Mahasiswa**.
        5. Sistem akan menampilkan status prediksi dan probabilitas
           untuk setiap kelas.
        """
    )

    st.divider()

    st.subheader("2. Prediksi Batch")

    st.write(
        "Gunakan tab **Prediksi Batch** apabila ingin "
        "memprediksi banyak mahasiswa sekaligus."
    )

    st.markdown(
        """
        **Langkah penggunaan:**

        1. Download **Template CSV**.
        2. Isi data mahasiswa pada template tersebut.
        3. Satu baris digunakan untuk satu mahasiswa.
        4. Pastikan seluruh 30 kolom tersedia.
        5. Upload file CSV atau Excel.
        6. Sistem akan melakukan prediksi untuk seluruh baris.
        7. Hasil prediksi dapat di-download kembali dalam format CSV.
        """
    )

    st.divider()

    st.subheader("3. Format Data Batch")

    st.write(
        "File batch menggunakan nama kolom yang sama dengan "
        "fitur yang digunakan ketika membangun model."
    )

    st.code(
        "\n".join(feature_columns),
        language="text"
    )

    st.divider()

    st.subheader("4. Interpretasi Status")

    st.markdown(
        """
        - **Dropout** → mahasiswa diprediksi termasuk kategori dropout.
        - **Enrolled** → mahasiswa diprediksi masih berstatus enrolled.
        - **Graduate** → mahasiswa diprediksi termasuk kategori graduate.
        """
    )

    st.divider()

    st.subheader("5. Catatan Penggunaan")

    st.warning(
        "Hasil prediksi merupakan informasi pendukung untuk "
        "identifikasi awal dan tidak menggantikan evaluasi atau "
        "keputusan akademik oleh pihak institusi."
    )