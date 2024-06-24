import os, environ
from pathlib import Path


env = environ.Env()
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


def google_analytics(request):
    return {'GOOGLE_ANALYTICS_ID' : env('GOOGLE_ANALYTICS_ID')}