'''
将数据保存为JSON、CSV和Excel格式
'''
import os
import sys
import argparse
from io import StringIO
import struct
import json
import csv

# 导入数据
def import_data(import_file):
    
    mask = '9s14s5s' #掩码
    data = []
    with open(import_file, 'rb') as f: #从定宽数据文件中读入数据
        for line in f:
            fields = struct.Struct(mask).unpack_from(line)
            data.append(list([str(f).strip() for f in fields]))
    return data

# 导出数据
def write_data(data, export_format):
    #选择导出数据的格式
    if export_format == 'csv':
        return write_csv(data)
    elif export_format == 'json':
        return write_json(data)
    elif export_format == 'xlsx':
        return write_xlsx(data)
    else:
        raise Exception("不合法的格式")

def write_csv(data):
    #导出csv格式的文件
    f = StringIO()
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)
    return f.getvalue()

def write_json(data):
    # 导出json文件
    j = json.dumps(data)
    return j

def write_xlsx(data):
    #导出excel文件
    from xlwt import Workbook
    book = Workbook()
    sheet1 = book.add_sheet("Sheet 1")
    row = 0
    for line in data:
        col = 0
        for datum in line:
            print(datum)
            sheet1.write(row, col, datum)
            col += 1
        row += 1
        # 最大导出65535行
        if row > 65535:
            print("Hit limit of # of rows in one sheet (65535).")
            break
    f = StringIO()
    book.save(f)
    return f.getvalue() 
   
   
if __name__ == '__main__':
    # parse input arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("import_file", help="导入文件的路径")
    parser.add_argument("export_format", help="导出文件的格式：json, csv, xlsx.")
    args = parser.parse_args()

    if args.import_file is None:
        print("需要输入导入文件的路径")
        sys.exit(1)

    if args.export_format not in ('csv','json','xlsx'):
        print("需要选择输出的格式")
        sys.exit(1)

    # verify given path is accesible file
    if not os.path.isfile(args.import_file):
        print(sys.stderr, "Given path is not a file: %s" % args.import_file)
        sys.exit(1)

    # read from formated fixed-width file
    data = import_data(args.import_file)

    # export data to specified format
    # to make this Unix-lixe pipe-able 
    # we just print to stdout
    print(write_data(data, args.export_format))

