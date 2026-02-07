import sys
import subprocess
import json

if len(sys.argv) < 2:
    print("Usage: python script.py <config_file> ")
    sys.exit(1)


def subprocess_output():
    try:
        result = subprocess.run(["uptime", "-p"], capture_output=True,
                                text=True, check=True)
        output_str = result.stdout
        print(output_str)
        with open("system_health.log", "a") as file:
            file.write(output_str)

    except subprocess.CalledProcessError as e:
        print(f"Command failed with exit code {e.returncode}")


def load_config():
    try:
        with open(sys.argv[1], "r") as config_file:
            config_dict = json.load(config_file)
            print(f"Checking status for: {config_dict["target_service"]}")
        return config_dict

    except FileNotFoundError:
        print(" deploy_config.json not found")
        sys.exit(1)
    except IndexError:
        print("File data missing")
        sys.exit(1)


if __name__ == "__main__":
    load_config()
    subprocess_output()
