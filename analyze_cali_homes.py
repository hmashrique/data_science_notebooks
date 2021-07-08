import pandas
import numpy
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.linear_model import SGDRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score, ShuffleSplit, KFold
from sklearn.externals import joblib

#---------------------------------------------------------------------------
def get_data():
	return pandas.read_csv('/Users/vphan/Dropbox/datasets/cali_housing.csv')

#---------------------------------------------------------------------------
def process_data(df):
	# Drop missing values
	df.dropna(inplace=True)

	# Discretize median income
	df['income_cat'] = numpy.ceil(df.median_income / 1.5)
	df['income_cat'] = df.income_cat.where( df.income_cat < 6 , 6)

	# Convert ocean proximity to non-categorical variables
	return pandas.get_dummies(df, columns=['ocean_proximity'])

#---------------------------------------------------------------------------
def validate(model, X, y):
	# v = KFold(n_splits=20, shuffle=True)
	print(model)
	v = ShuffleSplit(n_splits=100, test_size=0.1)
	scores = cross_val_score(model, X, y, cv=v)
	print('average score:', sum(scores)/len(scores))

#---------------------------------------------------------------------------

df = get_data()
df = process_data(df)

# print(df.columns)
y = df.median_house_value
X = df[ ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'income_cat', 'ocean_proximity_<1H OCEAN', 'ocean_proximity_INLAND', 'ocean_proximity_ISLAND','ocean_proximity_NEAR BAY', 'ocean_proximity_NEAR OCEAN'] ]

# models = [LinearRegression(), Ridge(), DecisionTreeRegressor()]
# for model in models:
# 	validate(model, X, y)

best_model = DecisionTreeRegressor()
best_model.fit(X,y)
joblib.dump(best_model, 'cali_home_regressor')

print('Done')

print(X.iloc[0])
print(y.iloc[0])