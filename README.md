# 🚴‍♂️ Bike Rental System (Python Project)

A simple **menu-driven Python project** that allows users to rent bikes from a store.  
It demonstrates **Object-Oriented Programming (OOP)**, **loops**, and **basic input handling** in Python.  

---

## 📌 Features
- View available stock of bikes.
- Request to rent bikes with validation:
  - Prevents negative or zero quantities.
  - Prevents renting more than available stock.
- Displays the total rental cost before confirmation.
- Updates stock after successful renting.
- Interactive CLI menu for user-friendly experience.

---

## 🛠️ Technologies Used
- **Python 3** (no external libraries needed).

---

## ▶️ How to Run

1. Clone this repository or download the file:
   ```bash
   git clone https://github.com/HimanshuAryaa/BikeRental.git
   cd BikeRental
   ```
2. Run the program:
   ```bash
   python bike_rental.py
   ```

## 📋 Menu Options
```
1. Display Available Stocks
2. Request for Renting bikes (Price - Rs100 per bike)
3. Exit
```
## 💡 Example Run
```
1. Display Available Stocks
2. Request for Renting bikes (Price - Rs100 per bike)
3. Exit
Enter your choice: 1

Available Stock: 200

Enter your choice: 2

Available Stock: 200
Enter the Qty you would like to rent: 3

Qty = 3
Price = 100
-----------------
Total Price = 300

Would you like to confirm your purchase? (Y/N): Y

Thank You for renting! Remaining stock: 197
```
## 📂 Project Structure
```
bike-rental-system/
│── bike_rental.py   # Main source code
│── README.md        # Documentation
```
## 🚀 Future Improvements

- Add hourly/daily rental system.

- Add customer history and receipts.

- Save data to a file or database.

## 👨‍💻 Author

- Developed by Your Himanshu Arya

- 🔗 [LinkedIn](https://linkedin.com/in/himanshuaryaa) | [GitHub](https://github.com/HimanshuAryaa)