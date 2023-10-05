import pandas as pd
# Replace 'your_file.xlsx' with the actual file path of your Excel file
df = pd.read_excel('/Users/muna/Documents/iMessage-Data.xlsx', sheet_name='iMessages')

column_names = df.columns
print(column_names)


# Assuming the 'User_ID' column contains 'MPesa'
messages_from_mpesa = df[df['User_ID'] == 'MPESA']
print(messages_from_mpesa)

# messages_from_mpesa [81].split()[2][3:]
for i in messages_from_mpesa:
    try:
        paid=float(i.split()[2][3:])
    except ValueError:
        pass
    else:
        print(paid)




