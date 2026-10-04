<h1 align="center"> Python Sales Management System </h1>

<p align="center">
  A sales management system built with Python and Streamlit.
  <br>
  The application allows users to register sales, store data in a CSV file, visualize sales records, and analyze results through an interactive dashboard.
</p>

<p align="center">  
  <a href="#-technologies">Technologies</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-project">Project</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-features">Features</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-workflow">Workflow</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-installation">Installation</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-additional-information">Additional Information</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-license">License</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-contributing">Contributing</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#support">Support</a>  
</p>

<br>

## 🛠 Technologies

- Python
- Streamlit
- Pandas
- Plotly
- CSV
- Git and GitHub

<br>

## 💻 Project

This project is a sales management system developed with Python and Streamlit.

The application allows users to register new sales, save the information in a CSV file, view registered sales, and analyze sales data through an interactive dashboard.

The project was developed step by step to practice building web applications with Python, working with data using Pandas, and creating interactive visualizations with Plotly.

<br>

## ✨ Features

- Register new sales
- Select seller and product
- Enter sale date, quantity, and value
- Validate required information
- Save new sales to a CSV file
- Display registered sales in a table
- Calculate total revenue
- Display sales metrics
- Visualize sales by seller
- Visualize sales distribution by product
- Interactive charts with Plotly

<br>

## 🔄 Workflow

### Step 1: Create the system interface

Build the main application interface using Streamlit.

### Step 2: Create the sales registration form

Create a form to collect:

- Date
- Seller
- Product
- Quantity
- Sale value

### Step 3: Validate and save the sale

Validate the information entered by the user and add valid sales to the dataset.

The updated data is then saved to the CSV file.

### Step 4: Display registered sales

Show the complete sales dataset directly in the application using a Pandas DataFrame.

### Step 5: Create the dashboard

Calculate sales metrics and create interactive charts to visualize the data.

<br>

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Chrysthy/python-sales-management-system.git
```

Access the project folder:

```bash
cd python-sales-management-system
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
python -m streamlit run src/main.py
```

The application will open in your browser.

You can also run the application with:

```bash
streamlit run src/main.py
```

> In some environments, such as GitHub Codespaces, `python -m streamlit` may work better if the `streamlit` command is not available directly in the PATH.

<br>
