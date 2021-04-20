from base import Extractive_Summarizer
import spacy
import json
from nltk import sent_tokenize
import random
from tqdm import tqdm
import numpy as np
import networkx as nx

spacy_en = spacy.load('en')


def tokenizer(text):  # create a tokenizer function
    """
    定义分词操作
    """
    return [tok.text for tok in spacy_en.tokenizer(text)]


class TextRank(Extractive_Summarizer):
    def __init__(self,method):
        super(TextRank, self).__init__()
        self.method = method

    def summary_file(self, file_path,output_path,is_dialogue=False):
        out = open(output_path, "w")

        if is_dialogue == False:
            pass

        else:
            with open(file_path, "r") as f:
                lines = f.readlines()
                for i in tqdm(lines):
                    src = json.loads(i)
                    sentences =src['source'].replace("\r", "").split("\n")
                    r_sentences = [i[i.find(":")+1:] for i in sentences]

                    top3_indexs = self.textrank(r_sentences)
                    summary = []
                    for i in top3_indexs:
                        summary.append(sentences[i])

                    outline = " ".join(tokenizer(" ".join(summary)))
                    out.write(outline+"\n")








    def textrank(self, sents: list):
        graph = np.zeros((len(sents),len(sents)))

        for i in range(len(sents)):
            for j in range(len(sents)):
                graph[i][j] = self.similarity(sents[i],sents[j],self.method)

        nx_graph = nx.from_numpy_matrix(graph)  # nx 就是 import networkx as nx
        scores = nx.pagerank(nx_graph, alpha=0.85)  # 调用networkx 里面的pagerank算法
        sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)  # 将计算结果按权重从大到小排序，取权重在前面的几个句子
        return [ i[0] for i in sorted_scores[:3]]


    def similarity(self, sent1, sent2, methods, alpha=0.5):
        tokens1 = tokenizer(sent1)
        tokens2 = tokenizer(sent2)

        if methods == "1-gram":
            return compute_ngram_cross(tokens1,tokens2,1)

        if methods == "2-gram":
            return compute_ngram_cross(tokens1,tokens2,2)

        if methods == "multi-gram":
            return alpha*compute_ngram_cross(tokens1,tokens2,1)+(1-alpha)*compute_ngram_cross(tokens1,tokens2,2)

        if methods == "word2vec":
            pass


def compute_ngram_cross(a: list, b: list, n: int):
    n_gram_a = [a[i:i + n] for i in range(len(a) - n + 1)]
    n_gram_b = [b[i:i + n] for i in range(len(b) - n + 1)]

    result = 0
    for i in n_gram_a:
        if i in n_gram_b:
            result += 1

    return result/(len(n_gram_a)+1)


if __name__ == '__main__':
    a = "I love eat apples"
    b = "I love apples"

    tr = TextRank("1-gram")
    tr.summary_file("/Users/leo/Desktop/桌面/NLPDataset/ricos/test.json","/Users/leo/Desktop/桌面/NLPDataset/ricos/test_text_rank.txt",True)
    tr.summary_file("/Users/leo/Desktop/桌面/NLPDataset/samsum_raw/test.json",
                    "/Users/leo/Desktop/桌面/NLPDataset/samsum_raw/test_text_rank.txt", True)
