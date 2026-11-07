import pandas as pd
import matplotlib.pyplot as plt

print("🚢 Ship Traffic Analysis - Zain Ali")

data = {
    'Ship_Type': ['Container', 'Tanker', 'Bulk', 'Container', 'Tanker'],
    'Port': ['Karachi', 'Gwadar', 'Port Qasim', 'Karachi', 'Gwadar'],
    'Traffic_Count': [120, 85, 95, 130, 90]
}
df = pd.DataFrame(data)

print("\n--- Busiest Ports ---")
print(df.groupby('Port')['Traffic_Count'].sum())

print("\n--- Ship Type Distribution ---")
print(df['Ship_Type'].value_counts())

df.groupby('Port')['Traffic_Count'].sum().plot(kind='bar')
plt.title('Busiest Ports - Ship Traffic')
plt.savefig('port_traffic.png')
print("\nChart saved!")