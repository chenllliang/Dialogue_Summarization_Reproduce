from tqdm import tqdm

from base import Extractive_Summarizer
import spacy
import json
from nltk import sent_tokenize
import random

spacy_en = spacy.load('en')
def tokenizer(text):  # create a tokenizer function
    """
    定义分词操作
    """
    return [tok.text for tok in spacy_en.tokenizer(text)]


class Lead3(Extractive_Summarizer):
    def __init__(self):
        super(Lead3, self).__init__()

    def summary_file(self,file_path,output_path,is_dialogue=False):
        """

        :param file_path: json format file , {"source":"xxx","summary":"x"} in each line
        :param output_path:
        :return:
        """
        out = open(output_path,"w")
        out_tgt = open(output_path+".tgt","w")
        if is_dialogue==False:
            with open(file_path,"r") as f:
                lines = f.readlines()
                for i in tqdm(lines):
                    src = json.loads(i)

                    tokenized = tokenizer(" ".join(sent_tokenize(src['source'].replace("\n"," ").replace("\r",""))[:3]))
                    tgt = tokenizer(src['summary'].replace("\n"," ").replace("\r",""))

                    out_tgt.write(" ".join(tgt)+"\n")
                    out.write(" ".join(tokenized)+"\n")

        else:
            with open(file_path,"r") as f:
                lines = f.readlines()
                for i in tqdm(lines):
                    src = json.loads(i)

                    tokenized = tokenizer(" ".join(lead3(src['source'].replace("\r","").split("\n"))))
                    tgt = tokenizer(src['summary'].replace("\n"," ").replace("\r",""))

                    out_tgt.write(" ".join(tgt)+"\n")
                    out.write(" ".join(tokenized)+"\n")


def mid3(src:list):
    lens = len(src)//2
    return src[lens-1:lens+2]

def lead3(src:list):
    return src[:3]


if __name__ == '__main__':
    l = Lead3()
    l.summary_file("/Users/leo/Desktop/桌面/NLPDataset/samsum_raw/test.json","/Users/leo/Desktop/桌面/NLPDataset/samsum_raw/lead3-n.txt",True)