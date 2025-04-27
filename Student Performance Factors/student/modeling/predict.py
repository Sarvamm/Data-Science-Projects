import pickle

# from train import XtestNorm, ytest
import os

os.getcwd()
model = pickle.load(
    open(
        r"C:\Users\Sarvamm\Documents\Repos\Data-Science-Projects\Student Performance Factors\models\linear_regression_model.pkl",
        "rb",
    )
)

# pred = model.predict(XtestNorm)
# residuals = ytest - pred

# import seaborn as sns  # noqa: E402
# import matplotlib.pyplot as plt  # noqa: E402

# sns.displot(residuals, kind="kde")
# plt.show()


# from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
# import pandas as pd


def getpred(input):
    pred = model.predict(input)
    return pred


# def evaluation(ytest, pred):
#     metrics = {
#         "Mean Squared Error": [mean_squared_error(ytest, pred)],
#         "Mean Absolute Error": [mean_absolute_error(ytest, pred)],
#         "R2 Score": [r2_score(ytest, pred)],
#     }
#     results_df = pd.DataFrame(metrics).T
#     print(results_df)


# evaluation(ytest, pred)
