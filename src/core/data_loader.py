import json

class DataLoader:
    """Load Data from rooms.json and students.json files"""
    def load_json(self, file_path: str) -> list[dict]:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            if not data:
                print("File is empty")
            if not isinstance(data, list):
                raise TypeError(f"Data in files is not list format")
            print(f"Data from {file_path} loaded successfully")

            return data
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            raise
        except json.JSONDecodeError:
            print(f"Error in json formatting while loading: {file_path}")
            raise
        except Exception as e:
            print(f"Unknown error while loading: {e}")

if __name__ == '__main__':
    rooms_path = "../../data/rooms.json"

    loader = DataLoader()
    try:
        rooms_data = loader.load_json(rooms_path)
        print(rooms_data)
    except Exception:
        print("Loading stopped")


#may add os library for file path