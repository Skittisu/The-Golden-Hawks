# Advanced Data Tagging for Data Fitness and Quality
Our goal is to use advanced data tagging  with metadata  for data fitness and quality to reduce the manually-intensive work in data management life cycle. It will ensure the metadata accurately enables discovery, access and usage of the data for data fitness and quality. Furthermore, we will use  data analytics and AI/ML techniques to improve this situation.
## Business Objective
The primary objective of this project is to better enable users to differentiate datasets that are more likely to meet their business needs. This helps users and organizations to save time and resources to refocus human efforts toward tuning parameters instead of data entry of metadata. 
## Solution Space
Our process helps users and organizations to incorporate data fitness measures or indicators into DLM processing that consider business questions and tasks by using meta data tags. Data tagging is the process of identifying, categorizing, and labeling data in order to make it easier for a machine learning model to learn. Our solution is to develop a topic modeling algorithm (LDA) that can be used to find topics and thus automate the metadata tagging process. Data tagging can help to improve the quality of data throughout its life cycle. We also aim to find the covid related keywords from business questions along with assessing the data quality and relevance indicators to measure data fitness.
## Project Pipeline
Out of the three text datasets, we are finding out which dataset gives better information about Covid-19. This model gives the user/business enough information to choose the most fit data for their business needs.
- Data Collection: we collected semi-structured and unstructured data from publicly available sources and detect the data types.
- Data Quality Assessment: ไe measureก data quality by assessing four quality dimensions (Accuracy, Completeness, Consistency, Uniqueness).
- Data Cleaning: Data is cleaned by tokenization, removing punctuation, and removing stop words.
- Topic Modeling: we used Latent Dirichlet Allocation (LDA) and it is part of Python's Gensim package.
- Data Relevance Assessment:  we calculated coherence score (LDA) and similarity score (BERTopic) to find the most relevant information regarding covid topics or business questions.

## Results
We compared the results of quality and relevance metrics about which dataset provides client enhanced information that allows them to easily differentiate datasets that best address their business questions and tasks.

## Use case


