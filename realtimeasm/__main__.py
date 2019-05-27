import argparse
from watchdog.events import LoggingEventHandler
from watchdog.observers import Observer
from realtimeasm.handler import AsmFileEventHandler

def main(args):
    observer = Observer()
    observer.schedule(AsmFileEventHandler(args.format), '.', recursive=True)
    observer.start()
    try:
        observer.join()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Assemble code in real time.')
    parser.add_argument('-f', '--format', default='elf64')
    args = parser.parse_args()
    main(args)
