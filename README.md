# MOMO APP

**Overview**  
MOMO APP is a full-stack application designed to process SMS data in XML format, clean and categorize the data, store it in a relational database, and provide a frontend dashboard for analysis and visualization. This project enables users to extract insights from mobile money transactions efficiently, tracking cash inflows and outflows.

**Live Demo:** [momoapp.netlify.app](https://momoapp.netlify.app)

---

**Table of Contents**  
- [Overview](#overview)  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Project Structure](#project-structure)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Database Setup](#database-setup)  
- [Deployment](#deployment)  
- [Authors](#authors)

---

**Features**  
- **Data Ingestion**: Extracts SMS data from XML files and parses them into a structured format.  
- **Data Cleaning & Categorization**: Uses regex to parse transaction details and categorize them (e.g., deposits, withdrawals, transfers).  
- **Database Storage**: Stores cleaned data in an SQLite relational database for easy querying and analysis.  
- **Frontend Dashboard**: Provides transaction history visualization, monthly/weekly summaries, and other analytics using HTML, CSS, and JavaScript.  
- **Scalability**: Optimized for handling large datasets, ensuring quick processing and data retrieval.

---

**Tech Stack**  
- **Programming Language**: Python  
- **Database**: SQLite  
- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Python scripts  
- **Data Processing**: Regex for cleaning and categorization

---

**Project Structure**  

MOMO_APP/
├── backend/

│   ├── __pycache__/

│   ├── database.py

│   ├── data_processing.py

│   └── venv/           # Virtual environment (not typically committed)

├── database/

│   └── momo.db         # SQLite database file

├── frontend/

│   ├── chart.js

│   ├── index.html

│   ├── script.js

│   └── styles.css

├── logs/

│   └── unprocessed_messages.log

├── transactions.json

└── AUTHORS

## Installation

**Clone the repository**
git clone https://github.com/Sougnabe/MOMO_APP.git
cd MOMO_APP

**Set up the backend**
cd backend
python -m venv venv

**On Windows**
venv\Scripts\activate

**On macOS/Linux**
source venv/bin/activate

**Install dependencies**
pip install -r requirements.txt

**Usage**

1. Process and categorize MoMo transaction data.  
   The system automatically reads and processes the data from the designated source.
2. View transaction analytics on the dashboard.  
   Access visual insights, summary charts, and detailed trends.
3. Export data insights as reports.  
   Generate exportable reports for further analysis.

**Deployment**

Our website was deployed here (https://momoapp.netlify.app)

**To use our website, click [this](https://momoapp.netlify.app)**
