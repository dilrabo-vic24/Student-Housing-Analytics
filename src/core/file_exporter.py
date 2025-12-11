import json
import xml.etree.ElementTree as ET

class FileExplorer:
    def save_to_json(self, data, file_path):
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False, default=str)
            print(f"Data saved in json. File path: {file_path}")
        except Exception as e:
            print(f"Error while saving data in json: {e}")
    
    def save_to_xml(self, data, file_path):
        try:
            root = ET.Element("root")

            for item in data:
                row_elem = ET.SubElement(root, "row")
                for key, value in item.items():
                    tag_name = str(key).replace(" ", "-")
                    child = ET.SubElement(row_elem, tag_name)
                    child.text = str(value)

            tree = ET.ElementTree(root)
            tree.write(file_path, encoding="utf-8", xml_declaration=True)
            print(f"Data saved in xml file. File path: {file_path}")

        except Exception as e:
            print(f"Error while saving data in xml: {e}")