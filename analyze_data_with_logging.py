import logging


def analyze_signal(filename):
    in_file = open(filename, 'r')
    number_of_positives = 0
    total_number = 0
    logging.basicConfig(filename="signal_analysis.log", filemode="w",
                        level=logging.DEBUG)
    while True:
        new_data = in_file.read(1)
        total_number += 1
        if new_data == "+":
            number_of_positives += 1
        elif new_data == "0":
            logging.warning("Signal contains a '0'")
        elif new_data == "-":
            logging.info("Signal contains a -")
        elif new_data == "\n":
            break
        elif new_data not in ["+", "-", "0"]:
            logging.error("Signal contains an invalid character")

    percent_positive = round(number_of_positives / total_number * 100, 1)
    return percent_positive


if __name__ == '__main__':
    answer = analyze_signal("signal.txt")
    print("Percent positive = {}".format(answer))
