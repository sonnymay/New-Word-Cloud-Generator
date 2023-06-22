import matplotlib.pyplot as plt
from wordcloud import WordCloud

def generate_word_cloud(text):
    wordcloud = WordCloud(width=1600, height=800, max_font_size=200).generate(text)
    plt.figure(figsize=(12,10))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

# Example usage
text = "Hello world! This is a word cloud generator. I hope it works."
generate_word_cloud(text)