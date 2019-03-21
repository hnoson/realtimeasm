from watchdog.events import PatternMatchingEventHandler, FileSystemEvent
from tempfile import NamedTemporaryFile
from hexdump import hexdump
import subprocess

def run(cmd: str) -> bool:
    res = subprocess.run(cmd, shell=True)
    return res.returncode == 0

class AsmFileEventHandler(PatternMatchingEventHandler):
    def __init__(self) -> None:
        super().__init__(patterns=['*.asm'])
        run('clear')

    def on_modified(self, event: FileSystemEvent) -> None:
        run('clear')
        filename = event.src_path
        with NamedTemporaryFile('w', delete=False) as temp:
            with open(filename) as f:
                temp.write(f.read())
            filename = temp.name
        objfile = filename + '.o'
        binfile = filename + '.bin'
        if not run('nasm -f elf64 %s -o %s' % (filename, objfile)):
            return
        run('objcopy -O binary %s %s' % (objfile, binfile))
        with open(binfile, 'rb') as f:
            hexdump(f.read())
