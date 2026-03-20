# Emotion-Aware Decision System

## Overview

This project is not a typical classification task. The goal is to build a system that can:

* Understand user emotions from text + context
* Decide what the user should do
* Suggest when they should do it
* Handle uncertainty in predictions

The system is designed to simulate a real-world scenario where data is noisy, incomplete, and sometimes contradictory.

---

## Problem Statement

Given user inputs like journal text, sleep, stress, and environment, the system predicts:

1. Emotional State
2. Emotional Intensity (1–5)
3. What the user should do (action)
4. When they should do it (timing)
5. Confidence and uncertainty

---

## Approach

### 1. Data Processing

* Text data (`journal_text`) is converted using TF-IDF
* Categorical features are one-hot encoded
* Numerical features are scaled
* Missing values are handled using defaults or median

---

### 2. Modeling

* Emotional State → Classification model
* Intensity → Regression model

I used simple models (RandomForest / Logistic Regression) to keep the system efficient and interpretable.

---

### 3. Decision Engine (Core Part)

Instead of learning actions from data, I designed a rule-based system using:

* predicted state
* intensity
* energy level
* stress level
* time of day

Example:

* High stress → breathing or grounding
* Low energy → rest or light planning
* High energy + focus → deep work

---

### 4. Uncertainty Handling

* Confidence is calculated from prediction probabilities
* If confidence is low → uncertain_flag = 1

This helps the system know when it might be wrong.

---

## Feature Importance

* **Text** helps capture emotional tone
* **Metadata** (sleep, stress, energy) adds important context

Example:

> A user may say "I'm fine", but high stress and low sleep indicate otherwise.

---

## Ablation Study

| Model Type      | Observation              |
| --------------- | ------------------------ |
| Text only       | Misses context           |
| Text + metadata | More accurate and stable |

Conclusion: metadata significantly improves performance.

---

## Robustness

The system is designed to handle:

* Short inputs ("ok", "fine") → fallback to metadata
* Missing values → default values used
* Conflicting signals → weighted decision logic

---

## Error Analysis

Some common failure cases:

* Ambiguous text
* Very short inputs
* Conflicting signals (text vs metadata)
* Noisy labels
* Mixed emotions

Detailed analysis is provided in `ERROR_ANALYSIS.md`.

---

## Edge Deployment Plan

* Use lightweight models (Logistic Regression)
* Reduce TF-IDF features for speed
* Convert model to ONNX / TensorFlow Lite
* Run on-device with low latency

Tradeoff: slightly lower accuracy for faster performance.

---

## Project Structure

```
ai_system/
│
├── data/
├── src/
├── models/
├── outputs/
├── README.md
├── ERROR_ANALYSIS.md
├── EDGE_PLAN.md
```

---

## How to Run

### Step 1: Navigate to project root

Open terminal and go to the main project folder:

```
cd path/to/ai_system
```

👉 Make sure you are in the root directory (not inside `src/`)

---

### Step 2: Install dependencies

```
pip install -r requirements.txt
```

---

### Step 3: Train the model

```
python src/train_model.py
```

This will automatically create the `models/` folder and save trained models.

---

### Step 4: Run predictions

```
python src/predict.py
```

---

### Step 5: Check output

The final predictions will be saved in:

```
outputs/predictions.csv
```


## Key Learnings

* Real-world ML systems must handle messy data
* Decision-making is as important as prediction
* Uncertainty handling is critical
* Metadata can be as important as text

---

## Conclusion

This project focuses more on real-world thinking than just model accuracy. It combines machine learning with decision logic to build a system that can understand, decide, and guide users in practical scenarios.
