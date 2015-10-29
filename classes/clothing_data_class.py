__author__ = 'CJeon'

"""
clothing attributes를 효율적으로 관리하는 class
"""

class clothing_data(object):

    def __init__(self, attribute_list):
        self.attributes = attribute_list

    def __repr__(self):
        # to support print
        # when called, it will print all the attributes.
        return str(self.get_attributes())

    def get_attributes(self, attribute_name = None):
        """
        :param attribute_name: a string of required attribute or list of strings.
        ex0) attribute_name = "Size"
        ex1) attribute_name = ["Size", "Rating"]
        :return: a string, or float value
        POWER HARD CODING!
        """
        if attribute_name == None:
            return self.attributes
        assert type(attribute_name) == type([]) or type(attribute_name) == type("")
        if type(attribute_name) == type([]):
            # if attribute_name is a list, i.e. multiple attributes are asked
            return_list = []
            for a_name in attribute_name:
                return_list.append(self.get_attributes(a_name))
            return return_list

        if attribute_name == "Dress_ID" or attribute_name == "did":
            return self.attributes[0]
        elif attribute_name == "Style" or attribute_name == "st":
            return self.attributes[1]
        elif attribute_name == "Price" or attribute_name == "p":
            return self.attributes[2]
        elif attribute_name == "Rating" or attribute_name == "r":
            return self.attributes[3]
        elif attribute_name == "Size" or attribute_name == "sz":
            return self.attributes[4]
        elif attribute_name == "Season" or attribute_name == "sn":
            return self.attributes[5]
        elif attribute_name == "NeckLine" or attribute_name == "nl":
            return self.attributes[6]
        elif attribute_name == "SleeveLength" or attribute_name == "sl":
            return self.attributes[7]
        elif attribute_name == "waiseline" or attribute_name == "wl":
            return self.attributes[8]
        elif attribute_name == "Material" or attribute_name == "m":
            return self.attributes[9]
        elif attribute_name == "FabricType" or attribute_name == "ft":
            return self.attributes[10]
        elif attribute_name == "Decoration" or attribute_name == "dc":
            return self.attributes[11]
        elif attribute_name == "Pattern Type" or attribute_name == "pt":
            return self.attributes[12]
        else:
            raise Exception("No such attribute. ", attribute_name)


