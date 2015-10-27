# Program starts automatically when you run it in Python console.
# Or, you can type 'ask_user()'


import csv

# these are lists of townships and boroughs in PE coverage area, sorted by county
c_localities = ["ARISTES", "BENTON", "BERWICK", "BLOOMSBURG", "CATAWISSA", "MIFFLINVILLE", "MILLVILLE", "NUMIDIA", "ORANGEVILLE", "STILLWATER", "WILBURTON"]
m_localities = ["DANVILLE", "WASHINGTONVILLE"]
lu_localities = ["BEACH HAVEN", "HUNLOCK CREEK", "MOCANAQUA", "NESCOPECK", "SHICKSHINNY", "WAPWALLOPEN"]
ly_localities = ["UNITYVILLE"]
n_localities = ["ELYSBURG", "PAXINOS", "RIVERSIDE", "TURBOTVILLE"]

# arrays for storing lottery winners by county
columbia_cnty = []
montour_cnty = []
luzerne_cnty = []
lycoming_cnty = []
norry_cnty = []

# this is a list of counties in PE coverage area
cnty_list = [["COLUMBIA", "COLUMBIAPA", "COLUMBIA PA", columbia_cnty], ["MONTOUR", "MONTOURPA", "MONTOUR PA", montour_cnty], ["LUZERNE", "LUZERNEPA", "LUZERNE PA", luzerne_cnty], ["LYCOMING", "LYCOMINGPA", "LYCOMING PA", lycoming_cnty], ["NORTHUMBERLAND", "NORTHUMBERLANDPA", "NORTHUMBERLAND PA", norry_cnty]]

# this is a list of all localities in PE coverage area
locality_list = []
locality_list.extend(c_localities)
locality_list.extend(m_localities)
locality_list.extend(lu_localities)
locality_list.extend(ly_localities)
locality_list.extend(n_localities)

# arrays for storing lottery winners by locality
aristes = []
benton = []
berwick = []
bloomsburg = []
catawissa = []
mifflinville = []
millville = []
numidia = []
orangeville = []
stillwater = []
wilburton = []
danville = []
washingtonville = []
beach_haven = []
hunlock_creek = []
mocanaqua = []
nescopeck = []
shickshinny = []
wapwallopen = []
unityville = []
elysburg = []
paxinos = []
riverside = []
turbotville = []

# array of arrays by locality. locality_arrays_list[i] is parallel to locality_list[i]
locality_arrays_list = [aristes, benton, berwick, bloomsburg, catawissa, mifflinville, millville, numidia, orangeville, stillwater, wilburton, danville, washingtonville, beach_haven, hunlock_creek, mocanaqua, nescopeck, shickshinny, wapwallopen, unityville, elysburg, paxinos, riverside, turbotville]

# final list of local winners, filtered down from arrays of winners by county
lotto_list = []

# opens csv file for some Python processing!
def file_opener(file_name):
    with open (file_name + '.csv', newline='') as f:
        global reader, new_list
        reader = csv.reader(f)
        county_sorter() # must call county_sorter() within file_opener. Else we get error of "I\O file is closed."
        new_list = open(file_name + ".txt", "w")

        
# sorts winners by county
def county_sorter():
    for row in reader:
        for cnty in cnty_list:
            if (cnty[0] in row) or (cnty[1] in row) or (cnty[2] in row):
                cnty[3].append(row)

# checks if winner's town is in PE coverage area, ex. as listed in 'c_localities'
def county_checker():
    for cnty in cnty_list:
        for winner in cnty[3]:
            # winner[i] might differ if the csv file stores "town" in different index/column
            if winner[1] in locality_list:
                print(winner)
                lotto_list.append(winner)

# sorts winners by locality (town, township, etc.)
def town_sorter():
    for winner in lotto_list:
        for area in locality_list:
            if winner[1] == area:
                # matches winner's hometown with locality_arrays_list[i] that matches locality_list[i]
                locality_arrays_list[locality_list.index(area)].append(winner)

# Makes list of lotto winners inside new txt file.
def list_maker():
    global new_list
    for locality in locality_arrays_list:
        # If a locality array has a winner, write the locality name as a subhead.
        if len(locality) > 0:
            new_list.write("\n")
            new_list.write(locality_list[locality_arrays_list.index(locality)].title())
            new_list.write("\n")
        # Writes winners' names, prizes and the games they won
        for winner in locality:
            # ("MOO MOO").title() returns "Moo Moo". What a handy string method!!
            # winner[i][0:-3] changes "$1,000.00" to "$1,000"
            new_list.write("• " + winner[0].title() + ", " + winner[-1][0:-3] + " from " + winner[-2].title())
            new_list.write("\n")

# Closes new txt file.
def file_close():
    new_list.close()

# Asks user for name of source csv. Passes user's input into def file_opener.
def ask_user():
    original_list = input("Enter name of csv file to compile. Omit '.csv' extension.")
    file_opener(original_list)
    county_checker()
    town_sorter()
    list_maker()
    file_close()

ask_user()
