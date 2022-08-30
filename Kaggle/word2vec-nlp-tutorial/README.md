# Bag of Words Meets Bags of Popcorn

## Notes

Some mentioned techniques:
- Bag of Words
- Word2Vec
- Vector Averaging
- tf-idf Weighted Vector Averaging
- Word2Vec + Clustering
- [Paragraph Vector](https://cs.stanford.edu/~quocle/paragraph_vector.pdf)

> **Advantages of paragraph vectors:** An important ad- vantage of paragraph vectors is that they are learned from unlabeled data and thus can work well for tasks that do not have enough labeled data.

> Paragraph vectors also address some of the key weaknesses of bag-of-words models. First, they inherit an important property of the word vectors: the semantics of the words. In this space, “powerful” is closer to “strong” than to “Paris.” The second advantage of the paragraph vectors is that they take into consideration the word order, at least in a small context, in the same way that an n-gram model with a large n would do. This is important, because the n-gram model preserves a lot of information of the paragraph, including the word order. That said, our model is perhaps better than a bag-of-n-grams model because a bag of n-grams model would create a very high-dimensional representation that tends to generalize poorly.
