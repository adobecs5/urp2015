__author__ = 'CJeon'
'''
Used to process excel data into clothing_data_class class and save it.
uses pickle.
'''
if __name__ == "__main__":
    import pickle
    from classes.clothing_data_class import clothing_data as cd
    raw_file = open("data/Dresses_Attribute_Sales/Attribute DataSet.csv", "r")
    raw_file_lines = raw_file.readlines()
    raw_file.close()
    clothing_data_list = [] # a list of clothing_data_class
    pickled_file = "data/pickled_clothing_data_class"

    for a_raw_data in raw_file_lines:
        list_of_attributes = a_raw_data.split(",")
        # remove line breakers
        list_of_attributes[-1] = list_of_attributes[-1].replace("\n", "")
        clothing_data_list.append(cd(list_of_attributes))

    # dump to pickle
    with open(pickled_file, "wb") as f:
        pickle.dump(clothing_data_list, f)


    # when you need to load pickled data, load like below.
    with open(pickled_file, "rb") as f:
        load = pickle.load(f)
    # usage example
    print(load[0])

