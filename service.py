from formula import evaluate
from storage import FileStore
class Service:
    def __init__(self,root):self.store=FileStore(root);self.sheets=self.store.load()
    def apply(self,q):
        if q['op']=='create':self.sheets.setdefault(q['sheet'],{});self.store.save(self.sheets);return {'sheet':q['sheet']}
        if q['op']=='read':
            cells=self.sheets[q['sheet']];value=cells.get(q['ref']);return {'input':value,'value':evaluate(value,cells)}
        return {'error':'UNSUPPORTED'}
