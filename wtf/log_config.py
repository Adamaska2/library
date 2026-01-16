import logging

def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('library.log'),  # логи в файл
            logging.StreamHandler()              # оги в консоль
        ]
    )