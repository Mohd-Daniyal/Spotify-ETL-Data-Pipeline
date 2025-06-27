# 🎧 Spotify End-to-End ETL Data Pipeline on AWS 🚀

This project demonstrates how to build a **serverless ETL data pipeline** using AWS services and the Spotify API. The pipeline automates data extraction, transformation, and loading of Spotify track data into an analytical layer using **Amazon Athena**.

---

## 📌 Project Objectives

✅ Extract data from the **Spotify Web API**  
✅ Store raw JSON data in **Amazon S3 (Raw Zone)**  
✅ Transform data using **AWS Glue** into clean, queryable format (Parquet/CSV)  
✅ Store processed data in **Amazon S3 (Processed Zone)**  
✅ Create a metadata layer using **AWS Glue Data Catalog**  
✅ Query the transformed data using **Amazon Athena**

---

## 🧱 Architecture Overview

![download](https://github.com/user-attachments/assets/4aa9fcca-3a55-4272-b0ad-ae7025c04990)

---

## ⚙️ Tech Stack

| Component         | Tool/Service Used           |
|------------------|-----------------------------|
| Language         | Python                      |
| API              | Spotify Web API (Spotipy)   |
| Extraction       | AWS Lambda                  |
| Storage          | Amazon S3                   |
| Transformation   | AWS Glue        |
| Metadata Layer   | AWS Glue Data Catalog       |
| Query Engine     | Amazon Athena               |

---

## 📁 S3 Bucket Structure

```

s3://spotify-etl/
│
├── raw_data/
│   └── processed/
│   └── to_processed/                 
│
└── transformed_data/
    └── albums_data/
    └── artist_data/
    └── songs_data/          

```

## ✅ Future Scope

- [ ] Integrate Power BI for visualization  
- [ ] Add orchestration using AWS Step Functions or Airflow  
- [ ] Add historical data tracking (delta loads)

---

## ⭐️ Star this repo if you're learning cloud ETL!
