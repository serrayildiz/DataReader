import random
import datetime

# Log templates
statuses = ['INFO', 'WARNING', 'ERROR']
modules = ['Main', 'T1_measure', 'T2_measure']
messages = [
    "Updating", "Progressing", "Message here", "Connection dropped",
    "Operation aborted", "You know this is random, right?", 
    "One does not simply walk into Mordor", "An error occurred and the operation failed",
    "Memory index out of bound"
]

# Function to generate log entries
def generate_log_entries(num_entries):
    log_entries = []
    timestamp = datetime.datetime(2022, 1, 25, 11, 0, 0)  # Starting time
    entry_count = 0
    
    active_modules = {}  # To track which modules are currently active

    while entry_count < num_entries:
        # Choose a new module to start
        module = random.choice(modules)
        
        if module not in active_modules:
            # Start a new module
            timestamp += datetime.timedelta(seconds=random.randint(1, 5))  # Shorter time interval
            start_log = f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')}   INFO      {module:<15} Starting"
            log_entries.append(start_log)
            active_modules[module] = True
            entry_count += 1

            # Generate intermediate messages
            while entry_count < num_entries - 1 and random.choice([True, False]):
                timestamp += datetime.timedelta(seconds=random.randint(1, 5))  # Shorter time interval
                status = random.choice(['WARNING', 'ERROR'])
                message = random.choice(messages)
                log_entries.append(f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')}   {status:<8} {module:<15} {message}")
                entry_count += 1
            
            # End with "Operation complete" entry
            timestamp += datetime.timedelta(seconds=random.randint(1, 5))  # Shorter time interval
            complete_log = f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')}   INFO      {module:<15} Operation complete"
            log_entries.append(complete_log)
            active_modules.pop(module)  # Module is no longer active
            entry_count += 1
        else:
            # Random non-INFO log for the remaining single entry if no modules are active
            if not active_modules:
                timestamp += datetime.timedelta(seconds=random.randint(1, 5))  # Shorter time interval
                status = random.choice(statuses)
                module = random.choice(modules)
                message = random.choice(messages)
                log_entries.append(f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')}   {status:<8} {module:<15} {message}")
                entry_count += 1

    return log_entries

# Function to create logs of different sizes
def create_logs(sizes):
    for size in sizes:
        if size == 0:
            # Create an empty file
            with open(f"log_{size}_entries.txt", 'w') as f:
                pass  # Create an empty file
        else:
            log_entries = generate_log_entries(size)
            with open(f"log_{size}_entries.txt", 'w') as f:
                f.write('\n'.join(log_entries))

# Define sizes for small, medium, large logs and an empty file
sizes = {'empty': 0, 'small': 50, 'medium': 1000, 'large': 5000}

# Create logs
create_logs(sizes.values())
