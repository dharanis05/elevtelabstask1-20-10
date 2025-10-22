# elevtelabstask1. 22-10-25

Marketing Campaign Data Cleaning

📄 Overview

This project focuses on cleaning and transforming a raw marketing campaign dataset (marketing_campaign_dirty.csv). The process ensures data consistency, integrity, and readiness for further analytics or modeling.

⚙️ Data Cleaning Steps

The cleaning script performs the following transformations:

Removes duplicate rows and columns

Formats date columns → dd-mm-yyyy

Capitalizes name fields (e.g., customer names)

Replaces ###### and missing values with column-wise averages or most frequent values

Copies “Education” and “Marital Status” columns from the original dirty dataset into the cleaned dataset

Exports the cleaned dataset → marketing_campaign_cleaned.csv → final version → marketing_campaign_final.csv

🧠 Tech Stack

Language: Python 3.x

Libraries: pandas, numpy

🏗️ How to Run

Clone the repository:

git clone https://github.com/<your-username>/marketing-data-cleaning.git
cd marketing-data-cleaning


Install dependencies:

pip install pandas numpy


Run the cleaning script:

python clean_dataset.py


The cleaned dataset will be saved as:

marketing_campaign_final.csv

📊 Files Included
File	Description
marketing_campaign_dirty.csv	Original raw dataset
marketing_campaign_cleaned.csv	Cleaned dataset (before merging Education & Marital Status)
marketing_campaign_final.csv	Final cleaned dataset
clean_dataset.py	Python cleaning script
README.md	Project documentation
🧾 License

This project is licensed under the MIT License — feel free to use and modify it.
