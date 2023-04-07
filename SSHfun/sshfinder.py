import socket

# Read in the list of IP addresses from a file
with open('programdata/ips.txt', 'r') as f:
    ips = f.read().splitlines()

# Loop through each IP address and check if it has an open SSH port
with open('programdata/sships.txt', 'w') as f:
    successful_connections = []
    for i, ip in enumerate(ips):
        try:
            # Create a new socket object and attempt to connect to the SSH port
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # set a timeout to prevent the script from hanging indefinitely
            result = sock.connect_ex((ip, 22))

            # If the result is 0, the port is open, otherwise it's closed or filtered
            if result == 0:
                successful_connections.append(ip)

            sock.close()  # close the socket connection

        except Exception as e:
            print(f'Error checking {ip}: {e}')

        # Print progress every 10% and when the loop is complete
        if (i + 1) % (len(ips) // 10) == 0 or i == len(ips) - 1:
            progress = (i + 1) / len(ips) * 100
            print(f'{progress:.0f}% complete')

    print(f'Successful connections: {len(successful_connections)}')

    # Write the list of successful IP addresses to the file
    f.write('\n'.join(successful_connections))
