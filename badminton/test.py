from __const import *

if __name__ == '__main__':
    main_list = load_pkl("./Data/detail.pkl")
    print(type(main_list[0]))





    # process raw data to display data
    # display_data = dict(
    #     list({
    #         k: v
    #         for k, v in sorted(species_data.items(), key=lambda item: item[1])
    #     }.items())[-2:-9:-1])
    # rosechart = PieChart()
    # rosechart.data = display_data
    # rosechart.pie_rose()
