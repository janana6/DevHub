# DevHub — Developer Project Hub & Dev Journal

A clean, focused personal workspace built with **Python 3.14.3+**, **Django 5**, **PostgreSQL**, and **Bootstrap 5**. DevHub strips away unnecessary gamification (streaks, habits, point systems) to provide a practical portfolio manager and daily development log.

---

## Features

- **Project Pipeline Board:** Group your portfolio projects into 3 clear states: `Idea`, `Building`, and `Done`.
- **Project CRUD Operations:** Easily create, view, edit, and update projects directly from your workspace.
- **Tech Stack & Repo Tracking:** Tag technologies per project and link directly to GitHub repositories.
- **Project-Linked Dev Journal:** Log daily engineering notes, bug fixes, and milestones—optionally associated with a specific project.
- **Authentication & Self-Registration:** Dedicated custom login (`/login/`) and registration (`/register/`) pages allow new developers to create accounts and log in securely.
- **User-Scoped Data Isolation:** All projects and journal entries are strictly isolated per authenticated user (`request.user`).
- **Built-in Django Admin Power:** Instantly manage, edit, filter, and audit data with elevated permissions.

---

## Tech Stack

- **Backend:** Python 3.12+ / Django 5
- **Database:** PostgreSQL (`psycopg` / `psycopg2`)
- **Frontend:** HTML5, Jinja/Django Templates, Bootstrap 5 (Dark Theme) + Bootstrap Icons

---

## Directory Layout

```text
DevHub/
├── config/                  # Django project configuration
│   ├── settings.py          # App settings, login/logout redirects & PostgreSQL connection
│   ├── urls.py              # Root URL routing
│   └── wsgi.py
├── devhub/                  # Core application
│   ├── admin.py             # Admin panel registrations for Project and DevJournal
│   ├── forms.py             # Bootstrap-styled ModelForms with user scoping
│   ├── models.py            # Project and DevJournal models
│   ├── urls.py              # App-level routing (board, auth, CRUD actions)
│   ├── views.py             # Board, Auth (Login/Register), Journal, and Edit views
│   └── templates/           # Django HTML templates
│       ├── base.html
│       └── devhub/
│           ├── form.html
│           ├── journal_list.html
│           ├── login.html
│           ├── project_board.html
│           ├── register.html
│           └── components/
│               └── project_card.html
├── manage.py
└── README.md
