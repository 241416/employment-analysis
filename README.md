## employment-analysis
This is a class project about employment analysis, our goal is to use data science to find what kind of person employers need given specific position so as to shorten the gap bewteen colleage students and employers.

### crawler
1. first, we crawled recruitment data from boss website and clean, combine them to 12 categories

### EDA(Explortary Data Analysis)
2. we use multiple statistical ML methods to analyze it including TF-IDF,random forest,heat map to explore which factor influences our salary most and relation between factors.
we use pca to get the dimensions HR pay attention to so to feed these dimensions to LLM.
Also, we did some visualization on these pre-processed data to make it clear.

### LLM_based marking and concluding
3. after clean, preprocess data, we use openai api to make chatgpt simulate HR to mark importance from 12 aspects and include detaild requirement(see ./outputs) given the data we clawed

### Analysis and Visualization
4. after getting score and content for every dimension for evey job, we visualize them(bar char & Rader Chart& Box chart, heat map, pie chart)
`
