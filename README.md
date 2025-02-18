# MOMO APP

## Overview
A full-stack application designed to process SMS data in XML format, clean and categorize the data, store it in a relational database, and provide a frontend dashboard for analysis and visualization. This project enables users to extract insights from mobile money transactions efficiently, tracking cash inflows and outflows.
Table of Contents
Overview
Features
Tech Stack
Project Structure
Installation
Usage
Database Setup
Deployment
Authors

Overview
MOMO Data Analysis processes XML-based SMS transaction data, applies regex for data cleaning, categorizes each transaction, and stores the results in an SQLite database. A frontend dashboard (using HTML/CSS/JavaScript) provides insightful visualizations and analytics, helping users understand their financial inflows and outflows at a glance.

Features
Data Ingestion

Extracts SMS data from XML files and parses them into a structured format.
Data Cleaning & Categorization

Uses regex to parse transaction details and categorize them (e.g., deposits, withdrawals, transfers).
Database Storage

Stores cleaned data in a relational SQLite database for easy querying and analysis.
Frontend Dashboard

Visualizes transaction history, monthly/weekly summaries, and other analytics using HTML/CSS/JavaScript.
Scalability

Optimized for handling large datasets, ensuring quick processing and data retrieval.

Tech Stack
Programming Language: Python 
Database: SQLite
Frontend: HTML, CSS, JavaScript
Backend: Python scripts 
Data Processing: Regex for cleaning/categorization

 ## Data Import Options
- **Feature**: Provide alternative ways to ingest data, such as uploading CSV files or connecting to APIs that provide mobile money transaction data.
- **Purpose**: Improve flexibility by allowing users to upload data in various formats and automate data import processes.

## Technologies Used
- **Backend**: Python
- **Frontend**: JavaScript
- **Database**: SQLITE
- **Data Processing**:Regex

## Installation

### Prerequisites
Ensure you have the following installed:
- Python3
- JAVASCRIPT
- QLITE

### Steps
1. **Clone the repository:**
   ```sh
   git clone https://github.com/Sougnabe/MOMO_APP.git
   cd MOMO_APP
   ```

2. **Set up the backend:**
   ```sh
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Set up the database:**
   - Create a database in SQLITE
   - Update `config.py` with your database credentials.

4. **Run the backend server:**
   ```sh
   python app.py
   ```

5. **Set up the frontend:**
   ```sh
   cd frontend
   npm install
   npm start
   ```

## Usage
1. Upload an XML file containing MoMo transaction data.
2. The system processes and categorizes the data.
3. View transaction analytics on the dashboard.
4. Export data insights as reports.

