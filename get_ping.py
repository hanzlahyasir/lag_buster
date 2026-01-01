import subprocess
import re
import time
import platform
import locale
import logging

logging.basicConfig(level=logging.INFO)

OS = platform.system()

def get_ping_value(param_count='4', target_ip='1.1.1.1'):
    try:
        param_count = '-n' if OS.lower() == 'windows' else '-c'
        result = subprocess.run(['ping', param_count, '4', target_ip], capture_output=True)
        preferred_encoding = locale.getpreferredencoding(result.stdout)
        output = result.stdout.decode(preferred_encoding)
        regex = r'Average\s*[=<]\s*(\d+\.?\d*)\s*ms' if OS.lower() == 'windows' else r'(\d+\.\d+)/(\d+\.\d+)/(\d+\.\d+)/(\d+\.\d+) ms\n'
        logging.debug(f"Using regex: {regex} for OS: {OS}")
        match = re.search(regex, output)
    except Exception as e:
        logging.error(f"Error executing ping command: {e}")
        return None
    logging.debug(f"Ping output: {match}")
    if match:
        return float(match.group(1 if OS.lower() == 'windows' else 2))
    return None

if __name__ == "__main__":
    while True:
        ping_value = get_ping_value()
        if ping_value is not None:
            print(f"Ping time: {ping_value} ms")
        else:
            print("Ping time not found.")
        time.sleep(2)