from PyQt5.QtWidgets import ( QWidget, )

class FeatureSelectionForm(QWidget):
    def __init__(self, photos_path: list, checked_features: list = []):
        super().__init__()
        self.photos_path = photos_path
        self.checked_features = checked_features
        self.setWindowTitle('feature Selection')
        self.resize(500, 480)
