import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def Gaussian(x, A, x0, sigma):
    return A * np.exp(-(x - x0)**2 / (2 * sigma**2))


x = np.linspace(0.4,3.5,32)
y = np.array([613,647,817,1008,1127,1194,1237,1262,1298,1381,1335,1446,1557,1641,1624,1660,1460,1301,1298,1104,1154,1216,1333,1757,2693,6624,7984,4680,2644,1803,1339,942])

xprime = x[22:31]
yprime = y[22:31]

print(xprime)
popt, pcov = curve_fit(Gaussian, xprime, yprime,
                       p0=[yprime.max(), xprime[np.argmax(yprime)], 0.1])
A, x0, sigma = popt
FWHM = 2*np.sqrt(2*np.log(2))*sigma
R = (FWHM / x0) * 100
print(f"Resolution: {R:.2f} %")
print(f"FWHM: {FWHM:.4f} V")
print(f"Mean Voltage (x0): {x0:.2f} V")
print(f"Standard Deviation (sigma): {sigma:.4f} V")
# Reduced chi-squared
sigma_y = np.sqrt(yprime)
residuals = yprime - Gaussian(xprime, *popt)
chi2 = np.sum((residuals / sigma_y)**2)
ndof = len(xprime) - len(popt)
chi2_red = chi2 / ndof
print(f"Reduced chi-squared: {chi2_red:.3f}")

x_fit = np.linspace(xprime.min(), xprime.max(), 1000)
y_fit = Gaussian(x_fit, *popt)


plt.plot(x, y, marker='o')
plt.plot(x_fit, y_fit, label='Gaussian Fit', color='blue')
plt.axhline(A / 2, linestyle='--', linewidth=1.5, label='Half Maximum')
plt.axvline(x0 - FWHM / 2, linestyle='--', linewidth=1.5, label='FWHM Left')
plt.axvline(x0 + FWHM / 2, linestyle='--', linewidth=1.5, label='FWHM Right')
plt.xlabel('LLD Voltage (V)')
plt.ylabel('Counts')
plt.title('SCA Counts vs LLD Voltage at 650V Operating Voltage')
plt.grid()
plt.legend()
plt.show()