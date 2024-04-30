# Registry App

Registry App is a web application built with Django that allows users to manage registries of items.

## Features

- **Search and Filter**: The application provides search  functionality to easily find items based on various criteria.
- **Pagination**: Support for pagination allows users to browse through large registries efficiently.

## Installation v1

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/Jumanazarov-Shukrullo/registry-app.git
    ```
2. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```
3. **Run Migrations**:
    ```sh
    python3 manage.py migrate
    ```
> :warning: **If you don't have chrome browser and chromedriver**: Install it here [here](https://github.com/Jumanazarov-Shukrullo/registry-app/edit/main/install.sh).

4. **Start the Development Server**:
    ```sh
    python3 manage.py runserver
    ```
## Installation v2
**If you have docker installed and docker account just follow next steps**
  1. ***Pull the image***
       ```
         docker pull shukrullo17/registry-app:1.0.0
       ```
  2. ***Run***
       ```
         docker run -p 8000:8000 shukrullo17/registry-app:1.0.0
       ```
