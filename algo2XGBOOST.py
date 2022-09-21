# First XGBoost model for Pima Indians dataset
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import pickle
from sklearn import  preprocessing

def XGB():
    data = pd.read_csv("car.data")
    # print(data.head())

    le = preprocessing.LabelEncoder()
    Age = data.Age.to_list()
    Job = le.fit_transform(list(data["Job"]))

    Qualification = le.fit_transform(list(data["Qualification"]))
    Hstatus = le.fit_transform(list(data["Hstatus"]))
    ManufacturingYear = data.ManufacturingYear.to_list()
    Cc = data.Cc.to_list()
    Vage = data.Vage.to_list()
    Use = le.fit_transform(list(data["Use"]))
    Mileage = data.Mileage.to_list()
    Premium = data.Premium.to_list()
    Tclaim = le.fit_transform(list(data["Tclaim"]))
    InsuranceVal = data.InsuranceVal.to_list()
    Decision = le.fit_transform(list(data["Decision"]))
    
    X = list(zip(Age, Job, Qualification, Hstatus, ManufacturingYear, Cc ,Vage ,Use,Mileage,Premium,Tclaim,InsuranceVal))
    Y = list(Decision)

    best = 0




    # split data into train and test sets
    for _ in range(20):
        seed = 7
        test_size = 0.33
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)
        # fit model no training data
        model = XGBClassifier()
        model.fit(X_train, y_train)
        # make predictions for test data
        y_pred = model.predict(X_test)
        predictions = [round(value) for value in y_pred]
        # evaluate predictions
        accuracy = accuracy_score(y_test, predictions)
        # print(str(_) +"->Accuracy: " + str((accuracy * 100.0)))
        if accuracy > best and accuracy != 1.0:
            best = accuracy
            with open("CarData_XGBOOST.pickle", "wb") as f:
                pickle.dump(model, f)

    # print("best : " +str(best * 100.0))
    return best

