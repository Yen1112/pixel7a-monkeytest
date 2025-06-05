import subprocess

package_name = "com.android.chrome"
event_count = 1000

print(f"Running Monkey test on: {package_name} for {event_count} events")

try:
    subprocess.run([
        "adb", "shell", "monkey",
        "-p", package_name,
        "-v", str(event_count)
    ], check=True)
    print("Monkey test completed.")
except subprocess.CalledProcessError as e:
    print("Monkey test failed.")
    print(e)
