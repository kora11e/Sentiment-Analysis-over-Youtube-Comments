<h1>Sentiment Analysis over Youtube Comments</h1>

<h2>The project's goal is to dive into the data associated with Commentary under political videos displayed on Youtube Platform and perform analysis of it using techniques of Natural Language Processing. 
The project was developed during NLP classes and serves as the final result of it.</h2>

<h1>Installation instruction for Conda Environemnt</h1>

1. Download the project as zip in the top right corner or clone it directly via git bash or github on your machine.
2. Open it with your preferred code editor.
3. Open the console, locate the project directory and run the following command to create Conda environment.

```python
conda create --name <your-name>
```

4. Run following command to install necessary packages from requirements.txt.

```python
conda install --file requirements.txt
```
   
6. Run individual blocks for the final results.

<h2>Project description:</h2>
The project is divided into the parts: analysis of sentiment coming from Youtube comments and and Individual Clients analysis.

<h3>Youtube Comments Sentiment Analysis</h3>
The notebook is designed to perform sentiment analysis on comments from YouTube videos. It likely analyzes the emotional tone (positive, negative, neutral) of user comments using Natural Language Processing (NLP) techniques.

<h3>Libraries and Setup:</h3>
It imports a variety of libraries for:

Data Handling: pandas, numpy
Visualization: matplotlib, seaborn

NLP: nltk (including stopwords, punkt, vader_lexicon)
Clustering & Vectorization: TfidfVectorizer, MiniBatchKMeans
Dimensionality Reduction: PCA, TSNE

Tokenizer (punkt)
Sentiment lexicon (VADER)

<h3>Data Sources:</h3>
Two datasets are loaded:

merged_comments.xlsx: Contains the actual YouTube comments.
yt_channels_topics.xlsx: Contains metadata or topic categories for the associated YouTube channels.

The final results are presented in the project file.
