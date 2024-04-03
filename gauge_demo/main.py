################################################################################################
# DEMO Routine
# required: analoggaugewidget_demo.ui
# compile analoggaugewidget_demo.ui -> analoggaugewidget_demo_ui.py
# show a lot of variables and possibilities formodification
################################################################################################
from PySide6.QtWidgets import QApplication, QMainWindow

# QtWidgets -> QPolygon, QPolygonF, QColor, QPen, QFont,
#       -> QWidget
#       -> QApplication

from PySide6.QtCore import *

if __name__ == "__main__":

    def main():
        app = QApplication()
        my_gauge = AnalogGaugeWidget()
        my_gauge.show()

    class mainclass:

        def __init__(self):
            import sys

            from analoggaugewidget_demo_ui import Ui_MainWindow

            self.app = QApplication(sys.argv)
            window = QMainWindow()
            self.my_gauge = Ui_MainWindow()
            self.my_gauge.setupUi(window)
            window.show()
            self.my_gauge.widget.enable_barGraph = True

            self.my_gauge.widget.value_needle_snapzone = 1

            self.my_gauge.widget.value_min = 0
            self.my_gauge.widget.value_max = 1100
            self.my_gauge.widget.scala_main_count = 11
            self.my_gauge.ActualSlider.setMaximum(self.my_gauge.widget.value_max)
            self.my_gauge.ActualSlider.setMinimum(self.my_gauge.widget.value_min)
            self.my_gauge.AussenRadiusSlider.setValue(
                self.my_gauge.widget.gauge_color_outer_radius_factor * 1000
            )
            self.my_gauge.InnenRadiusSlider.setValue(
                self.my_gauge.widget.gauge_color_inner_radius_factor * 1000
            )

            self.my_gauge.GaugeStartSlider.setValue(
                self.my_gauge.widget.scale_angle_start_value
            )
            self.my_gauge.GaugeSizeSlider.setValue(
                self.my_gauge.widget.scale_angle_size
            )

            # set Start Value
            # self.my_gauge.widget.update_value(self.my_gauge.widget.value_min)
            self.my_gauge.widget.update_value(
                int(self.my_gauge.widget.value_max - self.my_gauge.widget.value_min) / 2
            )

            ################################################################################################
            # Anzeigenadel Farbe anpassen
            # auf Slider Aenderung reagieren
            self.my_gauge.RedSlider_Needle.valueChanged.connect(self.set_NeedleColor)
            self.my_gauge.GreenSlider_Needle.valueChanged.connect(self.set_NeedleColor)
            self.my_gauge.BlueSlider_Needle.valueChanged.connect(self.set_NeedleColor)
            self.my_gauge.TrancSlider_Needle.valueChanged.connect(self.set_NeedleColor)

            # LCD Default Werte festlegen
            self.my_gauge.lcdNumber_Red_Needle.display(
                self.my_gauge.RedSlider_Needle.value()
            )
            self.my_gauge.lcdNumber_Green_Needle.display(
                self.my_gauge.GreenSlider_Needle.value()
            )
            self.my_gauge.lcdNumber_Blue_Needle.display(
                self.my_gauge.RedSlider_Needle.value()
            )
            self.my_gauge.lcdNumber_Trancparency_Needle.display(
                self.my_gauge.TrancSlider_Needle.value()
            )

            ################################################################################################
            # Anzeigenadel Farbe anpassen bei manueller Beswegung
            # auf Slider Aenderung reagieren
            self.my_gauge.RedSlider_NeedleDrag.valueChanged.connect(
                self.set_NeedleColorDrag
            )
            self.my_gauge.GreenSlider_NeedleDrag.valueChanged.connect(
                self.set_NeedleColorDrag
            )
            self.my_gauge.BlueSlider_NeedleDrag.valueChanged.connect(
                self.set_NeedleColorDrag
            )
            self.my_gauge.TrancSlider_NeedleDrag.valueChanged.connect(
                self.set_NeedleColorDrag
            )

            # LCD Default Werte festlegen
            self.my_gauge.lcdNumber_Red_NeedleDrag.display(
                self.my_gauge.RedSlider_NeedleDrag.value()
            )
            self.my_gauge.lcdNumber_Green_NeedleDrag.display(
                self.my_gauge.GreenSlider_NeedleDrag.value()
            )
            self.my_gauge.lcdNumber_Blue_NeedleDrag.display(
                self.my_gauge.BlueSlider_NeedleDrag.value()
            )
            self.my_gauge.lcdNumber_Trancparency_NeedleDrag.display(
                self.my_gauge.TrancSlider_NeedleDrag.value()
            )

            ################################################################################################
            # Skala Text Farbe anpassen
            # auf Slider Aenderung reagieren
            self.my_gauge.RedSlider_Scale.valueChanged.connect(self.set_ScaleValueColor)
            self.my_gauge.GreenSlider_Scale.valueChanged.connect(
                self.set_ScaleValueColor
            )
            self.my_gauge.BlueSlider_Scale.valueChanged.connect(
                self.set_ScaleValueColor
            )
            self.my_gauge.TrancSlider_Scale.valueChanged.connect(
                self.set_ScaleValueColor
            )

            # LCD Default Werte festlegen
            self.my_gauge.lcdNumber_Red_Scale.display(
                self.my_gauge.RedSlider_Scale.value()
            )
            self.my_gauge.lcdNumber_Green_Scale.display(
                self.my_gauge.GreenSlider_Scale.value()
            )
            self.my_gauge.lcdNumber_Blue_Scale.display(
                self.my_gauge.BlueSlider_Scale.value()
            )
            self.my_gauge.lcdNumber_Trancparency_Scale.display(
                self.my_gauge.TrancSlider_Scale.value()
            )

            ################################################################################################
            # Display Text Farbe anpassen
            # auf Slider Aenderung reagieren
            self.my_gauge.RedSlider_Display.valueChanged.connect(
                self.set_DisplayValueColor
            )
            self.my_gauge.GreenSlider_Display.valueChanged.connect(
                self.set_DisplayValueColor
            )
            self.my_gauge.BlueSlider_Display.valueChanged.connect(
                self.set_DisplayValueColor
            )
            self.my_gauge.TrancSlider_Display.valueChanged.connect(
                self.set_DisplayValueColor
            )

            # LCD Default Werte festlegen
            self.my_gauge.lcdNumber_Red_Display.display(
                self.my_gauge.RedSlider_Display.value()
            )
            self.my_gauge.lcdNumber_Green_Display.display(
                self.my_gauge.GreenSlider_Display.value()
            )
            self.my_gauge.lcdNumber_Blue_Display.display(
                self.my_gauge.BlueSlider_Display.value()
            )
            self.my_gauge.lcdNumber_Trancparency_Display.display(
                self.my_gauge.TrancSlider_Display.value()
            )

            self.my_gauge.CB_barGraph.stateChanged.connect(self.en_disable_barGraph)
            self.my_gauge.CB_ValueText.stateChanged.connect(self.en_disable_ValueText)
            self.my_gauge.CB_CenterPoint.stateChanged.connect(
                self.en_disable_CB_CenterPoint
            )
            self.my_gauge.CB_ScaleText.stateChanged.connect(self.en_disable_ScaleText)
            self.my_gauge.CB_ShowBarGraph.stateChanged.connect(
                self.set_enable_filled_Polygon
            )

            self.my_gauge.CB_Grid.stateChanged.connect(self.set_enable_Scale_Grid)
            self.my_gauge.CB_fineGrid.stateChanged.connect(
                self.set_enable_fine_Scale_Grid
            )

            self.my_gauge.CB_Needle.stateChanged.connect(self.en_disable_Needle)

            # my_gauge.widget.set_scale_polygon_colors([[.0, Qt.transparent]])
            # my_gauge.widget.set_scale_polygon_colors([[.0, Qt.yellow]])
            # my_gauge.widget.set_scale_polygon_colors(None)
            # my_gauge.widget.enable_filled_Polygon = False
            sys.exit(self.app.exec_())

        def set_NeedleColor(self):
            # print(self.my_gauge.RedSlider.value())
            R = self.my_gauge.RedSlider_Needle.value()
            G = self.my_gauge.GreenSlider_Needle.value()
            B = self.my_gauge.BlueSlider_Needle.value()
            Transparency = self.my_gauge.TrancSlider_Needle.value()
            # print(R, G, B, Transparency)
            self.my_gauge.widget.set_NeedleColor(
                R=R, G=G, B=B, Transparency=Transparency
            )

        def set_NeedleColorDrag(self):
            # print(self.my_gauge.RedSlider.value())
            R = self.my_gauge.RedSlider_NeedleDrag.value()
            G = self.my_gauge.GreenSlider_NeedleDrag.value()
            B = self.my_gauge.BlueSlider_NeedleDrag.value()
            Transparency = self.my_gauge.TrancSlider_NeedleDrag.value()
            # print(R, G, B, Transparency)
            self.my_gauge.widget.set_NeedleColorDrag(
                R=R, G=G, B=B, Transparency=Transparency
            )

        def set_ScaleValueColor(self):
            # print(self.my_gauge.RedSlider.value())
            R = self.my_gauge.RedSlider_Scale.value()
            G = self.my_gauge.GreenSlider_Scale.value()
            B = self.my_gauge.BlueSlider_Scale.value()
            Transparency = self.my_gauge.TrancSlider_Scale.value()
            # print(R, G, B, Transparency)
            self.my_gauge.widget.set_ScaleValueColor(
                R=R, G=G, B=B, Transparency=Transparency
            )

        def set_DisplayValueColor(self):
            # print(self.my_gauge.RedSlider.value())
            R = self.my_gauge.RedSlider_Display.value()
            G = self.my_gauge.GreenSlider_Display.value()
            B = self.my_gauge.BlueSlider_Display.value()
            Transparency = self.my_gauge.TrancSlider_Display.value()
            # print(R, G, B, Transparency)
            self.my_gauge.widget.set_DisplayValueColor(
                R=R, G=G, B=B, Transparency=Transparency
            )

        def en_disable_barGraph(self):
            self.my_gauge.widget.set_enable_barGraph(
                self.my_gauge.CB_barGraph.isChecked()
            )

        def en_disable_ValueText(self):
            self.my_gauge.widget.set_enable_value_text(
                self.my_gauge.CB_ValueText.isChecked()
            )

        def en_disable_CB_CenterPoint(self):
            self.my_gauge.widget.set_enable_CenterPoint(
                self.my_gauge.CB_CenterPoint.isChecked()
            )

        def en_disable_Needle(self):
            self.my_gauge.widget.set_enable_Needle_Polygon(
                self.my_gauge.CB_Needle.isChecked()
            )

        def en_disable_ScaleText(self):
            self.my_gauge.widget.set_enable_ScaleText(
                self.my_gauge.CB_ScaleText.isChecked()
            )

        def set_enable_filled_Polygon(self):
            self.my_gauge.widget.set_enable_filled_Polygon(
                self.my_gauge.CB_ShowBarGraph.isChecked()
            )

        def set_enable_Scale_Grid(self):
            self.my_gauge.widget.set_enable_big_scaled_grid(
                self.my_gauge.CB_Grid.isChecked()
            )

        def set_enable_fine_Scale_Grid(self):
            self.my_gauge.widget.set_enable_fine_scaled_marker(
                self.my_gauge.CB_fineGrid.isChecked()
            )

    ############################################
    # Run DEMO Routine
    ############################################
    main = mainclass()
