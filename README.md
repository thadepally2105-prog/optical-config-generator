# optical-config-generator
Optical Config Generator
A sanitized, generic Python automation tool that demonstrates how to parse optical planning data (CSV) and generate DWDM/ROADM node configurations.

Note: This repository uses generic, mock data to demonstrate Python automation skills due to NDA/proprietary restrictions on actual vendor tools and planning exports (like NPT).

Features
CSV Parsing: Reads span/channel data exported from an optical planning tool.
String Formatting: Uses Python f-strings to dynamically generate vendor-agnostic CLI configurations.
File I/O: Writes the generated commands to a text file ready for deployment via SSH/Netconf.
How to Run
Ensure you have Python 3 installed.
Clone this repository: git clone https://github.com/thadepally2105-prog/optical-config-generator.git
Navigate into the directory: cd optical-config-generator
Run the script: python3 generate_config.py
View the generated output: cat roadm_config_output.txt
Real-World Application
In a production environment (e.g., using data exported from tools like C-DOT NPT), this logic is extended to:

Parse GMPLS topology and ROADM constraints (WSS/MCS parameters).
Generate full node bootstraps (OSPF-TE, RSVP-TE, LSP definitions).
Push configurations via Netconf/SSH using libraries like netmiko or ncclient.
