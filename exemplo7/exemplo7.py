from sklearn.datasets import fetch_openml
mnist = fetch_openml('mnist_784', version=1)
mnist.keys()
dict_keys(['data', 'target', 'feature_names', 'DESCR', 'details', 'categories', 'url'])

x, y = mnist['data'], mnist['target']
x.shape(7000, 784)
y.shape(7000)
some_digit = X[0]
some_digit_image = some_digit.reshape(28, 28)
plt.imshow(some_digit_image, cpam='binary')
plt.axis('off')
plt.show()