# EDGE_PLAN.md

## Overview

This section explains how the system can be deployed on edge devices like mobile phones or low-resource environments.

---

## Model Choice

For edge deployment, lightweight models are preferred:

* Logistic Regression instead of RandomForest
* Reduced TF-IDF features (500–1000)

This helps reduce memory usage and improve speed.

---

## Deployment Approach

* Convert trained model to ONNX or TensorFlow Lite format
* Load model directly on device
* Run inference locally without internet

---

## Latency Considerations

* Prediction should happen in less than 100ms
* Smaller models ensure faster response

---

## Tradeoffs

* Smaller model → faster but slightly less accurate
* Larger model → more accurate but slower

For edge systems, speed and efficiency are more important.

---

## Memory Optimization

* Limit number of features
* Avoid heavy models like large neural networks
* Use efficient data structures

---

## Handling Real-World Constraints

* Works without internet
* Handles missing or partial input
* Uses fallback logic for short text

---

## Conclusion

The system can be adapted for edge deployment by using lightweight models and optimized feature processing. This ensures fast, reliable performance on mobile or low-resource devices.
