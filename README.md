# DevHub — Developer Project Hub & Dev Journal

A clean, focused personal workspace built with **Python 5**, **Django**, **PostgreSQL**, and **Bootstrap 5**. DevHub strips away unnecessary gamification (streaks, habits, point systems) to provide a practical portfolio manager and daily development log.

---

## Features

- **Project Pipeline Board:** Group your portfolio projects into 3 clear states: `Idea`, `Building`, and `Done`.
- **Tech Stack & Repo Tracking:** Tag technologies per project and link directly to GitHub repositories.
- **Project-Linked Dev Journal:** Log daily engineering notes, bug fixes, and milestones—optionally associated with a specific project.
- **Built-in Django Admin Power:** Instantly manage, edit, filter, and audit data without writing custom admin CRUD views.
- **User-Scoped Data:** All projects and journal entries are isolated per authenticated user.

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
│   ├── settings.py          # App settings & PostgreSQL database connection
│   ├── urls.py              # Root URL routing
│   └── wsgi.py
├── devhub/                  # Core application
│   ├── admin.py             # Admin panel registrations for Project and DevJournal
│   ├── forms.py             # Bootstrap-styled ModelForms with user scoping
│   ├── models.py            # Project and DevJournal models
│   ├── urls.py              # App-level routing
│   ├── views.py             # Board, Timeline, and Form views
│   └── templates/           # Django HTML templates
│       ├── base.html
│       └── devhub/
│           ├── form.html
│           ├── journal_list.html
│           ├── project_board.html
│           └── components/
│               └── project_card.html
├── manage.py
└── README.md
