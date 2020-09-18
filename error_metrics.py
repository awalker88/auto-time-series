import pandas as pd


def mse(data: pd.DataFrame, prediction: str, actuals: str):
    pass


def rmse(data: pd.DataFrame, prediction: str, actuals: str):
    pass


def mape(data: pd.DataFrame, prediction: str, actuals: str):
    pass


def smape(data: pd.DataFrame, prediction: str, actuals: str):
    pass


def mase(data: pd.DataFrame, prediction: str, actuals: str, step_size: int = 1):
    data = data[[prediction, actuals]].copy()
    data['shifted_actuals'] = data[actuals].shift(step_size)
    data['abs_shifted_error'] = abs(data[actuals] - data['shifted_actuals'])
    data['abs_prediction_error'] = abs(data[actuals] - data[prediction])

    avg_shifted_error = data[~data['abs_shifted_error'].isna()]['abs_shifted_error'].sum() / (len(data) - step_size)
    data['abs_scaled_error'] = data['abs_prediction_error'] / avg_shifted_error

    return data['abs_scaled_error'].mean()