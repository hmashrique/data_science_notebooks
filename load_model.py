from sklearn.externals import joblib

model = joblib.load('cali_home_regressor')
print(model)

# now I can use this model to predict new data.
d1 = [-122.5,37.9,41.05,880,129.1,322,126,6,0,0,0,1,0]

print(model.predict( [d1] ))