import os, sys

# def is_Citibank_eStatement_file(str):
#     return str.find('eStatement_') == 0

if __name__ == '__main__':

    dir = 'D:\download'
    files = os.listdir(dir)

    # files = filter(is_Citibank_eStatement_file, files)
    filtered_files = list( x for x in files if x.find('eStatement_') == 0 )

    sorted_filtered_files = sorted(filtered_files,  key=lambda x: os.path.getmtime(os.path.join(dir, x)), reverse = True)

    # starting from 2014-01 to 2017-11, 12x4-1=47
    # ok, start to rename.
    # src example:          eStatement_1599540611065.pdf
    # chg to:          20-08eStatement_1599540611065.pdf

    year = 2014
    month = 1

    for file in sorted_filtered_files:
        year_str = str(year)[2 : ]

        mon_str = str(month)
        mon_str = mon_str.zfill(2)

        prefix_str = year_str + '-' + mon_str

        new_file_name = os.path.join(dir, prefix_str+file)
        old_file_name = os.path.join(dir, file)

        os.rename(old_file_name, new_file_name)

        if year == 2017 and month == 11:
            sys.exit(0)

        if month == 12:
            year += 1
            month = 1
        else:
            month += 1
