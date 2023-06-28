import csv
import re

#pattern = r".......... .......... .......... .......... .........."

# Open the log file in read mode
with open('routetrace.log', 'r') as log_file:

    # Open the CSV file in write mode
    with open('routetrace.csv', 'w', newline='') as csv_file:

        # Create a CSV writer object
        writer = csv.writer(csv_file)

        # Loop through each line in the log file
        for line in log_file:
            line = line.replace("ms","")
            line = line.replace("(DUP!)","")
            line = line.replace("ttl", "")
            #ip_add = re.search(pattern,line)
            #if ip_add != None:
                #line = line.strip(".......... .......... .......... ..........")
            #line = line.replace("  "," ")
            #fields = line.split("‘/dev/null’")[-1].strip().split(" ")
            fields = line.split(" ")

            # Write the line to the CSV file as a single field
            writer.writerow(fields)




