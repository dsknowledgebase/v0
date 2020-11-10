# Facebook Prophet  

### What is Prophet?
Facebook Prophet is a forecasting model implemented in both R and Python.  It is available as a package and can be installed with the common methods for each language.  The underlying model is an additive model where non-linear trends are fit to the seasonality in the data.  It is fast and is able to handle outliers, missing data, and significant changes to the trends in the data.  The model also offers tunable parameters that can be used to add additional data to the model and improve the forecast.

### Who should use Prophet?
Often companies will produce forecasts using Excel using basic methods.  Prophet should be used when looking at improving forecast methods and if you are comfortable with the underlying models and programming required.   It is important to be able to explain the general ideas behind the model to your stakeholders. 

### When should I use Prophet?
* Forecasting systems that have a seasonal component.
* Testing different time series forecasting methods for your project.
* If your end users are comfortable with a product written in python or R and there is someone who can maintain the model.

### How do I learn about it?
The best way to learn how to implement and use the Facebook Prophet model is to read the documentation and to read the accompanying paper.  The paper can be a bit challenging but it is important to understand how the model works in order to diagnose potential problems when implementing the model.   In addition to the documentation there are several courses on Udemy or Coursera that cover Facebook Prophet as a module in the time series course.

### Strengths
* Robust to outliers and missing data.
* Built in methods to deal with shifts in the time series trend
* Ability to easily add additional regressors to the model.
* Built in methods to handle hyper parameter tuning and cross validation

### Limitations
* Must be implemented in either R or Python.  Requires skills in either programming language.
* Challenging to understand the underlying model.
* Works best with several periods of historical data that has a strong seasonal component

### Alternative Options
* Microsoft Excel
* Python – Statsmodels
* R – Time series packages

Last Updated:  10/31/2020
