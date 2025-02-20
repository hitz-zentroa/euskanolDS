# Imports
import fasttext
from huggingface_hub import hf_hub_download
import pandas as pd
import argparse
from datasets import load_dataset
parser = argparse.ArgumentParser()

parser.add_argument("--input_file", type=str, help="Input file")
parser.add_argument("--text_field", type=str, help="Column id with the text to process")
args = parser.parse_args()

input = args.input_file
column = args.text_field


#Load fasttext model
model_path = hf_hub_download(repo_id="facebook/fasttext-language-identification", filename="model.bin")
model = fasttext.load_model(model_path)


df = pd.read_csv(input, sep="\t")

# Predict for each row
label1_list = []
confidence1_list = []
label2_list = []
confidence2_list = []


for index, row in df.iterrows():
    prediction = model.predict(str(row[column]), k=2)
    
    labels = prediction[0]
    confidences = prediction[1]
   
    label1 =labels[0][9:12]
    label2 =labels[1][9:12]

    confidence1 = confidences[0]
    confidence2 = confidences[1]
    
    label1_list.append(label1)
    label2_list.append(label2)
    confidence1_list.append(confidence1)
    confidence2_list.append(confidence2)

# Assign label and confidence column
df["Label1"] = label1_list
df["Confidence1"] = confidence1_list
df["Label2"] = label2_list
df["Confidence2"] = confidence2_list


df_final = df[((df["Label1"]=="eus") & (df["Label2"]=="spa") & (df["Confidence2"]>=0.1)) | ((df["Label1"]=="spa") & (df["Label2"]=="eus") & (df["Confidence2"]>=0.1))]


df_final[column].to_csv(input[:-4]+"_code_switching.tsv", sep="\t", index=False)
