

from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error
from datetime import datetime

def SARIMAX_hyperparameter_tune(X_train, X_test, y_train, y_test, Pmax=3, Qmax=3, Dmax=3, pmax=5, qmax=5, dmax=5, S1 = 0, S2 = 3, S3 = 12):
    """
    This function attempts to find the best hyperparameters for a SARIMAX model by tuning the parameters P, D, Q, p, q, d, and S.

    Parameters:
    X_train (DataFrame): The training data for the exogenous variables.
    X_test (DataFrame): The testing data for the exogenous variables.
    y_train (Series): The training data for the response variable.
    y_test (Series): The testing data for the response variable.
    Pmax (int, optional): The maximum number of autoregressive terms to consider for the seasonal component. Defaults to 3.
    Qmax (int, optional): The maximum number of moving average terms to consider for the seasonal component. Defaults to 3.
    Dmax (int, optional): The maximum number of differences terms to consider for the seasonal component. Defaults to 3.
    pmax (int, optional): The maximum number of autoregressive terms to consider for the non-seasonal component. Defaults to 5.
    qmax (int, optional): The maximum number of moving average terms to consider for the non-seasonal component. Defaults to 5.
    dmax (int, optional): The maximum number of differences terms to consider for the non-seasonal component. Defaults to 5.

    Base on code by: Joseph Nelson, Justin Pounders, Matt Brems in General Assembly DSI curriculm.

    Returns:
    None

    """
def SARIMAX_hyperparameter_tune(X_train, X_test, y_train, y_test, Pmax=3, Qmax=3, Dmax=3, pmax=5, qmax=5, dmax=5):
    #import warnings

    #warnings.filterwarnings("ignore", message="No frequency information was provided")
    best_mse = float("inf")
    best_aic = float("inf")
    final_P = 0
    final_D = 0
    final_Q = 0
    final_S = 0
    final_p = 0
    final_d = 0
    final_q = 0


    for P in range(Pmax):
        for Q in range(Qmax):
            for D in range(Dmax):
                for p in range(pmax): 
                    for q in range(qmax):
                        for d in range(dmax):                            
                            for S in range(2,12):
                                #try:
                                    print(f'Attempting to fit SARIMAX({p},{d},{q})x({P},{D},{Q},{S})')
                                    # Instantiate SARIMAX model.
                                    sarimax = SARIMAX(endog = y_train,
                                                    order = (p, d, q),              # (p, d, q)
                                                    seasonal_order = (P, D, Q, S),  # (P, D, Q, S)
                                                    exog = X_train.dropna()) 
                
                                    # Fit SARIMAX model.
                                    model = sarimax.fit(disp=False)

                                    # Generate predictions based on test set.
                                    preds = model.predict(
                                                        start = datetime((int(str(y_test.index[0])[0:4])), 
                                                                            int(str(y_test.index[0])[5:7]), 
                                                                            int(str(y_test.index[0])[8:10])),
                                                        end = datetime((int(str(y_test.index[-1])[0:4])), 
                                                                        int(str(y_test.index[-1])[5:7]), 
                                                                        int(str(y_test.index[-1])[8:10])),
                                                        exog = X_test.dropna())
                                    
                                    current_aic = model.aic
                                    # Update best AIC and parameters if the current model's AIC is lower
                                    if current_aic < best_aic:
                                        best_aic = current_aic
                                        # Update best parameters for AIC
                                        final_P_aic = P
                                        final_D_aic = D
                                        final_Q_aic = Q
                                        final_S_aic = S
                                        final_p_aic = p
                                        final_d_aic = d
                                        final_q_aic = q

                                    # Evaluate predictions.
                                    print(f'The MSE for ({p},{d},{q})x({P},{D},{Q},{S}) is: {mean_squared_error(y_test, preds)}')

                                    # Save for final report.
                                    if best_mse > mean_squared_error(y_test, preds):
                                        best_mse = mean_squared_error(y_test, preds)
                                        final_P = P
                                        final_D = D
                                        final_Q = Q
                                        final_S = S
                                        final_p = p
                                        final_d = d
                                        final_q = q

                                #except:
                                    #   pass
                print(f'Our model that minimizes MSE on the testing data is the SARIMAX({final_p}, {final_d}, {final_q})x({final_P},{final_D},{final_Q},{final_S}).')
                print(f'This model has an MSE of {best_mse}.')

                print(f'Our model that minimizes AIC on the testing data is the SARIMAX({final_p_aic}, {final_d_aic}, {final_q_aic})x({final_P_aic},{final_D_aic},{final_Q_aic},{final_S_aic}).')
                print(f'This model has an AIC of {best_aic}.')