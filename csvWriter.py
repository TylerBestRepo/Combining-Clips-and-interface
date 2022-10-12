import csv

def csv_writing_module(stringTakenIn):
    print("Lets see how complex things can get here. Now gonna write a csv")
    # open the file in the write mode
    f = open('/Users/tylerbest/Desktop/Research Assistant/OutputsFromInterface/csv_file.csv', 'w')

    # create the csv writer
    writer = csv.writer(f)
    row = ["bingo","bango","bongo"]
    # write a row to the csv file
    row1 = [stringTakenIn]
    writer.writerow(row1)
    writer.writerow(row)
    writer.writerow(stringTakenIn)

    # close the file
    f.close()