# Cryptocurrency Portfolio Tracker

## Objective
Flask-based application that tracks a user's cryptocurrency portfolio by fetching real-time prices, allows for the recording of buy/sell transactions, calculates the portfolio's current value, and stores transaction data in a PostgreSQL database.

## Key Features
- **Real-time Cryptocurrency Price Updates**: Fetches up-to-date prices from an external API.
- **Transaction Management**: Users can add, read, update, and delete (CRUD) cryptocurrency transactions.
- **Portfolio Valuation**: Calculates the total value of the portfolio based on current prices.
- **Performance Metrics**: Provides detailed performance metrics for the portfolio over time.
- **Advanced Data Handling**: Utilizes advanced Python features and PostgreSQL for efficient data management.

## Installation

To install and run the Cryptocurrency Portfolio Tracker, follow these steps:

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/nikolov-daniel/cryptocurrency_portfolio.git
    cd cryptocurrency_assignment
    ```

2. **Set Up a Virtual Environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set Up PostgreSQL**:
    - Ensure PostgreSQL is installed and running.
    - Create a new database:
      ```sh
      createdb cryptocurrency_app
      ```

5. **Configure Environment Variables**:
    Create a `.env` file and add your configuration details:
    ```
    
    SQLALCHEMY_DATABASE_URI=postgresql://username:password@localhost/cryptocurrency_app
    API_TOKEN=your_api_key_here
    API_URL=https://rest.coinapi.io/v1/exchangerate
    ```

6. **Run Database Migrations**:
    ```sh
    python manage.py migrate
    ```

7. **Start the Application**:
    ```sh
    python manage.py runserver
    ```

## Usage

- **Add a Transaction**: Allows users to add a new cryptocurrency transaction.
- **View Transactions**: Lists all transactions with details.
- **Update a Transaction**: Edit details of an existing transaction.
- **Delete a Transaction**: Remove a transaction from the portfolio.
- **View Portfolio**: Displays the total valuation and performance metrics of the portfolio.

## Contributing

We welcome contributions to enhance the Cryptocurrency Portfolio Tracker. To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or support, please reach out at daniel.nikolov@hotmail.com.
"# cryptocurrency_portfolio" 
"# cryptocurrency_portfolio" 
