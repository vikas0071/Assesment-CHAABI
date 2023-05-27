# Q2. Dictionary, what?
# Write a program that returns the file type from a file name. The type of the file is determined
# from the extension. Initially, a list of values of the form "extension,type"(e.g. xls,spreadsheet;
# png,image) will be input.
# The program takes input in the following form:
# 1. Input extension and type values in the form of a string having the following format:
# a. "extension1,type1;extension2,type2;extension3,type3"
# b. E.g. If we needed to input xls → spreadsheet, xlsx → spreadsheet, jpg → image
# our string would be something like: "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
# 2. Input a list of filename.extension. E.g. an input list could be something like ["abc.html",
# "xyz.xls", "text.csv", "123"]
# The program should return a dict of filename: type pairs
# E.g.
# f("xls,spreadsheet;xlsx,spreadsheet;jpg,image", ["abc.jpg",
# "xyz.xls", "text.csv", "123"]) should return
# {
# "abc.jpg": "image",
# "xyz.xls": "spreadsheet",
# "Text.csv": "unknown",
# "123": "unknown"
# }


def get_file_types(extension_type_string, filenames):
    # Split the extension and type values and create a dictionary
    extension_type_pairs = extension_type_string.split(';')
    extension_type_dict = dict(pair.split(',') for pair in extension_type_pairs)

    # Create a dictionary of filename to type pairs
    file_type_dict = {}
    for filename in filenames:
        # Get the file extension from the filename
        file_extension = filename.split('.')[-1]

        # Look up the file type in the extension_type_dict
        file_type = extension_type_dict.get(file_extension, 'unknown')

        # Add the filename and type to the file_type_dict
        file_type_dict[filename] = file_type

    return file_type_dict

extension_type_string = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
filenames = ["abc.jpg", "xyz.xls", "text.csv", "123"]
file_types = get_file_types(extension_type_string, filenames)
print(file_types)
