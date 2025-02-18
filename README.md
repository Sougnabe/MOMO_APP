# MOMO APP

## Overview
Our MoMo APP is a full-stack application designed to process SMS data in XML format, clean and categorize the data, store it in a relational database, and provide a frontend dashboard for analysis and visualization. This project enables users to extract insights from mobile money transactions efficiently.

## Features
- **Data Ingestion**: Extracts SMS data from XML format.
- **Data Cleaning & Categorization**: Parses and organizes transaction details.
- **Database Storage**: Stores structured data in a relational database.
- **Frontend Dashboard**: Provides visual insights and analytics.
- **Efficient Processing**: Optimized for handling large datasets.
## Additional
## User Authentication & Role Management
- **Feature**: Implement user authentication to allow different access levels (admin, user).
- **Purpose**: This can help secure sensitive transaction data and provide users with role-based access to different features (e.g., admins can upload and delete data, while regular users can only view analytics).

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

