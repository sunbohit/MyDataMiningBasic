from scipy.io import loadmat
import pywt #sudo pip3 install PyWavelets

inputfile = 'leleccum.mat'
mat = loadmat(inputfile)
print(mat)
'''
{'leleccum': array([[ 420.20278994,  423.52653517,  423.52271225, ...,  323.96580997,
         323.2400761 ,  323.85476049]])}

'''
signal = mat['leleccum'][0]
print(signal)
'''
[ 420.20278994  423.52653517  423.52271225 ...,  323.96580997  323.2400761
  323.85476049]
'''

c = pywt.wavedec(signal, 'bior3.7', level=5)
