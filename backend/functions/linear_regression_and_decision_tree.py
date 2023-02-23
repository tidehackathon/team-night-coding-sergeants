# text preparation
def __punctuation_removal(text):
    import string
    all_list = [char for char in text if char not in string.punctuation]
    clean_str = ''.join(all_list)
    return clean_str


# datasets = list of dataframes {text: news, flag: label 1/0}
def learn_linear_regression_and_decisn_tree(datasets=None):
    if datasets is None:
        datasets = []

    import pandas as pd
    from sklearn.model_selection import train_test_split
    import nltk
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    import pickle

    # empty datasets
    if not datasets:
        return

    # join datasets
    data = pd.concat(datasets).reset_index(drop=True)



    stop = stopwords.words('english')
    data['text'] = data['text'].apply(lambda x: x.lower())
    data['text'] = data['text'].apply(__punctuation_removal)
    data['text'] = data['text'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop]))

    # split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(data['text'], data.flag, test_size=0, random_state=42)

    # learning logistic regression model
    model_logistic = pickle.load(open('./models/model_logistic_regression.sav', 'rb'))
    model_logistic = model_logistic.fit(X_train, y_train)
    pickle.dump(model_logistic, open('./models/model_logistic_regression.sav', 'wb'))

    # learning decision tree model
    model_decision_tree = pickle.load(open('./models/model_decision_tree.sav', 'rb'))
    model_decision_tree = model_decision_tree.fit(X_train, y_train)
    pickle.dump(model_decision_tree, open('./models/model_decision_tree.sav', 'wb'))

    return

# data = twitter data frame
# output_name = twitter file with prediction
def predict_file_linear_regression_and_decision_tree(data, output_name):
    import nltk
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    import pickle
    import os

    # text preparation
    stop = stopwords.words('english')
    data['text'] = data['text'].apply(lambda x: x.lower())
    data['text'] = data['text'].apply(__punctuation_removal)
    data['text'] = data['text'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop]))

    # predict logistic regression model
    model_logistic = pickle.load(open('./models/model_logistic_regression.sav', 'rb'))
    data['predict_logistic'] = model_logistic.predict(data['text'])

    # predict decision tree model
    model_decision_tree = pickle.load(open('./models/model_decision_tree.sav', 'rb'))
    data['predict_decision_tree'] = model_decision_tree.fit(data['text'])

    if not os.path.exists('./predicted'):
        os.makedirs('./predicted')

    data.to_csv(f'./predicted/{output_name}', index=False, encoding='utf-8')

    # prepare statistic

    verifiedUsers = data[data['user_verified'] == 'True'].drop_duplicates().count()[0]
    verifiedTrue = data[
        data['user_verified'] == 'True'
        and data['predict_logistic'] == 1
        and data['predict_decision_tree'] == 1
        ].count()[0]
    verifiedFalse = data[
        data['user_verified'] == 'True'
        and (data['predict_logistic'] == 0 or data['predict_decision_tree'] == 0)
        ].count()[0]

    unverifiedUsers = data[data['user_verified'] == 'False'].drop_duplicates().count()[0]
    unverifiedTrue = data[
        data['user_verified'] == 'False'
        and data['predict_logistic'] == 1
        and data['predict_decision_tree'] == 1
        ].count()[0]
    unverifiedFalse = data[
        data['user_verified'] == 'False'
        and (data['predict_logistic'] == 0 or data['predict_decision_tree'] == 0)
        ].count()[0]

    return verifiedUsers, verifiedTrue, verifiedFalse, unverifiedUsers, unverifiedTrue, unverifiedFalse


# fact - text to predict
def predict_fact_linear_regression_and_decision_tree(fact):
    import nltk
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    import pickle
    import os

    # text preparation
    stop = stopwords.words('english')
    fact = fact.lower()
    fact = __punctuation_removal(fact)
    fact = ' '.join([word for word in fact.split() if word not in stop])

    # predict logistic regression model
    model_logistic = pickle.load(open(os.path.abspath("./functions/models/model_logistic_regression.sav"), 'rb'))
    predict_logistic = model_logistic.predict([fact])

    # predict decision tree model
    model_decision_tree = pickle.load(open(os.path.abspath("./functions/models/model_decision_tree.sav"), 'rb'))
    predict_decision_tree = model_decision_tree.predict([fact])

    return predict_logistic, predict_decision_tree
