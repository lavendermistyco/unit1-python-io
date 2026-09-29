import os
import time
from datetime import datetime

def get_container_boot_metrics():
    """Calculates how long ago the cloud container booted up via PID 1."""
    try:
        # In Linux/Docker, PID 1 creation timestamp represents container spin-up time
        container_start_timestamp = os.stat('/proc/1').st_ctime
        current_time = time.time()
        
        # Calculate elapsed boot duration in seconds
        boot_seconds = round(current_time - container_start_timestamp, 2)
        boot_formatted_time = datetime.fromtimestamp(container_start_timestamp).strftime('%H:%M:%S UTC')
        
        return boot_seconds, boot_formatted_time
    except Exception as e:
        return None, str(e)

def main():
    print("\n" + "=" * 50)
    print(" 🚀 CLOUD COMPUTE INTERFACE INITIALIZED")
    print("=" * 50)
    time.sleep(0.8)

    # Capture user string data from keyboard input
    player_name = input("\nEnter your Engineer Call Sign: ")
    print(f"\n[SYSTEM]: Establishing network handshake for user: {player_name}...")
    time.sleep(1)

    # Telemetry & Boot Analytics Block
    print("\n" + "-" * 50)
    print(" 📡 TELEMETRY & CONTAINER BOOT METRICS")
    print("-" * 50)
    
    boot_seconds, boot_time = get_container_boot_metrics()
    
    if boot_seconds is not None:
        print(f" ⏱️  Container Spawn Time : {boot_time}")
        print(f" ⚡ Container Boot Age  : {boot_seconds} seconds")
        
        # Dynamic feedback based on boot speed
        if boot_seconds < 30:
            print(" 🟢 Status: FAST BOOT (Low network latency)")
        elif boot_seconds < 60:
            print(" 🟡 Status: NOMINAL BOOT (Standard cloud provisioning)")
        else:
            print(" 🔴 Status: DELAYED BOOT (Network rate-limit or queue detected)")
    else:
        print(" ⚠️ Could not determine container boot time.")

    print("-" * 50)
    time.sleep(1)

    # Final Execution Confirmation
    print("\n==================================================")
    print(f" SUCCESS! Engineer {player_name}, your thin-client")
    print(" tablet is successfully executing Python 3 inside")
    print(" a remote cloud container.")
    print("==================================================\n")

if __name__ == "__main__":
    main()
