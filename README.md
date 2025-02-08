
# Social Media Test API

## Overview
This is a simple social media API built using **Django**, **Django Rest Framework (DRF)**, **JWT (JSON Web Token)** authentication, and **PostgreSQL (Serverless with Neon)** for database management. The API allows users to:
- Register and authenticate.
- Create posts.
- Follow/unfollow other users.
- Retrieve a personalized feed based on user followings.
- Retrieve user details and posts.

## Getting Started

### 1. Clone the Repository

```bash
git clone  https://github.com/ouardiYakoubAbdallah/social-media-test-backend.git
cd social-media-test-backend
```

### 2. Set up the Virtual Environment

Create and activate a virtual environment to manage dependencies.

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

Install the required dependencies listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database

1. **Create a (PostgreSQL) Database**:
   - For Neon, sign up at [neon.tech](https://neon.tech) and create a new database instance.
   - Alternatively, you can use any PostgreSQL database provider.

2. **Set up the Database Connection**:
   - In your project, update the `DATABASES` settings in `settings.py`, use a connection string to connect to your PostgreSQL database. 

3. **Run Migrations**:
   Apply the database migrations to set up the tables.

```bash
python manage.py migrate
```

### 5. Create a Superuser (Optional)

If you want to use the Django Admin panel, create a superuser account.

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

Start the Django development server.

```bash
python manage.py runserver
```

Now, the application should be running at `http://127.0.0.1:8000/`.

---

## API Usage

### **1. User Registration**
- **POST** `/users/`
- Register a new user by providing **username**, **email**, and **password**.

#### Request Body:
```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "secure_password"
}
```

### **2. User Login & JWT Authentication**
- **POST** `/login/`
- Authenticate a user and receive a **JWT token**.

#### Request Body:
```json
{
    "email": "john@example.com",
    "password": "secure_password"
}
```

#### Response:
```json
{
    "refresh": "your_jwt_refresh_token",
    "access": "your_jwt_token"
}
```

### **3. Create a Post**
- **POST** `/posts/`
- Create a new post. You must be authenticated with a JWT token.

#### Request Header:
```plaintext
Authorization: Bearer your_jwt_token
```

#### Request Body:
```json
{
  "content": "Hello, this is my first post!"
}
```

### **4. Retrieve Posts**
- **GET** `/posts/`
- Retrieve a list of posts, including those from users the authenticated user is following.

#### Request Header:
```plaintext
Authorization: Bearer your_jwt_token
```

#### Response:
```json
[
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
          "id": 1,
          "content": "Hello, this is my first post!",
          "timestamp": "2025-02-08T12:34:56Z",
          "author": {
            "id": 1,
            "username": "john_doe"
          }
        }  
   ]
]
```

### **5. Follow a User**
- **POST** `/users/follow/{username}/`
- Follow another user. You must be authenticated with a JWT token.

#### Request Header:
```plaintext
Authorization: Bearer your_jwt_token
```

#### Response:
```json
{
  "message": "You are now following john_doe."
}
```

### **6. Unfollow a User**
- **POST** `/users/unfollow/{username}/`
- Unfollow a user. You must be authenticated with a JWT token.

#### Request Header:
```plaintext
Authorization: Bearer your_jwt_token
```

#### Response:
```json
{
  "message": "You have unfollowed john_doe."
}
```

### **7. View User Profile**
- **GET** `/users/profile/<id>`
- View your user profile, including your posts. You must be authenticated with a JWT token.

#### Request Header:
```plaintext
Authorization: Bearer your_jwt_token
```

#### Response:
```json
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com",
  "registration_date": "2025-01-01T00:00:00Z",
  "posts": [
    {
      "id": 1,
      "content": "Hello, this is my first post!",
      "timestamp": "2025-02-08T12:34:56Z"
    }
  ]
}
```

---

## Authentication

The API uses **JWT (JSON Web Token)** for user authentication. To authenticate a user, you must include the token in the `Authorization` header of the request:

```plaintext
Authorization: Bearer your_jwt_token
```

- **Login**: Obtain the JWT token by logging in with your credentials.
- **Authenticated Endpoints**: All endpoints related to user actions, such as creating posts, following users, and viewing the profile, require the user to be authenticated.

---

## Error Handling

The API returns proper HTTP status codes and messages for errors. Common errors include:

- **400 Bad Request**: Invalid data or malformed request.
- **401 Unauthorized**: Missing or invalid JWT token.
- **404 Not Found**: Resource not found (e.g., trying to follow a non-existent user).
- **403 FORBIDDEN**: Trying to do an action while not authenticated.

Example error response:
```json
{
    "detail": "No active account found with the given credentials"
}
```

---

## Additional Features Implemented

- **Follow/Unfollow Users**: Users can follow/unfollow other users to build a personalized feed.
- **Visit User profile**: User can retrieve users details and posts.

---

## Testing

To test the application, use **Django's testing framework** or a tool like **Postman** or **Insomnia** to interact with the API.

**Test Coverage**:
- We provide tests for successful and unsuccessful scenarios, including user authentication and post creation.

Run the tests with:

```bash
python manage.py test <path_to_the_test>
```

---

## License
