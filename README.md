# Data Reader

## Project Description

**Data Reader** is a Python-based application designed to analyze log files and extract critical operational insights. This tool processes a given log file to calculate metrics like error percentages, warning-error correlations, average operation durations, and the most frequent error messages across different system modules. The results are outputted in a structured JSON format for further analysis or integration with other tools.

### Key Features:
- **Operation Counting**: Tracks the total number of operations performed by each module.
- **Error and Warning Analysis**: Counts errors and warnings per module, along with detailed error messages.
- **Error-Warning Relationship**: Identifies cases where warnings occurred just before an error in a specific operation.
- **Operation Timing**: Calculates the average time taken for operations to complete per module.
- **Modular and Extensible**: Code can be easily extended for more complex log formats and analysis metrics.

This project is designed to be flexible, allowing easy integration with existing infrastructure for monitoring and log analysis.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Log File Generation](#log-file-generation)
- [Example](#example)
- [Output Structure](#output-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Installation

### Prerequisites
Ensure you have the following installed:
- **Python 3.6+**

No external libraries are required as the project uses Python's built-in libraries, but for good practice, you may wish to use a virtual environment.

### Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/serrayildiz/DataReader.git
   cd DataReader
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. **Activate the virtual environment**:
   ```bash
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
   
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
---

## Usage

To run the **Data Reader** application, use the following command:

```bash
python ./reader.py ./path/to/logfile.txt -o /path/to/output.json
```

- `filepath`: The path to the log file to be processed.
- `-o` or `--output`: Specifies the output file (optional; defaults to `result.json`).

### Optional Flags:
- `-o`, `--output`: Path to the output JSON file. If not specified, the results are saved in `result.json`.

---

## Log File Generation

To facilitate testing, you can generate log files of various sizes using the provided script. This script creates log files with different numbers of entries and a sample empty log file. Here’s how you can generate them:


### Log Generation Commands
To generate log files, run the following commands:
```bash
python logcreater.py
```

This will create the following files:
- `log_0_entries.txt` (empty log file)
- `log_50_entries.txt` (small log file with 50 entries)
- `log_1000_entries.txt` (medium log file with 1000 entries)
- `log_5000_entries.txt` (large log file with 5000 entries)

### Testing Commands
To test the **Data Reader** with generated log files, use the following commands:

- For `log_example.txt`:
  ```bash
  python ./reader.py ./log_example.txt -o ./result.json
  ```

- For `log_0_entries.txt`:
  ```bash
  python ./reader.py ./log_0_entries.txt -o ./result0.json
  ```

- For `log_50_entries.txt`:
  ```bash
  python ./reader.py ./log_50_entries.txt -o ./result50.json
  ```

- For `log_1000_entries.txt`:
  ```bash
  python ./reader.py ./log_1000_entries.txt -o ./result1000.json
  ```

- For `log_5000_entries.txt`:
  ```bash
  python ./reader.py ./log_5000_entries.txt -o ./result5000.json
  ```

---

## Output Structure

The output of **Data Reader** is a JSON file containing various analytics, including error counts, warning-error relations, and more. Below is the structure of the output JSON:

```json
{
  "date": "2024-09-12",
  "operations": {
    "Module_A": 120,
    "Module_B": 85
  },
  "errors": {
    "Module_A": 5,
    "Module_B": 2
  },
  "errors_percentage": {
    "Module_A": 4.17,
    "Module_B": 2.35
  },
  "warning_error_relation": {
    "Module_A": 60.0,
    "Module_B": 50.0
  },
  "most_frequent_errors": {
    "Module_A": "NullPointerException",
    "Module_B": "TimeoutError"
  },
  "average_operation_duration": {
    "Module_A": 5.8,
    "Module_B": 4.1
  }
}
```

### Explanation:
- **date**: The date of the log file's first entry.
- **operations**: The total number of operations processed by each module.
- **errors**: The number of errors that occurred in each module.
- **errors_percentage**: The percentage of operations that resulted in errors for each module.
- **warning_error_relation**: The percentage of warnings that were followed by an error within the same operation.
- **most_frequent_errors**: The most frequent error message for each module.
- **average_operation_duration**: The average time (in seconds) taken for operations to complete in each module.

---

## Development & Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request

. We welcome all contributions, including but not limited to:
- Bug fixes
- Performance improvements
- Feature requests

### Steps to Contribute:
1. Fork the repository
2. Create your feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature or fix"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a Pull Request on GitHub.

---

## License

This project is licensed under the [MIT License](LICENSE). You're free to use, modify, and distribute the software in your own projects, both commercial and non-commercial, as long as the original license terms are respected.

---

## Future Enhancements
Potential improvements to the project may include:
- **Custom Log Format Support**: Add support for user-defined log formats.
- **Visualization**: Include a dashboard or graphs to visualize the metrics.
- **Parallel Processing**: Speed up log processing by handling large logs in parallel.

---

## Contact

For any questions or feedback, please reach out to [serrayildiz1@gmail.com](mailto:serrayildiz1@gmail.com).

