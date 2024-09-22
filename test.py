import pandas
from main import DrawingPlots
import os
import unittest


class TestDrawingPlots(unittest.TestCase):
    def setUp(self):
        self.json_file = "deviation.json"
        self.drawing = DrawingPlots(self.json_file)

    def test_draw_plots_output(self):
        """Тест проверяет, что функция draw_plots возвращает список путей к файлам."""
        plot_paths = self.drawing.draw_plots()
        self.assertIsNotNone(plot_paths, "Функция должна вернуть список путей")
        self.assertIsInstance(plot_paths, list, "Результат должен быть списком")
        self.assertGreater(len(plot_paths), 0, "Список путей не должен быть пустым")
        for path in plot_paths:
            self.assertTrue(os.path.exists(path), f"Файл {path} должен существовать")

    def test_draw_plots_with_empty_dataframe(self):
        """Тест проверяет поведение функции, если датафрейм пустой."""
        # Создаём пустой датафрейм для теста
        self.drawing.dataframe = pandas.DataFrame()
        plot_paths = self.drawing.draw_plots()
        self.assertIsNone(plot_paths, "Функция должна вернуть None для пустого датафрейма")

    def test_draw_plots_missing_columns(self):
        """Тест проверяет, что функция правильно обрабатывает отсутствие нужных столбцов."""
        self.drawing.dataframe = self.drawing.dataframe.drop(columns=["gt_corners", "rb_corners"])
        plot_paths = self.drawing.draw_plots()
        self.assertIsNone(plot_paths, "Функция должна вернуть None при отсутствии необходимых столбцов")


# Запуск всех тестов
if __name__ == '__main__':
    unittest.main()
