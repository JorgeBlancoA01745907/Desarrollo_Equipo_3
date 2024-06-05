import os
from sklearn.metrics import roc_auc_score, roc_curve
import matplotlib.pyplot as plt
import numpy as np
from Model import TextProcessor

def main():
    # Datos de ejemplo
    # X contiene las similitudes calculadas por tu herramienta
    # y contiene las etiquetas reales: 1 para plagio y 0 para no plagio
    X = []
    y = []

    # Datos de ejemplo con etiquetas reales
    document_pairs = [
        ("FID-001.txt", "org-009.txt", 0),
        ("FID-002.txt", "org-010.txt", 0),
        ("FID-003.txt", "org-011.txt", 0),
        ("FID-004.txt", "org-011.txt", 0),
        ("FID-005.txt", "org-023.txt", 1),
        ("FID-005.txt", "org-059.txt", 1),
        ("FID-006.txt", "org-011.txt", 0),
        ("FID-007.txt", "org-011.txt", 0),
        ("FID-008.txt", "org-011.txt", 0),
        ("FID-009.txt", "org-011.txt", 0),
        ("FID-010.txt", "org-091.txt", 1),
        ("FID-011.txt", "org-011.txt", 0),
        ("FID-012.txt", "org-011.txt", 0),
        ("FID-013.txt", "org-009.txt", 1),
        ("FID-013.txt", "org-001.txt", 1),
        ("FID-014.txt", "org-019.txt", 1),
        ("FID-014.txt", "org-011.txt", 1),
        ("FID-015.txt", "org-034.txt", 1),
        ("FID-016.txt", "org-046.txt", 1),
        ("FID-017.txt", "org-062.txt", 1),
        ("FID-018.txt", "org-057.txt", 1),
        ("FID-019.txt", "org-066.txt", 1),
        ("FID-020.txt", "org-014.txt", 1),
    ]

    for file1, file2, label in document_pairs:
        file1_path = os.path.join("documents", file1)
        file2_path = os.path.join("documents", file2)
        processor = TextProcessor(file1_path, file2_path)
        similarity_score = processor.process()
        if (similarity_score['Percentage of similarity'] >= 50.1):
            print(similarity_score['Percentage of similarity'])
            X.append(1)
        else:
            print("0")
            X.append(0)
        y.append(label)

    # Calcula el AUC-ROC
    auc = roc_auc_score(y, X)
    print(f"AUC-ROC: {auc:.2f}")

    # Genera la curva ROC
    fpr, tpr, thresholds = roc_curve(y, X)

    plt.figure()
    plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic')
    plt.legend(loc="lower right")
    plt.show()

if __name__ == "__main__":
    main()
