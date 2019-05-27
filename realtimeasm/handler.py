from watchdog.events import PatternMatchingEventHandler, FileSystemEvent
from watchdog.observers import Observer
from tempfile import NamedTemporaryFile
from hexdump import hexdump
import subprocess

def run(cmd):
    res = subprocess.run(cmd, shell=True)
    return res.returncode == 0

class AsmFileEventHandler(PatternMatchingEventHandler):
    def __init__(self, fmt):
        super().__init__(patterns=['*.asm'])
        run('clear')
        self.fmt = fmt

    def on_modified(self, event):
        run('clear')
        filename = event.src_path
        with NamedTemporaryFile('w', delete=False) as temp:
            with open(filename) as f:
                temp.write(f.read())
            filename = temp.name
        objfile = filename + '.o'
        binfile = filename + '.bin'
        if not run('nasm -f %s %s -o %s' % (self.fmt, filename, objfile)):
            return
        run('objcopy -O binary %s %s' % (objfile, binfile))
        with open(binfile, 'rb') as f:
            hexdump(f.read())
        run('objdump -d -M intel %s' % objfile)
