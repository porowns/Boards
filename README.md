# Boards
Forum-like board software written in Django.

# Installation

1. Install Git, Python 2, Pip, Django 1.8

2. Clone the repository ```git clone https://github.com/porowns/Boards.git```

3. Navigate to Boards folder

4. Migrate the models ```python manage.py makemigrations``` ```python manage.py migrate```

5. Run the application ```python manage.py runserver```

# User Stories

### Dashboard

- User can view their profile

- User can modify their profile

- User can view their friends

- User can view their enemies

### Boards

- User can create a board (user will be moderator of that board)

- User can modify a board

- User can delete a board (if they own it)

- Boards will contain posts that match the category of the board

### Posts

- User can create a post

- User can modify a post

- User can delete a post (that they created)

### Moderators

- Moderator can delete a post on their board

- Moderator can edit a post on their board

- Moderator can block users, which will block them from their board

# Routes

### Dashboard

- /dashboard

- /profile

- /settings

- /change-username

- /change-password

### Boards

- /boards

- /create-board

- /modify-board

- /delete-board

### Posts

- /posts

- /create-post

- /modify-post

- /delete-post

### User

- /register

- /login

- /logout


