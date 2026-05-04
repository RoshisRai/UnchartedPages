![Uncharted Pages](https://i.ibb.co/Zpk77hLj/uncharted-homepage.png)

# Uncharted Pages

### [Live Website](https://unchartedpages.pythonanywhere.com/)

Uncharted Pages is a Django-based web app for publishing short stories and blog posts, with a public site, blog discovery, newsletter subscriptions, and a book purchase flow.

## Main Pages
1. Home: Landing page with the site overview.
2. About: Author background and inspiration.
3. Contact: Inquiry and feedback form.
4. Blogs: Blog list and details.
5. FAQ: Frequently asked questions.
6. Buy Book: Purchase and order flow.

## Tech Stack
- Python (Django 4.2)
- SQLite (default database)
- Pillow (image handling)
- python-dotenv (environment variables)

## Models
- Blog: Blog posts and categories.
- BookOrder: Book orders with payment receipt uploads.
- ContactUs: Contact form submissions.
- NewsletterSubscriber: Newsletter subscribers.

## Project Structure (Quick View)
- `manage.py`: Django entry point
- `unchartedpages/`: project settings and root URLs
- `home/`: main app with views, models, and URLs
- `templates/`: HTML templates
- `static/`: CSS, JS, images
- `db.sqlite3`: local database

## Full Folder and File Structure
Copy-friendly tree with right-side comments:

```
.
|-- .env                                   # environment variables (not committed)
|-- db.sqlite3                             # local SQLite database
|-- manage.py                              # Django entry point
|-- requirements.txt                       # Python dependencies
|-- draft-md.md                            # project documentation draft
|-- home/                                  # main Django app
|   |-- __init__.py                        # app package
|   |-- admin.py                           # admin registrations
|   |-- apps.py                            # app config
|   |-- context_processors.py              # template context processors
|   |-- models.py                          # database models
|   |-- tests.py                           # app tests
|   |-- urls.py                            # app routes
|   |-- views.py                           # request handlers
|   |-- migrations/                        # Django migrations
|   |   |-- __init__.py                    # migrations package
|   |   `-- 0001_initial.py                # initial schema
|   `-- templatetags/                      # custom template tags
|       |-- __init__.py                    # templatetags package
|       `-- custom_tags.py                 # custom tags/filters
|-- static/                                # global static assets
|   |-- css/                               # site CSS
|   |   |-- about.css                       # about page styles
|   |   |-- blogpost.css                    # blog post styles
|   |   |-- blogs.css                       # blog list styles
|   |   |-- blogsearch.css                  # search styles
|   |   |-- buybook.css                     # buy book styles
|   |   |-- contact.css                     # contact styles
|   |   |-- faq.css                         # FAQ styles
|   |   `-- styles.css                      # global styles
|   |-- img/                               # site images
|   `-- js/                                # site JS
|       |-- app.js                         # app scripts
|       |-- jquery.min.js                  # jQuery
|       |-- particles.min.js               # particles lib
|       |-- scripts.js                     # site scripts
|       `-- tinyinject.js                  # tinyinject lib
|-- templates/                             # Django templates
|   |-- base.html                          # base template
|   |-- admin/                             # admin template overrides
|   |   |-- 404.html                        # admin 404
|   |   |-- base_site.html                  # admin base site
|   |   `-- base.html                       # admin base
|   `-- home/                              # app templates
|       |-- about.html                      # about page
|       |-- blogpost.html                   # blog post page
|       |-- blogs.html                      # blog list page
|       |-- blogsearch.html                 # blog search page
|       |-- buybook.html                    # buy book page
|       |-- contact.html                    # contact page
|       |-- faq.html                        # FAQ page
|       `-- index.html                      # home page
`-- unchartedpages/                        # project configuration
    |-- __init__.py                         # package init
    |-- asgi.py                             # ASGI config
    |-- settings.py                         # settings
    |-- sitemaps.py                         # sitemap definitions
    |-- urls.py                             # root URLs
    `-- wsgi.py                             # WSGI config
```

## Environment Variables
Create a `.env` file in the project root with:

- `DJANGO_SECRET_KEY`

## Configuration Notes
- Set `DEBUG` to `False` for production.
- Configure `ALLOWED_HOSTS` for your domain(s).
- Static files are served from `static/` in development.
- Media uploads are stored under `media/`.

## URL Routes
Root routes are defined in the project and home app:
- `/`: Home page
- `/about-us/`: About page
- `/blogs/`: Blog list
- `/blog-search/`: Blog search
- `/blog-post/<slug>/`: Blog details
- `/buy-book/`: Book purchase form
- `/contact-us/`: Contact form
- `/frequently-asked-questions/`: FAQ
- `/newsletter-subscriber/`: Newsletter signup
- `/admin/`: Django admin
- `/sitemap.xml/`: Sitemap

## Local Development
1. Create and activate a virtual environment.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set `.env` values.
4. Make migrations (if needed):

   ```bash
   python manage.py makemigrations home
   ```

5. Run migrations:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

## Admin Content
- Visit http://localhost:8000/admin
- Log in with your superuser credentials
- Add or edit posts under the `Blog` section

## Production Checklist
1. Set `DEBUG` to `False` and configure `ALLOWED_HOSTS`.
2. Set `DJANGO_SECRET_KEY` in your environment.
3. Collect static files:

   ```bash
   python manage.py collectstatic
   ```

4. Configure media storage and backups.
5. Use a production-grade WSGI server (gunicorn/uwsgi) and a reverse proxy.

## Contributing
We welcome contributions. Suggested workflow:
1. Fork the repository.
2. Create a branch:

   ```bash
   git checkout -b <branch_name>
   ```

3. Commit changes:

   ```bash
   git commit -m "<commit_message>"
   ```

4. Push:

   ```bash
   git push origin <branch_name>
   ```

5. Open a pull request.

## License
MIT License. See `LICENSE` for details.

## Contact
Questions or feedback: roshis.awai@gmail.com
