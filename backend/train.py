import json
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

CSV_PATH = "Heart_disease_cleveland_new.csv"

# Update these columns if your dataset uses different names
TARGET_COL = "target"  # 1 = disease, 0 = no disease

def main():
    df = pd.read_csv(CSV_PATH)

    # Basic cleaning (optional)
    df = df.dropna()

    X = df.drop(columns=[TARGET_COL])
    y = df[TARGET_COL]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Pipeline: scaler + model
    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(max_iter=2000))
    ])

    pipe.fit(X_train, y_train)

    preds = pipe.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, preds))
    print(classification_report(y_test, preds))

    # Save separately (nice for clarity)
    scaler = pipe.named_steps["scaler"]
    model = pipe.named_steps["clf"]

    joblib.dump(scaler, "model/scaler.joblib")
    joblib.dump(model, "model/model.joblib")

    feature_names = list(X.columns)
    with open("model/feature_names.json", "w") as f:
        json.dump(feature_names, f)

    print("Saved model + scaler + feature names in backend/model/")

if __name__ == "__main__":
    import os
    os.makedirs("model", exist_ok=True)
    main()
