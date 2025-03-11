import json

def get_ticket(room_number, issue, priority, department):
    ticket_data = {
        "room_number":room_number,
        "issue": issue,
        "priority": priority,
        "department": department
    }
    response = json.dumps(ticket_data, indent=4)
    return response
    
      