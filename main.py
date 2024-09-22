import pandas
import matplotlib.pyplot as pyplot
import os


class DrawingPlots:
    def __init__(self, json_paket):
        self.dataframe = pandas.read_json(json_paket)

    def draw_plots(self, out_folder="result"):
        try:
            if not os.path.exists(out_folder):
                os.makedirs(out_folder)

            plot_paths = []

            print("Удаляем пробелы из названий столбцов")
            self.dataframe.columns = self.dataframe.columns.str.strip()
            print("Имеющиеся столбцы:", self.dataframe.columns.tolist())

            if ("name" in self.dataframe.columns and
                    "gt_corners" in self.dataframe.columns and
                    "rb_corners" in self.dataframe.columns):

                print("Столбцы найдены. Создаю график...")

                try:
                    pyplot.clf()
                    fig, ax = pyplot.subplots(figsize=(19.2, 10.8))
                    self.dataframe[["name", "gt_corners", "rb_corners"]].plot(
                        x="name",
                        y=["gt_corners", "rb_corners"],
                        kind="bar",
                        ax=ax
                    )
                    print("График построен.")

                except Exception as e:
                    print(f"Ошибка при построении графика: {e}")
                    return None

                finally:
                    pyplot.title("Corners of Gt_corners & Rb_corners")
                    pyplot.xlabel("Room Name")
                    pyplot.ylabel("Number of Corners")
                    pyplot.xticks(rotation=45)
                    plot_path = os.path.join(out_folder, "corners_result.jpg")

                    pyplot.savefig(plot_path)
                    pyplot.close()

                    plot_paths.append(plot_path)
                    return plot_paths

            else:
                print("Ошибка: Одно или несколько столбцов отсутствуют.")
                return None

        except Exception as e:
            print(f"Произошла ошибка: {e}")
            return None
