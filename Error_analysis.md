# ERROR_ANALYSIS.md

## Overview

In this project, I analyzed multiple failure cases of the model to understand where it struggles and how it can be improved. Since the data is noisy and real-world-like, the model does not always perform correctly. Below are 10 important failure cases along with insights and possible improvements.

---

## Case 1 — Ambiguous Text

**Text:** "I'm fine"
**Predicted:** calm
**Actual:** stressed

**Issue:**
The text does not clearly express emotion. The model relies heavily on text, which is ambiguous here.

**Improvement:**
Give more importance to metadata such as stress_level and sleep_hours.

---

## Case 2 — Conflicting Signals

**Text:** "I feel great today"
**Metadata:** stress_level = 5, sleep_hours = 3

**Predicted:** positive
**Actual:** stressed

**Issue:**
Text and metadata give opposite signals. The model prioritizes text.

**Improvement:**
Introduce weighted decision-making where extreme metadata overrides text.

---

## Case 3 — Very Short Input

**Text:** "ok"

**Predicted:** neutral
**Actual:** anxious

**Issue:**
Very little information in text, making prediction unreliable.

**Improvement:**
Fallback to metadata-based prediction when text length is too short.

---

## Case 4 — Noisy Labels

**Text:** "I feel relaxed and peaceful"
**Actual Label:** stressed

**Predicted:** calm

**Issue:**
Label itself seems incorrect or noisy.

**Improvement:**
Model cannot fully fix this. Use uncertainty flag to mark such cases.

---

## Case 5 — Over-reliance on Keywords

**Text:** "I am tired but satisfied with my work"

**Predicted:** low_energy
**Actual:** positive

**Issue:**
Model focuses on the word "tired" and ignores context.

**Improvement:**
Use n-grams or better text representation to capture full meaning.

---

## Case 6 — Missing Data

**Text:** "Had a long day"
**Metadata:** missing sleep_hours

**Predicted:** neutral
**Actual:** stressed

**Issue:**
Missing values reduce model accuracy.

**Improvement:**
Use better imputation strategies or add missing indicators.

---

## Case 7 — Sarcasm / Implicit Emotion

**Text:** "Yeah, everything is just perfect..."

**Predicted:** positive
**Actual:** frustrated

**Issue:**
Model cannot detect sarcasm.

**Improvement:**
Hard problem. Could be improved with more advanced NLP models.

---

## Case 8 — Medium Intensity Confusion

**Text:** "I feel a bit off today"

**Predicted intensity:** 2
**Actual intensity:** 3

**Issue:**
Subtle emotional differences are hard to capture.

**Improvement:**
Better regression tuning or more labeled data.

---

## Case 9 — Context Missing

**Text:** "Same as yesterday"

**Predicted:** neutral
**Actual:** stressed

**Issue:**
Model lacks previous context.

**Improvement:**
Use sequential or history-based models in future.

---

## Case 10 — Mixed Emotions

**Text:** "I’m anxious but also excited"

**Predicted:** anxious
**Actual:** mixed

**Issue:**
Model forces a single label.

**Improvement:**
Allow multi-label classification or probabilistic outputs.

---

## Key Insights

* Text alone is not reliable → metadata is very important
* Short and ambiguous inputs are major failure points
* Conflicting signals need better handling
* Noisy labels are unavoidable in real-world data
* Uncertainty modeling is important to flag unreliable predictions

---

## Conclusion

The model performs reasonably well but struggles in real-world scenarios such as ambiguity, missing data, and conflicting signals. Future improvements can focus on better text understanding, handling uncertainty, and incorporating more contextual information.
