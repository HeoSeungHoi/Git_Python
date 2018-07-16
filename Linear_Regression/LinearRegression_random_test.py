from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error

# scikit_learn에서 제공하는 데이터 제공 함수
X_train, y_train, coef = make_regression(n_samples=50, n_features=1, bias=50, noise=20, coef=True, random_state=1)

# 상수항이 있으면
model = LinearRegression(fit_intercept=True)  # 절편이 있는 리니어 하이파시스 생성
model.fit(X_train, y_train)  # X_train, y_train 데이터로 훈련을 시키고 모델 생성
a = model.coef_
b = model.intercept_
print("기울기 : {0} 절편 : {1}".format(a, b))
# 기울기 : [86.01397082] 절편 : 54.36888490326774

# 선형회귀 직선을 작성하기 위해 데이터 생성
# X_train 데이터의 초대, 최소 값 사이를 100개를 생성.
x_test = np.linspace(np.min(X_train), np.max(X_train), 10)
print(x_test)
# [-2.3015387  -2.25707613 -2.21261357 -2.168151   -2.12368844 -2.07922588
#  -2.03476331 -1.99030075 -1.94583819 -1.90137562 -1.85691306 -1.81245049
#  -1.76798793 -1.72352537 -1.6790628  -1.63460024 -1.59013767 -1.54567511
#  -1.50121255 -1.45674998 -1.41228742 -1.36782485 -1.32336229 -1.27889973
#  -1.23443716 -1.1899746  -1.14551203 -1.10104947 -1.05658691 -1.01212434
#  -0.96766178 -0.92319921 -0.87873665 -0.83427409 -0.78981152 -0.74534896
#  -0.70088639 -0.65642383 -0.61196127 -0.5674987  -0.52303614 -0.47857357
#  -0.43411101 -0.38964845 -0.34518588 -0.30072332 -0.25626075 -0.21179819
#  -0.16733563 -0.12287306 -0.0784105  -0.03394793  0.01051463  0.05497719
#   0.09943976  0.14390232  0.18836489  0.23282745  0.27729001  0.32175258
#   0.36621514  0.41067771  0.45514027  0.49960283  0.5440654   0.58852796
#   0.63299053  0.67745309  0.72191565  0.76637822  0.81084078  0.85530335
#   0.89976591  0.94422847  0.98869104  1.0331536   1.07761617  1.12207873
#   1.16654129  1.21100386  1.25546642  1.29992898  1.34439155  1.38885411
#   1.43331668  1.47777924  1.5222418   1.56670437  1.61116693  1.6556295
#   1.70009206  1.74455462  1.78901719  1.83347975  1.87794232  1.92240488
#   1.96686744  2.01133001  2.05579257  2.10025514]

X_test = x_test.reshape(-1, 1)
print(X_test)  # ( 100 x 1)
# [[-2.3015387 ]
#  [-2.25707613]
#  [-2.21261357]
#  [-2.168151  ]
#  [-2.12368844]
#  [-2.07922588]
#  [-2.03476331]
#  [-1.99030075]
#  [-1.94583819]
#  [-1.90137562]
#  [-1.85691306]
#  [-1.81245049]
#  [-1.76798793]
#  [-1.72352537]
#  [-1.6790628 ]
#  [-1.63460024]
#  [-1.59013767]
#  [-1.54567511]
#  [-1.50121255]
#  [-1.45674998]
#  [-1.41228742]
#  [-1.36782485]
#  [-1.32336229]
#  [-1.27889973]
#  [-1.23443716]
#  [-1.1899746 ]
#  [-1.14551203]
#  [-1.10104947]
#  [-1.05658691]
#  [-1.01212434]
#  [-0.96766178]
#  [-0.92319921]
#  [-0.87873665]
#  [-0.83427409]
#  [-0.78981152]
#  [-0.74534896]
#  [-0.70088639]
#  [-0.65642383]
#  [-0.61196127]
#  [-0.5674987 ]
#  [-0.52303614]
#  [-0.47857357]
#  [-0.43411101]
#  [-0.38964845]
#  [-0.34518588]
#  [-0.30072332]
#  [-0.25626075]
#  [-0.21179819]
#  [-0.16733563]
#  [-0.12287306]
#  [-0.0784105 ]
#  [-0.03394793]
#  [ 0.01051463]
#  [ 0.05497719]
#  [ 0.09943976]
#  [ 0.14390232]
#  [ 0.18836489]
#  [ 0.23282745]
#  [ 0.27729001]
#  [ 0.32175258]
#  [ 0.36621514]
#  [ 0.41067771]
#  [ 0.45514027]
#  [ 0.49960283]
#  [ 0.5440654 ]
#  [ 0.58852796]
#  [ 0.63299053]
#  [ 0.67745309]
#  [ 0.72191565]
#  [ 0.76637822]
#  [ 0.81084078]
#  [ 0.85530335]
#  [ 0.89976591]
#  [ 0.94422847]
#  [ 0.98869104]
#  [ 1.0331536 ]
#  [ 1.07761617]
#  [ 1.12207873]
#  [ 1.16654129]
#  [ 1.21100386]
#  [ 1.25546642]
#  [ 1.29992898]
#  [ 1.34439155]
#  [ 1.38885411]
#  [ 1.43331668]
#  [ 1.47777924]
#  [ 1.5222418 ]
#  [ 1.56670437]
#  [ 1.61116693]
#  [ 1.6556295 ]
#  [ 1.70009206]
#  [ 1.74455462]
#  [ 1.78901719]
#  [ 1.83347975]
#  [ 1.87794232]
#  [ 1.92240488]
#  [ 1.96686744]
#  [ 2.01133001]
#  [ 2.05579257]
#  [ 2.10025514]]

# 그래프를 그리기 위한 y 예측 값 --> 직선을 그리기 위한 x 값과 그에 따른 y 값 정의
y_predict = model.predict(X_test)  # 테스트 데이터를 내가 정한 모델에 넣은 결과

y_pred = model.predict(X_train)
mse = mean_squared_error(y_train, y_pred) # 학습결과를 테스트함
print(mse)
# 265.3944371681383

plt.plot(X_test, y_predict, 'g-', label="regression")
plt.scatter(X_train, y_train, c='r', label="train_data")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Regression")
plt.legend()
plt.show()