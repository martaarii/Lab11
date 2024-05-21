import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listColor = []

    def fillDD(self):
        colori = self._model.get_all_color()
        for color in colori:
            self._view._ddcolor.options.append(ft.dropdown.Option(color))
        self._view.update_page()

    def handle_graph(self, e):
        colore = self._view._ddcolor.value
        anno = self._view._ddyear.value
        self._model.get_grafo(anno, colore)
        num_nodi = self._model.num_vertici()
        num_archi = self._model.num_archi()
        self._view.txtOut.controls.append(ft.Text(f"Numero archi: {num_archi}\n"
                                                  f"Numero nodi: {num_nodi}"))
        self._view.update_page()

    def fillDDProduct(self):
        pass

    def handle_search(self, e):
        pass
