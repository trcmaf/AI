import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

true_labels = [2, 0, 0, 2, 4, 4, 1, 0, 3, 3, 3]
pred_labels = [2, 1, 0, 2, 4, 3, 1, 0, 1, 3, 3]

#Building confusion matrix
confusion_mat = confusion_matrix(true_labels, pred_labels)

#Visualization
plt.imshow(confusion_mat, interpolation='nearest', cmap=plt.cm.gray)
plt.title("Матрица неточностей")
plt.colorbar()
ticks = np.arange(5)
plt.xticks(ticks, ticks)
plt.yticks(ticks, ticks)
plt.ylabel('Калибровочные метки')
plt.xlabel('Предсказанные метки')
plt.show()

#Report
targets = ['Class-0', 'Class-1', 'Class-2', 'Class-3', 'Class-4']
print ('\n', classification_report(true_labels, pred_labels, target_names = targets))