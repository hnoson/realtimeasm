from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from handler import AsmFileEventHandler

if __name__ == '__main__':
    observer = Observer()
    observer.schedule(AsmFileEventHandler(), '.', recursive=True)
    observer.start()
    try:
        observer.join()
    except KeyboardInterrupt:
        pass
