# TSF-GRIP-Task---Simple-Banking-System
A simple banking system web app built using Python and Django.


## Overview

This is a Banking System web app developed to serve as the first task as a `Web Development Intern` at `TSF : The Sparks Foundation` in `GRIP : GRADUATE ROTATIONAL INTERNSHIP PROGRAM`.


## Description

Task Definition:
### Basic Banking System
Create a simple dynamic website which has the following specs:
Start with creating a dummy data in database for upto 10 customers. Database options: Mysql, Mongo, Postgres, etc.
Customers table will have basic fields such as name, email, current balance etc. Transfers table will record all transfers happened.
Flow: Home Page > View all Customers > Select and View one Customer > Transfer Money > Select customer to transfer to > View all Customers .
No Login Page. No User Creation. Only transfer of money between multiple users.


# Watch a Demo

https://github.com/Farahat612/TSF-GRIP-Task---Simple-Banking-System/assets/67427124/f7d6dc7e-84cc-4717-8a82-22a90a8028b7


## Key Features:

1. Listing all customers list.

2. Viewing Customer information like name, email and balance.

3. Transfering mony between customers.

4. Error handling like insufficient balance or transfering to the same user.


## Technologies Used:

- Python
- Django
- Django Template Language
- Sqlite3 DB
- HTML
- CSS


## Getting Started

To run the website on your local machine, follow these steps:

1. Clone the repository: `$ git clone <repository-url>`
2. Navigate to the project directory: `$ cd <project-directory>`
3. Install the required dependencies: `$ pip install -r requirements.txt`
4. Apply the database migrations: `$ python manage.py migrate`
5. Start the development server: `$ python manage.py runserver`
6. Open your web browser and visit `http://localhost:8000` to access the website.


## Contributing

Contributions to this project are welcome. If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch: `$ git checkout -b my-new-branch`
3. Make your changes and commit them: `$ git commit -am 'Add some feature'`
4. Push the changes to your branch: `$ git push origin my-new-branch`
5. Submit a pull request detailing your changes.


## Known Issues or Limitations

Currently, there are no known issues or limitations with this project.


## Acknowledgments

This project was completed as an internship task for `Web Development GRIP` at `The Sparks Foundation`. 


## License

This project is licensed under the [MIT License](LICENSE).
