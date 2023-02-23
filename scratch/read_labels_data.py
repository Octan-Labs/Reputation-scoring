import pandas as pd
root_dir = "E:/OCTAN/source/crawling_data/BlockchainSpider/data/bsc_data/labels/cryptoscam"
input_file = "E:/OCTAN/source/crawling_data/BlockchainSpider/data/bsc_data/labels/cryptoscam/labels.cryptoscamdb"

my_dict_list = []

with open(input_file, "r") as in_file:
    for line1 in in_file:
        # print(line1)
        line_dict = {}
        line = line1.replace("}", "")
        line = line.replace("{", "")
        line = line.replace('"', '')
        # print(line)
        for pair in line.split(","):
            if len(pair.split(":")) == 2:
                if pair.split(":")[0] == ' address':
                    line_dict['Address'] = pair.split(":")[1].replace("\n", "")
                if pair.split(":")[0] == ' label':
                    line_dict['Label'] = pair.split(":")[1]
                if pair.split(":")[0] == ' name':
                    line_dict['Name'] = pair.split(":")[1]
                # if pair.split(":")[0] == ' last_name':
                #     if pair.split(":")[1] == ' TORNADO CASH' or pair.split(":")[1] == ' LAZARUS GROUP':
                #         line_dict['NameTag'] = 'SCAM OFAC' + pair.split(":")[1]
                #     else:
                #         line_dict['NameTag'] = 'OFAC' + pair.split(":")[1]
                #line_dict[key_] = value
        my_dict_list.append(line_dict)
df_labels = pd.DataFrame(my_dict_list)
output_csv = root_dir + "/" + "labels_v3.csv"
df_labels.to_csv(output_csv, index=False)