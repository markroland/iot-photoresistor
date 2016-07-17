import serial
from datetime import datetime

# Open serial connection
ser = serial.Serial('/dev/ttyACM0', 9600)

# Open data file. Truncate. Don't buffer.
f = open('./data/data.csv', 'w', 0)

# Write header
f.write("Time,Value\n")

# Set flag to log to file. This is necessary since several readings per second may
# be coming through the serial port
save_to_file = 1

# Do forever...
while 1:

    # Get current time
    now = datetime.now()

    # Read from serial
    serial_line = ser.readline()

    # Define the data to log to
    line = "%s,%s" % ('{:%Y-%m-%d %H:%M:%S}'.format(now), serial_line.replace("\r",""))

    # Display incoming Serial data
    # print(line.replace("\n",""))

    # If seconds read as "00", then save to file if "save_to_file" flag is
    # set to 1 (otherwise ignore it and don't save). Reset the flag to "save" (1)
    # at the next second, "01".
    if '{:%S}'.format(now) == "00":
        if save_to_file == 1:
            f.write(line)
            # f.flush() # Unnecessary when buffering is disabled?
            save_to_file = 0
    if '{:%S}'.format(now) == "01":
        save_to_file = 1

# Close file
f.close()

# Close serial connection
ser.close()
