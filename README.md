# Cricket World Cup Points Table Project

This project involves data ingestion from CSV files, web scraping using Python, and the calculation of points tables for the ICC Cricket World Cup matches (including groups & qualifiers) for the years <b>2011-2023</b> (recently included). The project is organized into three directories, one for each World Cup year, and includes the following files:

## Directory Structure

```
├── CWC2011/
│   ├── icc_world_cup_2011.csv
│   ├── matches2011.py (Web Scraping)
│   ├── cwc2011.sql (Data Ingestion & Points Table Calculation Using SQL)
│   ├── cwc2011stats.ipynb (Points Table Calculation Using Pandas)
├── CWC2015/
│   ├── icc_world_cup_2015.csv
│   ├── matches2015.py (Web Scraping)
│   ├── cwc2015.sql (Data Ingestion & Points Table Calculation Using SQL)
│   ├── cwc2015stats.ipynb (Points Table Calculation Using Pandas)
├── CWC2019/
│   ├── icc_world_cup_2019.csv
│   ├── matches2019.py (Web Scraping)
│   ├── cwc2019.sql (Data Ingestion & Points Table Calculation Using SQL)
│   ├── cwc2019stats.ipynb (Points Table Calculation Using Pandas)
├── CWC2023/
│   ├── icc_world_cup_2023.csv
│   ├── matches2023.py (Web Scraping)
│   ├── cwc2023.sql (Data Ingestion & Points Table Calculation Using SQL)
│   ├── cwc2023stats.ipynb (Points Table Calculation Using Pandas)
├── README.md
```

## Project Overview

This project focuses on creating a points table for the Cricket World Cup for 2011, 2015, 2019 & 2023. The project can be broken down into the following major components:

1. **Data Ingestion:** The project begins with data ingestion from CSV files (icc_world_cup_*.csv) containing information about matches played during the respective World Cup years. The data from these CSV files is loaded into an SQL database using the SQL scripts provided in the "cwc*.sql" files.

2. **Web Scraping:** To ensure that the most up-to-date information is available, web scraping is performed to gather match results, including information on winners, scores, and dates. The Python scripts ("matches*.py") in each year's directory are responsible for scraping this data from the web.

3. **SQL Data Ingestion & Points Table Calculation:** After the data is ingested into an SQL database, the "cwc*.sql" scripts are used to calculate the points table for each World Cup year. These SQL scripts will handle the data processing and calculations required to generate the points table.

4. **Points Table Calculation Using Pandas:** Additionally, the project provides Jupyter Notebook files ("cwc*stats.ipynb") that demonstrate how to calculate the points table using Pandas, a popular data manipulation library in Python. These notebooks offer an alternative approach to generating the points table.

## Getting Started

To get started with this project, follow these steps:

1. Navigate to the directory corresponding to the World Cup year you are interested in (CWC2011, CWC2015, or CWC2019).

2. Run the Python script (e.g., "matches2011.py") to scrape the latest match results from the web.

3. Run the SQL script (e.g., "cwc2011.sql") to ingest data from the CSV file and calculate the points table using SQL.

4. Optionally, you can explore the Jupyter Notebook (e.g., "cwc2011stats.ipynb") to see how the points table can be calculated using Pandas.

### NOTE: As the ICC Mens' Cricket World Cup 2023 has come to an end, so, we have included the stats and the project files for the 2023 World Cup in the project.

## Credits

This project was created by [Abhisekh Nayak](https://linktr.ee/abhisekhnayak98) and is inspired by the love of cricket and the desire to analyze and visualize World Cup match data.

If you have any questions or suggestions, please feel free to contact [Email](mailto:abhinayak.gita2016@gmail.com). We hope you find this project helpful and insightful for cricket enthusiasts and data analysis enthusiasts alike!