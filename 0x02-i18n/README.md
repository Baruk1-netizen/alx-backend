# README

## Basic Flask App with Babel Localization

### Author
**Baruk1-netizen**

---

### Project Overview

This project involves creating a basic Flask application with localization support using the Flask-Babel extension. The app includes functionality for user login and displays content in different languages based on user preferences and request parameters.

---

### Steps and Files

1. **Basic Flask App**
   - **File:** `0-app.py`, `templates/0-index.html`
   - **Description:** Set up a basic Flask app with a single route (`/`) and an `index.html` template displaying "Welcome to Holberton" as the page title and "Hello world" as the header.

2. **Basic Babel Setup**
   - **File:** `1-app.py`, `templates/1-index.html`
   - **Description:** Install Flask-Babel, instantiate Babel, and configure available languages (English and French). Set default locale to English and timezone to UTC.

3. **Get Locale from Request**
   - **File:** `2-app.py`, `templates/2-index.html`
   - **Description:** Create a `get_locale` function to determine the best match with supported languages based on the request's accepted languages.

4. **Parametrize Templates**
   - **File:** `3-app.py`, `babel.cfg`, `templates/3-index.html`, `translations/en/LC_MESSAGES/messages.po`, `translations/fr/LC_MESSAGES/messages.po`, `translations/en/LC_MESSAGES/messages.mo`, `translations/fr/LC_MESSAGES/messages.mo`
   - **Description:** Use the `_` function to parametrize templates with message IDs. Initialize and compile translations for English and French.

5. **Force Locale with URL Parameter**
   - **File:** `4-app.py`, `templates/4-index.html`
   - **Description:** Implement locale detection from URL parameters, allowing users to force a particular locale using the `locale` parameter.

6. **Mock Logging In**
   - **File:** `5-app.py`, `templates/5-index.html`
   - **Description:** Mock a user login system with a user table. Implement `get_user` and `before_request` functions to handle user login. Display messages based on login status.

7. **Use User Locale**
   - **File:** `6-app.py`, `templates/6-index.html`
   - **Description:** Modify `get_locale` function to use the user's preferred locale, considering URL parameters, user settings, and request headers.

8. **Infer Appropriate Time Zone**
   - **File:** `7-app.py`, `templates/7-index.html`
   - **Description:** Define `get_timezone` function to determine the appropriate time zone based on URL parameters, user settings, and default to UTC. Validate time zones using `pytz`.

---

### Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Baruk1-netizen/alx-backend.git
   cd alx-backend/0x02-i18n
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```bash
   flask run
   ```

---

### Testing

To test different translations and user login functionality, you can use the following URLs:
- Default: `http://127.0.0.1:5000`
- Force locale: `http://127.0.0.1:5000/?locale=fr`
- Mock login: `http://127.0.0.1:5000/?login_as=2`

---

### Repository Structure

```
0x02-i18n/
│
├── templates/
│   ├── 0-index.html
│   ├── 1-index.html
│   ├── 2-index.html
│   ├── 3-index.html
│   ├── 4-index.html
│   ├── 5-index.html
│   └── 6-index.html
│   └── 7-index.html
│
├── translations/
│   ├── en/
│   │   └── LC_MESSAGES/
│   │       └── messages.po
│   │       └── messages.mo
│   ├── fr/
│       └── LC_MESSAGES/
│           └── messages.po
│           └── messages.mo
│
├── 0-app.py
├── 1-app.py
├── 2-app.py
├── 3-app.py
├── 4-app.py
├── 5-app.py
├── 6-app.py
├── 7-app.py
└── babel.cfg
```

---

### License

This project is licensed under the MIT License.

---

### Acknowledgments

Special thanks to the ALX program for providing the resources and guidance to complete this project.
