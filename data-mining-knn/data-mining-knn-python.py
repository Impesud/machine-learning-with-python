# Data Mining and KNN with Python
# Visit my profile: https://github.com/impesud
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()

# Create a Pandas DataFrame
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['target'] = iris.target

# Visualize the distribution of petal lengths for different species
#%%
plt.figure(figsize=(8, 6))

for i in range(3):
    species = iris_df[iris_df['target'] == i]
    plt.hist(species['petal length (cm)'], alpha=0.5, label=iris.target_names[i])

plt.xlabel('Petal Length (cm)')
plt.ylabel('Count')
plt.title('Distribution of Petal Lengths by Species')
plt.legend()
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

# Separate features from labels
X = iris_df.drop('target', axis=1)
y = iris_df['target']

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

k_range = range(1,31)
scores = {}
scores_list = []

# Try running from k=1 through 30 and record testing accuracy
#%%
for k in k_range:

    # Initialize the KNN classifier and train it
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)

    # Predict species labels for the test set
    y_pred = knn.predict(X_test)

    # Calculate the model's accuracy
    scores[k] = metrics.accuracy_score(y_test, y_pred)
    scores_list.append(metrics.accuracy_score(y_test, y_pred))

plt.plot(k_range, scores_list)
plt.xlabel("Value of K for KNN")
plt.ylabel("Testing accuracy")
plt.show()

knn = KNeighborsClassifier(n_neighbors=12)
knn.fit(X_train.values, y_train.values)

x_new = [[4,3,5,2], [4,5,2,3]]
y_predict = knn.predict(x_new)

predicted_species_0 = iris.target_names[y_predict[0]]
predicted_species_1 = iris.target_names[y_predict[1]]

print(f"The predicted species for the first example data point is: {predicted_species_0}")
print(f"The predicted species for the second example data point is: {predicted_species_1}")
