import sys
import math
#
# this is the Cellular Automaton transformation that is implemented for
# Leonardo Sisto's bachelor thesis.
#
def ca(tfreq, tmag):
	"""
	Cellular automaton-driven reshuffling of magnitues
        tfreq: frequency vector, tmag: magnitude vector
	returns y: the re-shuffled magnitudes
	"""
        step = min(tfreq.size, tmag.size)
        print("# outer_size: %d (tfreq.size %d, tmag.size %d)" % (step, tfreq.size, tmag.size))
        k = 0
        while (k < step):
            l = 0
            inner_size = min(tfreq[k].size, tmag[k].size)
            print("# inner_size: %d (tfreq.size %d, tmag.size %d)" % (inner_size, tfreq[k].size, tmag[k].size))
            while (l < inner_size):
                sys.stdout.write("%8.4f %+9.4f " % (tfreq[k][l], tmag[k][l]))
                l += 1
            print("")
            k += 1
        return tmag
