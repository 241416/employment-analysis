# employment-analysis
This is a class project about employment analysis, our goal is to use data science to find what kind of person employers need given specific position so as to shorten the gap bewteen colleage students and employers.
1. first, we crawled recruitment data from boss website and clean, combine them to 12 categories
2. we statistical ML methods to analyze it including TF-IDF,visualization etc.
we use pca to get the dimensions HR pay attention to so to feed these dimensions to LLM.
3. after clean, preprocess data, we use openai api to make chatgpt simulate HR to mark importance from 12 aspects and include detaild requirement(see ./outputs) given the data we clawed
4. after getting score and content for every dimension for evey job, we visualize them(bar char & Rader Chart& Box chart, heat map, pie chart)
`
