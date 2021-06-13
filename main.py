import serial

ser = serial.Serial()

ser.baudrate = 9600
ser.port = '/dev/ttyUSB0'
ser.open()

print("___________Listening_to_UART_sinals___________")
while True:
    if ser.in_waiting:
        data = ser.readline()
        try:
            print(data.decode('utf'))
        except UnicodeDecodeError:
            print(data)
