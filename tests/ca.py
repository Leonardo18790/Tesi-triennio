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
        step = tmag.size
        k = 0
        while (k < step):
            print("%8.4f %+9.4f\n" % (tfreq[k], tmag[k]))
        return tmag
