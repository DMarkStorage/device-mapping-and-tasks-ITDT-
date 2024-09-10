# device-mapping-and-tasks-ITDT-
**device-mapping-and-tasks** is a command-line tool for managing and inspecting devices in a library system using ITDT (IBM Tape Diagnostic Tool). It allows users to view tasks, logs, drives, slots, and other key components of a tape library, while mapping devices to their respective libraries for easier management and diagnostics.

## Features

- Map devices to their libraries based on vendor information.
- Fetch and display tasks, logs, drives, slots, node cards, cartridges, and more from the library system.
- Provides detailed inspection of various library components.
- Simple CLI interface for querying specific library information.

## Requirements

- Python 3.x
- [docopt](https://github.com/docopt/docopt) - for command-line argument parsing
- [PrettyTable](https://pypi.org/project/prettytable/) - for displaying data in a tabular format
- Pandas - for processing and mapping data

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/DMarkStorage/device-mapping-and-tasks-ITDT-.git
    ```

2. Navigate into the project directory:
    ```bash
    cd device-mapping-and-tasks-ITDT-
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Make sure ITDT is installed and accessible on your system. You can download ITDT from IBM's official website.

## Usage

The program provides several options for querying and inspecting the library system. You can use it to view tasks, logs, drives, and more by specifying the library (`<LIB>`) and the desired action.

### Command-Line Options

```bash
Usage:
    itdt6.py -l <LIB> --vtask
    itdt6.py -l <LIB> --vlogs
    itdt6.py -l <LIB> --vdrives
    itdt6.py -l <LIB> --vlibrary
    itdt6.py -l <LIB> --slots
    itdt6.py -l <LIB> --nodecards
    itdt6.py -l <LIB> --datacart
    itdt6.py -l <LIB> --diagcart
    itdt6.py -l <LIB> --Accessors
    itdt6.py -l <LIB> --cleaningcart

    itdt6.py --version
    itdt6.py -h | --help
```

### Examples

1. **View tasks for a specific library**:
    ```bash
    python itdt6.py -l 1 --vtask
    ```

2. **View logs for a specific library**:
    ```bash
    python itdt6.py -l 2 --vlogs
    ```

3. **View drives in a specific library**:
    ```bash
    python itdt6.py -l 3 --vdrives
    ```

4. **View all slots in a library**:
    ```bash
    python itdt6.py -l 1 --slots
    ```

The `<LIB>` argument specifies the library number (e.g., `1`, `2`, `3`), and the options define the specific action you want to perform.

### Available Options

- `--vtask`: View tasks for the specified library.
- `--vlogs`: View logs for the specified library.
- `--vdrives`: View drives in the specified library.
- `--vlibrary`: View library details.
- `--slots`: View all slots in the library.
- `--nodecards`: View node cards information.
- `--datacart`: View data cartridges in the library.
- `--diagcart`: View diagnostic cartridges.
- `--Accessors`: View access...

### Error Handling

If an error occurs while executing a command, the program will print an error message and exit. Ensure that the ITDT command is correctly installed and accessible.

## Logging

All outputs are displayed in the terminal. If you need to redirect logs or store results in a file, you can modify the script to include logging functionality.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributing

Feel free to submit issues or pull requests to improve the program. Contributions are welcome!
