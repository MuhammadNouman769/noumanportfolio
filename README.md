# Muhammad Nouman — Portfolio (Django)

A full Django portfolio site for Muhammad Nouman — Backend Engineer / Founder, Xvera Labs.

Home, About, Experience, Projects, Services, and Skills all read their content from the
database (via each app's models), and Contact saves submitted messages to the database
so you can review them from the Django admin.

## Project layout

```
nouman_portfolio/
├── core/                  # settings, root urls, wsgi/asgi
├── apps/
│   ├── home/              # landing page (pulls highlights from other apps)
│   ├── about/              # Profile bio + Education
│   ├── experience/         # Experience + ExperienceHighlight
│   ├── projects/           # Project + ProjectTag
│   ├── services/           # Service (the "Our Services" grid)
│   ├── skills/              # SkillCategory + Skill
│   └── contact/             # ContactMessage + form (saved to DB)
├── templates/               # base.html, partials/, and one folder per app
├── static/                  # css/, js/, images/ (your photo lives here)
├── media/                    # uploaded project images (optional, via admin)
├── requirements.txt
├── .env                       # already filled in and ready to run
└── .env.example
```

## Setup (first time)

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create the database tables
python manage.py makemigrations
python manage.py migrate

# 4. Load the real portfolio content (experience, projects, services, skills, education)
python manage.py seed_data

# 5. Create an admin login for yourself
python manage.py createsuperuser

# 6. Run it
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` for the site and `http://127.0.0.1:8000/admin/` to manage
content (edit projects, experience, services, skills, education, and read contact messages).

> A `.env` file is already included with a generated `SECRET_KEY` and your contact details,
> so the site runs as-is. `.env.example` is there as a template if you ever need to
> regenerate it or deploy elsewhere — never commit a real `.env` to a public repo.

## Editing content

Everything shown on the site comes from the database, editable two ways:

1. **Django admin** (`/admin/`) — the easiest way. Add/edit Projects, Experience,
   Services, Skills, and Education visually, including uploading a project image.
2. **`apps/home/management/commands/seed_data.py`** — the source of truth for the
   initial content. Edit this file and re-run `python manage.py seed_data` to reset
   to your latest version (it's idempotent — safe to re-run).

## Adding a new project

Easiest: Django admin → Projects → Add Project → fill in title, slug, summary, status,
GitHub/live URL, tags (inline), and optionally an image.

## Contact form

Messages submitted on `/contact/` are saved as `ContactMessage` rows — view them under
Django admin → Contact → Contact messages. No email server is configured; wiring up
email notifications later just means adding `EMAIL_*` settings and calling `send_mail()`
in `apps/contact/views.py`.

## Moving to PostgreSQL later

Update `.env`:

```env
DB_ENGINE=django.db.backends.postgresql
DB_NAME=nouman_portfolio
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=127.0.0.1
DB_PORT=5432
```

Then `pip install psycopg2-binary`, run `python manage.py migrate` again, and re-run
`seed_data` (or re-enter content via admin).

## Before deploying

- Set `DEBUG=False` in `.env`
- Set `ALLOWED_HOSTS` to your real domain
- Generate a fresh `SECRET_KEY`
- Run `python manage.py collectstatic`
- Move off SQLite to PostgreSQL for production
