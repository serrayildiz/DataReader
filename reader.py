from collections import defaultdict
import json
import argparse
import datetime


def parselogline(line):
    """
    Parses a single line of the log file and returns the extracted components.
    """
    parts = line.split()
    datetime_str = ' '.join(parts[:2])  
    msgtype = parts[2]
    module_name = parts[3]
    message = ' '.join(parts[4:])
    return datetime_str, msgtype, module_name, message


def process_log_file(filepath):
    operations_count = defaultdict(int)
    errors_count = defaultdict(int)
    error_messages = defaultdict(lambda: defaultdict(int))
    warnings_before_errors = defaultdict(int)
    warnings_count = defaultdict(int)
    current_operation_error = defaultdict(bool)
    current_operation_warning = defaultdict(bool)
    operation_start_time = defaultdict(str)
    operation_durations = defaultdict(list)
    log_date = None

    with open(filepath, 'r') as file:
        for line in file:
            datetime_str, msgtype, module_name, message = parselogline(line)
            date = datetime_str.split()[0]

            # Normalize the module_name to ensure consistent casing
            module_name = module_name.replace('_', ' ').title().replace(' ', '_')

            # Set log_date once based on the first entry
            if log_date is None:
                log_date = date

            # Increment operation count for each log entry per module
            operations_count[module_name] += 1

            if msgtype == "INFO" and "Starting" in message:
                current_operation_error[module_name] = False
                current_operation_warning[module_name] = False
                operation_start_time[module_name] = datetime_str  # Store start time

            elif msgtype == "WARNING":
                current_operation_warning[module_name] = True
                warnings_count[module_name] += 1

            elif msgtype == "ERROR":
                # Count every error occurrence for the module
                current_operation_error[module_name] = True
                errors_count[module_name] += 1
                error_messages[module_name][message] += 1

                # Check if a warning occurred just before this error in the same operation
                if current_operation_warning[module_name]:
                    warnings_before_errors[module_name] += 1

                # Reset the warning flag after the error has been processed
                current_operation_warning[module_name] = False

            elif msgtype == "INFO" and "Operation complete" in message:
                # Calculate operation duration
                if operation_start_time[module_name]:
                    start_datetime = datetime.datetime.strptime(operation_start_time[module_name], "%Y-%m-%d %H:%M:%S")
                    end_datetime = datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
                    duration = (end_datetime - start_datetime).total_seconds()
                    operation_durations[module_name].append(duration)

    # Calculate average durations and identify most frequent errors
    average_durations = {module: sum(times) / len(times) if times else 0 for module, times in operation_durations.items()}

    most_frequent_errors = {module: max(errors.items(), key=lambda x: x[1])[0] if errors else "None" for module, errors in error_messages.items()}

    # Calculate error percentages and warning-error relation
    errors_percentage = {module: round(errors_count[module] / operations_count[module] * 100, 2) if operations_count[module] else 0 for module in operations_count}
    warning_error_percentage = {module: round(warnings_before_errors[module] / warnings_count[module] * 100, 2) 
                            if warnings_count[module] > 0 else 0 
                            for module in warnings_count}

    # Build the final output dictionary
    result = {
        "date": log_date,
        "operations": dict(operations_count),
        "errors": dict(errors_count),
        "errors_percentage": {k: round(v, 2) for k, v in errors_percentage.items()},
        "warning_error_relation": dict(warning_error_percentage),
        "most_frequent_errors": most_frequent_errors,
        "average_operation_duration": average_durations
    }

    return result



def main():
    parser = argparse.ArgumentParser(description="Process a log file and analyze system behavior.")
    parser.add_argument('filepath', type=str, help="The path to the log file to be processed.")
    parser.add_argument('-o', '--output', type=str, default='result.json', help="Output JSON file path.")

    args = parser.parse_args()

    # Process the log file and capture the results
    result = process_log_file(args.filepath)
    print(result)

    # Save the result to a JSON file specified by the output argument
    with open(args.output, 'w') as json_file:
        json.dump(result, json_file, indent=4)


if __name__ == "__main__":
    main()
