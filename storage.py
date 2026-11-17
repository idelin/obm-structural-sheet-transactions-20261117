import json,os
from pathlib import Path
class FileStore:
    def __init__(self,root):self.root=Path(root);self.root.mkdir(exist_ok=True)
    def load(self):
        p=self.root/'state.json';return json.loads(p.read_text()) if p.exists() else {}
    def save(self,state):
        p=self.root/'next.json'
        with p.open('w') as f:json.dump(state,f);f.flush();os.fsync(f.fileno())
        p.replace(self.root/'state.json')
