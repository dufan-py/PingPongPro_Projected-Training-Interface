import os
import sys
import webbrowser
import threading

def open_browser():
    webbrowser.open('http://127.0.0.1:8000')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject6.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise

    if len(sys.argv) > 1 and sys.argv[1] == 'runserver':
        # 延迟2秒打开浏览器，确保服务器已启动
        threading.Timer(2, open_browser).start()

    execute_from_command_line(sys.argv)
