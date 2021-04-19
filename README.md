# Easy_summarizatioon
 easy summarization methods via pytorch
 
## Available Resource

### Model

*Extractive*
- LEAD3
- TextRank

*Abstractive*
- None

### Dataset
- CNNDM3.0
- XSUM
- SAMSUM


## Experiment Results

| CNNDM3.0/Ext | ROUGE1 | ROUGE2 | ROUGEL | ROUGEW
| :-----| :----: | :----: |:----: |:----: |
| LEAD3 | 40.52 | 17.60 | 31.53 | 13.63
| TextRank |  |  |

| CNNDM3.0/Abs | ROUGE1 | ROUGE2 | ROUGEL | ROUGEW
| :-----| :----: | :----: |:----: |:----: |
| Pointer+Coverage |  |  |  | 
| Transformer |  |  |

| Xsum/Ext | ROUGE1 | ROUGE2 | ROUGEL | ROUGEW
| :-----| :----: | :----: |:----: |:----: |
| LEAD3 | 19.78 | 2.71 | 17.85 | 8.32
| TextRank |  |  |

| Samsum/Ext | ROUGE1 | ROUGE2 | ROUGEL | ROUGEW
| :-----| :----: | :----: |:----: |:----: |
| LEAD3 | 31.47 | 8.83 | 30.41 | 15.43
| TextRank |  |  |