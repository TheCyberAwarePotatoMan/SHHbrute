# DISCLAIMER:
## This cybersecurity tool is intended for educational and research purposes only. The tool is provided "as is" without warranty of any kind, and is intended to be used at your own risk. The authors of this tool are not responsible for any damage or harm caused by the use or misuse of the tool.
## This tool is designed to identify vulnerabilities and test the security of systems that you own or have permission to test. Any unauthorized or malicious use of the tool is strictly prohibited and may be illegal. You are solely responsible for ensuring that you have the legal right to use the tool in the manner in which it is intended.
## By downloading or using this tool, you agree to be bound by these terms and conditions. If you do not agree to these terms, you should not use the tool.
# USAGE INSTRUCTIONS:
### To use this tool, follow these steps:

### Run iplistmaker.py to generate a list of IP addresses based on your input. The output will be saved to a file called ips.txt.

### Run sshfinder.py to scan the IP addresses in ips.txt for open SSH ports. Any matches will be added to a file called sships.txt.

### Run sshbrute.py to perform a brute force attack on the IP addresses in sships.txt, using a list of 10,000 usernames in user.txt and 10,000 passwords in pass.txt. Any successful login attempts will be recorded in a file called yay.txt.

## Please use this tool responsibly and with caution. If you have any questions or concerns about the legal or ethical implications of using this tool, we strongly encourage you to consult with a lawyer or other legal professional before proceeding.
