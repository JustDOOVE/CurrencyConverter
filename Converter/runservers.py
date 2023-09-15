import subprocess
import threading


def start_django_server():
    subprocess.run(["python", "manage.py", "runserver", "--noreload", "--nothreading", "0.0.0.0:8005"])


def start_django_command():
    subprocess.run(["python", "manage.py", "getcourses"])


if __name__ == "__main__":
    server_thread = threading.Thread(target=start_django_server)
    command_thread = threading.Thread(target=start_django_command)

    server_thread.start()
    command_thread.start()

    server_thread.join()
    command_thread.join()
