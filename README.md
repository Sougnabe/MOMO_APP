# MOMO APP

## Overview
MOMO APP is a full-stack application designed to process SMS data in XML format, clean and categorize the data, store it in a relational database, and provide a frontend dashboard for analysis and visualization. This project enables users to extract insights from mobile money transactions efficiently, tracking cash inflows and outflows.

🔗 Live Demo: momoapp.netlify.app  

## Table of Contents

Overview
Features
Tech Stack
Project Structure
Installation
Usage
Deployment
Authors
## Features

Data Ingestion
Extracts SMS data from XML files and parses them into a structured format.
Data Cleaning & Categorization
Uses regex to parse transaction details and categorize them (e.g., deposits, withdrawals, transfers).
Database Storage
Stores cleaned data in an SQLite relational database for easy querying and analysis.
Frontend Dashboard
Provides transaction history visualization, monthly/weekly summaries, and other analytics using HTML, CSS, and JavaScript.
Scalability
Optimized for handling large datasets, ensuring quick processing and data retrieval.
## Tech Stack

Programming Language: Python
Database: SQLite
Frontend: HTML, CSS, JavaScript
Backend: Python scripts
Data Processing: Regex for cleaning and categorization
## Project Structure

pgsql
Copy
Edit
MOMO_APP/
├── backend/
│   ├── __pycache__/
│   ├── database.py
│   ├── data_processing.py
│   ├── venv/  # Virtual environment (not typically committed)
├── database/
│   ├── momo.db  # SQLite database file
├── frontend/
│   ├── chart.js
│   ├── index.html
│   ├── script.js
│   ├── styles.css
├── logs/
│   ├── unprocessed_messages.log
├── transactions.json
├── AUTHORS
## Installation

Clone the repository

bash
Copy
Edit
git clone https://github.com/Sougnabe/MOMO_APP.git
cd MOMO_APP
Set up the backend

bash
Copy
Edit
cd backend
python -m venv venv
On Windows
bash
Copy
Edit
venv\Scripts\activate
On macOS/Linux
bash
Copy
Edit
source venv/bin/activate
Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
Set up the database

Create an SQLite database.
Update config.py with your database credentials (if needed).
Run the backend server

bash
Copy
Edit
python app.py
Set up the frontend

bash
Copy
Edit
cd ../frontend
npm install
npm start
## Usage

Upload an XML file containing MoMo transaction data.
The system processes and categorizes the data.
View transaction analytics on the dashboard.
Export data insights as reports.
## Deployment

Frontend Deployment: The frontend is deployed on Netlify.

Live URL: momoapp.netlify.app
Backend Deployment: Can be deployed on Heroku, AWS Lambda, or Google Cloud Functions (or other hosting platforms).

## Authors
This project is developed and maintained by the MOMO APP team.
