import pandas as pd
import streamlit as st 
from constants import PathOfFile
def generate_code():
    st.title("To transform clinical study data from RAW to SDTM")

    # Upload raw file
    column_mapping = st.file_uploader("Upload Column Level Mapping File")
    raw_mapping = st.file_uploader("Upload Row Level Mapping File")
        
    # Read technical details file
    column_mapping =  pd.read_csv(column_mapping)
    raw_mapping = pd.read_csv(raw_mapping)


    prompt = """**You are a helpful assistant who is guiding in writing the Python program and always following the instructions enclosed in **.
    INSTRUCTIONS:-
    **Use pandas as pd to open the csv file**
    **Only give the code for the manipulation and do not give any additional information**
    **Just give the code only and do not give any extra information**
    **The output should be a JSON Object always and never use any other format as {"Program":"code"}**
    **Open the config files DM_Column_Level_Maps_Updated.csv and DM_Row_Level_Maps_New.csv**
    Operations:-

    **For Row level mapping DM_Row_Level_Maps_New according to Function Copy And Merge, with use as below mentioned and enclosed in # and comma separated**
    #COPY = take column and their values as it is,
    MERGE = this is nothing but a left JOIN Condition we are using in pandas#
    **For DM_Row_Level_Maps_New according to the column 'New Technical Logic' we need to transform the data**
    **source dataset files are as follows dm_RAW.csv,dov_RAW.csv,ifc_RAW.csv,subj_RAW.csv**
    **Join this two tables on these columns 'SITE','SUBJECT' and according to there source_dataset and target_variable from the DM_Column_Level_Maps_Updated.csv**

    **then for Column level operations use the dataframe genearted from row level opearations according to the specified columns source_variable and target variables **
    **For column level maping DM_Column_Level_Maps_Updated Follow below mention conditional instruction enclose in ``` to generate python code**
    ```
    **Don't be confused in 'New Technical Logic' column which is in both files, make sure to use them differently for each column and row level operations**
    **If you didn't get technical logic pass literal null to that respective column column**
    """

    for index, row in tech_details_df.iterrows():
        source_variable = row['Source_Variable']
        target_variable = row['Target_Variable']
        function_name = row['New_Function_Name']
        Actual_Logic = row['Actual_Logic']

        prompt += f"**Source_Variable: {source_variable}\n"
        prompt += f"Target_Variable: {target_variable}\n"
        if function_name == 'COPY':
            prompt += f"Copy data from source column '{source_variable}' to target column '{target_variable} as it is'\n"
        elif function_name == 'CONDITION':
            prompt += f"Apply conditions mention further as <'{Actual_Logic}'> on  source column '{source_variable}' and update target column '{target_variable}' accordingly\n"
        # else:
        #     prompt += "Logic: Add custom logic here\n"  # Add logic for other function types

        prompt += "\b**\n\n"
    prompt += """```\n**additional Note for you: when Source_Variable is nan or not present then the target_variable column value should be same as source_dataset column value**
    **understand the requirement carefully and the conditions mentioned above**
    **DO NOT CONVERT IT INTO A JSON OBJECT**
    **Do not change anything which is not mentioned in the prompt such as datatype, column names, etc**"""
    print(prompt)


if __name__ == "__main__":
    config_folder = PathOfFile.config.value
    generate_code(config_folder)
    print("Schemas for files in raw folder:")
    print(raw_schemas)
    print("Schemas for files in output folder:")
    print(output_schemas)