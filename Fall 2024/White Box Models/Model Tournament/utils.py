from rich.console import Console
from rich import traceback

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import CategoricalNB
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier

from sklearn.datasets import load_iris, load_wine, load_breast_cancer, load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
print("Loaded imports")

console = Console() #for logging information to terminal with pretty colors

MODELS = {"Logistic Regression #1": LogisticRegression(penalty="l1", solver='liblinear'), "Logistic Regression #2": LogisticRegression(penalty="l2"), "Decision Tree #1": DecisionTreeClassifier(max_depth=2), "Decision Tree #2": DecisionTreeClassifier(max_depth=4),
          "Random Forest #1": RandomForestClassifier(max_depth=2), "Random Forest #2": RandomForestClassifier(max_depth=4), "SVM #1": SVC(kernel="linear"), "SVM #2": SVC(kernel="poly"), "KNN #1": KNeighborsClassifier(n_neighbors=5),
          "KNN #2": KNeighborsClassifier(n_neighbors=2), "Naïve Bayes #1": GaussianNB(), "Naïve Bayes #2": CategoricalNB(), "Gradient Boost #1": GradientBoostingClassifier(max_depth=3), "Gradient Boost #2": GradientBoostingClassifier(max_depth=5),
          "Neural Network #1": MLPClassifier(hidden_layer_sizes=(10, 7)), "Neural Network #2": MLPClassifier(hidden_layer_sizes=(5, 5))}

DATASETS = [load_iris, load_wine, load_breast_cancer, load_digits]

def compare_models(model1, model2, round_number): #round number should start at 1 and be 4 at most
    function1 = MODELS[model1]
    function2 = MODELS[model2]

    accuracy1, accuracy2 = train_test_model(function1, DATASETS[round_number-1]), train_test_model(function2, DATASETS[round_number-1])
    best = model1 if accuracy1 >= accuracy2 else model2
    log_info(model1, model2, accuracy1, accuracy2, round_number, best) #printing to the console
    return best

def train_test_model(model, load_dataset):
    X, Y = load_dataset(return_X_y=True)
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)

    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    accuracy = accuracy_score(y_pred, y_test)
    return accuracy

def log_info(model1, model2, accuracy1, accuracy2, round_number, best):
    dataset_names = ["Iris", "Wine", "Cancer", "Digit"]
    console.print()
    console.print(f"Working with the [yellow]{dataset_names[round_number-1]} dataset[/yellow]...")
    console.print(f"[blue]{model1}[/blue] had an accuracy of [red]{accuracy1 * 100}%[/red]")
    console.print(f"[blue]{model2}[/blue] had an accuracy of [red]{accuracy2 * 100}%[/red]")
    console.print(f"[bold green]{best} wins![/bold green]")

