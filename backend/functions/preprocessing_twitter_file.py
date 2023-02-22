# source_path = raw twitter csv
# destination_path = where save new csv
def preproccessing_twitter_file(source_path, destination_path):
    import pandas as pd
    import ast

    # read csv
    df = pd.read_csv(filepath_or_buffer=source_path, encoding="utf-8",
                     engine='python', memory_map=True, on_bad_lines='skip', parse_dates=['date'])

    # expand date
    df['Hour'] = df['date'].dt.hour
    df['Year'] = df['date'].dt.year
    df['Month'] = df['date'].dt.month
    df['MonthName'] = df['date'].dt.month_name()
    df['MonthDay'] = df['date'].dt.day
    df['DayName'] = df['date'].dt.day_name()
    df['Week'] = df['date'].dt.isocalendar().week
    df['Date'] = [d.date() for d in df['date']]
    df['Time'] = [d.time() for d in df['date']]
    df = df.drop(columns=['date'], inplace=True)

    # drop useless columns
    useless_columns = ['_type', 'url', 'conversationId', 'source', 'sourceUrl', 'sourceLabel', 'tcooutlinks', 'media',
                       'lang', 'outlinks', 'quotedTweet', 'coordinates', 'inReplyToTweetId', 'retweetedTweet',
                       'inReplyToUser', 'Searh', 'id']
    df_reduced = df.drop(columns=useless_columns)

    # expand user data
    user = df_reduced['user'][0]
    user_json = ast.literal_eval(user)
    user_columns = pd.DataFrame(user_json, index=['id'])

    useless_user_columns = ['_type', 'id', 'description', 'rawDescription', 'descriptionUrls', 'protected', 'linkUrl',
                            'linkTcourl', 'profileImageUrl', 'profileBannerUrl', 'label', 'url']

    df_user = pd.DataFrame(columns=user_columns.columns, index=range(0, len(df_reduced)))
    for index, row in df_reduced.iterrows():
        user = ast.literal_eval(row['user'])
        df_user.loc[index] = user
    df_user = df_user.drop(columns=useless_user_columns)
    df_user = df_user.add_prefix('user_')

    df_expanded = pd.concat([df_reduced, df_user], axis=1, join='inner')
    df_expanded = df_expanded.drop(columns=['user'])

    # expand mentioned_user
    df_mentioned_user = pd.DataFrame(columns=['mentionedUsers'], index=range(0, len(df_reduced)))
    for index, row in df_reduced.iterrows():
        if not pd.isna(row['mentionedUsers']):
            mentionedUsers = ast.literal_eval(row['mentionedUsers'])
            mentionedUsers = [item['username'] for item in mentionedUsers]
            df_mentioned_user.loc[index]['mentionedUsers'] = mentionedUsers
    df_expanded['mentionedUsers'] = df_mentioned_user['mentionedUsers']

    df_expanded.to_csv(destination_path, index=False, encoding='utf-8')