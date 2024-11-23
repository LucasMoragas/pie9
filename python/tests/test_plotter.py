from python.plotter.plotter import Plotter
from python.data_sources.mock_data_source import MockDataSource

def main():
    # Configura a fonte de dados simulada   
    mock_data_source = MockDataSource(min_value=10, max_value=90, delay=0.1)

    # Inicia o plotter com os dados simulados
    plotter = Plotter()
    plotter.run(mock_data_source)

if __name__ == "__main__":
    main() 
