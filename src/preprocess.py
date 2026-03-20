import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler


def load_data(path):
    return pd.read_csv(path)


def preprocess(df, fit=True, tfidf=None, scaler=None, feature_columns=None):

    df = df.copy()

    
    #--------------------------------------------- 1. Handle missing values-------------------------------------
    
    df['journal_text'] = df['journal_text'].fillna("")
    df['sleep_hours'] = df['sleep_hours'].fillna(df['sleep_hours'].median())
    df['energy_level'] = df['energy_level'].fillna(3)
    df['stress_level'] = df['stress_level'].fillna(3)

    
    #--------------------------------------------- 2. Categorical encoding---------------------------------------
    
    categorical_cols = [
        'ambience_type',
        'time_of_day',
        'previous_day_mood',
        'face_emotion_hint'
    ]

    for col in categorical_cols:
        if col in df.columns:
            df[col] = df[col].fillna("unknown")

    df = pd.get_dummies(df, columns=categorical_cols)

    #------------------------------------------ 3. Text processing------------------------------------------
    
    if fit:
        tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
        X_text = tfidf.fit_transform(df['journal_text'])
    else:
        X_text = tfidf.transform(df['journal_text'])

   
   #------------------------------------------- 4. Metadata selection----------------------------------------

    drop_cols = ['journal_text', 'emotional_state', 'intensity', 'id']

    # Remove unwanted columns
    df_meta = df.drop(columns=[col for col in drop_cols if col in df.columns])

    # Keep ONLY numeric columns
    X_meta = df_meta.select_dtypes(include=['number'])

    
    #-------------------------------------------5. Align columns----------------------------------------------------

    if fit:
        feature_columns = X_meta.columns
    else:
        # Add missing columns
        for col in feature_columns:
            if col not in X_meta:
                X_meta[col] = 0

        # Remove extra columns
        X_meta = X_meta[feature_columns]


    #-----------------------------------------6. Scaling---------------------------------------------------

    if fit:
        scaler = StandardScaler()
        X_meta = scaler.fit_transform(X_meta)
    else:
        X_meta = scaler.transform(X_meta)

    return X_text, X_meta, tfidf, scaler, feature_columns