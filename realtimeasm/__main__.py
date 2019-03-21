from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from realtimeasm.handler import AsmFileEventHandler

def main() -> None:
    observer = Observer()
    observer.schedule(AsmFileEventHandler(), '.', recursive=True)
    observer.start()
    try:
        observer.join()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
