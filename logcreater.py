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
    
    while entry_count < num_entries:
        if num_entries - entry_count > 1:
            # INFO operation starts and ends with "Operation complete"
            timestamp += datetime.timedelta(seconds=random.randint(1, 60))
            start_log = f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')}   INFO      {random.choice(modules):<15} Starting"
            log_entries.append(start_log)
            entry_count += 1
            
            # Add intermediate random messages (up to the remaining entry count - 1)
            for _ in range(random.randint(0, min(2, num_entries - entry_count - 1))):
                timestamp += datetime.timedelta(seconds=random.randint(1, 60))
                status = random.choice(['WARNING', 'ERROR'])
                module = random.choice(modules)
                message = random.choice(messages)
                log_entries.append(f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')}   {status:<8} {module:<15} {message}")
                entry_count += 1
            
            # Add Operation complete, this must always happen if an INFO "Starting" occurred
            timestamp += datetime.timedelta(seconds=random.randint(1, 60))
            complete_log = f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')}   INFO      {random.choice(modules):<15} Operation complete"
            log_entries.append(complete_log)
            entry_count += 1
        else:
            # Random non-INFO log for the remaining single entry
            timestamp += datetime.timedelta(seconds=random.randint(1, 60))
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
