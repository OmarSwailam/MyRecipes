# MyRecipes RESTful API
Django Rest Framework API that allows users to share and discover recipes. Users can sign up for an account, create their own recipes, and share them with the community. The application also allows users to search for recipes by title, description, ingredients, and tags.

the project includes a user-friendly interface that provides comprehensive documentation for all API endpoints. This makes it easy for developers to understand and interact with the various endpoints and their parameters.

## Features

- Implemented a comprehensive authentication system using JWT that requires users to activate their accounts through a verification link
- Implemented key features such as password and email change functionality
- Utilized Celery to enable asynchronous email sending
- Designed a solid tagging system that enhances filtering options for users, enabling them to filter recipes based on specific ingredients or tags
- Added a search functionality for finding recipes by title
- Implemented a streamlined process that enables users to add multiple images to a recipe in a single post request, improving the user experience and reducing the time required to add images to a recipe.
- Implemented custom permissions to ensure secure access and prevent unauthorized actions.
- Added the capability for users to set recipes as private or public, giving them control over their content and visibility to the community


```

# Clone repository
  git clone https://github.com/OmarSwailam/MyRecipes.git

# Create a virtualenv(optional)
  python3 -m venv env


# Install all dependencies
  pip install -r requirements.txt


# Activate the virtualenv
  source venv/bin/activate or .venv/bin/activate

# Run application
  python manage.py runserver
  or if you want to run it using waitress
  python server.py

# Run celery
  celery -A myrecipes worker -P threads


```

Author: Omar Swailam
