import numpy as np
import matplotlib.pyplot as plt


wavsols = [ 'wavsol0.txt', 'wavsol1.txt', 'wavsol2.txt' ]
wavcors = [ 'wavcor0.txt', 'wavcor1.txt', 'wavcor2.txt' ]
spectra = [ 'spectra0.txt', 'spectra1.txt', 'spectra2.txt' ]

bandpass = [ 450, 475 ]
fluxes = []
for k in range( 3 ):
    wavsol = np.loadtxt( wavsols[k] )
    spectrum = np.loadtxt( spectra[k] )
    ixs_bandpass = ( wavsol[0,:]>bandpass[0] )*( wavsol[0,:]<bandpass[1] )
    fluxes += [ np.sum( spectrum[:,ixs_bandpass], axis=1 ) ]
plt.figure()
plt.plot( fluxes[0]/( fluxes[1]+fluxes[2] ), '.k' )
plt.ylim( [ 0.18, 0.195 ] )

# Attempt to apply wavelength corrections:
fluxes = []
for k in range( 3 ):
    wavsol = np.loadtxt( wavsols[k] )
    wavcor = np.loadtxt( wavcors[k] )
    spectrum = np.loadtxt( spectra[k] )
    n, m = np.shape( spectrum )
    fluxes_k = np.zeros( n )
    for j in range( n ):
        ixs_bandpass = ( wavsol[j,:]+wavcor[j,:]>bandpass[0] )*( wavsol[j,:]+wavcor[j,:]<bandpass[1] )
        fluxes_k[j] = np.sum( spectrum[j,ixs_bandpass] )
    fluxes += [ fluxes_k ]
plt.figure()
plt.plot( fluxes[0]/( fluxes[1]+fluxes[2] ), '.k' )
plt.ylim( [ 0.18, 0.195 ] )
# doesn't look that good!
