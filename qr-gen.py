#! /usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import pyqrcode

def csv_dict_reader(file_obj):
    try:
#read csv
        reader = csv.DictReader(file_obj, delimiter=';')
        rownum = 0
#parsing csv
        for row in reader:
            rownum = rownum + 1
            lname = row['lname']
            fname = row['fname']
            mname = row['mname']
            org = row['org']
            dept = row['dept']
            title = row['title']
            po_box = row['po_box']
            address1 = row['address1']
            address2 = row['address2']
            city = row['city']
            state = row['state']
            index = row['index']
            country = row['country']
            office_phone = row['office_phone']
            mobile_phone = row['mobile_phone']
            fax = row['fax']
            pager = row['pager']
            email = row['email']
            site = row['site']

#create vcard
            vcard = 'BEGIN:VCARD\r\nVERSION:3.0\r\nN:{};{};{}\r\nFN:\r\nORG:{};{}\r\nTITLE:{}\r\nADR:{};{};{};{};{};{};{}\r\nTEL;TYPE=work:{}\r\nTEL;TYPE=cell:{}\r\n\TEL;TYPE=fax:{}\r\nTEL;TYPE=pager:{}\r\nEMAIL;PREF;INTERNET:{}\r\nURL:{}\r\nEND:VCARD'
            vcard = vcard.format(lname, fname, mname, org, dept, title, po_box, address1, address2, city, state, index, country, office_phone, mobile_phone, fax, pager, email, site)
#generate QR
            qr = pyqrcode.create(vcard, error = 'L', encoding = 'utf-8')
            qr.png(lname + ' ' + fname + ' ' + mname + '.png', scale=10)

            print('Printing QR code', rownum)

    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    with open('qr.csv', 'r', encoding='utf-8-sig') as file_obj:
        csv_dict_reader(file_obj)
