import pandas as pd
from datetime import datetime

data = {
    "Name": ["Nikhil", "John", "Ram"],
    "DueDate": [datetime(2025, 6, 25), datetime(2025, 7, 1), datetime(2025, 6, 10)],
    "Status": ["30day", "paid", "30day"]
}

df = pd.DataFrame(data)
df.to_excel("due_data.xlsx", index=False)
print("✅ Sample due_data.xlsx created.")
