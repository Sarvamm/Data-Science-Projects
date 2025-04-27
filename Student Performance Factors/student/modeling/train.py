import pandas as pd

df = pd.read_csv(
    r"C:\Users\Sarvamm\Documents\Repos\Data-Science-Projects\Student Performance Factors\data\processed\numeric_data.csv"
)
df.head()

y = df["Exam_Score"]
X = df.drop(columns=["Exam_Score"])


# train test split
from sklearn.model_selection import train_test_split  # noqa: E402

Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.3, random_state=42)


# standardization
from sklearn.preprocessing import StandardScaler  # noqa: E402

scaler = StandardScaler()
XtrainNorm = scaler.fit_transform(Xtrain)
XtestNorm = scaler.transform(Xtest)


# import seaborn as sns; import matplotlib.pyplot as plt  # noqa: E402
# fig, ax = plt.subplots(1, 2, figsize=(12, 6))
# sns.boxplot(XtrainNorm, ax=ax[0])
# sns.boxplot(XtestNorm, ax=ax[1])
# plt.show()

# Training
from sklearn.linear_model import LinearRegression  # noqa: E402

reg = LinearRegression()

reg.fit(XtrainNorm, ytrain)

# from IPython.display import display, Math

# def format_regression_equation(intercept, coefficients):
#     equation = r"y = {:.2f}".format(intercept)
#     for i, beta in enumerate(coefficients):
#         equation += r" + {:.2f}x_{}".format(beta, i+1)

#     display(Math(equation))

# # Example usage:
# reg_intercept = reg.intercept_
# reg_coef = reg.coef_

# format_regression_equation(reg_intercept, reg_coef)


# save the model
import pickle

pickle.dump(
    reg,
    open(
        r"C:\Users\Sarvamm\Documents\Repos\Data-Science-Projects\Student Performance Factors\models\linear_regression_model.pkl",
        "wb",
    ),
)
