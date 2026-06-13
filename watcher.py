import os
import time
from dotenv import load_dotenv
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from update_db import processar_arquivo

load_dotenv()

VAULT_ALUNOS = os.getenv("VAULT_ALUNOS")
DB_PATH = os.getenv("DB_PATH")

class IIVAHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path.endswith(".md"):
            print(f"📄 Criado: {event.src_path}")
            processar_arquivo(event.src_path)

    def on_modified(self, event):
        if event.src_path.endswith(".md"):
            print(f"📝 Modificado: {event.src_path}")
            processar_arquivo(event.src_path)

if __name__ == "__main__":
    event_handler = IIVAHandler()
    observer = Observer()
    observer.schedule(event_handler, VAULT_ALUNOS, recursive=True)
    observer.start()
    print(f"👁️ Watcher iniciado em: {VAULT_ALUNOS}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


