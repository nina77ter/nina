# chapter 10: Files and Exception

# with open('filepath') as aliasNameForTheFile:
#    line1 = aliasNameForTheFile.read()
#    line2 = aliasNameForTheFile.read()
#    line3 = aliasNameForTheFile.read()
#
#    all_lines = aliasNameForTheFile.readline()
#
#    file_content = aliasNameForTheFile.read()
#
#    aliasNameForTheFile.close()
filepath = '../data/product'
with open(filepath) as  prod_list:
    contents = prod_list.read()
    print("Contents of the filr:\n,", contents)

with open(filepath) as prod_list:
    print("now we are trying to loop through the contents")
    all_lines = prod_list.readline()
    print(all_lines)
for line in all_lines:
    print(line)

print('************ WRITE FILE *********************')
with open(filepath, 'a') as prod_list:
    prod_list.write('playstation 5\n')
    prod_list.write('Learning Python book\n')
    prod_list.write("first head to Selenium book\n")


filepath1= '../data/credentials.yml'

with open(filepath1, 'r') as stream:
    credentials = yaml.safe_load(stream):

print(credentials)
qa_uname = credentials['qa']['username']
qa_uname = credentials['qa']['pasword']
qa_uname = credentials['uat']['username']


