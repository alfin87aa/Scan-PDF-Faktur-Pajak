import asyncio
from pathlib import Path
import time
import watchdog.events
import watchdog.observers
from .controllers.readPdf import fakturPajak
from app.config import FOLDER_INBOX, FOLDER_OUTBOX

class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        # Set the patterns for PatternMatchingEventHandler
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.pdf'],
                                                             ignore_directories=True, case_sensitive=False)

    def on_created(self, event):
        asyncio.run(fakturPajak(event.src_path))

def create_app():
    Path(FOLDER_INBOX).mkdir(parents=True, exist_ok=True)
    Path(FOLDER_OUTBOX).mkdir(parents=True, exist_ok=True)

    # Watch File Event
    event_handler = Handler()
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path=FOLDER_INBOX, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
