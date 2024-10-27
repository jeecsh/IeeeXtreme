import csv
from collections import defaultdict
import io

def process_events(input_data):
    events = []
    
    # Step 1: Read the CSV input
    reader = csv.reader(input_data)
    for row in reader:
        event_id, title, acronym, project_code, three_digit_code, record_type = row
        events.append({
            'event_id': event_id,
            'title': title,
            'acronym': acronym,
            'project_code': project_code,
            'three_digit_code': three_digit_code,
            'record_type': record_type
        })

    # Step 2: Organize events
    parent_events = {}
    child_events = defaultdict(list)

    for event in events:
        if event['record_type'] == "Parent Event":
            parent_events[event['event_id']] = event
        elif event['record_type'] == "IEEE Event":
            # Assign the child to its respective parent
            parent_id = event.get('parent_id')  # Replace this with the actual parent ID if available
            if parent_id:
                child_events[parent_id].append(event)

    # Step 3: Filter events
    filtered_events = []
    
    for parent_id, parent_event in parent_events.items():
        if parent_event['acronym']:  # Ensure parent has an acronym
            children = child_events[parent_id]
            if children:  # Parent must have children
                # Determine project codes from children
                project_codes = {child['three_digit_code'] for child in children}
                if len(project_codes) == 1:
                    parent_event['three_digit_code'] = children[0]['three_digit_code']
                else:
                    parent_event['three_digit_code'] = '???'  # Mixed project codes
                
                # Prepare output for the parent and children
                output_children = []
                for child in children:
                    if child['acronym']:  # Child must have an acronym
                        child['parent_id'] = parent_id  # Append parent ID
                        output_children.append(child)

                # Sort children lexicographically by title, then by event_id
                output_children.sort(key=lambda x: (x['title'], x['event_id']))
                filtered_events.append((parent_event, output_children))

    # Step 4: Sort parent events by acronym
    filtered_events.sort(key=lambda x: x[0]['acronym'])

    # Step 5: Output the results
    output = []
    for parent, children in filtered_events:
        output.append(f"{parent['event_id']},\"{parent['title']}\",\"{parent['acronym']}\","
                      f"{parent['project_code']},{parent['three_digit_code']},\"{parent['record_type']}\"")
        for child in children:
            output.append(f"{child['event_id']},\"{child['title']}\",\"{child['acronym']}\","
                          f"{child['project_code']},{child['three_digit_code']},\"{child['record_type']}\","
                          f"{parent['event_id']}")
    
    return "\n".join(output)

# Step 6: Gather input from the user
def get_input():
    print("Enter event data (CSV format). Type 'END' on a new line to finish:")
    input_lines = []
    
    while True:
        line = input()
        if line.strip() == "END":
            break
        input_lines.append(line)
    
    return io.StringIO("\n".join(input_lines))

# Main program
if __name__ == "__main__":
    input_csv = get_input()
    output = process_events(input_csv)
    print("\nProcessed Output:")
    print(output)
