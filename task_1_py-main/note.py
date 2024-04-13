import json
import datetime
import os

NOTES_FILE = 'notes.json'

def create_note():
    try:
        note_id = input("Enter note ID: ")
        title = input("Enter note title: ")
        body = input("Enter note body: ")
        created_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        note = {
            "id": note_id,
            "title": title,
            "body": body,
            "created_date": created_date
        }
        return note
    except Exception as e:
        print("An error occurred while creating the note:", e)
        return None

def save_notes(notes):
    try:
        with open(NOTES_FILE, 'w') as file:
            json.dump(notes, file, indent=4)
    except Exception as e:
        print("An error occurred while saving notes:", e)

def read_notes():
    try:
        if not os.path.exists(NOTES_FILE):
            print("No notes found.")
            return

        with open(NOTES_FILE) as file:
            notes = json.load(file)
            for note in notes:
                print("ID: ", note["id"])
                print("Title: ", note["title"])
                print("Body: ", note["body"])
                print("Created on: ", note["created_date"])
                print()
    except Exception as e:
        print("An error occurred while reading notes:", e)


def filter_notes_by_date(date):
    try:
        if not os.path.exists(NOTES_FILE):
            print("No notes found.")
            return []

        with open(NOTES_FILE) as file:
            notes = json.load(file)
            filtered_notes = [note for note in notes if note["created_date"].split()[0] == date]
            if not filtered_notes:
                print("No notes found for the specified date.")
                return []

            print("Notes found for the specified date:")
            for i, note in enumerate(filtered_notes):
                print(f"{i+1}. ID: {note['id']}, Title: {note['title']}")
            return filtered_notes
    except Exception as e:
        print("An error occurred while filtering notes by date:", e)
        return []


def print_selected_note(filtered_notes):
    try:
        if not filtered_notes:
            return

        choice = int(input("Enter the number of the note to view: "))
        selected_note = filtered_notes[choice - 1]
        print("Selected note:")
        print("ID: ", selected_note["id"])
        print("Title: ", selected_note["title"])
        print("Body: ", selected_note["body"])
        print("Created on: ", selected_note["created_date"])
    except (IndexError, ValueError):
        print("Invalid input. Please enter a valid note number.")

def edit_note(note_id):
    try:
        if not os.path.exists(NOTES_FILE):
            print("No notes found.")
            return

        with open(NOTES_FILE, 'r') as file:
            notes = json.load(file)

        for note in notes:
            if note["id"] == note_id:
                title = input("Enter new title: ")
                body = input("Enter new body: ")
                note["title"] = title
                note["body"] = body
                note["created_date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                break

        save_notes(notes)
    except Exception as e:
        print("An error occurred while editing note:", e)

def delete_note(note_id):
    try:
        if not os.path.exists(NOTES_FILE):
            print("No notes found.")
            return

        with open(NOTES_FILE, 'r') as file:
            notes = json.load(file)

        notes = [note for note in notes if note["id"] != note_id]
        save_notes(notes)
    except Exception as e:
        print("An error occurred while deleting note:", e)

def main():
    while True:
        print("1. Create a new note")
        print("2. Read all notes")
        print("3. Read notes by date range")
        print("4. Print selected note")
        print("5. Edit a note")
        print("6. Delete a note")
        print("7. Search notes by date")
        print("8. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                note = create_note()
                if note:
                    if not os.path.exists(NOTES_FILE):
                        save_notes([note])
                    else:
                        with open(NOTES_FILE, 'r') as file:
                            notes = json.load(file)
                            notes.append(note)
                        save_notes(notes)
            elif choice == "2":
                read_notes()
            elif choice == "3":
                start_date = input("Enter start date (YYYY-MM-DD): ")
                end_date = input("Enter end date (YYYY-MM-DD): ")
                filtered_notes = filter_notes_by_date(start_date, end_date)
            elif choice == "4":
                if filtered_notes:
                    print_selected_note(filtered_notes)
                else:
                    print("No filtered notes available. Please perform search operation first.")
            elif choice == "5":
                note_id = input("Enter note ID to edit: ")
                edit_note(note_id)
            elif choice == "6":
                note_id = input("Enter note ID to delete: ")
                delete_note(note_id)
            elif choice == "7":
                search_date = input("Enter date to search (YYYY-MM-DD): ")
                filtered_notes = filter_notes_by_date(search_date)
            elif choice == "8":
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()