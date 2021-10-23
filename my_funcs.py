import re
import pandas as pd

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

def get_df_keywords(lda_model, num_topics):
    model_topics = lda_model.show_topics(num_topics, formatted=True, num_words=25)
    #print(model_topics[0][1])
    topicos = {}
    for topic in model_topics:
        words = re.findall( r'"(.*?)"', topic[1])
        topicos.update({topic[0]: words})
    return pd.DataFrame.from_dict(topicos)