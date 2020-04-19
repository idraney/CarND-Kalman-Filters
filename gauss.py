#   One Dimensional Kalman Filter

# (Update) Measurement parameter update step in a Kalman filter
# Uses two gaussian distributions: prior and measurement distributions.

# (Predict) Measurement of new mean and variance given the 
# mean and variance of the prior belief and the mean and variance of motion.

def update(mean1, var1, mean2, var2):
    new_mean = (var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = 1 / (1 / var1 + 1 / var2)
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

### First Run: Using Scalars
# mean1 = 10
# var1  = 4
# mean2 = 12
# var2  = 4

# print("Update:    ", update(mean1, var1, mean2, var2))
# print("Prediction:", predict(mean1, var1, mean2, var2))

### Second Run: Using Vectors
measurements = [5, 6, 7, 9, 10]
motion = [1, 1, 2, 1, 1]
measurement_sig = 4
motion_sig = 2
mu = 0
sig = 10000

# Prep mu and sig for use in loop
new_mean = mu
new_var = sig

# Loop to obtain updates and predictions from measurement & motion lists
for i in range(len(measurements)):
    [new_mean, new_var] = update(measurements[i], measurement_sig, new_mean, new_var)
    print("Update:    ", [new_mean, new_var])
    [new_mean, new_var] = predict(motion[i], motion_sig, new_mean, new_var)
    print("Predict:    ", [new_mean, new_var])

