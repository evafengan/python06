# """openpyxl打开excel"""
# from openpyxl import Workbook
# wb = Workbook()
#
# # grab the active worksheet
# ws = wb.active
#
# # Data can be assigned directly to cells
# ws['A1'] = 42
#
# # Rows can also be appended
# ws.append([1, 2, 3])
#
# # Python types will automatically be converted
# import datetime
# ws['A2'] = datetime.datetime.now()
#
# # Save the file
# wb.save("/Users/eva/Documents/hogwards202009/code/python06/07/sample.xlsx")
#
# import os
# os.remove("/Users/eva/Documents/hogwards202009/code/python06/07/demo.yaml")


import yaml

#打印成列表形式
print(yaml.load("""
 - Hesperiidae
 - Papilionidae
 - Apatelodidae
 - Epiplemidae
 """, Loader=yaml.FullLoader))

#打印成字典形式
print(yaml.load("""
a: 1
 """, Loader=yaml.FullLoader))

print(yaml.dump({'a': [1, 2]}))

#打开一个demo.yaml文件
print(yaml.load(open("demo.yaml"), Loader=yaml.FullLoader))



