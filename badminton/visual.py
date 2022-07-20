from luck import analyse
from luck.plot import BarChart, PieChart

if __name__ == '__main__':
    data_file = analyse.File('./Data/result.xlsx')

    brand_data = data_file.count('brand')
    species_data = data_file.count('species')
    grade_data = data_file.count('grade')

    # process raw data to display data
    display_data = dict(
        list({
            k: v
            for k, v in sorted(species_data.items(), key=lambda item: item[1])
        }.items())[-2:-9:-1])

    barchart = BarChart()
    barchart.data = brand_data
    barchart.title = 'Badminton Brand'
    barchart.mark_line = False
    barchart.mark_point = True
    barchart.file_name = 'brand.html'
    barchart.data_zoom = True
    barchart.bar_base()
    piechart = PieChart()
    piechart.data = display_data
    piechart.title = 'Badminton Species'
    piechart.file_name = 'species.html'
    piechart.pie_base()

    rosechart = PieChart()
    rosechart.data = display_data
    rosechart.visual_map = True
    rosechart.tool_box = True
    rosechart.title = 'Badminton Species Rose Type'
    rosechart.file_name = 'species_rose.html'
    rosechart.pie_rose()
