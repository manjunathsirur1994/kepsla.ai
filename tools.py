tool = [{
    "type": "function",
    "function": {
        "name": "ticket_generator",
        "description": "Generate a ticket for the addressed issue by the customer",
        "parameters": {
            "type": "object",
            "properties": {
                "issue": {
                    "type": "string",
                    "description": "The issue addressed by the customer"
                },
                "priority": {
                    "type": "integer",
                    "description": "Prioritize on a scale of 5, based on the customer sentiment"
                },
                "department": {
                    "type": "string",
                    "description": "Assign the issue to the concerned department"
                },
                "room_number": {
                    "type": "integer",
                    "description": "ask for the room number of the customer"
                }
            },
            "required": ["issue", "priority", "department", "room_number"]
        }
    }
}
]