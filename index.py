import pandas as pd

def read_text_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:  # empty string check
                id_, email = line.split(',', 1)
                data.append({'ID': id_, 'Email': email})
    return data

def main():
    # Reading data from text files
    data1 = read_text_file('index1.txt')
    data2 = read_text_file('index2.txt')
    data3 = read_text_file('index3.txt')

    # Creating a DataFrame from data
    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)
    df3 = pd.DataFrame(data3)

    # Adding a prefix to column names
    df1.columns = ['ID1', 'Email1']
    df2.columns = ['ID2', 'Email2']
    df3.columns = ['ID3', 'Email3']

    # Setting the data type "text" for columns with ids
    df1['ID1'] = df1['ID1'].astype(str)
    df2['ID2'] = df2['ID2'].astype(str)
    df3['ID3'] = df3['ID3'].astype(str)

    # Data merging
    combined_df = pd.concat([df1, df2, df3], axis=1)

    # Writing to Excel file
    combined_df.to_excel('combine.xlsx', index=False)

if __name__ == "__main__":
    main()
