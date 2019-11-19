freq = 542445
temp = 400

humidity = (freq + 130*temp - 551999)/(-1.1*temp - 34.7)

humidity = (freq*10 + 130*temp -5519990)/(-11*temp/10 - 347)

print(humidity)

C = 5.48753740e+05
M = -6.49137947e+01

humidity = (freq - C)/M

print(humidity)
