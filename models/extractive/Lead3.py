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

    def summary_file(self, file_path, output_path, multi_ref=0, is_dialogue=False, methods="lead3"):
        """

        :param file_path: json format file , {"source":"xxx","summary":["x"]} in each line
        :param output_path:
        :return:
        """
        out = open(output_path, "w")

        out_tgt = None

        if multi_ref == 0:
            out_tgt = open(output_path + ".tgt", "w")
        else:
            out_tgt = [open(output_path + ".tgt" + str(i + 1), "w") for i in range(multi_ref)]

        method = getattr(Lead3, methods)

        if is_dialogue == False:
            with open(file_path, "r") as f:
                lines = f.readlines()
                for i in tqdm(lines):
                    src = json.loads(i)

                    tokenized = tokenizer(
                        " ".join(sent_tokenize(src['source'].replace("\n", " ").replace("\r", ""))[:3]))
                    tgt = tokenizer(src['summary'].replace("\n", " ").replace("\r", ""))

                    out_tgt.write(" ".join(tgt) + "\n")
                    out.write(" ".join(tokenized) + "\n")

        else:
            with open(file_path, "r") as f:
                lines = f.readlines()
                for i in tqdm(lines):
                    src = json.loads(i)

                    tokenized = tokenizer(" ".join(method(src['source'].replace("\r", "").split("\n"))))

                    if multi_ref:
                        refs = [tokenizer(i.replace("\n", " ").replace("\r", "")) for i in src['summary']]
                        for i, j in enumerate(out_tgt):
                            j.write(" ".join(refs[i]) + "\n")
                    else:
                        tgt = tokenizer(src['summary'].replace("\n", " ").replace("\r", ""))
                        out_tgt.write(" ".join(tgt) + "\n")
                    out.write(" ".join(tokenized) + "\n")

    def mid3(src: list):
        lens = len(src) // 2
        return src[lens - 1:lens + 2]

    def lead3(src: list):
        return src[:3]

    def last3(src: list):
        return src[-3:]

    def random3(src: list):
        if len(src)>3:
            return random.sample(src, 3)
        else:
            return src


if __name__ == '__main__':
    l = Lead3()
    l.summary_file("/Users/leo/Desktop/桌面/NLPDataset/ricos/test.json",
                   "/Users/leo/Desktop/桌面/NLPDataset/ricos/lead3-n.txt", 3, True, methods="lead3")
    l.summary_file("/Users/leo/Desktop/桌面/NLPDataset/ricos/test.json",
                   "/Users/leo/Desktop/桌面/NLPDataset/ricos/mid3-n.txt", 3, True, methods="mid3")
    l.summary_file("/Users/leo/Desktop/桌面/NLPDataset/ricos/test.json",
                   "/Users/leo/Desktop/桌面/NLPDataset/ricos/last3-n.txt", 3, True, methods="last3")
    l.summary_file("/Users/leo/Desktop/桌面/NLPDataset/ricos/test.json",
                   "/Users/leo/Desktop/桌面/NLPDataset/ricos/random3-n.txt", 3, True, methods="random3")
