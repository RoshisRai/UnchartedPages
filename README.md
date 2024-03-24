# 📚 Uncharted Pages

Uncharted Pages is a Python web application 🕸️ built using Django in the backend and HTML, CSS, JavaScript, and jQuery in the front end. This website features 3D animations and transitions 🎞️ to create an engaging user experience. Originally created to publish a collection of short stories, Uncharted Pages consists of six main pages:

1. **Home** 🏠: The landing page provides an overview of the website.
2. **About** 📖: Offers information about the author and the inspiration behind the short stories.
3. **Contact** 📞: Allows visitors to make inquiries or provide feedback.
4. **Blogs** 📝: Contains blog posts related to the short stories.
5. **FAQ** ❓: Provides answers to frequently asked questions about the book and its content.
6. **Buy Book** 💰: Provides information on purchasing the short story book.

## Models

The website utilizes four models:

- **Blog** 📝: Stores blog posts related to the short stories.
- **BookOrder** 📦: Manages orders made for the book, including proof of payment upload.
- **ContactUs** 📞: Records contact inquiries made by visitors.
- **NewsLetterSubscriber** 📧: Manages subscribers for newsletters.

## Usage

To use Uncharted Pages:

1. Clone the repository:

    ```bash
    git clone https://github.com/RoshisRai/UnchartedPages.git
    ```

2. Install Dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Make Migrations:

    Generate migration files for the four models (Blog, BookOrder, ContactUs, NewsLetterSubscriber) in the `home` app:
    ```bash
    python manage.py makemigrations home
    ```

4. Run Migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a Superuser:

    ```bash
    python manage.py createsuperuser
    ```

6. Start the Development Server:

    ```bash
    python manage.py runserver
    ```

7. Adding Blog Posts:

    To add blog posts, log in to the admin dashboard:
    - Navigate to [http://localhost:8000/admin](http://localhost:8000/admin)
    - Enter your superuser credentials
    - Add/edit blog posts under the Blog section

### Contributing

We welcome contributions to this project! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`.
4. Push to the original branch: `git push origin <project_name>/<location>`.
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).

### License

This project is licensed under the MIT License - see the `LICENSE` file for details.

### Contact

If you have any questions or feedback, please contact me at 📧 roshis.awai@gmail.com.
