import csv
import os

def generate_optical_config(csv_filename, output_filename):
    """
    Reads optical span data from a CSV file and generates 
    a generic DWDM/ROADM CLI configuration using string formatting.
    """
    
    if not os.path.exists(csv_filename):
        print(f"Error: {csv_filename} not found.")
        return

    config_blocks = []

    with open(csv_filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            node_name = row['Node_Name']
            interface = row['Interface']
            channel = row['Channel_Number']
            target_power = row['Target_Power_dBm']
            fiber_length = row['Fiber_Length_km']
            span_loss = row['Span_Loss_dB']

            config_block = f"""
! -------------------------------------------
! Configuration for Node: {node_name}
! Fiber Length: {fiber_length} km | Span Loss: {span_loss} dB
! -------------------------------------------
configure terminal
 interface {interface}
  description "Span to {node_name} - {fiber_length}km"
  dwdm-channel {channel}
   power-target {target_power}
   no shutdown
  exit
 exit
commit
"""
            config_blocks.append(config_block)

    with open(output_filename, mode='w', encoding='utf-8') as out_file:
        out_file.write("! Auto-Generated DWDM Configuration\n")
        out_file.write("! Do not edit manually.\n\n")
        out_file.write("\n".join(config_blocks))

    print(f"Success! Configuration generated and saved to '{output_filename}'.")

if __name__ == "__main__":
    INPUT_CSV = "optical_spans.csv"
    OUTPUT_CONFIG = "roadm_config_output.txt"
    generate_optical_config(INPUT_CSV, OUTPUT_CONFIG)
