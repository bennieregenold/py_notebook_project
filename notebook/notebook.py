import datetime

#next available id for new notes
last_id = 0

class Note:
    '''Represents a note in the notebook.'''

    def __init__(self, memo, tags=''):
        '''Initialize a note with memo and optional space-separated tags. Auto set id and create date.'''
        self.memo= memo
        self. tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        '''Determine if this note matches the filter text.

        Search is case sensitive and matches both text and tags.'''

        return filter in self.memo or filter in self.tags


class Notebook:
    '''Represents a collection of notes that can be tagged, modified, and searched'''

    def __init__(self):
        '''Initiate a notebook with an empty list.'''
        self.notes = []

    def new_note(self, memo, tags=''):
        '''Create a new note and add it to the list.'''
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        '''Locate the note with a give id'''
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

    def modify_memo(self, note_id, memo):
        '''Find the note with an id and change its memo.'''
        self._find_note(note_id).memo = memo

    def modify_tags(self, note_id, tags):
        '''Find the note with given id and change its tags.'''
        self._find_note(note_id).tags = tags

    def search(self, filter):
        '''Find all notes that match the given filter string.'''
        return [note for note in self.notes if note.match(filter)]
    
