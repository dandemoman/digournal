months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
import json
import os
monthLengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def create_json(filename: str, root_name: str="2025" ):
    data = {
        "name": root_name,
        "children": []
    }
    for i in range(12):
        month = {
            "name": months[i],
            "children": []
        }
        for j in range(monthLengths[i]):
            day = {
                "name": str(j + 1),
                "children": []
            }
            month["children"].append(day)
        data["children"].append(month)
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

create_json("calendar.json", "2025")