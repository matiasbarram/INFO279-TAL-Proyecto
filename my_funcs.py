import re
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
from functools import partial
import matplotlib.pyplot as plt
import numpy as np
import string
import spacy
from spacy.lang.es.stop_words import STOP_WORDS
import re

prefix_re = re.compile('''^\$[a-zA-Z0-9]''')
spacy_es = spacy.load('es_core_news_md')


def tokenize_es_a(sentence):
    return [tok.lower_ for tok in spacy_es.tokenizer(sentence)]

def tokenize_es_b(sentence):
    return list(filter(lambda x: x not in string.punctuation,
                       [tok.lower_ for tok in spacy_es.tokenizer(sentence)]))

def tokenize_es_c(sentence):
    return list(filter(lambda x: x not in string.punctuation and x not in STOP_WORDS,
                       [tok.lower_ for tok in spacy_es.tokenizer(sentence)]))

def tokenize_es_d(sentence):
    return [tok.text for tok in spacy_es.tokenizer(sentence)]

def tokenize_es_string(sentence):
    return " ".join(list(filter(lambda x: x not in string.punctuation and x not in STOP_WORDS,
                       [tok.lower_ for tok in spacy_es.tokenizer(sentence)])))


def plot_confusion_matrix(cm, labels, cmap=plt.cm.Blues, clf_name=''):
    fig, ax = plt.subplots(figsize=(7, 7), tight_layout=True)
    ax.imshow(cm, interpolation='nearest', cmap=cmap)
    for i in range(cm.shape[1]):
        for j in range(cm.shape[0]):
            ax.text(j, i, "{:,}".format(cm[i, j]), 
                    horizontalalignment="center", verticalalignment="center",
                    color="white" if cm[i, j] > np.amax(cm)/2 else "black")
    ax.set_title(f"Matriz de confusión {clf_name}")
    tick_marks = np.arange(len(labels))
    plt.yticks(tick_marks, labels)
    plt.xticks(tick_marks, labels, rotation=90)
    plt.ylabel('Etiqueta real')
    plt.xlabel('Predicción')

def get_tag(row):
    if row.media_outlet == 'emol':
        tag_idx = 4
    else:
        tag_idx = 3
    link = row.url.split('/')
    if link[tag_idx] == 'noticias' and link[tag_idx + 1] not in ['2020', '2021']:
        return link[tag_idx + 1]
    return link[tag_idx]

def clean_and_tag(df):
    df.drop('year', inplace=True, axis=1)
    df.drop('id_journalist', inplace=True, axis=1)
    #print(corpus['media_outlet'].unique())
    df['tag'] = df.apply(get_tag, axis=1)
    #df['text'] = df['text'].astype('string')
    df = df[df['text'].notna()]
    df = df[df.text.str.len() > 100]
    return df

def get_df_keywords(lda_model, num_topics=None):
    if num_topics is None:
        num_topics = len(lda_model.get_topics())
    model_topics = lda_model.show_topics(num_topics, formatted=True, num_words=25)
    #print(model_topics[0][1])
    topicos = {}
    for topic in model_topics:
        words = re.findall( r'"(.*?)"', topic[1])
        topicos.update({topic[0]: words})
    return pd.DataFrame.from_dict(topicos)

def predict_and_compare(df, vectorized_df, idxs=(0, 6)):
    predictions = lgr.predict(vectorized_df[idxs[0]:idxs[1]])
    predict_probs = lgr.predict_proba(vectorized_df[idxs[0]:idxs[1]])
    for i, (pred, probs) in enumerate(zip(predictions, predict_probs)):
        print('\n', df.iloc[i+idxs[0]].url)
        print()
        print(df.iloc[i+idxs[0]].text[:200], '...')
        print()
        print(f'predicted ---{lb.inverse_transform([pred])[0]}---', end=' ')
        print(f'prob: {probs[pred]:.3f}')
        print('*'*60)
        
def results(ylb, text_clf, X_test, true_labels):
    predicted = text_clf.predict(X_test)
    clf_name = type(text_clf).__name__
    print(f"Resultados clasificación\n{clf_name}\n\n")
    print(classification_report(ylb, predicted, target_names=true_labels))
    cm = confusion_matrix(y_true=ylb, y_pred=predicted)
    plot_confusion_matrix(cm, labels=true_labels, clf_name=clf_name)