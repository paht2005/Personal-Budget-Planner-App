# 💰 Personal Budget Planner App

![screen](/imgs/screen.png)

This repository contains the implementation of a **Personal Budget Planner App** built using **Streamlit** and **Matplotlib**.  
It allows users to manage their personal finances by adding income and expenses, setting monthly savings goals, and visualizing expenses by category.

---

## 🗂️ Table of Contents

- [✨ Features](#-features)
- [🗂️ Repository Structure](#️-repository-structure)
- [⚙️ Installation](#️-installation)
- [🎯 Usage](#-usage)
- [📄 License](#-license)
- [🤝 Contributing](#-contributing)
- [🧠 Acknowledgements](#-acknowledgements)
- [⭐ Future Enhancements](#-future-enhancements)

---

## ✨ Features

- **Monthly Budget Input**: Enter your income and define your monthly savings goal.
- **Expense Tracker**: Add categorized expenses (Food, Housing, Transport, etc.).
- **Real-time Budget Summary**: View remaining budget and whether you’ve met your savings goal.
- **Expense Visualization**: Automatically generates a pie chart showing the distribution of expenses by category.
- **Session Persistence**: Stores data during session for consistent experience.
- **Minimalist UI with Enhanced Styling** (coming soon).

---

## 🗂️ Repository Structure
```
├── imgs/ # Folder for storing screenshots
├── Personal-Budget-Planner_app.py # Main Streamlit app script
├── requirements.txt # Python dependencies
└── README.md # Project documentation
└── LICENSE

```
---

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/paht2005/Personal-Budget-Planner-App.git
   cd Personal-Budget-Planner-App
   ```
2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Streamlit app:**
   ```bash
   streamlit run Personal-Budget-Planner_app.py
   ```
---
## 🎯 Usage
- Launch the app in your browser using Streamlit.
- Use the **sidebar** to enter income and set your monthly savings goal.
- Use the **main section** to add expenses by category.
- The app shows:
  - **Total expenses**
  - **Remaining budget**
  - **Savings goal progress**
  - **Expense distribution pie chart**
---
## 📄 License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---
## 🤝 Contributing
I welcome contributions to improve this project!
Feel free to:
- Submit pull requests
- Report bugs
- Suggest new features
Contact for work: **Nguyễn Công Phát** – congphatnguyen.work@gmail.com
---
## 🧠 Acknowledgements
- **Streamlit** - For creating an amazing platform to build data apps.
- **Matplotlib** - For powerful and customizable visualizations.
---
## ⭐ Future Enhancements
- Multi-chart Support: Add bar charts and time-series plots for monthly trend tracking.
- Export/Import Data: Enable exporting and importing budget data to/from .csv or .xlsx files.
- Persistent Storage: Integrate with a database (e.g., SQLite) for saving data across sessions.
- Mobile-Responsive UI: Optimize the app layout for mobile and tablet views.
- Budget Alerts: Add notifications or warnings when nearing budget limits.
- Calendar View: Visualize expenses across days or weeks in a calendar layout.
- Multi-language Support: Add support for both English and Vietnamese.
- User Authentication: Add login functionality for personal user profiles and secure data.
