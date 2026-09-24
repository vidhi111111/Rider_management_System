# Day 1 Angular & Flask Setup

Today I started working on the Angular and Flask setup for the registration project. My main focus was to get both the frontend and backend running properly on my system and understand how they will communicate with each other.

I started with the Angular setup and used Node.js 16 for the project. Since I had to use a specific Node version, I used NVM to switch to Node 16. After setting up Angular 14, I created the basic registration page and started working with Reactive Forms.

The registration form includes:

Full Name
Email
Mobile Number
Password
Confirm Password

I also worked on the basic form validations. I added checks for empty fields, email format, mobile number, and password and confirm password matching. While doing this, I also got a better understanding of how form controls and validation work in Angular.

For the backend, I started with Python Flask and created a virtual environment for the project. I set up the basic Flask application structure and created the registration API using POST /register.

The API receives the registration details in JSON format and performs basic validation on the data before sending a JSON response back to the frontend.

I also checked the frontend and backend separately to make sure both were running correctly on their respective local ports. This helped me understand the basic flow of the application, from entering the details in the Angular form to sending them to the Flask API.

## Technologies Used
Angular 14
TypeScript
Reactive Forms
Angular Router
Python
Flask
Node.js 16
NVM
## What I understood today
How to set up an Angular 14 project with the required Node version.
How NVM can be used to switch between Node.js versions.
Basic usage of Reactive Forms in Angular.
How frontend form validation works.
How to create a basic Flask application.
How to create a POST API in Flask.
How JSON data is received and validated in the backend.
Basic communication flow between an Angular frontend and Flask backend.
