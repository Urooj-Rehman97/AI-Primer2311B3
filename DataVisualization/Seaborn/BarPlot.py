import matplotlib.pyplot as plt
import seaborn as sns

products = ["Skin Care", "Home Appliances", "House Cleaning", "Hair Care", "Home Decor"]
quantity = [150, 90, 100, 230, 120]
sns.barplot(x=products, y=quantity)
plt.show()