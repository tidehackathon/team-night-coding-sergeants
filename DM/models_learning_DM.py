import pandas as pd
from sklearn.model_selection import train_test_split
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
import joblib
from backend.DM import df_maker as dfm

dir_path = 'D:/Desktop/Hackathon/NewOne/'

fake_news = dfm.return_df_from_csv(dir_path, 'Fake.csv')
true_news = dfm.return_df_from_csv(dir_path, 'True.csv')

fake_news['class'] = 1
true_news['class'] = 0


def remove_unused_characters(data):
    data = data.lower()
    data = re.sub('\[.*?\]', '', data)
    data = re.sub('\\W', ' ', data)
    data = re.sub('https?://\S+|www.\S+', '', data)
    data = re.sub('<.*?>+', '', data)
    data = re.sub('[%s]' % re.escape(string.punctuation), '', data)
    data = re.sub('\n', '', data)
    data = re.sub('\w*\d\w', '', data)
    return data


merged_data = pd.concat([true_news, fake_news], axis=0)
df = merged_data.sample(frac=1)
df['text'] = df['text'].apply(remove_unused_characters)

x = df['text']
y = df['class']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.05)
vectorizer = TfidfVectorizer()
xv_train = vectorizer.fit_transform(x_train)
xv_test = vectorizer.transform(x_test)
joblib.dump(vectorizer, 'models/vectorizer.pkl')
print('Wektoryzacja zakończona')

LR = LogisticRegression(solver='lbfgs', max_iter=200)
LR.fit(xv_train, y_train)
print('LR nauczony')
joblib.dump(LR, 'models/LR.sav')

DT = DecisionTreeClassifier()
DT.fit(xv_train, y_train)
print('DT nauczony')
joblib.dump(DT, 'models/DT.sav')

GBC = GradientBoostingClassifier(random_state=0)
GBC.fit(xv_train, y_train)
print('GBC nauczony')
joblib.dump(GBC, 'models/GBC.sav')

RFC = RandomForestClassifier(random_state=0)
RFC.fit(xv_train, y_train)
print('RFC nauczony')
joblib.dump(RFC, 'models/RFC.sav')
