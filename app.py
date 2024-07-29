from transformers import pipeline

# here, I'm telling my model that I am using the sentiment analysis pipeline.
# The variable is sentiment_analysis while the stuff in the parentheses is the
# actual tool we're using.
sentiment_analysis = pipeline("sentiment-analysis")

while True:
  result = sentiment_analysis(input("Enter A Sentence"))
  print(result)
