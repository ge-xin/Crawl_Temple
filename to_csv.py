from parser import HTMLTableParser
import csv
import codecs
import xlwt

if __name__ == '__main__':
    f = open('temple.html', 'r', encoding='utf-8')
    xhtml = f.read()
    p = HTMLTableParser()
    p.feed(xhtml)

    data = p.tables[0]

    o = open('temple_for_python.csv', 'w+')

    for d in data:
        for i in range(0, len(d) - 1):
            d[i] = ''.join(d[i].splitlines())


    writer = csv.writer(o, dialect='excel')
    writer.writerows(data)

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('A Test Sheet')

    for i, l in enumerate(data):
        for j, col in enumerate(l):
            ws.write(i, j, col)

    wb.save('temple_for_excel.xls')
    # print(len(data))
    # # j = 1
    # for d in data:
    #     # o.write(str(j) + ',')
    #     # j += 1
    #     for i in range(0, len(d) - 1):
    #         str = ''.join(d[i].splitlines())
    #         o.write(str + ',')
    #     o.write(d[-1] + '\n')

    f1 = open('temple_for_python.csv', 'r')
    reader = csv.reader(f1)

    list = []
    for row in reader:
        list.append(row)

    for i in range(0, len(list)):
        if(data[i] != list[i]):
            print(i)
            print(data[i])
            print(list[i])
            break


    print('done')