# AI Risk Classification From Financial Documents of US SEC 

The objective of this project is to classify the risks associated with artificial intelligence (AI) technologies based on corporate financial disclosure texts, specifically the financial statements of U.S. public firms. 

As AI continues to gain popularity, U.S. firms increasingly adopt AI technologies to boost revenue by integrating AI into their business or products and to reduce costs by automating tasks traditionally performed by human labor. 

However, these opportunities come with inherent risks. In this project, we try to develop methods to efficiently improve the process of analysing corporate AI risk exposure by examining the annual financial reports of these firms. These reports provide insights from firm executives on potential risk factors affecting their business.

Tech Stack: NLP, BERT, Python, Pandas, Numpy, NLTK (punkt)

![Ai RISK Factors Classification from financial reports (1)](https://github.com/user-attachments/assets/d7785c73-9347-413c-9511-d18858508e8f)


[Literature Review Link](https://github.com/rxdhikx/AI-Risk_Classification-From-Financial-Documents/blob/main/Literature_Review.md)

Note: This is an ongoing research project estimated to be complete by mid August 2024. Stay tuned!

--------------------------------------------------------------------------------------------------------------------------------------------------

## Dataset:

The concerned dataset consists of about 4 GB of dataset samples collected from the Software Repository for Accounting and Finance from US EDGAR, which has financial reports from US companies published each quarter from 1993-2023 (44GB)

--------------------------------------------------------------------------------------------------------------------------------------------------
## About the files in this repo:

test - folder containing test financial reports among which 2 are related to AI

extracting_risk_factors.py - code to extract the relevant content from files (risk factor section)

read_files.ipynb - Analysis of extracted content 

uncleaned_test.ipynb - this file shows us the discrepancies of formatting in some files, which affects the extraction if data is not properly cleaned

word_list_AI.py - contains the keywords related to AI 

Literature_Review - literature review of some relevant papers on risk factor extraction and categorization

bert_ai.ipynb - BERT code used on a sample 

bert_on_large_input_dataset.ipynb - BERT code for massive datasets, with edge cases handled 
