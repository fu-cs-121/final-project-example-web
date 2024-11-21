# core.py
from datetime import datetime
import json

class JournalEntry:
    def __init__(self, title, content, date=None):
        self.title = title
        self.content = content
        self.date = date if date else datetime.now()
        
    def to_dict(self):
        """Convert entry to dictionary format"""
        return {
            'title': self.title,
            'content': self.content,
            'date': self.date.strftime("%Y-%m-%d %H:%M:%S")
        }
        
    def __str__(self):
        """String representation of the entry"""
        return f"{self.title} ({self.date.strftime('%Y-%m-%d %H:%M:%S')})\n{self.content}"

class Journal:
    def __init__(self):
        self.entries = []
    
    def add_entry(self, title, content):
        """Add a new entry to the journal"""
        entry = JournalEntry(title, content)
        self.entries.append(entry)
        return entry
    
    def get_all_entries(self):
        """Get all journal entries"""
        return self.entries
    
    def get_entry_by_title(self, title):
        """Find an entry by its title"""
        for entry in self.entries:
            if entry.title.lower() == title.lower():
                return entry
        return None
    
    def get_entries_by_date(self, date_str):
        """Find entries by date (YYYY-MM-DD)"""
        matching_entries = []
        for entry in self.entries:
            if entry.date.strftime("%Y-%m-%d") == date_str:
                matching_entries.append(entry)
        return matching_entries
    
    def clear(self):
        """Remove all entries"""
        self.entries = []
    
    def save_to_file(self, filename):
        """Save all entries to a JSON file"""
        entries_data = [entry.to_dict() for entry in self.entries]
        with open(filename, 'w') as f:
            json.dump(entries_data, f, indent=4)
        print(f"Journal saved to {filename}.")
    
    def load_from_file(self, filename):
        """Load entries from a JSON file"""
        try:
            with open(filename, 'r') as f:
                entries_data = json.load(f)
            self.entries = []
            for data in entries_data:
                title = data['title']
                content = data['content']
                date_str = data['date']
                date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
                entry = JournalEntry(title, content, date)
                self.entries.append(entry)
            print(f"Journal loaded from {filename}.")
        except FileNotFoundError:
            print(f"File '{filename}' not found. Starting with an empty journal.")
            self.entries = []
    
    def __str__(self):
        """String representation of the journal"""
        return "\n".join(str(entry) for entry in self.entries)