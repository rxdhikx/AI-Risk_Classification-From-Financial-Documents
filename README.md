# AI Risk Classification From Financial Documents of US SEC 

The objective of this project is to classify the risks associated with artificial intelligence (AI) technologies based on corporate financial disclosure texts, specifically the financial statements of U.S. public firms. 

As AI continues to gain popularity, U.S. firms increasingly adopt AI technologies to boost revenue by integrating AI into their business or products and to reduce costs by automating tasks traditionally performed by human labor. 

However, these opportunities come with inherent risks. In this project, we try to develop methods to efficiently improve the process of analysing corporate AI risk exposure by examining the annual financial reports of these firms. These reports provide insights from firm executives on potential risk factors affecting their business.

Tech Stack: NLP, BERT, Python, Pandas, Numpy, NLTK (punkt)

[Literature Review Link](https://github.com/rxdhikx/AI-Risk_Classification-From-Financial-Documents/blob/main/Literature_Review.md)

Note: This is an ongoing research project estimated to be complete by mid August 2024. Stay tuned!

--------------------------------------------------------------------------------------------------------------------------------------------------

## Dataset:

The concerned dataset consists of about 4 GB of dataset samples collected from the Software Repository for Accounting and Finance from US EDGAR, which has financial reports from US companies published each quarter from 1993-2003 (44GB)


## About the files in this repo:

test - folder containing test financial reports among which 2 are related to AI

extracting_risk_factors.py - code to extract the relevant content from files (risk factor section)

Literature_Review - literature review of some relevant papers on risk factor extraction and categorization
