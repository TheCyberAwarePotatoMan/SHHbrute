ip_range = input("Enter IP range: ")
segments = ip_range.split(".")  # split IP range into segments

if len(segments) != 4:
    print("Invalid IP range")
else:
    ip_list = []  # initialize empty list to store IP addresses

    for a in range(int(segments[0].split("-")[0]), int(segments[0].split("-")[-1]) + 1):
        for b in range(int(segments[1].split("-")[0]), int(segments[1].split("-")[-1]) + 1):
            for c in range(int(segments[2].split("-")[0]), int(segments[2].split("-")[-1]) + 1):
                for d in range(int(segments[3].split("-")[0]), int(segments[3].split("-")[-1]) + 1):
                    ip = f"{a}.{b}.{c}.{d}"  # concatenate segments to form IP address
                    ip_list.append(ip)  # add IP address to list

    with open('programdata/ips.txt', 'w') as f:
        f.write('\n'.join(ip_list))

    print(ip_list)  # print list of all possible IP addresses
