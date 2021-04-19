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
| LEAD3 | **31.47** | **8.83** | **30.41** | **15.43**
| MID3 | 28.15 | 6.78 | 27.25| 13.64
| LAST3 | 26.38 | 5.91 | 25.79 | 12.75
| RANDOM3 | 28.29 | 7.36 | 27.25 | 13.75
| TextRank |  |  |


| Ricos/Ext | ROUGE1 | ROUGE2 | ROUGEL | ROUGEW
| :-----| :----: | :----: |:----: |:----: |
| LEAD3 | **27.15** | **6.83** | **26.78** | **13.71**
| MID3 | 23.30 | 4.65 | 22.84| 11.48
| LAST3 | 23.04 | 4.81 | 22.39 | 11.25
| RANDOM3 | 24.39 | 5.65 | 23.16 | 11.77
| TextRank |  |  |