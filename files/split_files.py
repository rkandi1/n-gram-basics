
def line_counting():
    """
    Adds the index to each query and places the total number of queries on the top.
    Reads and writes the the same file.
    """
    with open("edited_queries.txt", 'r+') as f:
        i = 0
        successful_write = True
        for line in f:
            line = str(i+1) + '.' + line
            i += 1
            try:
                f.write(line)
            except IOError:
                print("Value could not be written written")
                successful_write = False

        if successful_write:
            f.seek(0)
            f.write(str(i) + "\n")

            print("Values written")

def split_file(file):
    """
    Splits the clueweb dataset into the training set and the test set.
    Training set will have it's own file, and so will test set.
    :param file: Name of the file
    """
    train_write = open("train_set.txt", 'w')
    test_write = open("test_set.txt", 'w')
    try:
        with open(file) as f:
            size = int(f.readline())
            train_size = int(size * 0.8)
            index = 0
            while index != train_size:
                r_line = str(f.readline())
                index += 1
                train_write.write(r_line)

            while index != size:
                r_line = str(f.readline())
                index += 1
                test_write.write(r_line)

    except IOError:
        print("Couldn't work with the train or test set.")
    finally:
        train_write.close()
        test_write.close()


if __name__ == "__main__":
    # line_counting() // Only need this once.
    # split_file("edited_queries.txt") // Only need this once also.
    pass
