import pandas as pd

data = pd.read_excel('data/테스트 결과_4개 비교.xlsx')

result_sentiments = []
for index, row in data.iterrows():
    sentiments = [
        row['sentiment_5차년도'],
        row['sentiment_단발성+말뭉치'],
        row['sentiment_단발성'],
        row['sentiment']
    ]

    sentiment_counts = pd.Series(sentiments).value_counts()

    if len(sentiment_counts) == 4:
        most_common_sentiment = row['sentiment_5차년도']
    # 네 가지 라벨이 두 개씩 묶여서 두 가지 다른 값을 가질 때
    elif len(sentiment_counts) == 2 and sentiment_counts.nlargest(2).sum() == 2:
        # sentiment_5차년도와 일치하는 값을 선택
        for sentiment in sentiment_counts.index:
            if sentiment != row['sentiment_5차년도']:
                most_common_sentiment = row['sentiment_5차년도']
    else:
        most_common_sentiment = sentiment_counts.idxmax()

    result_sentiments.append(most_common_sentiment)

# 결과를 새로운 열로 추가
data['sentiment_결과'] = result_sentiments
print(data)
# 결과를 CSV 파일로 저장
data.to_csv('최종결과.csv', index=False)  # 파일 경로를 적절히 변경하세요