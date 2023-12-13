import pandas as pd
from textstat import textstat
import matplotlib.pyplot as plt
import re

year = 2015
path = f'../raw_data/TOI_{year}_data.csv'

df = pd.read_csv(path)


def plot_day_wise():
    scores = []
    for i in range(1, 366):
        score = 0
        count = 0
        for t in df[df['Day'] == i]['article']:
            try:
                score += textstat.flesch_reading_ease(t)
                count += 1
            except TypeError:
                continue

        if count != 0:
            scores.append(score / count)
        else:
            # scores.append(0)
            continue
    plt.title(f'Reading ease for Times of India, {year}')
    plt.xlabel('Days')
    plt.ylabel('Readability score')
    plt.plot(scores)
    plt.show()


def plot_all():
    skipped = 0
    scores = []
    for idx, t in enumerate(df['article']):
        try:
            scores.append(textstat.flesch_reading_ease(t))
        except TypeError:
            skipped += 1
    print(f'No. of articles skipped = {skipped}')
    plt.plot(scores)
    plt.show()


# plot_day_wise()

tags = [extract_unique_names(url) for url in df['URL']]
df['Tag'] = tags

def plot_tag_wise():
    scores = []
    for tag in set(tags):
        score = 0
        count = 0
        for t in df[df['Tag'] == tag]['article']:
            try:
                score += textstat.flesch_reading_ease(t)
                count += 1
            except TypeError:
                continue

        if count != 0:
            scores.append(score / count)
        else:
            scores.append(0)
            continue
    # plt.figure(figsize=(20,20))
    plt.title(f'Reading ease for Times of India, {year} (By tag)')
    plt.xlabel('Tags')
    plt.ylabel('Readability score')
    print(len(list(set(tags))), len(scores))
    plt.bar(list(set(tags)), scores)
    plt.show()

plot_day_wise()
plot_tag_wise()