# Proyek Akhir: Menyelesaikan Permasalahan Jaya Jaya Institut

## Business Understanding

Jaya Jaya Institut merupakan institusi pendidikan tinggi yang berdiri sejak tahun 2000 dan telah menghasilkan banyak lulusan. Namun, institusi juga menghadapi permasalahan berupa mahasiswa yang tidak menyelesaikan pendidikannya atau mengalami dropout. Kondisi tersebut menjadi perhatian karena dapat memengaruhi keberhasilan mahasiswa dalam menyelesaikan pendidikan.

Untuk membantu menangani permasalahan tersebut, data karakteristik mahasiswa serta performa akademik dapat digunakan untuk memahami pola yang berkaitan dengan status mahasiswa. Proyek ini berfokus pada analisis data mahasiswa dan pembangunan model machine learning yang dapat membantu memprediksi status mahasiswa berdasarkan data yang tersedia.

Dengan adanya prediksi tersebut, institusi dapat memperoleh informasi pendukung untuk mengidentifikasi mahasiswa yang memiliki kemungkinan mengalami dropout sehingga dapat menjadi bahan pertimbangan dalam pemberian bimbingan atau pendampingan lebih awal.

### Permasalahan Bisnis

Permasalahan yang ingin diselesaikan dalam proyek ini adalah:

1. Bagaimana kondisi dan karakteristik mahasiswa berdasarkan data yang tersedia?
2. Faktor apa saja yang menunjukkan pola berbeda antara mahasiswa yang berstatus Dropout, Enrolled, dan Graduate?
3. Bagaimana hubungan karakteristik mahasiswa dan performa akademik semester pertama dengan status mahasiswa?
4. Bagaimana membangun model machine learning yang dapat memprediksi status mahasiswa?
5. Model machine learning mana yang memberikan performa yang sesuai berdasarkan hasil evaluasi pada data pengujian?

### Cakupan Proyek

Cakupan proyek meliputi:

1. Mengambil dataset students' performance dari sumber dataset yang telah disediakan oleh Dicoding.
2. Melakukan data understanding untuk memahami struktur, tipe data, distribusi nilai, unique values, missing values, dan duplikasi data.
3. Melakukan data preparation, termasuk menentukan fitur dan target, memilih fitur yang tersedia untuk deteksi lebih awal, membagi data menjadi training dan testing, serta melakukan preprocessing data.
4. Melakukan Exploratory Data Analysis (EDA) untuk memahami distribusi data dan hubungan beberapa variabel dengan status mahasiswa.
5. Membangun dan membandingkan tiga model klasifikasi:
   - Logistic Regression
   - Decision Tree
   - Random Forest
6. Mengevaluasi performa model menggunakan Accuracy, Precision, Recall, F1-Score, Macro F1-Score, Confusion Matrix, dan Classification Report.
7. Menentukan model final berdasarkan hasil evaluasi pada data pengujian.
8. Menyimpan model final dalam format `.pkl`.
9. Membuat script `prediction.py` untuk melakukan prediksi terhadap data mahasiswa baru menggunakan model yang telah disimpan.
10. Membuat sistem machine learning menggunakan Streamlit untuk menyediakan antarmuka prediksi status mahasiswa.
11. Menyediakan `requirements.txt` agar environment proyek dapat dipersiapkan kembali.


### Persiapan
1. Sumber dataset

https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance
Dataset students' performance yang digunakan dalam proyek ini berasal dari repository dataset Dicoding.

2. Struktur File

Proyek Menyelesaikan Permasalahan Jaya Jaya Institut/
├── notebook.ipynb
├── prediction.py
├── app.py
├── model_dropout.pkl
├── requirements.txt
└── README.md
└── ulum_al_hikam-dashboard.png

3. Library yang digunakan:

pandas==3.0.6
numpy==2.5.3
matplotlib==3.11.2
seaborn==0.13.2
scikit-learn==1.9.1
scipy==1.18.1
joblib==1.6.0
streamlit==1.64.0

4. Setup Environment - Anaconda

Pastikan Anaconda sudah terpasang pada komputer. Kemudian buka Anaconda Prompt dan jalankan perintah berikut untuk membuat environment baru:
conda create --name main-ds python=3.9
conda activate main-ds

Setelah environment berhasil dibuat dan diaktifkan, instal seluruh dependency proyek menggunakan:
pip install -r requirements.txt

5. Setup Environment - Shell/Termina:

Instal Pipenv dengan perintah:
pip install pipenv

Kemudian jalankan perintah berikut:
pipenv install
pipenv shell

Setelah environment aktif, instal seluruh dependency proyek menggunakan:
pip install -r requirements.txt

6. Menjalankan Prediction Script

Setelah seluruh dependency terpasang dan file model_dropout.pkl tersedia, prediction script dapat dijalankan menggunakan:
python prediction.py

Script tersebut akan menerima data mahasiswa contoh dan menampilkan hasil prediksi status mahasiswa beserta probabilitas untuk setiap kelas.


## Business Dashboard (BELUM)
Business Dashboard pada proyek ini dibuat menggunakan Google Looker Studio untuk menampilkan analisis karakteristik mahasiswa dan status akademik.
Link dashboard: https://datastudio.google.com/reporting/63177695-9c15-41cb-82ee-8e6f0c11d800

## Menjalankan Sistem Aplikasi Steamlit Machine Learning

Setelah seluruh dependency terpasang dan file model_dropout.pkl tersedia, dashboard dapat dijalankan menggunakan perintah:
python -m streamlit run app.py

Setelah perintah dijalankan, Streamlit akan menjalankan aplikasi dan memberikan alamat lokal untuk mengakses aplikasi melalui browser.
aplikasi digunakan untuk memasukkan karakteristik mahasiswa dan performa akademik semester pertama, kemudian menampilkan hasil prediksi status mahasiswa berupa:
- Dropout
- Enrolled
- Graduate
aplikasi juga menampilkan probabilitas dari masing-masing status berdasarkan hasil prediksi model.

## Conclusion

Berdasarkan hasil Data Understanding dan Exploratory Data Analysis (EDA), dataset students' performance yang digunakan dalam proyek ini terdiri dari 4.424 data mahasiswa dengan 37 kolom. Dataset memiliki tiga kategori pada target `Status`, yaitu `Dropout`, `Enrolled`, dan `Graduate`. Berdasarkan distribusi target, terdapat 2.209 mahasiswa berstatus Graduate, 1.421 mahasiswa berstatus Dropout, dan 794 mahasiswa berstatus Enrolled.

Pada tahap Data Preparation, digunakan 30 fitur yang terdiri dari karakteristik mahasiswa, informasi penerimaan, kondisi sosial dan finansial, serta performa akademik semester pertama. Fitur yang berkaitan dengan semester kedua tidak digunakan karena proyek ini diarahkan untuk melakukan prediksi berdasarkan informasi yang tersedia lebih awal.

Hasil Exploratory Data Analysis menunjukkan adanya perbedaan pola pada beberapa karakteristik mahasiswa berdasarkan statusnya. Perbedaan tersebut dapat diamati melalui variabel karakteristik mahasiswa, kondisi finansial, serta performa akademik semester pertama. Beberapa variabel akademik semester pertama juga menunjukkan pola yang berbeda berdasarkan status mahasiswa. Hasil EDA bersifat deskriptif sehingga pola yang ditemukan tidak dapat digunakan untuk menyimpulkan hubungan sebab-akibat.

Untuk membangun model prediksi, tiga algoritma klasifikasi dibandingkan, yaitu Logistic Regression, Decision Tree, dan Random Forest. Evaluasi dilakukan menggunakan Accuracy, Precision, Recall, F1-Score, dan Macro F1-Score pada data pengujian.

Hasil evaluasi adalah sebagai berikut:

| Model | Accuracy | Precision | Recall | F1-Score | Macro F1-Score |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.7401 | 0.7202 | 0.7401 | 0.7252 | 0.6514 |
| Decision Tree | 0.6576 | 0.6641 | 0.6576 | 0.6607 | 0.5966 |
| Random Forest | 0.7141 | 0.6790 | 0.7141 | 0.6837 | 0.5938 |

Berdasarkan hasil pengujian pada dataset ini, Logistic Regression memperoleh nilai Accuracy, Precision, Recall, F1-Score, dan Macro F1-Score yang lebih tinggi dibandingkan Decision Tree dan Random Forest. Oleh karena itu, Logistic Regression digunakan sebagai model final dalam proyek ini.

Model Logistic Regression memperoleh Accuracy sebesar 74,01% dengan F1-Score weighted sebesar 72,52%. Pada evaluasi per kelas, model memiliki performa yang berbeda untuk setiap status. Untuk kelas `Graduate`, model memperoleh recall sebesar 89%, sedangkan untuk kelas `Dropout` memperoleh recall sebesar 75%. Sementara itu, kelas `Enrolled` memiliki recall sebesar 30%, sehingga model masih memiliki keterbatasan dalam mengidentifikasi mahasiswa yang termasuk dalam kategori tersebut.

Confusion Matrix menunjukkan bahwa model mampu mengidentifikasi sebagian besar mahasiswa pada kelas `Graduate` dan `Dropout`, tetapi masih terdapat kesalahan prediksi terutama pada kelas `Enrolled`. Hal ini menunjukkan bahwa distribusi kelas yang tidak seimbang serta karakteristik antarstatus yang dapat memiliki kemiripan masih menjadi tantangan dalam proses klasifikasi.

Dengan demikian, model yang dibangun dapat digunakan sebagai prototype untuk membantu memberikan informasi pendukung mengenai status mahasiswa berdasarkan karakteristik dan performa akademik semester pertama. Hasil prediksi sebaiknya digunakan sebagai salah satu bahan pertimbangan dalam proses identifikasi mahasiswa yang membutuhkan perhatian lebih lanjut dan tidak digunakan sebagai satu-satunya dasar dalam menentukan tindakan terhadap mahasiswa.

### Rekomendasi Action Items (Optional)

Berdasarkan hasil analisis dan model yang telah dibangun, beberapa hal yang dapat menjadi perhatian Jaya Jaya Institut adalah:

- Menggunakan hasil prediksi sebagai informasi pendukung untuk mengidentifikasi mahasiswa yang berpotensi mengalami dropout.
- Memberikan perhatian lebih lanjut kepada mahasiswa yang menunjukkan pola akademik semester pertama yang berkaitan dengan status Dropout pada dataset.
- Melakukan pendampingan atau evaluasi lebih lanjut terhadap mahasiswa yang teridentifikasi memiliki risiko dropout.
- Mengembangkan model dengan data akademik dan karakteristik mahasiswa terbaru agar performa model dapat terus dievaluasi.
- Melakukan evaluasi model secara berkala, terutama terhadap kemampuan model dalam mendeteksi kelas `Dropout` dan `Enrolled`.
- Mempertimbangkan pengembangan model atau teknik preprocessing tambahan apabila institusi ingin meningkatkan kemampuan model dalam menangani ketidakseimbangan kelas.


