"""This module is run by gunicorn to start the application."""
from app import app

if __name__ == "__main__":
  app.run()
