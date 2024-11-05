# MAC Changer

A Python script to change the MAC address of the `eth0` network interface. This script uses the `ifconfig` command to bring the interface down, change its MAC address, and bring it back up. A progress bar visualizes the process.

## Features
- Brings down the network interface, changes the MAC address, and brings it back up.
- Progress bar to visualize processing status.

### Prerequisites
- **Python 3.x** is required.
- **tqdm** for the progress bar display.
  
You can install `tqdm` via pip:
```bash
pip install tqdm
```

- **sudo privileges** are needed to change the MAC address and modify network interface settings.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/MAC_Changer.git
   cd MAC_Changer
   ```

2. Install `tqdm` if you haven't already:

   ```bash
   pip install tqdm
   ```

3. Run the script:

   ```bash
   sudo python3 Mac_Changer.py
   ```

## Usage

Run the script with `sudo` to ensure it has permission to modify network interface settings:

```bash
sudo python3 Mac_Changer.py
```

## Script Breakdown

- **`run_command(command)`**: Executes shell commands and checks for success.
- The script brings down the `eth0` interface, changes its MAC address to `00:11:22:33:44:55`, and then re-enables it.
- A progress bar indicates ongoing processing.

> **Note**: Ensure you replace `eth0` with the actual network interface name on your machine.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
