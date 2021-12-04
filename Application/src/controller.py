from matplotlib import pyplot as plt

from model import Model
import Ui_Simulation
from PyQt5.QtWidgets import QMainWindow

class control(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Simulation.Ui_MainWindow()
        self.ui.setupUi(self)
        #self.ui.updateButton.clicked.connect(self.update_view)
        self.m = Model(self.ui)
        self.m.stateChangedSignal.connect(self.update_view)
        self.start()

    def start(self):
        self.m.run_simu()
    
    def update_view(self):
        self.ui.animationSubstrat.data_ref.set_data(self.m.concentrations)
        self.ui.animationSubstrat.draw()
        self.ui.graph_1.data_ref.set_data(self.m.concentrations)
        self.ui.graph_1.draw()
        self.ui.graph_2.data_ref.set_data(self.m.concentrations)
        self.ui.graph_2.draw()
