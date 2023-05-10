import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

# Define true labels and predicted labels
y_true = np.array(["Covid", "Normal", "Virus", "Covid", "Normal", "Virus", "Covid", "Normal", "Virus"])
y_pred = np.array(["Covid", "Normal", "Virus", "Covid", "Normal", "Virus", "Covid", "Normal", "Virus"])

# Define confusion matrix
cm = np.array([[347, 0, 0],
               [16, 624, 27],
               [3, 8, 605]])

# Define class labels
classes = ['Covid', 'Normal', 'Virus']

# Plot confusion matrix
fig, ax = plt.subplots()
im = ax.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
ax.figure.colorbar(im, ax=ax)
ax.set(xticks=np.arange(cm.shape[1]),
       yticks=np.arange(cm.shape[0]),
       xticklabels=classes, yticklabels=classes,
       title='Confusion matrix',
       ylabel='True label',
       xlabel='Predicted label')

# Rotate the x-axis labels
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
fmt = 'd'
thresh = cm.max() / 2.
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        ax.text(j, i, format(cm[i, j], fmt),
                ha="center", va="center",
                color="white" if cm[i, j] > thresh else "black")

fig.tight_layout()
plt.show()
