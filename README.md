# Face Verification Web Application

## Overview

The Face Verification Web Application is a user-friendly web-based tool that leverages advanced face recognition technology to provide a range of functionalities, including face comparison, image upload, and database management. It is built using Flask, a micro web framework in Python, and incorporates various libraries for image processing and database management.

![image](https://github.com/kumar-chetan/face-verification-app/assets/112582415/9eb48db3-f140-43f0-be18-d6215f0afc24)



## Features

- **Face Comparison:** Upload two images to compare faces and determine if they belong to the same person. The application uses face recognition techniques to analyze and compare facial features, providing results indicating whether the uploaded images match.

- **Face Upload:** Users can contribute to the database by uploading their own images along with their names. The application processes and securely stores these images.

- **Database Management:** The application maintains a database of uploaded images and associated names. Users can view all records stored in the database, including whether image data is available for each person. The database management functionality offers search capabilities to quickly find records based on names.

- **User Interface:** The project includes a user-friendly interface designed with HTML, CSS, and templates. The interface allows users to navigate between different functionalities, upload images, perform face comparisons, and view database records.

- **Dynamic Routing:** The application uses Flask, enabling dynamic routing and rendering of HTML templates based on user interactions. Different routes are used for face comparison, face upload, and database management.

- **Face Recognition:** The application utilizes the face_recognition library to perform facial feature extraction and comparison. This library employs advanced machine learning algorithms to recognize and compare faces within images.

- **Styling and UI Enhancement:** The user interface is enhanced with CSS styling, making the application visually appealing and user-friendly. Layout, colors, and design elements are customized to provide an engaging experience.

## Getting Started

### Prerequisites

- Python (3.7 or higher)
- Flask
- face_recognition

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/kumar-chetan/face-verification-app.git
   cd face-verification-app
      ```
2. Create a virtual environment (recommended):
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
      ```
3. Install required packages:
      ```bash
    pip install -r requirements.txt
      ```
4. Run the application:
    ```bash
    python app.py
    ```
   
### The web application should be accessible at http://localhost:5000.

## **Future Enhancements**
- User authentication for secure access.
- Confidence score display for face verification results.
- Integration of more advanced face recognition models.
- Enhanced error handling and user feedback.

### Contributing :-
Contributions are welcome! If you'd like to contribute to the project, please follow our contribution guidelines.


### Contact :-
For questions or feedback, please contact Name- Chetan Kumar , Gmail- 9013chetankumar@gmail.com .

