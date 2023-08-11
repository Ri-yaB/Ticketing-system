from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample static data of 5 people
people = [
    {"id": "#1", "name": "Person 1", "tickets_assigned": []},
    {"id": "#2", "name": "Person 2", "tickets_assigned": []},
    {"id": "#3", "name": "Person 3", "tickets_assigned": []},
    {"id": "#4", "name": "Person 4", "tickets_assigned": []},
    {"id": "#5", "name": "Person 5", "tickets_assigned": []}
]

# Counter to keep track of the next person to assign tickets to
round_robin_counter = 0

# Route to assign a new ticket
@app.route('/assign_ticket', methods=['POST'])
def assign_ticket():
    global round_robin_counter

    data = request.get_json()
    ticket_id = len(people[round_robin_counter]['tickets_assigned']) + 1
    assigned_to = people[round_robin_counter]['id']
    raised_by = data.get('raised_by')
    issue_description = data.get('issue_description')

    ticket = {
        "id": ticket_id,
        "issue_description": issue_description,
        "assigned_to": assigned_to,
        "raised_by": raised_by
    }

    people[round_robin_counter]['tickets_assigned'].append(ticket)
    round_robin_counter = (round_robin_counter + 1) % len(people)

    return jsonify({"message": "Ticket assigned successfully"})

if __name__ == '__main__':
    app.run(debug=True)
