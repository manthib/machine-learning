import pandas as pd

from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier as RandomForest
from sklearn import datasets
from sklearn import svm

bc_dataset = datasets.load_breast_cancer()

# Initialize label encoder
label_encoder = preprocessing.LabelEncoder()

# define target (what we want to predict) and train (data used to predict)
target = bc_dataset.target
train = bc_dataset.data

# Split: train 60% test 40%
from sklearn.cross_validation import train_test_split
split = train_test_split(train, target, test_size=0.4, random_state=42)
data_train, data_test, target_train, target_test = split

## train with RandomForest
model = RandomForest(n_estimators=10)
model.fit(data_train[:None], target_train)
print 'perf: '
print model.score(data_test[:None], target_test)
    
# variable with the more impact ?
features = ['mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness', 'mean compactness', 'mean concavity', 'mean concave points', 'mean symmetry', 'mean fractal dimension', 'radius error', 'texture error', 'perimeter error', 'area error', 'smoothness error', 'compactness error', 'concavity error', 'concave points error', 'symmetry error', 'fractal dimension error', 'worst radius', 'worst texture', 'worst perimeter', 'worst area', 'worst smoothness', 'worst compactness', 'worst concavity', 'worst concave points', 'worst symmetry', 'worst fractal dimension']
for feature, imp in zip(features, model.feature_importances_):
    print(feature, imp)    
    
# ## now we predict
print('==> predict: ')
prediction = model.predict(data_test[:None])
reality = target_test
result = pd.DataFrame({'reality': reality,
                       'prediction': prediction})

result['get_it'] = 'nop'
result.loc[result.prediction == result.reality, 'get_it'] = 'yes'
print result.head(20)

print('  == get_it:')
print(result.get_it.value_counts())