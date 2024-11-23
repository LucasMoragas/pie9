from data_sources.serial_comm import SerialComm
from plotter.plotter import Plotter

def main():
    # Configura a comunicação serial
    serial_port = "COM3"  # Substitua pela porta correta do seu Arduino (ex.: /dev/ttyUSB0 no Linux)
    baudrate = 9600  # Deve ser o mesmo configurado no Arduino

    try:
        # Instancia o comunicador serial
        serial_comm = SerialComm(port=serial_port, baudrate=baudrate)

        # Instancia o plotter e conecta à comunicação serial
        plotter = Plotter()
        print("Conectado à porta serial. Recebendo dados...")
        plotter.run(serial_comm)

    except Exception as e:
        print(f"Erro: {e}")
    finally:
        # Fecha a conexão serial quando o programa é encerrado
        if 'serial_comm' in locals():
            serial_comm.close()
            print("Conexão serial encerrada.")

if __name__ == "__main__":
    main()
