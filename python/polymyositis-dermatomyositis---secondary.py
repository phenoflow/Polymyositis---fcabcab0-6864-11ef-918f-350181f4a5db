# phekb, 2024.

import sys, csv, re

codes = [{"code":"1570614","system":"ICD10CM"},{"code":"1570616","system":"ICD10CM"},{"code":"1570618","system":"ICD10CM"},{"code":"45553168","system":"ICD10CM"},{"code":"45553170","system":"ICD10CM"},{"code":"45562710","system":"ICD10CM"},{"code":"45586956","system":"ICD10CM"},{"code":"1570614","system":"ICD10CM"},{"code":"1570616","system":"ICD10CM"},{"code":"45562710","system":"ICD10CM"},{"code":"45553168","system":"ICD10CM"},{"code":"1570618","system":"ICD10CM"},{"code":"45553170","system":"ICD10CM"},{"code":"45586956","system":"ICD10CM"},{"code":"44796752","system":"ICD10CM"},{"code":"44796752","system":"ICD10CM"},{"code":"1570614","system":"ICD10CM"},{"code":"1570616","system":"ICD10CM"},{"code":"1570618","system":"ICD10CM"},{"code":"45553168","system":"ICD10CM"},{"code":"45553170","system":"ICD10CM"},{"code":"45562710","system":"ICD10CM"},{"code":"45586956","system":"ICD10CM"},{"code":"1570614","system":"ICD10CM"},{"code":"1570616","system":"ICD10CM"},{"code":"45562710","system":"ICD10CM"},{"code":"45553168","system":"ICD10CM"},{"code":"1570618","system":"ICD10CM"},{"code":"45553170","system":"ICD10CM"},{"code":"45586956","system":"ICD10CM"},{"code":"44796752","system":"ICD10CM"},{"code":"44796752","system":"ICD10CM"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('polymyositis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["polymyositis-dermatomyositis---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["polymyositis-dermatomyositis---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["polymyositis-dermatomyositis---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
