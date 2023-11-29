import serial
import time

def send_sms(serial_port, phone_number, message):
    serial_port.write(b'AT\r')
    time.sleep(1)
    serial_port.write(b'AT+CMGF=1\r')  # Set SMS text mode
    time.sleep(1)
    serial_port.write(f'AT+CMGS="{phone_number}"\r'.encode())  # Set recipient number
    time.sleep(1)
    serial_port.write(message.encode() + b'\x1A')  # Send message and Ctrl+Z to end
    time.sleep(2)

def main():
    port_name = 'COM3'  # Replace with your modem's serial port
    phone_numbers = ['+79811437228', '+987654321']  # Add recipient numbers
    message = 'Your bulk message here'

    try:
        with serial.Serial(port_name, 9600, timeout=1) as ser:
            for number in phone_numbers:
                send_sms(ser, number, message)
                print(f"Message sent to {number}")
    except serial.SerialException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()