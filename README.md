# Django REST API Project

This Django project provides RESTful API endpoints for managing categories, tags, and items.

## Overview

- The project includes API endpoints for CRUD operations on categories, tags, and items.
- Data validation ensures non-negative stock and price values for items.
- Pagination is implemented for listing categories, tags, and items.

## API Endpoints

- `/category/create/`: Create a new category.
- `/tag/create/`: Create a new tag.
- `/item/create/`: Create a new item.
- `/category/`: List all categories.
- `/tag/`: List all tags.
- `/item/`: List all items.
- `/category/<int:pk>/`: Retrieve, update, or delete a category by ID.
- `/tag/<int:pk>/`: Retrieve, update, or delete a tag by ID.
- `/item/<int:pk>/`: Retrieve, update, or delete an item by ID.
- `/category/delete/<int:pk>/`: Delete a category by ID.
- `/tag/delete/<int:pk>/`: Delete a tag by ID.
- `/item/delete/<int:pk>/`: Delete an item by ID.
- `/item/update/<int:pk>/`: Update stock of an item by ID.




