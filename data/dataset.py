# generate datasets for common summarization tasks
from torchtext.data import Field, TabularDataset, Dataset
import spacy

spacy_en = spacy.load('en')


def tokenizer(text):  # create a tokenizer function
    """
    定义分词操作
    """
    return [tok.text for tok in spacy_en.tokenizer(text)]


class SummDataset:
    def __init__(self, path, src_max=512, tgt_max=64, lower=True):
        self.SRC = Field(tokenize=tokenizer, sequential=True, lower=lower)
        self.TGT = Field(tokenize=tokenizer, sequential=True, lower=lower)
        self.validation = TabularDataset(
            path=path+"validation.json", format="json",
            fields={"source":("source", self.SRC),"summary":("summary", self.TGT)}
        )


if __name__ == '__main__':
    cnndm = SummDataset("/Users/leo/Desktop/桌面/NLPDataset/cnndm/")
    print(cnndm.validation[1].source)
