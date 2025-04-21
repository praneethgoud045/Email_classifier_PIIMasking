# Email_classifier_PIIMasking
Email Classification for Support Team

# Email Classification for Support Team 

This project implements an Email Classification system for a company's support team.

It includes:
- **Personal Information (PII) masking** using Regex (without using LLMs),
- **Email classification** into predefined categories (e.g., Billing Issues, Technical Support),
- **API development** using FastAPI,
- **Deployment ready** for Hugging Face Spaces.

---

## 🛠️ Technologies Used

- Python 3.12
- FastAPI
- Uvicorn
- scikit-learn
- Pandas
- Joblib
- Regex

---

## 📚 Project Structure

```
.
├── api.py                # FastAPI application exposing the API
├── utils.py              # Utility functions for PII masking
├── models.py             # (Optional) Model training functions
├── saved_models/         # Folder containing trained ML model (email_classifier.pkl)
├── requirements.txt      # List of required Python libraries
├── README.md             # This file
└── data/                 # Dataset folder (used for training)
```

---

## 🚀 How to Set Up and Run Locally

### 1. Clone the Repository

```bash
git clone <your-github-repo-link>
cd <project-folder>
```

Or download the project manually.

---

### 2. Install the Requirements

```bash
pip install -r requirements.txt
```

---

### 3. Start the API Server

```bash
uvicorn api:app --reload
```

The server will run at:

```
http://127.0.0.1:8000
```

---

### 4. Open Swagger UI for Testing

Navigate to:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

You will see the API documentation where you can test the POST endpoint `/classify-email`.

---

## 📬 API Endpoint Details

### Endpoint: `/classify-email`

- **Method:** `POST`
- **Request Body (JSON):**
```json
{
  "email_body": "Email content goes here."
}
```

- **Response Body (JSON):**
```json
{
  "input_email_body": "Original email text",
  "list_of_masked_entities": [
    {
      "position": [start_index, end_index],
      "classification": "entity_type",
      "entity": "original_text"
    }
  ],
  "masked_email": "Masked email text",
  "category_of_the_email": "Predicted category"
}
```

✅ **This matches the exact output format required in assignment instructions.**

---

## ⚙️ How the System Works

1. **PII Masking:**  
   - Detects and masks fields like `full_name`, `email`, `phone_number`, `dob`, `aadhar_num`, `credit_debit_no`, `cvv_no`, `expiry_no` using Regex.
2. **Classification:**  
   - The masked email is passed to a trained Naive Bayes model (or another ML model) for classification into support categories.
3. **API Output:**  
   - The API returns the original input, the list of masked entities, the masked email, and the predicted category.

---

OUTPUT:
![Screenshot 2025-04-21 004731](https://github.com/user-attachments/assets/9c330951-6a6e-4ff1-9a93-1df949fd3c83)
![Screenshot 2025-04-21 004835](https://github.com/user-attachments/assets/85b81e45-1817-4d1f-9300-d1aa21aa281d)

