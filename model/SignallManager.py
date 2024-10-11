class SignalManager():
    def __init__(self):
        pass

    def handler_signal(self, event, data):
        """ Manipulador de sinal. """
        if event == 'add':
            print('Added', flush=True)
        if event == 'save':
            print('Saved', flush=True)
        if event == 'searcher':
            text = data.text().lower()
            print(text  , flush=True)