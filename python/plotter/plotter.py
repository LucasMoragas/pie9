import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Plotter:
    def __init__(self):
        self.data = []
        
        
    def update(self, frame, data_source):
        """Atualiza o gráfico com novos dados da fonte."""
        line = data_source.read_line()
        if line is not None:
            try:
                value = int(line)
                self.data.append(value)
                self.data = self.data[-30:]  # Mantém os últimos 100 pontos
                plt.cla()
                plt.plot(self.data, label="Sensor Data")
                plt.ylim(0, 50)
                plt.legend()
                plt.title("Real-Time Data Plot")
                plt.xlabel("Time")
                plt.ylabel("Value")
            except ValueError:
                pass

    def run(self, data_source):
        """Inicia a animação do gráfico com a fonte de dados."""
        fig = plt.figure()
        ani = FuncAnimation(fig, self.update, fargs=(data_source,), interval=100)
        plt.show()