from core import Journal, JournalEntry
from datetime import datetime

def test_journal_creation():
    journal = Journal()
    assert len(journal.entries) == 0, "New journal should have no entries"
    print("✓ Journal creation test passed")

def test_adding_entry():
    journal = Journal()
    entry = journal.add_entry("Test Title", "Test Content")
    
    assert len(journal.entries) == 1, "Journal should have one entry"
    assert isinstance(entry, JournalEntry), "add_entry should return a JournalEntry object"
    assert entry.title == "Test Title", "Entry title should match input"
    assert entry.content == "Test Content", "Entry content should match input"
    print("✓ Adding entry test passed")

def test_get_all_entries():
    journal = Journal()
    journal.add_entry("Title 1", "Content 1")
    journal.add_entry("Title 2", "Content 2")
    
    entries = journal.get_all_entries()
    assert len(entries) == 2, "Should return all entries"
    assert entries[0].title == "Title 1", "First entry title should match"
    assert entries[1].title == "Title 2", "Second entry title should match"
    print("✓ Get all entries test passed")

def test_get_entry_by_title():
    journal = Journal()
    journal.add_entry("Unique Title", "Content")
    journal.add_entry("Another Title", "Content")
    
    entry = journal.get_entry_by_title("Unique Title")
    assert entry is not None, "Should find entry with matching title"
    assert entry.title == "Unique Title", "Should return correct entry"
    
    # Test case-insensitive search
    entry = journal.get_entry_by_title("unique TITLE")
    assert entry is not None, "Should find entry regardless of case"
    
    # Test non-existent title
    entry = journal.get_entry_by_title("Non-existent")
    assert entry is None, "Should return None for non-existent title"
    print("✓ Get entry by title test passed")

def test_get_entries_by_date():
    journal = Journal()
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Add entries
    journal.add_entry("Today's Entry", "Content")
    
    # Test finding today's entries
    entries = journal.get_entries_by_date(today)
    assert len(entries) == 1, "Should find one entry for today"
    assert entries[0].title == "Today's Entry", "Should find correct entry"
    
    # Test non-existent date
    entries = journal.get_entries_by_date("2000-01-01")
    assert len(entries) == 0, "Should return empty list for date with no entries"
    print("✓ Get entries by date test passed")

def test_clear_journal():
    journal = Journal()
    journal.add_entry("Title", "Content")
    journal.clear()
    
    assert len(journal.entries) == 0, "Journal should be empty after clearing"
    print("✓ Clear journal test passed")

def test_entry_string_representation():
    journal = Journal()
    entry = journal.add_entry("Test Title", "Test Content")
    
    entry_str = str(entry)
    assert "Test Title" in entry_str, "String representation should contain title"
    assert "Test Content" in entry_str, "String representation should contain content"
    print("✓ Entry string representation test passed")

def test_entry_to_dict():
    journal = Journal()
    entry = journal.add_entry("Test Title", "Test Content")
    
    entry_dict = entry.to_dict()
    assert entry_dict['title'] == "Test Title", "Dictionary should contain correct title"
    assert entry_dict['content'] == "Test Content", "Dictionary should contain correct content"
    assert 'date' in entry_dict, "Dictionary should contain date"
    print("✓ Entry to dictionary test passed")

if __name__ == "__main__":
    # Run all tests
    print("Running Journal tests...\n")
    
    try:
        test_journal_creation()
        test_adding_entry()
        test_get_all_entries()
        test_get_entry_by_title()
        test_get_entries_by_date()
        test_clear_journal()
        test_entry_string_representation()
        test_entry_to_dict()
        
        print("\nAll tests passed successfully! ✨")
    except AssertionError as e:
        print(f"\n❌ Test failed: {str(e)}")