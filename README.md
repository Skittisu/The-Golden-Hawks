# Advanced Data Tagging for Data Fitness and Quality
Our goal is to use advanced data tagging with metadata for data fitness and quality to reduce the manually-intensive work in data management life cycle. It ensures the metadata accurately enables discovery, access and usage of the data for data fitness and quality. Furthermore, we use data analytics and AI/ML techniques to improve this situation.
## Business Objective
The primary objective of this project is to better enable users to differentiate datasets that are more likely to meet their business needs. This helps users and organizations to save time and resources to refocus human efforts toward tuning parameters instead of data entry of metadata. 
## Solution Space
Our process helps users and organizations to incorporate data fitness measures or indicators into DLM processing that consider business questions and tasks by using meta data tags. Data tagging is the process of identifying, categorizing, and labeling data in order to make it easier for a machine learning model to learn. Our solution is to develop a topic modeling algorithm (LDA) that can be used to find topics and thus automate the metadata tagging process. Data tagging can help to improve the quality of data throughout its life cycle. We also aim to find the covid related keywords from business questions for text dataset and to find which image dataset predicts covid information along with assessing the data quality and relevance indicators to measure data fitness.
## Project Pipeline
Out of the three text datasets, we are finding out which dataset gives better information about Covid-19. This model gives the user/business enough information to choose the most fit data for their business needs.
- Data Collection: we collected semi-structured and unstructured data from publicly available sources and detected the data types.
- Data Quality Assessment: we measured data quality by assessing four quality dimensions (Accuracy, Completeness, Consistency, Uniqueness).
- Data Cleaning: Data is cleaned by tokenization, removing punctuation, and removing stop words.
- Topic Modeling: we used Latent Dirichlet Allocation (LDA) and it is part of Python's Gensim package.
- Data Relevance Assessment:  we calculated coherence score (LDA) and similarity score (BERTopic) to find the most relevant information regarding covid topics or business questions.

On the other hand we have two image datasets namely covid-19 and COVID CXR image datasets which gives visual information of chest x-rays predciting the possibility of covid.Following back to our business question in order to predict which dataset best gives covid information we have performed the following steps.

- Data Collection: we collected unstructured data from publicly available sources and detect the data types.
- Data Quality Assessment: we measured data quality by assessing four quality dimensions (Accuracy, Completeness, Consistency, Uniqueness).
- Data Cleaning: Data is cleaned by removing duplicate images, checking consistency, and removing corrupted files.
- Modeling: we used convolutional neural networks(CNN) a machine learning algorithm in momentum AI to predict covid from the chest x-ray images.


## Results
We compared the results of quality and relevance metrics about which dataset provides client enhanced information that allows them to easily differentiate datasets that best address their business questions and tasks.

<img width="400" alt="Untitled" src="https://github.com/Skittisu/The-Golden-Hawks/assets/123661501/e16fa9fe-7c63-4a3b-90be-91dd05e0928b">
<img width="417" alt="Untitled" src="https://github.com/Skittisu/The-Golden-Hawks/assets/123661501/9551991b-e296-4ef1-8fcc-d91b286d767d">


## Use case
Our framework provides a means to link business questions and tasks to better differentiate data using advanced metadata tagging and indicators for data fitness. The tags are useful in creating content rating tools that allow users to extract datasets based on keywords that match the tag. This tool will provide users with information on how much of a dataset is relevant to COVID and in what context

<img width="344" alt="mh" src="https://github.com/Skittisu/The-Golden-Hawks/assets/123661501/900d78a7-32c0-4389-95d2-ff744d76cc12">
<img width="346" alt="mj" src="https://github.com/Skittisu/The-Golden-Hawks/assets/123661501/3894b3ce-1b7a-465e-b107-8df77cdd53d0">

