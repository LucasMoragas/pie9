import serial

class SerialComm:
    def __init__(self, port, baudrate=9600):
        self.serial = serial.Serial(port, baudrate, timeout=1)

    def read_line(self):
        """Lê uma linha de dados da porta serial."""
        if self.serial.in_waiting > 0:
            return self.serial.readline().decode('utf-8').strip()
        return None

    def close(self):
        """Fecha a conexão serial."""
        self.serial.close()
